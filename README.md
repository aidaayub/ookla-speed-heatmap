# Ookla Download Speed Map - No-Tiles Version

## Open on Windows (no Python, no map API key)
1. Extract the ZIP file completely.
2. Open the extracted folder.
3. Double-click `index.html` in Microsoft Edge or Chrome.
4. Keep `data-bundle.js` in the same folder as `index.html`.

The map shows the supplied State, District, Parliament and DUN boundaries, shaded using the original Ookla-extracted average download speeds through Q2 2026. It does NOT request OpenStreetMap or CARTO background tiles, avoiding their 403 and API-key messages. Zoom, hover, click, quarter/year filters, and CSV export are retained.

**Internet still required:** Leaflet and TopoJSON JavaScript libraries are loaded from unpkg.com. If company network blocks that CDN, the page may not render until those libraries are made available locally. The actual map geography and speed data are bundled in `data-bundle.js`, so no Python server is required.

To deploy on Vercel, upload or import the project directory. Keep the JSON files and `build_data.py` for future updates, and regenerate `data-bundle.js` when updating data.
