# code adaptive v2 prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_adaptive_v2_prep_20260514T133217_result.json`
- **Structured JSON:** [`5ae599fb4b9bd0e9a026.json`](../../sessions/5a/5ae599fb4b9bd0e9a026.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**pretrain_weighted.py 已同步到服务器**
- L280: `n_min = max(1, batch_size // 2)` → batch_size=4 时 n_min=2（原来是 3）
- 新增 `unweighted_loss` 日志到 step_metrics.jsonl 和 W&B

**3 个脚本已就绪**（`scripts/run_adaptive_v2_seed{42,123,456}.sh`）
- 路径已修正（`data/scored_data.jsonl`, `models/Qwen/Qwen3-0.6B`, `output/models/`）
- 相比 v1 新增：`--eval_data_path data/human/eval_holdout.jsonl`, `--use_wandb`
- 其他参数与原始 adaptive 实验完全一致（contamination_ratio=0.4, lr=5e-5, 200M tokens → 6103 steps）

**验证结果**
- `batch_size // 2` 确认存在 ✓
- `unweighted_loss` 确认存在 ✓
- `n_min=2` 确认 ✓
- 所有脚本 chmod +x ✓
- 数据/模型/eval 路径均存在 ✓

---
