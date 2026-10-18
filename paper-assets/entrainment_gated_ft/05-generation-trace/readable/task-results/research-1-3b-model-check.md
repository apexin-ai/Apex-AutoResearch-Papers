# research 1 3b model check

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_1_3b-model-check_20260518T072556_result.json`
- **Structured JSON:** [`76290cbceaf1cdfe1dd0.json`](../../sessions/76/76290cbceaf1cdfe1dd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：1.3B 模型完整可用

### 完整 checkpoint 清单（31 个模型）

**6 种线性注意力架构 × 5 种配置 + 1 个 Transformer baseline：**

| 架构 | pure | 24:1 | 12:1 | 6:1 | 3:1 |
|------|------|------|------|-----|-----|
| GatedDeltaNet | ✅ (1.57k↓) | ✅ | ✅ | ✅ (9↓) | ✅ (14↓) |
| GLA | ✅ (557↓) | ✅ | ✅ | ✅ | ✅ (55↓) |
| HGRN2 | ✅ | ✅ | ✅ (10↓) | ✅ (7↓) | ✅ |
| HGRN | ✅ (5↓) | ✅ (25↓) | ✅ | ✅ | ✅ |
| DeltaNet | ✅ (516↓) | ✅ (6↓) | ✅ (5↓) | ✅ | ✅ (5↓) |
| RetNet | ✅ (519↓) | ✅ (7↓) | ✅ | ✅ | ✅ (16↓) |
| **Transformer** | **✅ baseline (683↓)** | | | | |

训练数据：100B tokens（340M 是 20B tokens）

### 架构参数（GatedDeltaNet 1.3B hybrid-3-1 为例）

| 参数 | 值 |
|------|-----|
| hidden_size | 2048 |
| num_hidden_layers | 24 |
| num_heads | 8 |
| head_dim | 256 |
| hidden_ratio | 4 (→ intermediate ≈ 8192) |
| vocab_size | 32000 |
| max_position_embeddings | 2048 |
| attention layers (3:1) | [2, 5, 8, 11, 14, 17, 20, 23] (8/24 layers) |
| torch_dtype | float32 |

### 磁盘与下载估算

- 单个模型：**~5.6 GB**（F32 safetensors，2 个分片：4.99 GB + 606 MB）
- 我们实验所需子集（GatedDeltaNet + HGRN2 + RetNet × 5 ratios + Transformer baseline = 16 个模型）：**~90 GB**
- 全部 31 个 1.3B 模型：**~174 GB**

### 论文中关于 ICL/function composition 的发现

**论文没有评估 ICL 或 function composition。** 评估任务为：

- **语言建模**：ARC-c, ARC-e, HellaSwag, LAMBADA, OBQA, PIQA
- **Recall**：RULER suite（Single/Multi-Key/Query/Value retrieval, CWE, FWE, QA, VT）

关键发现：**"340M models show insignificant recall capability due to their relatively small parameter count"**，recall 仅在 1.3B 上评估。这直接解释了我们 340M 模型在 function composition 上全部 random chance 的结果。

### 对我们实验的启示

1. **必须升级到 1.3B** — 340M 连 recall 能力都不足，function composition（更难的任务）自然无法完成
2. 论文推荐的最优配置是 **HGRN2 或 GatedDeltaNet，ratio 3:1 到 6:1**，这些应是我们重点关注的 variant
3. 1.3B 模型训练了 100B tokens（5× 于 340M 的 20B），能力差异不仅来自参数量，也来自训练数据量

---
