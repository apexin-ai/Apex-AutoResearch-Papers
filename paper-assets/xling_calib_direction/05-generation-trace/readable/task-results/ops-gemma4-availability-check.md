# ops gemma4 availability check

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gemma4-availability-check_20260521T085713_result.json`
- **Structured JSON:** [`710123e2ecbd6b326ddb.json`](../../sessions/71/710123e2ecbd6b326ddb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。汇总如下：

---

## Gemma 4 31B 可获取性报告

### 1. HuggingFace Model ID
| 版本 | Model ID | Gated |
|------|----------|-------|
| Base | `google/gemma-4-31B` | **No** |
| IT | `google/gemma-4-31B-it` | **No** |

注意大写 `B`。Gemma 3 系列 (`gemma-3-27b-it`) 是 `gated=manual` 需人工审批，**Gemma 4 完全开放**。

### 2. ModelScope
`google/gemma-4-31B` 已上架，304,868 次下载，Apache 2.0。国内下载可用。

### 3. License
**Apache 2.0**，无需 Google 许可协议，无需 accept terms。

### 4. 架构

| 属性 | 值 |
|------|-----|
| Architecture | `Gemma4ForConditionalGeneration` (多模态：vision + text) |
| **Dense/MoE** | **Dense** (`enable_moe_block: False`) |
| Text layers | **60** (50 sliding_attention + 10 full_attention，每6层1个full) |
| hidden_size | 5376 |
| intermediate_size | 21504 |
| num_attention_heads | 32 |
| num_key_value_heads | 16 (sliding) / 4 (global) |
| head_dim | 256 (sliding) / 512 (full) |
| vocab_size | 262,144 |
| sliding_window | 1024 |
| max_position_embeddings | 262,144 (256K context) |
| Vision encoder | 27 layers, hidden=1152, patch=16 |
| dtype | BF16 |
| tie_word_embeddings | True |

### 5. 参数量 & 权重大小

| 指标 | 值 |
|------|-----|
| 总参数量 | **32,682,372,656 (~32.7B)** |
| 文本部分 | ~31.3B |
| Vision 部分 | ~1.4B |
| BF16 权重总大小 | **62.5 GB** (2个 shard: 49.8 GB + 12.8 GB) |

### 6. 下载可行性评估

- **无任何访问限制**：Apache 2.0 + 非 gated，可直接下载
- **HuggingFace**：`source /etc/network_turbo` 后可下载，62.5 GB 预计耗时取决于带宽
- **ModelScope**：国内 CDN 速度更快，推荐优先使用
- **显存需求**：BF16 加载需 ~63 GB VRAM；4-bit 量化约 ~18 GB
- **注意**：这是**多模态模型**（含视觉编码器），非纯文本模型。如果只需要文本部分，权重仍含 vision encoder 参数

---
