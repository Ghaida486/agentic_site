# VenueFit Boston

VenueFit Boston is a responsive, public-data event-venue decision tool. It helps Boston university event offices, nonprofit producers, and community organizers shortlist venues by expected attendance, preferred setting, operating season, and an approximate transit-distance tolerance.

## Open the site

Open `index.html` in a browser. The site has no build step and stores its comparison data in `data/venues.csv`.

## Deliverables

- `index.html` — the responsive site
- `data/venues.csv` — collected source-linked dataset
- `deliverables/VenueFit_Boston_Data_and_Methodology_Note.docx` — one-page methodology note
- `deliverables/VenueFit_Boston_Presentation.pptx` — six-slide presentation for a five-minute demonstration
- `reflection.md` — evidence and limits reflection

## Publication

The project is ready for static hosting. Upload the folder to GitHub Pages, Netlify, Vercel, or Cloudflare Pages. No account or hosting destination is configured in this workspace.


## September 20 update

Open `index.html` in a browser. The local site works without a server. After editing the source CSV, run `python3 build_data.py` to regenerate `data/venues-data.js`, then refresh the page. Do not edit the generated file manually. Run `node check_planner.cjs` for the capacity and season checks.

The Deliverables page links the updated methodology and presentation, reflection, and a timed recording script. PowerPoint speaker notes contain the narration. The recording is embedded on guide.html and stored at media/venuefit-walkthrough.mp4. Distance estimates remain unverified and are optional filters only. Original supporting documents remain in the repository for reference; use the files with `_Updated` in their names for submission.
