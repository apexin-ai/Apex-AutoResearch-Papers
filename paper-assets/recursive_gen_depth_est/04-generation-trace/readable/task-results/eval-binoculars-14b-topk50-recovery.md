# eval binoculars 14b topk50 recovery

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_binoculars_14b_topk50_recovery_20260520T054202_result.json`
- **Structured JSON:** [`107ed08ab17c1b73ad98.json`](../../sessions/10/107ed08ab17c1b73ad98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型加载中，正常运行。预计 binoculars 特征提取需要 30-60 分钟（20k 样本，双模型推理），ablation 几分钟。

已提交的 pipeline：
1. **Binoculars 特征提取**: `binoculars_ordinal_eval.py` → `results/binoculars_14b_topk50/binoculars_14b_topk50.json` + `pythia_nucleus_bino_features.npz`
2. **Merged ablation**: `merged_ablation_14b_topk50.py` → `results/merged_ablation_14b_topk50.json`

tmux session: `bino_topk50`，日志: `/tmp/bino_topk50.log` 和 `/tmp/ablation_topk50.log`

完成后需要：读取结果 → 写 artifact → register_artifact。可以稍后检查进度。

---
