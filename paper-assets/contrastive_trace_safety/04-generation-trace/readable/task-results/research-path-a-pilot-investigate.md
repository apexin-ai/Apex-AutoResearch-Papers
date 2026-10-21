# research path a pilot investigate

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_path_a_pilot_investigate_20260517T052318_result.json`
- **Structured JSON:** [`180eb5b47ea079325248.json`](../../sessions/18/180eb5b47ea079325248.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Pilot 结果总结

### Phase 1: 数据调查

| 项目 | 结果 |
|------|------|
| HarmThoughts 总样本 | 56,931 |
| 模型 | r1-8b (14,746), r1-32b (8,525), QwQ (7,007), ot-7b (26,653) |
| **R1-Distill-Qwen-7B 在数据集中** | **不存在** |
| r1-8b jailbreak queries | 265 个唯一 query |
| 当前 hidden states | R1-8B: 268, R1-32B: 101, QwQ-32B: 96 |

### Phase 2: 7B 模型可行性

| 项目 | 结果 |
|------|------|
| 模型 | deepseek-ai/DeepSeek-R1-Distill-Qwen-7B |
| 模型大小 | ~15.2GB (2 shards: 6.6GB + 8.6GB) |
| GPU 占用 | 15.4GB / 98GB VRAM |
| 架构 | Qwen2-7B, 28 layers, hidden_dim=3584 |

### Phase 3: Pilot 结果 (关键发现)

| 指标 | 结果 |
|------|------|
| **Jailbreak rate** | **0/10 (0%)** |
| `&lt;think>` tags | **无** — 模型不产生 think tags |
| Safety reasoning | 0/10 |
| Direct compliance | 4/10 (直接执行有害请求，无安全推理) |
| Avg response length | ~7,337 chars |
| CoT 风格 | "Okay, so I..." 式思考，但无显式分隔 |

### 问题分析

R1-Distill-Qwen-7B 的行为与 R1-8B **截然不同**：

1. **无 `&lt;think>` tags** — 输出是一个连续的 CoT 流（"Okay, so I'm trying to figure out..."），没有 think/answer 分离
2. **无 self-jailbreak 模式** — 不存在"safety commitment → 继续生成有害内容"的转折，模型要么直接 comply，要么 refuse
3. **可能原因**：chat template 未正确触发 thinking 模式；或此模型的 distillation 未保留 think tag 行为

### 可行性判断

**当前形式不可用**。需要进一步调查：
- 检查 tokenizer chat template 是否正确触发 thinking mode（可能需要加 system prompt 或调整 generation 参数）
- 对比 R1-8B 的 prompt format（HarmThoughts 中 R1-8B 的 traces 确实有 "Okay, so..." 开头的 CoT，说明原始数据生成时可能使用了不同 prompt 策略）
- 如果调整 prompt 后仍无 think tags 和 self-jailbreak 行为，则此模型不适用于当前实验框架

是否需要我进一步调查 prompt format 或尝试其他方式触发 thinking 行为？

---
