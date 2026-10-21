# research path b data utilization

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_path_b_data_utilization_20260517T060123_result.json`
- **Structured JSON:** [`1a0b466641e41675804d.json`](../../sessions/1a/1a0b466641e41675804d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入。核心结论：

**所有符合条件的 traces 已 100% 提取完毕。** 8,525/7,007 是 sentence 数不是 trace 数。实际只有 R1-32B=100 条、QwQ=95 条符合 jailbreak+CP 条件的 traces，已全部提取。

瓶颈是数据集规模，不是提取率。扩展 test set 到 n≥40 的最快路径是：调整 train/test split 比例（从 60/20/20 改为 50/10/40），或合并 R1-32B 和 QwQ-32B 数据（两者同为 Qwen2-32B 架构，64 layers，5120 dim）。

---
