# Manifests

`mayuri_ja_filtered.list` is not tracked in git because it depends on the local clone path of this repository.

After downloading the full dataset into `data/raw/wav/`, regenerate it with:

```bash
python scripts/build_manifest.py
```

Tracked files here:

- `mayuri_ja_filtered.stats.json`
- `mayuri_ja_filtered.rejects.csv`

These are dataset metadata snapshots from the original filtering pass.
