# MIA 2

MIA 2 is a browser-based tool for drawing the volume contour of a music program, piece by piece, over its whole length. It is a modern successor to MIA (Music Imagery Analysis, Rickman 2005), made for Bonny Method Guided Imagery and Music (GIM) and for other music research, such as studies of recorded improvisations.

**Try it:** https://aljhoberman-sys.github.io/mia2-app/

## What it does

- Drop audio files onto the page to lay them out as one program, with a mini-map of the whole program below the main chart.
- Smoothing from 0.1 to 20 s (default about 3.5 s), linear or decibel volume axis, and one shared scale for the whole program or each piece to its own peak.
- Reorder, rename, recolor and remove pieces, and add notes at points in time.
- Play the program back with a moving playhead, zoom and scroll, save the chart as an image or print it.
- The current program, audio included, is kept in your browser as you work, so reloading the page or reopening the tab brings it back. Use New to start over.
- Save a session file that keeps the chart, order, titles, colors and notes, so it opens without the audio. Optionally save one .zip that also holds the audio.

Level is measured A-weighted on a linear scale, which matches the contours of the original MIA closely.

## Your audio stays on your computer

All analysis runs locally in your browser. Audio files are never uploaded anywhere. MIA 2 does not include any music; you bring your own recordings and are responsible for how you use them.

## Running it locally

MIA 2 is plain HTML and JavaScript with no build step and no dependencies. From the repository folder:

```sh
python3 -m http.server 8765
```

Then open http://localhost:8765/web/ in Chrome or Edge. Other modern browsers work too, but only Chrome and Edge can remember where your audio files are so a saved session reconnects to them.

## Repository layout

- `web/` holds the app: `index.html` and `classic.js`.
- `prototype/` holds an early Python sketch of a combined intensity curve (`pip install -r requirements.txt`).
- `scripts/publish_site.sh` copies the app to the GitHub Pages site.

## Roadmap

The current Classic view recreates the original MIA readout. Planned next: key and modulation, timbre, tension, and combined metrics.

## Feedback

Feature requests and bug reports are welcome as GitHub issues.

## License

MIT. See [LICENSE](LICENSE).
