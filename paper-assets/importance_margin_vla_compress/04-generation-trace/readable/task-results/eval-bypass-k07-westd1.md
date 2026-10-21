# eval bypass k07 westd1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_bypass_k07_westd1_20260517T033420_result.json`
- **Structured JSON:** [`1bdae9562729d950645f.json`](../../sessions/1b/1bdae9562729d950645f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**已启动 k=0.7 bypass eval**
- PID: 876957
- GPU: cuda:1 @ westd-27271
- tmux session: `eval_k07_bypass_v2`
- Log: `~/runs/importance_margin_vla_compress/eval_k07_bypass_v2.log`
- Output: `eval_results/eval_imm_k07_bypass_object.json`
- Registry: `eval_k07_bypass_v2` → RUNNING

**确认事项：**
- Checkpoint: 879MB，存在且完整
- Config `k_ratio: 0.7` 确认正确（注释 "Retain 50%" 是旧注释未更新，实际值 0.7）
- Mode: `baseline`（跳过 ACIS wrapper，全 token forward，即 bypass）

**异常记录：**
- 首次提交失败因 `python: command not found`（tmux 下 PATH 不含 conda），已用 `source activate` 重新提交
- 旧失败 entry `eval_k07_bypass` 仍在 registry 中（PREPARING 状态），可后续清理

---
