const fs = require('fs');
const path = require('path');

const ARTIFACT_DIR = 'C:\\Users\\HP\\.gemini\\antigravity-ide\\brain\\a7060d48-ace3-4fe3-a7cb-3f64db45c701';

async function captureAll() {
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

  // --- 1. DESKTOP HERO (1280x900) ---
  console.log('Capturing Desktop 1280px...');
  await send('Emulation.setDeviceMetricsOverride', {
    width: 1280,
    height: 900,
    deviceScaleFactor: 1,
    mobile: false
  });
  await send('Page.navigate', { url: 'http://localhost:8080/index.html' });
  await new Promise(r => setTimeout(r, 2000));
  await send('Runtime.evaluate', { expression: 'window.scrollTo(0, 0);' });
  await new Promise(r => setTimeout(r, 500));

  const heroDeskShot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'hero_desktop_1280.png'), Buffer.from(heroDeskShot.data, 'base64'));
  console.log('Saved hero_desktop_1280.png');

  // --- 2. DESKTOP PRODUCTS (1280x900) ---
  await send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.querySelector('.product-track');
      el.scrollIntoView({ behavior: 'instant', block: 'center' });
    })()`
  });
  await new Promise(r => setTimeout(r, 800));

  const prodDeskShot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'products_desktop_1280.png'), Buffer.from(prodDeskShot.data, 'base64'));
  console.log('Saved products_desktop_1280.png');

  // --- 3. MOBILE HERO (375x812) ---
  console.log('Capturing Mobile 375px...');
  await send('Emulation.setDeviceMetricsOverride', {
    width: 375,
    height: 812,
    deviceScaleFactor: 2,
    mobile: true
  });
  await send('Page.navigate', { url: 'http://localhost:8080/index.html' });
  await new Promise(r => setTimeout(r, 2000));
  await send('Runtime.evaluate', { expression: 'window.scrollTo(0, 0);' });
  await new Promise(r => setTimeout(r, 500));

  const heroMobShot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'hero_mobile_375.png'), Buffer.from(heroMobShot.data, 'base64'));
  console.log('Saved hero_mobile_375.png');

  // --- 4. MOBILE PRODUCTS (375x812) ---
  await send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.querySelector('.product-card');
      el.scrollIntoView({ behavior: 'instant', block: 'center' });
    })()`
  });
  await new Promise(r => setTimeout(r, 800));

  const prodMobShot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(path.join(ARTIFACT_DIR, 'products_mobile_375.png'), Buffer.from(prodMobShot.data, 'base64'));
  console.log('Saved products_mobile_375.png');

  ws.close();
  console.log('All 4 final screenshots captured successfully!');
}

captureAll().catch(console.error);
