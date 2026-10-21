## Plan 008: Multi-Domain Seeds Experiment

**Status**: Running (PID 234061 on autodl-5090)
**Started**: 2026-05-16 ~02:25 UTC+8
**Est. completion**: ~6 hours (generation) + 30 min (features+eval)

### Seeds (Phase 1 — DONE)
| Domain | Dataset | Seeds |
|--------|---------|-------|
| news | CNN/DailyMail (abisee/cnn_dailymail) | 500 |
| scientific | arXiv abstracts (ccdv/arxiv-summarization) | 500 |
| creative | WritingPrompts (euclaise/writingprompts) | 500 |

### Generation (Phase 2 — IN PROGRESS)
- Model: Pythia-2.8B (same as main experiment)
- Device: cuda:0 only
- Params: temperature=1.0, top_p=0.95 (same as generate_chain.py)
- Rate: ~13.5s/seed, ~112 min/domain
- Resumable: script tracks done_seeds

### Feature Extraction (Phase 3 — PENDING)
- Reference model: Pythia-410M
- 7 features: entropy_{mean,std,min,max}, tail_decay, ttr, hapax_ratio

### Evaluation (Phase 4 — PENDING)
- Per-domain 5-fold CV F1
- Cross-domain leave-one-domain-out F1
- Wikipedia transfer (train wiki → test each domain)

### Monitoring
```bash
# Check progress
wc -l /root/gen-depth-fingerprint/data/pythia-2.8b-{news,scientific,creative}/generations_shard0.jsonl
# Check log
tail -20 /tmp/plan008_full.log
# Check process
ps -p 234061 -o pid=
```

### Output paths
- Seeds: /root/gen-depth-fingerprint/data/seeds/{domain}_seed_500.jsonl
- Generations: /root/gen-depth-fingerprint/data/pythia-2.8b-{domain}/generations_shard0.jsonl
- Features: /root/gen-depth-fingerprint/data/features_pythia-2.8b-{domain}.csv
- Results: /root/gen-depth-fingerprint/results/multi_domain_results.json
