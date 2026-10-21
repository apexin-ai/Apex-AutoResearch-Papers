# code action trajectory control

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_action_trajectory_control_20260518T113458_result.json`
- **Structured JSON:** [`e8f723f30e434b112716.json`](../../sessions/e8/e8f723f30e434b112716.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交。总结：

- **脚本**: `/root/vla-ssd/scripts/action_trajectory_control.py`
- **改动**: `CONTROL_HEADS_8 = [3, 5, 6, 9, 13, 21, 24, 28]`，ablation 描述改为 `L1_non_instruction_8_heads_zeroed`，输出文件 `action_trajectory_control.json`
- **Dry-run**: 通过，control heads ablation 几乎不影响 action（paired_mse≈0, token_div=0），与 instruction heads 的结果形成对照
- **任务**: `action_trajectory_control` 运行在 cuda:0，timeout 2h，日志在 `/root/autodl-tmp/vla-ssd/results/action_trajectory_control.log`

---
