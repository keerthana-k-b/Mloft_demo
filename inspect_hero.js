async function test() {
  const v = await (await fetch('http://127.0.0.1:9222/json/list')).json();
  const tab = v.find(t => t.type === 'page' && t.url.includes('8080'));
  const ws = new WebSocket(tab.webSocketDebuggerUrl);
  await new Promise(r => ws.onopen = r);
  let id = 1;
  function send(method, params={}) {
    return new Promise(resolve => {
      const mid = id++;
      const handler = (e) => {
        const msg = JSON.parse(e.data);
        if (msg.id === mid) { ws.removeEventListener('message', handler); resolve(msg.result); }
      };
      ws.addEventListener('message', handler);
      ws.send(JSON.stringify({ id: mid, method, params }));
    });
  }
  await send('Emulation.setDeviceMetricsOverride', { width: 1280, height: 900, deviceScaleFactor: 1, mobile: false });
  const expr = `(() => {
    function elInfo(x, y) {
      const el = document.elementFromPoint(x, y);
      return el ? { tag: el.tagName, class: el.className, id: el.id } : null;
    }
    const heroSec = document.querySelector('.hero-section');
    const heroSlider = document.querySelector('.hero-slider');
    const heroPanel = document.querySelector('.hero-panel');
    const heroImg = document.querySelector('.hero-panel img');
    const heroOverlay = document.querySelector('.hero-overlay');
    return {
      pt1: elInfo(150, 200),
      pt2: elInfo(350, 200),
      pt3: elInfo(640, 200),
      heroSectionBg: window.getComputedStyle(heroSec).backgroundColor,
      heroSliderBg: window.getComputedStyle(heroSlider).backgroundColor,
      panelBg: window.getComputedStyle(heroPanel).backgroundColor,
      imgZIndex: window.getComputedStyle(heroImg).zIndex,
      overlayZIndex: window.getComputedStyle(heroOverlay).zIndex,
      overlayBg: window.getComputedStyle(heroOverlay).backgroundColor
    };
  })()`;
  const res = await send('Runtime.evaluate', { expression: expr, returnByValue: true });
  console.log(JSON.stringify(res.result.value, null, 2));
  ws.close();
}
test();
