# diagnosis exp062 final4 status

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp062_final4_status_20260521T170621_result.json`
- **Structured JSON:** [`5d891a4e9604209673ee.json`](../../sessions/5d/5d891a4e9604209673ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态汇总：

**1. Mistral-7B topk — DONE ✓**
- 4851 chains, features 已提取, Cohen's d 已计算
- **Shape=PASS** (entropy_max=0.064, entropy_min=0.013, tail_decay=0.123)
- **Drift=PASS** (entropy_mean=0.697, TTR=0.644, hapax=0.668)
- Mistral-7B 在 top-k 下仍保留完整 depth fingerprint，与 LLaMA 和 Qwen3-1.7B 一致

**2. Qwen3-0.6B topk — 运行中 (40%)**
- 1956/~4850 行，GPU 3 上运行，ETA ~05:00-06:00 CST

**3. Qwen3-8B greedy — 运行中 (38%)**
- 1833/~4850 行，GPU 1 上运行，ETA ~04:00 CST

**4. Qwen3-8B topk — 排队中**
- greedy 完成后自动启动，ETA ~08:00-09:00 CST

Feature watcher 工作正常，已完成 Mistral 提取，正在等待后续 combo。

**进度：13/16 combos 有 Cohen's d，最后 3 个预计 ~09:00 CST 全部完成。**

已更新文件：
- `exp062_final4_status.txt` — 完整状态报告
- `decoding_cohens_d_all.txt` — 添加 Mistral-7B top-k 行（13/16）
- `exp062_cohens_d_summary.txt` — 添加 Mistral-7B top-k 摘要

---
