# research keydiff details

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_keydiff_details_20260512T172753_result.json`
- **Structured JSON:** [`916c5fa9c144c53409ff.json`](../../sessions/91/916c5fa9c144c53409ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是 KeyDiff 论文精确实验条件的汇总。

---

## KeyDiff (arXiv:2504.15364) 实验条件汇总

### 1. 模型

| 模型 | 参数量 | 用途 |
|------|--------|------|
| Llama 3.1-8B-Instruct | 8B | 主实验 (LongBench) |
| Llama 3.2-3B-Instruct | 3B | 主实验 (LongBench) |
| Qwen 2.5-3B-Instruct | 3B | 附录 (Table 9, 未在 HTML 中完整展示) |
| Qwen 2.5-7B-Instruct | 7B | 附录 (Table 9) |
| Deepseek-R1-Distill-Llama-8B | 8B | Math500 (仅在 abstract 提及, 正文/附录未找到详细数据) |

### 2. 评测数据集

**LongBench (English subset, 16 tasks):**
- Single Doc QA: NarrativeQA, Qasper
- Multi Doc QA: MultifieldQA-en, HotpotQA, 2WikiMQA, Musique
- Summarization: GovReport, QMSum, MultiNews
- Few-shot: TREC, TriviaQA, SAMSum
- Synthetic: PassageCount, PassageRetrieval-en
- Code: LCC, RepoBench-P

**其他:** Needle In a Haystack, Math500 (仅 abstract 提及)

### 3. KV Cache Budget

| Budget | Token 数 | 近似压缩比 (基于 LongBench 平均) |
|--------|----------|--------------------------------|
| 2K | 2048 | ~80% reduction |
| 4K | 4096 | ~55% reduction |
| 6K | 6144 | ~33% reduction |
| 8K | 8192 | **~23% reduction** |

Block size: B=128 (prompt processing), B=1 (generation)。51% 的 LongBench prompt 长度超过 8K。

### 4. "<0.04% loss" 精确含义

**论文原文：** "a performance gap of less than 0.04% with 8K cache budget (~23% KV cache reduction) from the non-evicting baseline on LongBench for Llama 3.1-8B and Llama 3.2-3B"

**但实际表格数据存在不一致：**

| 模型 | Full Context | KeyDiff@8K | 绝对差 (pp) | 相对差 |
|------|-------------|------------|-------------|--------|
| Llama 3.1-8B | 49.20 | 49.03 | **0.17 pp** | **0.35%** |
| Llama 3.2-3B | 45.87 | 45.78 | **0.09 pp** | **0.20%** |

- **度量：** LongBench 各任务平均分 (各任务有自己的 metric，综合后取均值)
- **0.04% 与表格数据不匹配** — 可能指特定 subset、附录中的 full-prompt-processing (B=∞) 配置 (Table 7)，或者 abstract 的表述有误。HTML 版未完整展示附录表格，无法最终确认。

### 5. Centroid (Anchor) 计算方式

**公式：**
$$\mu(\hat{K}) = \frac{1}{n}\sum_{i=1}^{n} \frac{k_i}{\|k_i\|}$$

- **先对每个 key 做 L2 归一化，再取算术平均** — 即 exact mean of normalized keys
- 论文**未明确说明**是 per-step 重新计算还是 running mean (incremental)
- 由于是简单均值，理论上可用 running sum 增量维护：`sum += new_key/||new_key||; sum -= evicted_key/||evicted_key||; anchor = sum/n`
- **复杂度：O(n) per eviction step** (n = cache size)，计算所有 token 与 anchor 的 cosine similarity 以选出要驱逐的 token

**Ablation (Llama 3.2-3B, Table 2) — anchor 选择方式对比：**

| Budget | Pairwise | Median | KeyDiff (Mean) |
|--------|----------|--------|----------------|
| 2K | 35.24 | 35.43 | 35.09 |
| 4K | 40.61 | 40.67 | 40.28 |
| 6K | 41.87 | 41.89 | 41.88 |
| 8K | 42.45 | 42.26 | 42.40 |

差异很小，Mean 方案在大 budget 下接近其他方案，但计算最简单。

### 6. Baseline 对比 (主表)

**Llama 3.1-8B-Instruct, LongBench Average, B=128:**

| Budget | H2O | TOVA | StreamingLLM (Sink) | SnapKV | **KeyDiff** | Full Context |
|--------|-----|------|---------------------|--------|-------------|-------------|
| 2K | 16.89 | 37.52 | 36.88 | 39.60 | **44.33** | 49.20 |
| 4K | 26.37 | 41.49 | 40.95 | 45.18 | **47.66** | 49.20 |
| 6K | 33.19 | 45.24 | 43.39 | 47.12 | **48.51** | 49.20 |
| 8K | 38.20 | 47.09 | 44.68 | 48.06 | **49.03** | 49.20 |

**Llama 3.2-3B-Instruct, LongBench Average, B=128:**

| Budget | H2O | TOVA | StreamingLLM (Sink) | SnapKV | **KeyDiff** | Full Context |
|--------|-----|------|---------------------|--------|-------------|-------------|
| 2K | 14.25 | 33.52 | 33.74 | 35.46 | **38.14** | 45.87 |
| 4K | 22.38 | 38.24 | 37.96 | 40.60 | **43.67** | 45.87 |
| 6K | 28.44 | 41.02 | 40.01 | 43.55 | **45.27** | 45.87 |
| 8K | 33.46 | 43.21 | 41.97 | 44.96 | **45.78** | 45.87 |

**Similarity metric ablation (Table 3, Llama 3.2-3B):**

| Budget | Dot Product | Euclidean | **Cosine (KeyDiff)** |
|--------|------------|-----------|---------------------|
| 2K | 30.14 | 13.68 | **35.09** |
| 4K | 38.01 | 21.06 | **40.28** |
| 8K | 42.23 | 29.53 | **42.40** |

### 7. 缺失/不完整数据

| 信息 | 状态 |
|------|------|
| Deepseek-R1 + Math500 精确数字 | **仅 abstract 提及 "near baseline"，正文无详细表格** |
| 延迟 "up to 30% speedup" 具体数据 | **仅 abstract 提及，正文无 latency 表格** |
| Qwen 2.5-3B/7B 完整结果 | **在附录 Table 9，HTML 版未完整渲染** |
| Full prompt processing (B=∞) 结果 | **在附录 Table 7，HTML 版未完整渲染** |
| 0.04% claim 的精确来源 | **与主表数据不一致，可能来自未展示的附录表** |

---

**核心结论：** KeyDiff 在所有 budget 下均优于 H2O、TOVA、StreamingLLM、SnapKV。8K budget 下与 full context 的差距为 0.17pp (Llama-8B) / 0.09pp (Llama-3B)。Anchor 是 normalized keys 的 exact mean，O(n) 复杂度。Abstract 中的 "0.04%"、"30% latency"、"Math500" 三项 claim 在论文正文中均未找到支撑数据表格。

Sources:
- [KeyDiff Paper (arXiv abstract)](https://arxiv.org/abs/2504.15364)
- [KeyDiff Paper (HTML full text)](https://arxiv.org/html/2504.15364v1)
- [AlphaXiv page](https://www.alphaxiv.org/abs/2504.15364)

---
