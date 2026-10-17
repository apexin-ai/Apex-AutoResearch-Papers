# Generation trace archive (split for GitHub)

The original sanitized archive was `trace-files.tar.gz` (112,525,857 bytes). GitHub rejects files above 100 MB, so it is stored as 2 ordered parts.

From the repository root, reconstruct and verify it with:

```bash
python3 scripts/reconstruct_trace.py paper-assets/importance_margin_vla_compress/05-generation-trace/trace-files.tar.gz.parts /tmp/importance_margin_vla_trace.tar.gz
```

The resulting SHA-256 is `8d7f59e84c2a604909c54a5c667bef36d5daf20ceed25970b118e0a3056b282c`. `manifest.csv` contains per-part hashes.
