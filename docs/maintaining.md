# Edit and host this course

This page is for the course owner. The student handbook keeps the teaching content; this website guide explains publishing and maintenance.

## Where to edit

Open the `quiver-lab-course` folder in VS Code or another text editor. The files in `docs/` are the editable course. **Do not edit generated HTML in `dist/` or `dist-vercel/`: a build replaces it.**

| What you want to change | File |
| --- | --- |
| TATTU handling and charging | `docs/batteries.md` and `docs/charging.md` |
| P2S printing lesson | `docs/printing.md` |
| A build module | `docs/m1.md` through `docs/m6.md` |
| Equipment manuals | `docs/equipment-sources.md` |
| Menu labels and page order | `mkdocs.yml` |
| Word handbook chapters and order | `course-order.json` |
| Colours, spacing and print appearance | `docs/assets/course.css` |
| Word layout | `scripts/build_handbook.py` |

Markdown uses `#` for a page title, `##` for a section, `-` for a bullet and `**text**` for bold. Put a blank line between paragraphs. A link to another course page looks like `[Charging](charging.md)`. Add an image to `docs/assets/`, then reference it with `![Description](assets/filename.png)`.

For a new chapter, create `docs/new-topic.md`, add it to `nav` in `mkdocs.yml` and, if it belongs in the Word handbook, add its slug/title/group to `course-order.json`. Keep the same short pattern: outcome, preparation, procedure, stop conditions, demonstration and evidence.

## Install and preview on Windows

Install Python 3.10 or newer. Open PowerShell in the course folder. These commands do not require activating a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt -r requirements-docx.txt
.\.venv\Scripts\python.exe -m mkdocs serve
```

Open the local URL printed by MkDocs, normally `http://127.0.0.1:8000/`. Save a Markdown edit and the preview refreshes. Press Ctrl+C to stop the server. Search needs HTTP/HTTPS; double-clicking a generated HTML file is not a valid preview.

On macOS/Linux, use `python3 -m venv .venv` and `.venv/bin/python` in place of the Windows Python path.

## Keep the Word handbook in sync

```powershell
.\.venv\Scripts\python.exe scripts/build_handbook.py
.\.venv\Scripts\python.exe -m mkdocs build --strict
```

The first command writes `docs/downloads/Quiver_Student_Laboratory_Handbook_v5_1.docx`; the second builds the website and includes that download. Open the Word file and review every page, tables, images and contents links before sharing. Update Word fields if page numbers have not refreshed.

Editing the DOCX directly is possible, but those edits do **not** update the website and will be replaced by regeneration. Make permanent content changes in Markdown. If you rename the download, update the home-page link and builder output filename too.

## Publish on Vercel

Use a locally built static upload. It preserves search and navigation without requiring a Python build environment on Vercel. Install Node.js LTS, then install Vercel's CLI and link your account/project:

```powershell
npm install -g vercel
vercel login
vercel link
```

Run those commands in the course folder. Choose your Vercel account/team and create or select the intended project. If asked for a framework, choose **Other**. Account sign-in and project selection are completed by you.

Build and prepare the site:

```powershell
.\.venv\Scripts\python.exe -m mkdocs build --strict -f mkdocs.vercel.yml
.\.venv\Scripts\python.exe scripts/prepare_vercel.py
vercel deploy --prebuilt
```

The last command creates a preview deployment and prints its URL. Check the home page, a module deep link, search for `TATTU`, and the Word download. Then publish the same prepared output:

```powershell
vercel deploy --prebuilt --prod
```

`--prebuilt` reads `.vercel/output/`, which the helper creates. It does not read MkDocs' `dist/` directly. The helper preserves the project link in `.vercel/project.json`. Never commit `.vercel/`, account credentials or student records.

After your first deployment, set the production address before future builds so canonical links and the sitemap use it:

```powershell
$env:COURSE_SITE_URL = 'https://YOUR-PROJECT.vercel.app/'
.\.venv\Scripts\python.exe -m mkdocs build --strict -f mkdocs.vercel.yml
.\.venv\Scripts\python.exe scripts/prepare_vercel.py
vercel deploy --prebuilt
# After checking the preview:
vercel deploy --prebuilt --prod
```

Replace the example address with your actual production URL or custom domain. The Vercel configuration inherits the course settings while keeping its output separate from the existing Sites build. This workflow uploads local builds; it does not enable automatic deployment on Git pushes.

Vercel documents the [CLI deployment workflow](https://vercel.com/docs/cli/deploying-from-cli), [prebuilt option](https://vercel.com/docs/cli/deploy) and [Build Output API configuration](https://vercel.com/docs/build-output-api/configuration).

## Before releasing a revision

Have the responsible technical reviewer check changed equipment instructions. Record the revision/date and update the handbook. Build with `--strict`, check search and links, review the Word layout and retain a backup of the source. Keep completed student, incident and authorisation records in restricted university storage; this static site does not collect them.
