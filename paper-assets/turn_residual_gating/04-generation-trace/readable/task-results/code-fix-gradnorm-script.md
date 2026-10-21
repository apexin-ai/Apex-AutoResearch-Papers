# code fix gradnorm script

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_gradnorm_script_20260522T115310_result.json`
- **Structured JSON:** [`f9d840f15cd5f62190d4.json`](../../sessions/f9/f9d840f15cd5f62190d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项验证全部通过：

1. **脚本内容** — `--gar-loss-mode mse_target` 已替换，`--lambda-gate-div 1.0` 已添加在 `--lambda-gar` 之后
2. **语法检查** — `bash -n` 返回 0，无语法错误
3. **参数对比** — 与 `d048_tg_s123.sh` 比较，共享参数完全一致（model、gate-type、gar-loss-mode、gar-target、lambda-gar、lambda-gate-div、init-bias、gate-lr-multiplier、min-gate-std、max-seq-len、epochs、lr、batch-size、grad-accum、data-dir），仅有预期差异：
   - gradnorm 脚本多了 `--gradnorm`、`--gradnorm-alpha 1.5`、`--gradnorm-lr 0.025`
   - 训练脚本为 `train_phase2_gradnorm.py` vs `train_phase2.py`
   - seed/output-dir 不同

---
