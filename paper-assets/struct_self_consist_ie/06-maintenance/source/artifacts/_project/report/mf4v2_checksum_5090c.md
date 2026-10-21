## MF4v2 Data Integrity Checksum — autodl-5090-c

Computed 2026-05-21

| File | Lines | Size | N_samples | MD5 | Valid | Invalid |
|------|-------|------|-----------|-----|-------|---------|
| conll_mf4v2_seed42/samples.jsonl | 3453 | 56.9 MB | 8 | 8c3ff024f4abf11968176dd7e3af308d | 3453 | 0 |
| conll_mf4v2_s42_rerun/samples.jsonl | 3453 | 56.9 MB | 8 | 4159462c2a3b5d73040562b7188eaf36 | 3453 | 0 |

- Both files pass integrity check: valid JSON, required fields (id/gold/samples/greedy) present
- MD5 differs: expected due to sampling randomness (same model+seed but different run)
- **5090-c only has CoNLL MF4v2 data**. FewNERD and SciERC MF4v2 data are on 5090 only.

Remote file: /root/autodl-tmp/struct_self_consist_ie/mf4v2_checksum_5090c.txt