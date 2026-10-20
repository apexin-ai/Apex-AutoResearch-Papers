# fix gemma2 s0 clean restart

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gemma2-s0-clean-restart_20260520T094657_result.json`
- **Structured JSON:** [`08e27a44c82f641c7635.json`](../../sessions/08/08e27a44c82f641c7635.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**根因找到了。** PID 314035 就是之前"被 SIGTERM"的那个 gemma2 s0 训练进程——**它没死。** SIGTERM 杀掉了 tmux wrapper，但 python 子进程存活并继续训练，已加载 95GB 到 cuda:1。

时间线：
- 17:47:10 — PID 314035 启动 gemma-2-9b d000 s0 训练
- 17:47:23 — 我第一次 nvidia-smi 时它还在加载权重（显存仅 3MiB，看起来"空闲"）
- 17:48:xx — 我们提交了 v2（PID 315220），两个进程碰撞在 cuda:1 上

另外 cuda:0 上有一个 phi-4 d050 s0 训练（PID 313782，55GB），也是新出现的。

**两个进程写同一 output dir (`gemma-2-9b_d000_s0`)，有数据腐败风险。**

建议：
1. 杀掉我们刚提交的 PID 315220（仅 550MB，无损失）
2. PID 314035 已经在训练，但它是孤儿进程（无 tmux 管理）。两个选择：
   - **保留 314035**：已加载 95GB，让它跑完，但没有 tmux session 做 lifecycle 管理
   - **全杀重来**：kill 314035 + 315220，干净重提交

你要哪个方案？

---
