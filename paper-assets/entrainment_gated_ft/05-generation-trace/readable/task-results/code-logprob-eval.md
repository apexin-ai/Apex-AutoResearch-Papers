# code logprob eval

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_logprob-eval_20260518T072542_result.json`
- **Structured JSON:** [`af6f55da19bd4dc77c68.json`](../../sessions/af/af6f55da19bd4dc77c68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量评估已在后台运行，3 分钟后自动检查进度。

产出：
1. 脚本已部署到 `/root/entrainment_gated_ft/scripts/eval_logprob.py`
2. Dry-run 验证通过（GatedDeltaNet-pure, D=1: mean_rank=4.1, mean_prob=0.110, 优于 random 的 5.5/0.100）
3. 全量 16 models × 5 depths × 500 samples 正在运行，结果将写入 `/root/entrainment_gated_ft/results/mvp_logprob/`

---
