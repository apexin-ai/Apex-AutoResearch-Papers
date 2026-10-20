# infra westd25068 network gpu saturation

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd25068-network-gpu-saturation_20260518T173821_result.json`
- **Structured JSON:** [`a5b6b103cfac3b016992.json`](../../sessions/a5/a5b6b103cfac3b016992.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**GPU 利用率：12.5% → 100%**（~15 分钟内完成）

| GPU | 实验 | 模型 | 数据集 | 利用率 |
|-----|------|------|--------|--------|
| cuda:0 | exp-033 | Mistral-7B | FOLIO-204 | 96% |
| cuda:1 | exp-034 | Qwen2.5-14B | ProofWriter-600 | 98% |
| cuda:2 | exp-028 | Qwen3-14B thinking | FOLIO-204 | 97% |
| cuda:3 | exp-035 | Qwen2.5-7B | FOLIO-204 | 97% |

**exp-027 关键结果**：Qwen3-14B non-thinking FOLIO-204 SICA=**84.31%**，比 Qwen2.5-14B (74.51%) 高 +9.8pp。

**修复的问题**：HF 镜像设置、Llama-3.1-8B 权重不完整（重新下载中）、conda PATH 问题（改用绝对路径）。

**5 个模型在后台下载中**（DeepSeek-R1-Distill-Llama-8B、deepseek-r1-0528-qwen3-8b、gemma-3-27b-it、phi-4-reasoning、Llama-3.1-8B 重新下载）。

---
