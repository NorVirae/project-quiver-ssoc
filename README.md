# Quiver student laboratory course

A MkDocs Material course for University of Lagos students. Thirty-two practical topic pages cover daily lab routines, equipment induction, six parallel build modules, assessment and printable records. The Word handbook is built from the same Markdown source.

## Run and edit

Requires Python 3.10 or newer.

```sh
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS or Linux instead
# source .venv/bin/activate
python -m pip install -r requirements.txt
python -m mkdocs serve
```

Open the local address printed by MkDocs. Edit pages in `docs/`; the preview refreshes automatically. Change page navigation in `mkdocs.yml`. Search is generated at build time. The site uses no online font service, analytics or student database.

```sh
python -m mkdocs build --strict
```

The complete static website is written to `dist/`. Serve that folder through any static host, including GitHub Pages, Cloudflare Pages or university web hosting. For a subpath host, set `site_url` to its exact URL before building. The home-page buttons use relative paths. Search works over HTTP or HTTPS; do not open `index.html` using a `file://` URL.

## Rebuild the Word handbook

```sh
python -m pip install -r requirements-docx.txt
python scripts/build_handbook.py
python -m mkdocs build --strict
```

The generated Word file is written to `docs/downloads/Quiver_Student_Laboratory_Handbook_v5_1.docx`. After editing, open and check the complete Word document before distributing it. The contents page uses Word page-reference fields; update all fields if your Word processor does not refresh them automatically. Keep `course-order.json` aligned with any new or renamed pages.

`scripts/create_diagrams.py` contains the original teaching diagrams. It uses Arial on Windows; adapt the font path on other systems. Existing PNGs are ready to use. The script copies the aircraft image from the enclosing engineering repository when available; the packaged image already exists in `docs/assets/`.

## Editing and Vercel hosting

See [the step-by-step maintenance guide](docs/maintaining.md) for Windows setup, Markdown examples, adding pages, rebuilding Word and publishing a Vercel preview and production site. The Vercel workflow uses `mkdocs.vercel.yml` and `scripts/prepare_vercel.py`; it does not require a server or database.

The examples now use the TATTU 4.0 14S 20 Ah pack, manufacturer-listed TA7200Pro charger, Bambu Lab P2S and named Quiver parts. Equipment references are in [equipment-sources.md](docs/equipment-sources.md).

## Teaching and access

The laboratory manager must fill in the actual room arrangements, approve equipment-specific procedures and adopt the course before practical work. Thirty contact hours are a suggested plan, not an accredited credit award or a promise of a flight-ready aircraft. Use the linked sources for provenance; imported overseas rules are not Nigerian law.

Checkboxes are temporary practice aids. They reset on reload and do not sign students off. Keep completed personal, incident and authorisation records in restricted university systems. MkDocs provides search and navigation; content is edited in Markdown, not a shared Notion-style database.

The hosted Sites version starts private to its owner. Publishing this package elsewhere is a separate hosting decision. `.openai/hosting.json` binds the working checkout to its existing Sites project; do not replace that project ID when updating that site.

## Provenance

The source pages list the university laboratory guidance, equipment guidance and pinned Quiver technical references used. The aircraft photo is copied unaltered from the project repository, which identifies CERN-OHL-S v2. Review applicable source and third-party rights before redistributing engineering material. The five conceptual teaching diagrams were created for this course.

Course version 5.1, 25 October 2026.
