FOLIO Dataset Reference

Source: GitHub Yale-LILY/FOLIO
Server path: /root/autodl-tmp/data/folio/
Format: JSONL with fields: premises (list), premises-FOL, conclusion, conclusion-FOL, label

Splits:
- Train: 1004 samples (True: 388, False: 286, Unknown: 330)
- Validation: 204 samples (True: 72, False: 63, Uncertain: 69)

Label mapping note: Train uses "Unknown", Validation uses "Uncertain". Must normalize when loading.