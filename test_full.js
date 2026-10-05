const fs = require('fs');
const path = require('path');

const ARTIFACT_DIR = 'C:\\Users\\HP\\.gemini\\antigravity-ide\\brain\\a7060d48-ace3-4fe3-a7cb-3f64db45c701';

async function testMobileProducts() {
  const tabs = await (await fetch('http://127.0.0.1:9222/json/list')).json();
  const tab = tabs.find(t => t.type === 'page' && t.url.includes('8080'));
  const ws = new WebSocket(tab.webSocketDebuggerUrl);
  await new Promise(r => ws.onopen = r);
  let id = 1;
  function send(method, params={}) {
    return new Promise((resolve, reject) => {
      const mid = id++;
      const handler = (e) => {
        const msg = JSON.parse(e.data);
        if (msg.id === mid) {
          ws.removeEventListener('message', handler);
          if (msg.error) reject(msg.error);
          else resolve(msg.result);
        }
      };
      ws.addEventListener('message', handler);
      ws.send(JSON.stringify({ id: mid, method, params }));
    });
  }

  await send('Emulation.setDeviceMetricsOverride', {
    width: 375,
    height: 812,
    deviceScaleFactor: 2,
    mobile: true
  });

  // Scroll to show the product card with its Enquire button
  await send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.querySelector('.product-card');
      const r = el.getBoundingClientRect();
      window.scrollBy({ top: r.top - 80, behavior: 'instant' });
    })()`
  });
  await new Promise(r => setTimeout(r, 1000));

  const shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'test_products_mobile_375.png'), Buffer.from(shot.data, 'base64'));
  console.log('Saved test_products_mobile_375.png');
  ws.close();
}

testMobileProducts().catch(console.error);
