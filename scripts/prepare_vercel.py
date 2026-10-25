"""Package an already built MkDocs site for Vercel's static Build Output API."""
from pathlib import Path
import json
import re
import shutil

root = Path(__file__).resolve().parents[1]
source = root / 'dist-vercel'
output = root / '.vercel' / 'output'
if not (source / 'index.html').is_file():
    raise SystemExit('First run: python -m mkdocs build --strict -f mkdocs.vercel.yml')

# Clear only this project's generated output; retain .vercel/project.json.
resolved = output.resolve()
if not resolved.is_relative_to(root) or resolved == root:
    raise SystemExit(f'Refusing to replace output outside the project: {resolved}')
if output.exists():
    shutil.rmtree(output)
static = output / 'static'
shutil.copytree(source, static)

# Explicit directory routes preserve MkDocs relative links and deep links.
routes = [{'src': '^/$', 'dest': '/index.html'}]
for page in sorted(static.rglob('index.html')):
    relative = page.relative_to(static).as_posix()
    if relative == 'index.html':
        continue
    prefix = '/' + relative.removesuffix('/index.html')
    routes.extend([
        {'src': '^' + re.escape(prefix) + '$', 'status': 308,
         'headers': {'Location': prefix + '/'}},
        {'src': '^' + re.escape(prefix) + '/$', 'dest': '/' + relative},
    ])
routes.append({'handle': 'filesystem'})
if (static / '404.html').exists():
    routes.append({'src': '/.*', 'status': 404, 'dest': '/404.html'})
(output / 'config.json').write_text(
    json.dumps({'version': 3, 'routes': routes}, indent=2) + '\n', encoding='utf-8')
print(f'Vercel static output prepared: {output}')
print('Next: vercel deploy --prebuilt (preview), then --prebuilt --prod when ready.')
