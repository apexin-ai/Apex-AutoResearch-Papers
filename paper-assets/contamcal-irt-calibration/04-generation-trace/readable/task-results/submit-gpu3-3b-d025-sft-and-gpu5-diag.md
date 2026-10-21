# submit gpu3 3B d025 sft and gpu5 diag

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_gpu3_3B_d025_sft_and_gpu5_diag_20260514T154149_result.json`
- **Structured JSON:** [`bf6472eaf05151a5d87c.json`](../../sessions/bf/bf6472eaf05151a5d87c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`submit_training_job` MCP 工具在当前 session 不可用，需要用 `ssh_execute` + tmux 模式手动提交。

## 三个任务状态总结

**Task B (cuda:5 调查)**：✅ 已完成。cuda:5 当前 0 MiB，无任何进程。用户说的 8.3GB 进程已消失。

**Task C (0.5B d025 aligned eval)**：⚠️ **已在 cuda:3 上运行**。
- tmux session: `exp_001_eval_05B_d025_aligned`
- PID 398501，命令与你给的完全一致
- MMLU 已完成 (28.03%, 14042 items)，正在跑 GSM8K
- 预计 ~10min 内全部完成

**Task A (3B d025 SFT)**：🚫 cuda:3 被 Task C 的 eval 占用（C001 约束不允许提交）。
- **cuda:5 空闲可用** — 是否改在 cuda:5 提交 3B d025 SFT？

请确认：
1. Task A 改用 cuda:5？
2. Task C 既然已在运行，是否还需要提交 v2？还是等当前这个跑完即可？

---
