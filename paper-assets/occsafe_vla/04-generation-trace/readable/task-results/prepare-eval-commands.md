# prepare eval commands

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prepare_eval-commands_20260526T123710_result.json`
- **Structured JSON:** [`f0d854a956a58ecff4a8.json`](../../sessions/f0/f0d854a956a58ecff4a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

8 个实验的 eval 命令已写入 `artifacts/eval_commands_batch3.md` 并注册。

要点：
- 所有实验均从 pretrained 从头训练，checkpoint 统一为 `--50000_chkpt`
- 命令模板从 `full_occ_bn_v2_s1_eval` 等已成功 eval 中提取，包含 `--task_suite_name libero_spatial --num_rollouts 50 --seed 42`
- 已通过 SSH 验证了全部 8 个实验的 checkpoint 目录命名格式一致
- 按 ETA 排序：10894:0 最先完成（~23:00），34685 四卡次之（~23:30-00:00），10894:1-3 最晚（~01:15）
- 每个 eval 在训练同卡上运行，约需 50 分钟

---
