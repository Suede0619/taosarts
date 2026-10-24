# Build and validation notes

Financial/calendar/partner outputs: Python 3 standard library.

```sh
python3 tools/build_execution.py
```

Inputs: data/project.json, partners.json, weekly-work.json and event-program.json. Preserve unknowns, evidence status and the public/private boundary. Update prose when assumptions change; the generator does not rewrite every narrative paragraph.

PowerPoint/brand assets: Python with python-pptx and Pillow, plus available Arial/Arial Bold system font files. This environment uses macOS Supplemental Fonts; the script's font path must be adapted on another system using appropriately licensed files.

```sh
python3 tools/build_decks.py
```

LibreOffice is used locally for PDF export. Run headless with a profile under ignored private/ and output to decks/. PyMuPDF supports page-count/text/bounds checks and local contact-sheet rendering. The environment/dependency versions are recorded in data/build-environment.json. These tools do not contact recipients or deploy a site.

PowerPoint and PDF binaries may include generated package metadata; content/model/calendar reproducibility is validated separately from binary byte identity. No proprietary font files or third-party art assets are distributed.

The source-capture helper and raw evidence remain ignored under private/. Do not move them into public Git. Private named-team deck generation also stays ignored.

Run `python3 tools/validate_package.py` after generation/export. Participant-name checks load ignored `private/privacy-terms.json`; a fresh clone lacks that input and reports the audit as unconfigured rather than claiming it passed. Other consistency checks remain runnable. The report is data/package-validation.json and explicitly does not validate real demand, rights, funding, availability or safe/legal capacity.
