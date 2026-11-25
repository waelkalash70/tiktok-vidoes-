// Rendert profilbild.html?v=A|B|C zu PNG (1080×1080) mit Playwright + lokalem Server
const { chromium } = require("playwright");
const http = require("http"), fs = require("fs"), path = require("path");
const root = __dirname;
const types = { ".html": "text/html", ".js": "text/javascript", ".png": "image/png" };
const srv = http.createServer((q, r) => {
  const p = path.join(root, decodeURIComponent(q.url.split("?")[0]));
  fs.readFile(p, (e, d) => { if (e) { r.writeHead(404); r.end(); } else { r.writeHead(200, { "Content-Type": types[path.extname(p)] || "application/octet-stream" }); r.end(d); } });
}).listen(8799, async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1080, height: 1080 } });
  // Montserrat aus dem HyperFrames-Font-Cache einbinden (sonst Fallback-Schrift)
  const fontDir = "/root/.cache/hyperframes/fonts/montserrat";
  const files = fs.readdirSync(fontDir).filter((x) => x.startsWith("900-normal"));
  const fonts = files.map((x) => fs.readFileSync(path.join(fontDir, x)).toString("base64"));
  await pg.addInitScript(`(() => { for (const b of ${JSON.stringify(fonts)}) { const bin = Uint8Array.from(atob(b), c => c.charCodeAt(0)); document.fonts.add(new FontFace('Montserrat', bin, { weight: '900' })); } })()`);
  pg.on("pageerror", (e) => console.log("pageerror", e.message));
  for (const v of (process.argv[2] || "A,B,C").split(",")) {
    await pg.goto(`http://127.0.0.1:8799/profilbild.html?v=${v}`);
    await pg.waitForFunction(() => window.__done === true, null, { timeout: 120000 });
    await pg.locator("canvas").screenshot({ path: path.join(root, `profilbild_${v}.png`) });
    console.log("ok", v);
  }
  await b.close(); srv.close();
});
