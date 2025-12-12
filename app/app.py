from flask import Flask, Response, jsonify

app = Flask(__name__)


@app.route("/app")
def app_route():
    # UI for APP (backend-app-1 via NGINX)
    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>App One - DevOps Lab</title>
  <style>
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: radial-gradient(circle at top, #38bdf8 0, #020617 55%);
      color: #e5e7eb;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .card {
      background: rgba(15,23,42,0.96);
      border-radius: 18px;
      padding: 28px 32px;
      width: 480px;
      max-width: 92%;
      box-shadow: 0 24px 60px rgba(15,23,42,0.9);
      border: 1px solid rgba(148,163,184,0.4);
    }
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 4px 10px;
      border-radius: 999px;
      background: rgba(56,189,248,0.1);
      border: 1px solid rgba(56,189,248,0.5);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.09em;
      color: #7dd3fc;
      margin-bottom: 14px;
    }
    .dot {
      width: 8px;
      height: 8px;
      border-radius: 999px;
      background: #22c55e;
      box-shadow: 0 0 8px #22c55e;
    }
    h1 {
      margin: 0 0 6px;
      font-size: 26px;
    }
    p.subtitle {
      margin: 0 0 18px;
      font-size: 14px;
      color: #9ca3af;
    }
    .grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-top: 14px;
    }
    .metric {
      background: rgba(15,23,42,0.96);
      border-radius: 12px;
      padding: 10px 12px;
      border: 1px solid rgba(148,163,184,0.5);
    }
    .metric-label {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #9ca3af;
      margin-bottom: 4px;
    }
    .metric-value {
      font-size: 18px;
      font-weight: 600;
      color: #e5e7eb;
    }
    .metric-sub {
      font-size: 11px;
      color: #6b7280;
      margin-top: 2px;
    }
    .tags {
      margin-top: 18px;
      font-size: 11px;
      color: #9ca3af;
    }
    .tag {
      display: inline-block;
      padding: 4px 10px;
      border-radius: 999px;
      border: 1px solid rgba(148,163,184,0.5);
      background: rgba(15,23,42,0.96);
      margin-right: 6px;
      margin-bottom: 4px;
    }
  </style>
</head>
<body>
  <div class="card">
    <div class="badge">
      <span class="dot"></span>
      APP ONE • FRONTEND
    </div>
    <h1>App One behind NGINX</h1>
    <p class="subtitle">
      This is the user-facing app instance. Traffic reached this page through NGINX as a reverse proxy.
    </p>
    <div class="grid">
      <div class="metric">
        <div class="metric-label">Route</div>
        <div class="metric-value">/app</div>
        <div class="metric-sub">mapped in NGINX</div>
      </div>
      <div class="metric">
        <div class="metric-label">Role</div>
        <div class="metric-value">UI service</div>
        <div class="metric-sub">backend-app-1</div>
      </div>
    </div>
    <div class="tags">
      <span class="tag">Docker</span>
      <span class="tag">NGINX</span>
      <span class="tag">Reverse Proxy</span>
      <span class="tag">Path Routing</span>
    </div>
  </div>
</body>
</html>"""
    return Response(html, mimetype="text/html")


@app.route("/api")
def api_route():
    # UI for API (backend-app-2 via NGINX)
    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>App Two - API Service</title>
  <style>
    :root {
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    body {
      margin: 0;
      min-height: 100vh;
      background: radial-gradient(circle at bottom right, #f97316 0, #020617 60%);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #e5e7eb;
    }
    .shell {
      background: #020617;
      border-radius: 18px;
      padding: 24px 26px;
      width: 540px;
      max-width: 94%;
      box-shadow: 0 24px 60px rgba(15,23,42,0.9);
      border: 1px solid rgba(248,250,252,0.1);
    }
    .shell-header {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 14px;
    }
    .dot {
      width: 10px;
      height: 10px;
      border-radius: 999px;
    }
    .dot.red { background: #f97373; }
    .dot.yellow { background: #facc15; }
    .dot.green { background: #22c55e; }
    .shell-title {
      font-size: 12px;
      color: #9ca3af;
      margin-left: 6px;
    }
    pre {
      margin: 0;
      font-size: 13px;
      line-height: 1.7;
      white-space: pre-wrap;
    }
    .comment { color: #6b7280; }
    .key { color: #facc15; }
    .value { color: #4ade80; }
    .accent { color: #f97316; }
  </style>
</head>
<body>
  <div class="shell">
    <div class="shell-header">
      <div class="dot red"></div>
      <div class="dot yellow"></div>
      <div class="dot green"></div>
      <div class="shell-title">APP TWO • api service behind nginx</div>
    </div>
<pre><span class="comment"># APP TWO - API style view</span>

<span class="key">service</span>:       <span class="value">APP_TWO</span>
<span class="key">role</span>:          <span class="value">API backend</span>
<span class="key">route</span>:         <span class="value">/api</span>
<span class="key">routed_via</span>:   <span class="value">NGINX reverse proxy</span>

<span class="comment"># behaviour</span>
- only traffic for <span class="accent">/api</span> is forwarded here
- ideal place for REST/JSON endpoints
- mirrors a real microservice API behind a gateway

<span class="accent">You are currently hitting APP TWO via NGINX.</span></pre>
  </div>
</body>
</html>"""
    return Response(html, mimetype="text/html")


@app.route("/")
def home():
    return Response(
        "<h2 style='font-family: system-ui; text-align:center; margin-top:40px;'>"
        "Root endpoint – try <code>/app</code> or <code>/api</code> via NGINX."
        "</h2>",
        mimetype="text/html",
    )


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    # nosemgrep: python.flask.security.audit.app-run-param-config.avoid_app_run_with_bad_host
    app.run(host="0.0.0.0", port=5000)
