import json
import re
import html

with open('data.json', 'r') as f:
    data = json.load(f)

blocks = []

for i, msg in enumerate(data['messages']):
    if msg['role'] == 'Response':
        text = msg['say']
        prompts = re.findall(r'<prompt[^>]*>.*?</prompt>', text, re.DOTALL)
        pomls = re.findall(r'<poml>.*?</poml>', text, re.DOTALL)
        for p in prompts:
            id_match = re.search(r'id="([^"]+)"', p)
            pid = id_match.group(1) if id_match else f'PROMPT_{len(blocks)+1}'
            blocks.append({'type': 'prompt', 'id': pid, 'content': p, 'response': i})
        for p in pomls:
            blocks.append({'type': 'poml', 'id': f'POML_{len(blocks)+1}', 'content': p, 'response': i})

# Generate HTML
html_out = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>POML Codex: Source Extraction</title>
  <style>
    :root {
      --bg: #08080c;
      --surface: #0f0f16;
      --border: #1e1e2e;
      --text: #d4d4dc;
      --dim: #6a6a7a;
      --accent: #00ffa3;
      --accent2: #ff5f87;
      --accent3: #8787ff;
      --mono: 'SF Mono', 'Fira Code', monospace;
      --sans: system-ui, sans-serif;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      font-family: var(--sans);
      background: var(--bg);
      color: var(--text);
      line-height: 1.5;
      padding: 12px;
      max-width: 100%;
    }
    header {
      border-bottom: 1px solid var(--border);
      padding-bottom: 12px;
      margin-bottom: 16px;
    }
    h1 {
      font-size: 1.2rem;
      color: var(--accent);
      font-weight: 600;
    }
    .meta { font-size: 0.7rem; color: var(--dim); margin-top: 4px; }
    .index {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 12px;
      margin-bottom: 20px;
    }
    .index h2 {
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--dim);
      margin-bottom: 8px;
    }
    .index a {
      display: block;
      color: var(--text);
      text-decoration: none;
      font-size: 0.8rem;
      padding: 6px 0;
      border-bottom: 1px solid var(--border);
    }
    .index a:last-child { border-bottom: none; }
    .index a:hover { color: var(--accent); }
    .index .type {
      font-family: var(--mono);
      font-size: 0.6rem;
      padding: 2px 5px;
      border-radius: 3px;
      margin-right: 6px;
    }
    .type-poml { background: rgba(0,255,163,0.15); color: var(--accent); }
    .type-prompt { background: rgba(135,135,255,0.15); color: var(--accent3); }
    
    .block {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      margin-bottom: 16px;
      overflow: hidden;
    }
    .block-header {
      background: rgba(0,0,0,0.4);
      padding: 10px 12px;
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border);
    }
    .block-header:active { background: rgba(0,255,163,0.05); }
    .block-title {
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--accent);
    }
    .block-id {
      font-family: var(--mono);
      font-size: 0.65rem;
      color: var(--dim);
      margin-top: 2px;
    }
    .toggle { font-size: 1rem; color: var(--dim); }
    .block.open .toggle { transform: rotate(90deg); }
    .block-body {
      display: none;
      padding: 0;
    }
    .block.open .block-body { display: block; }
    .block.open .block-header { border-bottom-color: var(--accent); }
    
    .source {
      background: #050508;
      padding: 12px;
      font-family: var(--mono);
      font-size: 0.7rem;
      white-space: pre-wrap;
      word-break: break-word;
      overflow-x: auto;
      color: #9999aa;
      max-height: 70vh;
      overflow-y: auto;
    }
    
    .toolbar {
      background: rgba(0,0,0,0.3);
      padding: 8px 12px;
      display: flex;
      gap: 8px;
      border-top: 1px solid var(--border);
    }
    .btn {
      background: var(--border);
      border: none;
      color: var(--dim);
      padding: 6px 10px;
      border-radius: 4px;
      font-size: 0.65rem;
      cursor: pointer;
      font-family: var(--mono);
    }
    .btn:active { background: var(--accent); color: var(--bg); }
    
    footer {
      margin-top: 24px;
      padding-top: 12px;
      border-top: 1px solid var(--border);
      font-size: 0.65rem;
      color: var(--dim);
      text-align: center;
    }
  </style>
</head>
<body>

<header>
  <h1>POML Codex: Source Extraction</h1>
  <p class="meta">''' + f'{len(blocks)} blocks extracted verbatim from data.json completions' + '''</p>
</header>

<div class="index">
  <h2>Block Index</h2>
'''

for i, b in enumerate(blocks):
    tclass = 'type-poml' if b['type'] == 'poml' else 'type-prompt'
    html_out += f'  <a href="#block-{i}"><span class="type {tclass}">{b["type"].upper()}</span>{b["id"]}</a>\n'

html_out += '''</div>

'''

for i, b in enumerate(blocks):
    escaped = html.escape(b['content'])
    
    html_out += f'''<div class="block" id="block-{i}">
  <div class="block-header" onclick="this.parentElement.classList.toggle('open')">
    <div>
      <div class="block-title">{html.escape(b['id'])}</div>
      <div class="block-id">{b['type'].upper()} | Response #{b['response']}</div>
    </div>
    <span class="toggle">▸</span>
  </div>
  <div class="block-body">
    <pre class="source">{escaped}</pre>
    <div class="toolbar">
      <button class="btn" onclick="copyBlock({i})">COPY</button>
      <button class="btn" onclick="downloadBlock({i})">SAVE .poml</button>
    </div>
  </div>
</div>

'''

# Escape the blocks for JS
blocks_json = json.dumps([b['content'] for b in blocks])

html_out += f'''<footer>
  Bottom-up extraction | Raw POML/Prompt notation verbatim from completions
</footer>

<script>
const blocks = {blocks_json};

function copyBlock(i) {{
  navigator.clipboard.writeText(blocks[i]).then(() => {{
    event.target.textContent = 'COPIED';
    setTimeout(() => event.target.textContent = 'COPY', 1200);
  }});
}}

function downloadBlock(i) {{
  const blob = new Blob([blocks[i]], {{type: 'text/xml'}});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'block-' + i + '.poml';
  a.click();
}}
</script>

</body>
</html>'''

with open('poml-codex-source.html', 'w') as f:
    f.write(html_out)

print(f'Extracted {len(blocks)} blocks to poml-codex-source.html')
for b in blocks:
    print(f"  - {b['type'].upper()}: {b['id']}")
