# ops check eval status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-eval-status_20260515T005053_result.json`
- **Structured JSON:** [`687c81cd8aefa5a791d8.json`](../../sessions/68/687c81cd8aefa5a791d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两组 eval 都已完成。汇总结果：

## SFT Eval 完整结果 (N=100 greedy + N=5 sampling EOS test)

| Metric | sft_rasp_20 | sft_standard_20 |
|--------|-------------|-----------------|
| **Greedy Accuracy** | **57.0%** (57/100) | **64.0%** (64/100) |
| Greedy EOS Rate | 99.0% (99/100) | 99.0% (99/100) |
| Greedy Natural EOS | 99 | 99 |
| Greedy Truncated (hit 4096) | 1 | 1 |
| Greedy Avg Response Len | 180 tokens | 176 tokens |
| Greedy Max/Min Len | 4096 / 59 | 4096 / 43 |
| **Sampling EOS Rate (T=0.7)** | **100%** (5/5) | **100%** (5/5) |
| Sampling Avg Len | 132 tokens | 145 tokens |

**关键发现**：
1. **EOS 行为完全健康** — 两个模型 greedy 99% + sampling 100% 正常终止，GRPO 不会遇到 EOS 问题
2. **Standard 比 RASP 高 7 个点** (64% vs 57%) — 这是剪枝后 SFT 恢复的差距
3. 两个模型只有 1/100 样本 truncated，说明模型不会陷入无限生成

**注意**：sampling mode 只测了 5 样本的 EOS 率，未测 N=100 的 sampling accuracy。如果 gate check 需要 sampling 精度数据，需要额外跑一轮。但 EOS 行为已经确认健康，可以作为 GRPO Stage 2 的 go/no-go 依据。

---
