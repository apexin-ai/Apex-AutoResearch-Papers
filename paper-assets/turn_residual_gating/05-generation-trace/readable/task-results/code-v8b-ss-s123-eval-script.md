# code v8b ss s123 eval script

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v8b_ss_s123_eval_script_20260521T152221_result.json`
- **Structured JSON:** [`c1228a68775ea3d470c3.json`](../../sessions/c1/c1228a68775ea3d470c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建并通过语法检查。

`/root/turn_residual_gating/scripts/eval_v8b_ss_s123.sh` 包含：
- **TF eval** (4 runs): Base × {ours, Dongre} + v8b-SS-s123 × {ours, Dongre}，使用 `ultrachat_eval_heldout.json`
- **AR eval** (4 runs): 同上 4 组，无 conversations-path（自回归生成）
- **PPL summary**: 自动从结果 JSON 提取 avg_ppl 汇总
- Checkpoint: `checkpoints/tg_v8b_ss_s123/epoch_2/`
- 输出: `runs/eval_v8b_ss_s123/`
- 参数与 s42 eval 完全一致（`--gate-profile`, gate-type threadgate）

---
