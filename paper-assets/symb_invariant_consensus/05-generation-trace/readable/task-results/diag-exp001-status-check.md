# diag exp001 status check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp001-status-check_20260516T184614_result.json`
- **Structured JSON:** [`de7c080504121831e7d5.json`](../../sessions/de/de7c080504121831e7d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### exp-001：仍在运行 (PID 181491)

结果文件 `sica_expanded_14b.json` 持续更新中（最后修改 0.3 分钟前）。

**当前进度**：
| 指标 | 值 |
|------|-----|
| 已完成问题数 | **785** |
| SICA 准确率 | **76.31%** |
| SC (Self-Consistency) 准确率 | 76.05% |
| SICA 提升 | +0.26% (599 vs 597 correct) |
| 约束提取率 | 88.78% |
| 矛盾检出率 | 2.25% (327/785 problems) |
| 总约束提取数 | 86,957 (unique: 16,853) |

结果目录为单文件 `results/sica_expanded_14b.json`（3.1MB），非 per-question 子目录。

---

### 模型下载状态

| 模型 | 状态 |
|------|------|
| **Mistral-7B-Instruct-v0.3** | 完成 (3 shards) |
| **Llama-3.1-8B-Instruct** | 完成 (4 shards) |
| **DeepSeek-R1-Distill-Llama-8B** | 完成 (2 shards, 15GB) |
| Qwen2.5-14B-Instruct | 已存在 |
| QwQ-32B | 已存在 |
| Qwen3-32B-AWQ | 已存在 |

所有模型下载均已完成，safetensors 文件齐全。

---
