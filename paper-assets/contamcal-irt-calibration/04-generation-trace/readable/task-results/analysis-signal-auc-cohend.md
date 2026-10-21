# analysis signal auc cohend

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_signal_auc_cohend_20260516T205703_result.json`
- **Structured JSON:** [`7b4447b073197cacbe89.json`](../../sessions/7b/7b4447b073197cacbe89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Status: BLOCKED — no SSH access in this session.**

What I've done:
- Wrote `compute_signal_summary.py` — complete script that computes AUC(d005 vs d000) and Cohen's d(d100 vs d000) for all signal×benchmark combos for 1.5B and 3B
- Handles C006 blacklist, both key naming conventions (`s1_embedding` / `embedding_similarity`), automatic directory discovery with _v3/_a32 priority
- Registered as artifact `art_20260516_8b5cb5`

What's needed to complete:
1. A worker with SSH tools needs to copy the script to `/root/autodl-tmp/exp002/signals/compute_signal_summary.py`
2. Run: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/exp002/signals && python compute_signal_summary.py`
3. Output will be saved to `/root/autodl-tmp/exp002/signals/signal_summary_15B_3B.json`

The worker pool is full (6/6) and this session lacks SSH tools. The parent worker (`data:signal_heatmap_extract`) has SSH access and can deploy this.

---
