# analysis r1 distill br gpt41 check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r1-distill-br-gpt41-check_20260521T152210_result.json`
- **Structured JSON:** [`3bf6a235434e8c9beb0e.json`](../../sessions/3b/3bf6a235434e8c9beb0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## 1. R1-Distill Cross-Model Extraction — **已完成**

BPE fix 重提取（R1-Distill-LLaMA-8B traces → Mistral-7B extraction）全部完成：93/93 问题，100% 问题级提取率。

### 完整指标表

| Metric | Value |
|--------|-------|
| **N problems** | 93 |
| **SC accuracy** | 0.7312 |
| **SICA accuracy** | **0.7527** |
| **Δ (SICA−SC)** | **+2.15 pp** |
| Extraction rate | 93.2% (vs 原来自提取 8.3%) |
| Total constraints | 6,364 |
| Unique constraints | 3,726 |
| SICA wrong count | 23 |
| **Mean BR** | **2.63** |
| **Median BR** | **1.74** |
| BR sample size | 12 |
| **Process-κ (TF-IDF cos)** | **0.2522** |
| **Answer Fleiss' κ** | **0.6629** |

关键发现：跨模型提取修复 BPE 问题后，提取率从 8.3% 暴涨到 93.2%，SICA 相比 SC 提升 +2.15pp。BR=2.63 说明 SICA 错的题目中，错误答案的约束权重平均是正确答案的 2.6 倍。

## 2. gpt-4.1 SC 进度 — **未启动**

westd-25068 上没有 gpt-4.1 相关进程或数据。

## 3. Gemini 2.5 Pro SC（正在运行）

- westd-25068 上 `exp_d135_frontier_scb`
- 进度：**10/204**，当前 100% accuracy（前 10 题全对）
- ETA：~8 小时（~495 min）

## 4. gpt-5.5 / o3 — **无数据**

westd-25068 上无相关进程或 intermediates 目录。

---
