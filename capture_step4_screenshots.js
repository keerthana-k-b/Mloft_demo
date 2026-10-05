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
  console.log('Spawning Chrome...');
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

  const tabs = await fetchJson('http://127.0.0.1:9222/json/list');
  let targetTab = tabs.find(t => t.type === 'page' && t.url.includes('localhost:8080'));
  if (!targetTab) {
    targetTab = tabs.find(t => t.type === 'page');
  }

  if (!targetTab || !targetTab.webSocketDebuggerUrl) {
    console.error('No page tab found.');
    if (chromeProc) chromeProc.kill();
    process.exit(1);
  }

  const client = new CdpClient(targetTab.webSocketDebuggerUrl);
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

  async function captureElement(selector, filename, padTop = 10, padBottom = 10) {
    const rectRes = await client.send('Runtime.evaluate', {
      expression: `(() => {
        const el = document.querySelector('${selector}');
        if (!el) return null;
        el.scrollIntoView({ behavior: 'instant', block: 'start' });
        const r = el.getBoundingClientRect();
        return { x: window.scrollX + r.left, y: window.scrollY + r.top, width: r.width, height: r.height };
      })()`,
      returnByValue: true
    });
    await sleep(600);
    const rect = rectRes.result.value;
    if (!rect) {
      console.error('Element not found:', selector);
      return;
    }
    console.log(`Element ${selector} rect:`, rect);

    const shot = await client.send('Page.captureScreenshot', {
      format: 'png',
      clip: {
        x: Math.max(0, Math.round(rect.x)),
        y: Math.max(0, Math.round(rect.y - padTop)),
        width: Math.round(rect.width),
        height: Math.round(rect.height + padTop + padBottom),
        scale: 1
      }
    });
    const savePath = path.join(ARTIFACT_DIR, filename);
    fs.writeFileSync(savePath, Buffer.from(shot.data, 'base64'));
    console.log('Saved:', filename);
  }

  // ==========================================
  // 1. DESKTOP (1280px)
  // ==========================================
  console.log('\n--- CAPTURING DESKTOP 1280px ---');
  await client.send('Emulation.setDeviceMetricsOverride', {
    width: 1280,
    height: 900,
    deviceScaleFactor: 1,
    mobile: false
  });
  await sleep(1000);
  await captureElement('#mosaic', 'step4_mosaic_1280.png', 10, 20);
  await captureElement('#new-launch', 'step4_newlaunch_1280.png', 10, 20);

  // ==========================================
  // 2. TABLET (768px)
  // ==========================================
  console.log('\n--- CAPTURING TABLET 768px ---');
  await client.send('Emulation.setDeviceMetricsOverride', {
    width: 768,
    height: 1024,
    deviceScaleFactor: 1,
    mobile: false
  });
  await sleep(1000);
  await captureElement('#mosaic', 'step4_mosaic_768.png', 10, 20);
  await captureElement('#new-launch', 'step4_newlaunch_768.png', 10, 20);

  // ==========================================
  // 3. MOBILE (375px)
  // ==========================================
  console.log('\n--- CAPTURING MOBILE 375px ---');
  await client.send('Emulation.setDeviceMetricsOverride', {
    width: 375,
    height: 812,
    deviceScaleFactor: 2,
    mobile: true
  });
  await sleep(1000);
  await captureElement('#mosaic', 'step4_mosaic_375.png', 10, 20);
  await captureElement('#new-launch', 'step4_newlaunch_375.png', 10, 20);

  client.close();
  if (chromeProc) chromeProc.kill();
  console.log('\nAll Step 4 screenshots captured successfully!');
  process.exit(0);
}

run().catch((err) => {
  console.error('Error:', err);
  process.exit(1);
});
