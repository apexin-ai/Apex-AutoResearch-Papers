# ops watcher check m1 combine

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_watcher_check_m1_combine_20260516T030529_result.json`
- **Structured JSON:** [`4dbc5116a53d47aebd16.json`](../../sessions/4d/4dbc5116a53d47aebd16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部任务完成。汇总报告：

---

## 汇总报告

### 1. Watcher PID 966920 — ALIVE，尚未触发

- 进程存活：`bash /root/structfuse/watch_and_chain_qwen_s42.sh`（May 14 启动）
- s42 supplement chain **未启动**：`embedding_distance_s42/` 和 `dataflow_aware_s42/` 目录均不存在
- 原因：Qwen 主链尚未完成（当前在 dataflow_aware_s44，还有 bm25_s43 + bm25_s44）

### 2. M1 合并 — 成功

| 指标 | 值 |
|---|---|
| Total instances | 44,173 |
| With structural data | 39,750 (**90.0%**) |
| Remaining errors | 241 |
| codeql extraction | 39,730 (89.9%) |
| beniget fallback | 4,202 (9.5%) |
| Replaced | 28,035 / 28,276 errors |
| 文件大小 | 6.2GB → **34GB** |
| 磁盘剩余 | 48GB (81% used) |

structural_data_rate **90.0%**，与 dry-run 的 89.9% 一致。Stats 已写入 `artifacts/m1_final_stats.json`，原文件备份为 `all.jsonl.bak`。

### 3. Qwen (cuda:0) — dataflow_aware_s44, epoch 1 step 50/1408

- PID 337267 ALIVE
- GPU 0: 100% util, 49.5GB/97.9GB VRAM
- 主链进度：7/9 subruns（已完成 random×3 + embed×2 + df_s43）
- 当前 subrun 刚开始（~1.8%），预估 ~11h → **ETA ~22:00 今天**
- 主链剩余：dataflow_aware_s44 + bm25_s43 + bm25_s44 ≈ **33h → 主链完成 ~May 17 20:00**
- 之后 watcher 自动触发 s42 supplement chain（3 subruns ~33h → ~May 19 05:00）

### 4. StarCoder (cuda:1) — embedding_distance_s43, epoch 1 step 200/1405

- PID 519791 ALIVE
- GPU 1: 100% util, 53.5GB/97.9GB VRAM
- 链进度：5/10（已完成 random×3 + bm25_s42 + embed_s42）
- 当前 subrun ~7.1%，每 subrun ~9h → **当前 ETA ~19:00 今天**
- 剩余 5 subruns（embed_s44 + df×3）≈ **45h → 全部完成 ~May 18 ~16:00**

---
