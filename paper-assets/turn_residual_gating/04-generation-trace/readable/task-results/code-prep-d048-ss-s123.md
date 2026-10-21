# code prep d048 ss s123

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_d048_ss_s123_20260522T235449_result.json`
- **Structured JSON:** [`98b2d951139b3fecbe60.json`](../../sessions/98/98b2d951139b3fecbe60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本均通过 `bash -n` 语法检查。

**产出汇总：**

| 脚本 | 路径 |
|------|------|
| 训练 | `/root/turn_residual_gating/scripts/d048_ss_s123.sh` |
| Eval | `/root/turn_residual_gating/scripts/d048_eval_ss_s123.sh` |

**与 s42 的差异：**
- `--seed 123`（原 42）
- `--output-dir runs/d048_ss_s123`（原 d048_ss_s42）
- eval 脚本中 `CKPT_DIR`、`OUT_ROOT`、`output-name` 均改为 s123
- 其他参数完全一致（`--scheduled-sampling --ss-max-ratio 0.3 --lambda-gar 1.0 --epochs 3` 等）

---
