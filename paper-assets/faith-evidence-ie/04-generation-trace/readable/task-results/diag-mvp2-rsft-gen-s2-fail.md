# diag mvp2 rsft gen s2 fail

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_mvp2_rsft_gen_s2_fail_20260515T043833_result.json`
- **Structured JSON:** [`3ef9f5a02c0b641e6cfb.json`](../../sessions/3e/3ef9f5a02c0b641e6cfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。以下是诊断报告：

---

## RSFT Generation 诊断报告

### 结论：s1/s2 没有死，它们已正常完成

exit 文件中的 `143|2026-05-15T01:44:04Z` 是**第一次 tmux 启动**的残留记录，不是当前运行的状态。

### 完整时间线

| 时间 (UTC+8) | 事件 |
|---|---|
| 09:31 | 旧的单 shard 运行被 SIGKILL (137/OOM) 杀死，已完成 302 docs |
| 09:39 | 第一次 tmux 启动 s0/s1/s2（[0:756], [756:1512], [1512:2268]）|
| **09:44** | **s0/s1/s2 全部被 SIGTERM 杀死**（启动仅 5 分钟，各只跑了 ~13 docs）|
| 09:40-09:42 | 用 nohup 重启 s0/s1/s2，调整为 [302:984], [984:1665], [1665:2346] |
| 09:49 | s3 通过 tmux 启动 [2346:3027] |
| **12:32** | **s1 正常完成** 681/681 docs（format compliance 99.6%）|
| **12:34** | **s2 正常完成** 681/681 docs（format compliance 100.0%）|

### 各 shard 当前状态

| Shard | 范围 | 状态 | 进度 | GPU |
|---|---|---|---|---|
| s0 | [302:984] 682 docs | **运行中** | 670/682 (98%) | GPU 0, 17.9GB |
| s1 | [984:1665] 681 docs | **已完成** | 681/681 (100%) | - |
| s2 | [1665:2346] 681 docs | **已完成** | 681/681 (100%) | - |
| s3 | [2346:3027] 657 pending | **运行中** | 650/657 (99%) | GPU 3, 19.4GB |

### 09:44 的 SIGTERM 来源

三个 shard 在**完全相同的时间 01:44:04Z** 被杀，说明是**有意的批量终止**——agent-ml 系统或用户主动 kill 了第一批 tmux session，目的是调整 shard 范围（从 [0:756] 改为 [302:984]，跳过旧 run 已完成的 302 docs）。

### 行动建议

- **无需重启 s1/s2**——已跑完
- **s0 和 s3 还有约 20 docs**，按 ~17s/doc 估算，**约 5-10 分钟内全部完成**
- 已有 `rsft_score_filter` 进程 (pid 155566) 在运行，可能需要等 s0/s3 完成后重跑以包含全部数据
- 注意 s1 truncation_rate > 10%（warning），后续可考虑 `--max_new_tokens 3072`

---
