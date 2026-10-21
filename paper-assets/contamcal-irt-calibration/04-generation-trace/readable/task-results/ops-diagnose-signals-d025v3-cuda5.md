# ops diagnose signals d025v3 cuda5

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-signals-d025v3-cuda5_20260516T034826_result.json`
- **Structured JSON:** [`b3404e17abfed40f9f1a.json`](../../sessions/b3/b3404e17abfed40f9f1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### Part 1: d025_v3_s42 信号 — 全部完成 ✓

日志末尾 `ALL_DONE Sat May 16 10:58:37`，9/9 信号文件完整：

| Signal | mmlu | gsm8k | arc_challenge |
|--------|------|-------|---------------|
| s1_embedding | 7.8MB ✓ | 734KB ✓ | 664KB ✓ |
| s2_minkpp | 2.9MB ✓ | 272KB ✓ | 250KB ✓ |
| s4_selfcritique | 3.4MB ✓ | 317KB ✓ | 290KB ✓ |

Registry 已更新 conclusion=success。

### Part 2: 0.5B s123 批次 — 有问题

**cuda:5 状态**：PID 687036 正在运行 `compute_signals.py` for `Qwen2.5-0.5B_d000_s123`，benchmark=mmlu，signal=all。GPU 占用 1606MiB/24564MiB。

**已完成文件**：仅 `d000_s123` 的 s1_embedding_mmlu 和 s2_minkpp_mmlu（2 个文件），当前应在计算 s4_selfcritique_mmlu。

**关键问题**：批次日志显示 `run_05B_s123_signals.sh: No such file or directory`（EXIT_CODE=127）。当前 PID 687036 不是批次脚本启动的，是单独运行的 d000_s123/mmlu。**批次脚本不存在，d000_s123/mmlu 完成后不会自动继续其余 11 个子任务。**

进度：约 1/12 子任务进行中（d000_s123/mmlu 的 s4 阶段）。需要创建批次脚本或手动依次提交剩余任务。

---
