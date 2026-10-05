const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const ARTIFACT_DIR = 'C:\\Users\\HP\\.gemini\\antigravity-ide\\brain\\a7060d48-ace3-4fe3-a7cb-3f64db45c701';
const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function fetchJson(url, options) {
  const res = await fetch(url, options);
  return await res.json();
}

class CdpClient {
  constructor(wsUrl) {
    this.ws = new WebSocket(wsUrl);
    this.id = 1;
    this.callbacks = new Map();
    this.ready = new Promise((resolve, reject) => {
      this.ws.onopen = resolve;
      this.ws.onerror = reject;
    });
    this.ws.onmessage = (event) => {
      const msg = JSON.parse(event.data);
      if (msg.id && this.callbacks.has(msg.id)) {
        const { resolve, reject } = this.callbacks.get(msg.id);
        this.callbacks.delete(msg.id);
        if (msg.error) reject(msg.error);
        else resolve(msg.result);
      }
    };
  }

  async send(method, params = {}) {
    await this.ready;
    const msgId = this.id++;
    return new Promise((resolve, reject) => {
      this.callbacks.set(msgId, { resolve, reject });
      this.ws.send(JSON.stringify({ id: msgId, method, params }));
    });
  }

  close() {
    this.ws.close();
  }
}

async function run() {
  console.log('Checking for existing or spawning Chrome...');
  let debugUrl = null;
  let chromeProc = null;

  try {
    const v = await fetchJson('http://127.0.0.1:9222/json/version');
    debugUrl = v.webSocketDebuggerUrl;
  } catch (e) {}

  if (!debugUrl) {
    chromeProc = spawn(CHROME_PATH, [
      '--headless=new',
      '--remote-debugging-port=9222',
      '--remote-allow-origins=*',
      '--disable-gpu',
      '--no-first-run',
      '--no-default-browser-check',
      '--user-data-dir=' + path.join(__dirname, 'chrome-temp-profile'),
      'http://localhost:8080/index.html'
    ]);

    for (let i = 0; i < 30; i++) {
      await sleep(500);
      try {
        const version = await fetchJson('http://127.0.0.1:9222/json/version');
        debugUrl = version.webSocketDebuggerUrl;
        if (debugUrl) break;
      } catch (e) {}
    }
  }

  if (!debugUrl) {
    console.error('Could not connect to Chrome debugging port.');
    if (chromeProc) chromeProc.kill();
    process.exit(1);
  }
  console.log('Chrome debugger ready.');

  // Find page target
  const tabs = await fetchJson('http://127.0.0.1:9222/json/list');
  let targetTab = tabs.find(t => t.type === 'page' && t.url.includes('localhost:8080'));
  if (!targetTab) {
    targetTab = tabs.find(t => t.type === 'page');
  }

  if (!targetTab || !targetTab.webSocketDebuggerUrl) {
    console.error('No page tab found.');
    process.exit(1);
  }

  const pageWsUrl = targetTab.webSocketDebuggerUrl;
  console.log('Connecting to page WebSocket:', pageWsUrl);

  const client = new CdpClient(pageWsUrl);
  await client.send('Page.enable');
  await client.send('DOM.enable');
  await client.send('Runtime.enable');

  console.log('Navigating to http://localhost:8080/index.html...');
  await client.send('Page.navigate', { url: 'http://localhost:8080/index.html' });
  await sleep(2500);

  // Wait for fonts & images
  await client.send('Runtime.evaluate', {
    expression: 'document.fonts.ready',
    awaitPromise: true
  });
  await sleep(1500);

  // --- DESKTOP VIEWPORT (1280x900) ---
  console.log('Capturing Desktop 1280px...');
  await client.send('Emulation.setDeviceMetricsOverride', {
    width: 1280,
    height: 900,
    deviceScaleFactor: 1,
    mobile: false
  });
  await client.send('Runtime.evaluate', { expression: 'window.scrollTo(0, 0);' });
  await sleep(1000);

  // 1. Hero desktop screenshot
  const heroDesktopRectRes = await client.send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.getElementById('hero');
      const r = el.getBoundingClientRect();
      return { x: window.scrollX + r.left, y: window.scrollY + r.top, width: r.width, height: r.height };
    })()`,
    returnByValue: true
  });
  const heroDeskRect = heroDesktopRectRes.result.value;
  console.log('Hero desktop rect:', heroDeskRect);

  const heroDeskShot = await client.send('Page.captureScreenshot', {
    format: 'png',
    clip: {
      x: Math.round(heroDeskRect.x),
      y: Math.max(0, Math.round(heroDeskRect.y)),
      width: Math.round(heroDeskRect.width),
      height: Math.min(Math.round(heroDeskRect.height), 750),
      scale: 1
    }
  });
  const heroDeskPath = path.join(ARTIFACT_DIR, 'hero_desktop_1280.png');
  fs.writeFileSync(heroDeskPath, Buffer.from(heroDeskShot.data, 'base64'));
  console.log('Saved hero_desktop_1280.png');

  // 2. Products desktop screenshot
  const prodDeskRectRes = await client.send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.getElementById('products');
      el.scrollIntoView({ behavior: 'instant', block: 'start' });
      const r = el.getBoundingClientRect();
      return { x: window.scrollX + r.left, y: window.scrollY + r.top, width: r.width, height: r.height };
    })()`,
    returnByValue: true
  });
  await sleep(1000);
  const prodDeskRect = prodDeskRectRes.result.value;
  console.log('Products desktop rect:', prodDeskRect);

  const prodDeskShot = await client.send('Page.captureScreenshot', {
    format: 'png',
    clip: {
      x: Math.round(prodDeskRect.x),
      y: Math.round(prodDeskRect.y),
      width: Math.round(prodDeskRect.width),
      height: Math.min(Math.round(prodDeskRect.height), 850),
      scale: 1
    }
  });
  const prodDeskPath = path.join(ARTIFACT_DIR, 'products_desktop_1280.png');
  fs.writeFileSync(prodDeskPath, Buffer.from(prodDeskShot.data, 'base64'));
  console.log('Saved products_desktop_1280.png');

  // --- MOBILE VIEWPORT (375x812) ---
  console.log('Capturing Mobile 375px...');
  await client.send('Emulation.setDeviceMetricsOverride', {
    width: 375,
    height: 812,
    deviceScaleFactor: 2,
    mobile: true
  });
  await client.send('Runtime.evaluate', { expression: 'window.scrollTo(0, 0);' });
  await sleep(1200);

  // 3. Hero mobile screenshot
  const heroMobRectRes = await client.send('Runtime.evaluate', {
    expression: `(() => {
      window.scrollTo(0, 0);
      const el = document.getElementById('hero');
      const r = el.getBoundingClientRect();
      return { x: window.scrollX + r.left, y: window.scrollY + r.top, width: r.width, height: r.height };
    })()`,
    returnByValue: true
  });
  await sleep(500);
  const heroMobRect = heroMobRectRes.result.value;
  console.log('Hero mobile rect:', heroMobRect);

  const heroMobShot = await client.send('Page.captureScreenshot', {
    format: 'png',
    clip: {
      x: Math.round(heroMobRect.x),
      y: Math.max(0, Math.round(heroMobRect.y)),
      width: Math.round(heroMobRect.width),
      height: Math.min(Math.round(heroMobRect.height), 650),
      scale: 1
    }
  });
  const heroMobPath = path.join(ARTIFACT_DIR, 'hero_mobile_375.png');
  fs.writeFileSync(heroMobPath, Buffer.from(heroMobShot.data, 'base64'));
  console.log('Saved hero_mobile_375.png');

  // 4. Products mobile screenshot
  const prodMobRectRes = await client.send('Runtime.evaluate', {
    expression: `(() => {
      const el = document.getElementById('products');
      el.scrollIntoView({ behavior: 'instant', block: 'start' });
      const r = el.getBoundingClientRect();
      return { x: window.scrollX + r.left, y: window.scrollY + r.top, width: r.width, height: r.height };
    })()`,
    returnByValue: true
  });
  await sleep(1000);
  const prodMobRect = prodMobRectRes.result.value;
  console.log('Products mobile rect:', prodMobRect);

  const prodMobShot = await client.send('Page.captureScreenshot', {
    format: 'png',
    clip: {
      x: Math.round(prodMobRect.x),
      y: Math.round(prodMobRect.y),
      width: Math.round(prodMobRect.width),
      height: Math.min(Math.round(prodMobRect.height), 880),
      scale: 1
    }
  });
  const prodMobPath = path.join(ARTIFACT_DIR, 'products_mobile_375.png');
  fs.writeFileSync(prodMobPath, Buffer.from(prodMobShot.data, 'base64'));
  console.log('Saved products_mobile_375.png');

  client.close();
  if (chromeProc) chromeProc.kill();
  console.log('ALL SCREENSHOTS CAPTURED SUCCESSFULLY!');
  process.exit(0);
}

run().catch((err) => {
  console.error('Error during execution:', err);
  process.exit(1);
});
