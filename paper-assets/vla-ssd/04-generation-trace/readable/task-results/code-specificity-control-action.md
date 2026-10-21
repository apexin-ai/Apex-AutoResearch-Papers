# code specificity control action

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_specificity_control_action_20260518T182924_result.json`
- **Structured JSON:** [`fd7f772e447dcc1ce658.json`](../../sessions/fd/fd7f772e447dcc1ce658.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交并注册为 RUNNING。

**总结：**
- 脚本 `/root/vla-ssd/scripts/specificity_control_action.py` 已创建
- Bottom-24 heads: `[1,3,4,5,6,7,8,9,11,12,13,15,16,17,18,20,21,23,24,26,28,29,30,31]`（包含全部 control-8 + 16 个次低 instruction attention heads）
- Top-8 excluded: `[0,2,10,14,19,22,25,27]`（instruction attn 0.65-0.86）
- Dry-run 通过，tmux session `specificity_control_action` 运行中
- 3 tasks × 10 demos × 50 timesteps = 1500 samples，预计 ~18 分钟
- 输出: `/root/autodl-tmp/vla-ssd/results/specificity_control_action.json`
- Registry: `specificity_control_action` → RUNNING

---
