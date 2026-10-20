# code d048 gradnorm script

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d048_gradnorm_script_20260522T115016_result.json`
- **Structured JSON:** [`9018084c1322a11128f8.json`](../../sessions/90/9018084c1322a11128f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建，`chmod +x` 完成，语法检查通过。路径：`/root/turn_residual_gating/scripts/d048_gradnorm_s42.sh`

与参考脚本格式一致，额外包含 `--gradnorm --gradnorm-alpha 1.5 --gradnorm-lr 0.025`，使用 `train_phase2_gradnorm.py`，输出到 `runs/d048_gradnorm_s42`。同时保留了参考脚本中的 `--model`、`--lr`、`--batch-size`、`--grad-accum` 等参数。

---
