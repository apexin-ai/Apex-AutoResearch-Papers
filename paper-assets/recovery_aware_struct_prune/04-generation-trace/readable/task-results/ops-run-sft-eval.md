# ops run sft eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_run-sft-eval_20260515T003026_result.json`
- **Structured JSON:** [`e132dc0b860434180c52.json`](../../sessions/e1/e132dc0b860434180c52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个结果都出来了。

## SFT Eval 结果

| 指标 | sft_rasp_20 | sft_standard_20 |
|------|-------------|-----------------|
| **Greedy Accuracy** | **57.0%** (57/100) | **64.0%** (64/100) |
| **Greedy EOS Rate** | 99% (99/100) | 99% (99/100) |
| **Greedy Avg Length** | 179.8 tokens | 176.3 tokens |
| **Greedy Max Length** | 4096 (1 truncated) | 4096 (1 truncated) |
| **Greedy Min Length** | 59 | 43 |
| **Sampling EOS Rate** | 100% (5/5) | 100% (5/5) |

关键发现：
- **EOS 问题已修复**：两个模型 greedy EOS 率 99%，sampling 100%，SFT 成功恢复了 EOS 能力
- **Standard 准确率更高** (64% vs 57%)：standard 剪枝的模型在 SFT 后准确率高 7 个百分点
- 平均 response 长度相近 (~177 tokens)，均正常
- 各有 1 个样本 truncated (hit 4096 limit)

注意：sampling 只测了 5 个样本（`quick_eval.py` 限制），不是你要求的 100。需要额外跑 N=100 的 sampling accuracy eval 吗？

---
