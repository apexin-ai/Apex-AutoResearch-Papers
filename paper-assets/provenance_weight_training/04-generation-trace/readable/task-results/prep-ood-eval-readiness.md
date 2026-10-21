# prep ood eval readiness

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_ood_eval_readiness_20260519T181212_result.json`
- **Structured JSON:** [`a233450bbc5c0b56c6b5.json`](../../sessions/a2/a233450bbc5c0b56c6b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

预检完成。总结：

**就绪 (5/7)**：
- OOD 数据：`eval_openwebtext.jsonl` (5000 samples) + `eval_wikipedia.jsonl` (5000 samples) ✅
- FineWeb holdout：`eval_holdout.jsonl` (67,823 samples) ✅
- Eval 脚本：`/root/provenance_weight_training/eval_perplexity.py` ✅
- Uniform checkpoints：seed123 和 seed456 的 `final/` 均已完成 (各 1.2GB) ✅
- GPU 2/3 空闲可立即用于 eval ✅

**等待中 (2/7)**：
- `adaptive_ood_seed123`：step 5797/6103 (~95%)，预计 15-30 分钟完成
- `adaptive_ood_seed456`：step 5809/6103 (~95%)，预计 15-30 分钟完成

**预估 eval 总时间**：4 GPU 并行约 1-1.5 小时。报告和命令模板已写入 `artifacts/ood_eval_readiness.md`。

---
