# research 2025 2026 base models

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_2025-2026-base-models_20260518T070717_result.json`
- **Structured JSON:** [`d3c72a396b47b53d656a.json`](../../sessions/d3/d3c72a396b47b53d656a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

搜索完成。以下是汇总。

---

## 全部候选模型（7B-14B dense base，按推荐度排序）

| 模型 | HF Repo ID | 参数量 | 发布日期 | License | Gated | 训练数据 | MMLU (base) |
|---|---|---|---|---|---|---|---|
| **Qwen3-8B-Base** | `Qwen/Qwen3-8B-Base` | 8.2B | 2025-04 | Apache 2.0 | No | 36T tokens | 79.7 |
| **Qwen3-14B-Base** | `Qwen/Qwen3-14B-Base` | 14.8B | 2025-04 | Apache 2.0 | No | 36T tokens | 81.1 |
| **Phi-4** | `microsoft/phi-4` | 14.7B | 2024-12 | MIT | No | 9.8T tokens | 84.8 |
| **Ministral-3-8B-Base** | `mistralai/Ministral-3-8B-Base-2512` | 8.4B | 2025-12 | Apache 2.0 | No | 未公开 | 70.6 |
| **Ministral-3-14B-Base** | `mistralai/Ministral-3-14B-Base-2512` | ~14B | 2025-12 | Apache 2.0 | No | 未公开 | 79.4 |
| **Gemma 3 12B PT** | `google/gemma-3-12b-pt` | 12B | 2025-03 | Gemma ToU | **Yes** | 12T tokens | 71.9 |
| **OLMo 2 7B** | `allenai/OLMo-2-1124-7B` | 7B | 2024-11 | Apache 2.0 | No | 4T tokens | 63.7 |
| **OLMo 2 13B** | `allenai/OLMo-2-1124-13B` | 13B | 2024-11 | Apache 2.0 | No | 5T tokens | 67.5 |
| **Falcon3-10B-Base** | `tiiuae/Falcon3-10B-Base` | 10B | 2024-12 | Falcon 2.0 | No | 14T+2T | 73.1 |
| **Falcon3-7B-Base** | `tiiuae/Falcon3-7B-Base` | 7B | 2024-12 | Falcon 2.0 | No | 14T tokens | 67.4 |
| **Falcon-H1-7B-Base** | `tiiuae/Falcon-H1-7B-Base` | 7B | 2025 | Open | No | 未公开 | — |
| Qwen2.5-7B | `Qwen/Qwen2.5-7B` | 7B | 2024-09 | Apache 2.0 | No | 18T tokens | 74.2 |
| Qwen2.5-14B | `Qwen/Qwen2.5-14B` | 14B | 2024-09 | Apache 2.0 | No | 18T tokens | 79.7 |
| Mistral-Nemo-12B | `mistralai/Mistral-Nemo-Base-2407` | 12B | 2024-07 | Apache 2.0 | No | 未公开 | 68.0 |
| Llama 3.1 8B | `meta-llama/Llama-3.1-8B` | 8B | 2024-07 | Llama CLA | **Yes** | 15T tokens | 65.6 |
| Yi-1.5-9B | `01-ai/Yi-1.5-9B` | 9B | 2024-05 | Apache 2.0 | No | ~3T tokens | 76.3 |

### 排除的模型
- **Llama 4**: 全部 MoE（Scout 17B active/109B total），无 dense 7B-14B base
- **DeepSeek R2**: 未发布
- **DeepSeek V3/V4**: 671B+ MoE，远超范围
- **DeepSeek-R1-Distill-***: 是 SFT 微调模型，不是 base pretrained model，不适合做 controlled contamination injection
- **Gemma 4**: MoE 架构，无 dense 7B-14B
- **InternLM3-8B**: base checkpoint 未公开发布（仅 instruct）

---

## 推荐

### 1. 最佳 5 模型组合（全部 2024Q4-2025，全部 non-gated）

| Family | 模型 | 理由 |
|---|---|---|
| **Qwen** (Alibaba) | Qwen3-8B-Base | 2025-04，36T tokens，Apache 2.0，MMLU 79.7，直接替代 Qwen 2.5 |
| **Phi** (Microsoft) | Phi-4 | 2024-12，MIT，MMLU 84.8，14.7B 强基线 |
| **Mistral** (Mistral AI) | Ministral-3-8B-Base | 2025-12，Apache 2.0，替代 Mistral v0.3 |
| **OLMo** (Allen AI) | OLMo-2-1124-7B | 完全开源（数据+代码+权重），Apache 2.0，学术可复现性最强 |
| **Falcon** (TII) | Falcon3-10B-Base | 2024-12，14T tokens，MMLU 73.1 |

**优势**：5 个不同机构/家族，全部 non-gated，全部 2024Q4+，覆盖不同训练规模（4T-36T tokens）和能力水平（MMLU 63.7-84.8），审稿人无法质疑模型过时。

**备选**：如果想用 Google 家族替换 Falcon，可选 Gemma 3 12B PT（但 gated）。

### 2. Llama-3.1-8B 的替代

Llama 4 无 dense 7B-14B，所以 Meta 家族无直接替代。最佳替代方案按优先级：

1. **Phi-4** (14.7B) — 不同家族，MIT 开放，性能最强
2. **OLMo-2-7B** — 参数量最接近（7B），完全开源，学术论文天然认可
3. **Falcon3-10B-Base** — 不同家族，non-gated

### 3. Qwen 3 状况

**Qwen3 已发布（2025-04-29）**，有完整的 base 系列。Qwen3-8B-Base 在 36T tokens 上训练，MMLU 79.7（vs Qwen2.5-7B 的 74.2），性能已达 Qwen2.5-14B 水平。**强烈建议用 Qwen3-8B-Base 替换 Qwen 2.5**。技术报告：arXiv 2505.09388。

---

### 实际操作注意

- Phi-4 是 14.7B，bf16 下约 29.4GB，96GB GPU 做 LoRA SFT 无压力
- Ministral-3-8B-Base 是 2025-12 发布，如果论文投稿时间早于此，改用 Mistral-Nemo-Base-2407 (12B, 2024-07)
- OLMo 2 的 MMLU 偏低（63.7），但其完全开源属性在 contamination 研究中是加分项（审稿人重视可复现性）
- Falcon-H1-7B 是 hybrid SSM+Attention 架构，可能引入架构差异混淆因素，建议用 Falcon3 而非 H1

---
