# code extract l1 attention data

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_extract_l1_attention_data_20260517T081258_result.json`
- **Structured JSON:** [`9c21f1c87c530cca4409.json`](../../sessions/9c/9c21f1c87c530cca4409.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## L1 精确数值

### trained L1
| 字段 | 值 |
|---|---|
| n_instruction_dominant | 24 |
| mean_text_attn | 0.5729 |
| mean_image_attn | 0.2173 |
| mean_bos_attn | 0.2098 |
| per_head_text_attn | [0.8589, 0.5308, 0.6857, 0.4749, 0.5781, 0.4976, 0.4083, 0.5673, 0.5797, 0.43, 0.7138, 0.5671, 0.5216, 0.4147, 0.704, 0.6226, 0.5382, 0.529, 0.5196, 0.65, 0.5185, 0.4537, 0.8264, 0.5683, 0.3657, 0.7706, 0.5614, 0.6854, 0.4949, 0.5971, 0.543, 0.5552] |

### llama2base L1
| 字段 | 值 |
|---|---|
| n_instruction_dominant | 9 |
| mean_text_attn | 0.3627 |
| mean_image_attn | 0.6106 |
| mean_bos_attn | 0.0267 |
| per_head_text_attn | [0.5806, 0.2172, 0.3154, 0.2547, 0.2543, 0.1904, 0.2234, 0.2305, 0.2378, 0.1894, 0.3154, 0.2526, 0.2098, 0.4152, 0.339, 0.6021, 0.5381, 0.7711, 0.5301, 0.2532, 0.2266, 0.1911, 0.1412, 0.5898, 0.2522, 0.8287, 0.5397, 0.8955, 0.2846, 0.2525, 0.2778, 0.2049] |

### untrained L1
| 字段 | 值 |
|---|---|
| n_instruction_dominant | 0 |
| mean_text_attn | 0.0778 |
| mean_image_attn | 0.9187 |
| mean_bos_attn | 0.0036 |
| per_head_text_attn | [0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778, 0.0778] |

注意：untrained 的 32 个 head 的 text_attn 全部相同（0.0778），说明 untrained 模型在 L1 没有任何 head 级别的分化。

---
