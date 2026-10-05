async function inspectCardMobile() {
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

  const res = await send('Runtime.evaluate', {
    expression: `(() => {
      const card = document.querySelector('.product-card');
      const btn = card.querySelector('.btn-product-enquire');
      const svg = btn.querySelector('svg');
      const span = btn.querySelector('span');
      const info = card.querySelector('.product-info');
      const imgWrap = card.querySelector('.product-img-wrap');
      return {
        cardHeight: card.offsetHeight,
        imgWrapHeight: imgWrap.offsetHeight,
        infoHeight: info.offsetHeight,
        btnHeight: btn.offsetHeight,
        btnDisplay: window.getComputedStyle(btn).display,
        btnOverflow: window.getComputedStyle(btn).overflow,
        btnColor: window.getComputedStyle(btn).color,
        cardOverflow: window.getComputedStyle(card).overflow,
        svgWidth: svg ? svg.clientWidth : null,
        svgHeight: svg ? svg.clientHeight : null,
        svgFill: svg ? window.getComputedStyle(svg).fill : null,
        spanText: span ? span.innerText : null,
        spanColor: span ? window.getComputedStyle(span).color : null,
        spanDisplay: span ? window.getComputedStyle(span).display : null,
        btnRect: btn.getBoundingClientRect(),
        cardRect: card.getBoundingClientRect()
      };
    })()`,
    returnByValue: true
  });

  console.log(JSON.stringify(res.result.value, null, 2));
  ws.close();
}

inspectCardMobile().catch(console.error);
