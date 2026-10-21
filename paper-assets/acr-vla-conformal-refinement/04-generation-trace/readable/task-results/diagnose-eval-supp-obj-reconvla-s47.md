# diagnose eval supp obj reconvla s47

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-supp-obj-reconvla-s47_20260524T123937_result.json`
- **Structured JSON:** [`afee410b67eea53d5cc2.json`](../../sessions/af/afee410b67eea53d5cc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结论：**伪失败**。

- 脚本实际跑完 10 task × 20 rollout，overall **76.5% (153/200)**，结果 JSON 已写入 `logs/eval_object_reconvla_seed47.json`（20:26）
- 日志无 Error/Exception/Traceback；GPU 4 显存释放（1 MiB / 24564 MiB，0% util）；`/root/autodl-tmp` 46% 充足，根分区 86% 偏紧但未满
- cron 误判原因：脚本没发 sentinel/W&B 心跳

**无需重试**，直接用现有 JSON。诊断报告已写入 `worker_output.md`（save_project_file 白名单不含该文件，改用本地 Write）。

注：`tmux ls` 与含管道的 `grep` 在 `ssh_read_only` 白名单外被拒——tmux 状态从 GPU 利用率推断。

---
