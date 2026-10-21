# analysis text match dstudy

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_text_match_dstudy_20260520T190911_result.json`
- **Structured JSON:** [`d4f278e1f3f0cb2b7557.json`](../../sessions/d4/d4f278e1f3f0cb2b7557.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下：

---

## 1. 当前 G 系数

| 指标 | G 系数 | σ²(τ) | σ²(δ) |
|------|--------|--------|--------|
| **text_exact_match** | **0.9749** | 0.02724 | 0.00070 |
| correct (对比) | **0.3570** | — | — |

text_exact_match 的 G = 0.975，远高于 correct 的 0.357。说明在当前设计 (3 prompts × 3 seeds × 2 orderings × 50 items) 下，text_exact_match 的测量已经非常可靠，模型间差异相对于误差方差占绝对主导。

## 2. Per-facet Sweep (n=1→20)

| n | prompt_template | seed | ordering | item_id |
|---|----------------|------|----------|---------|
| 1 | 0.9354 | 0.9701 | 0.9712 | **0.5003** |
| 2 | 0.9647 | 0.9737 | 0.9749 | 0.6656 |
| 3 | 0.9749 | 0.9749 | 0.9761 | 0.7480 |
| 5 | 0.9831 | 0.9758 | 0.9771 | 0.8302 |
| 10 | 0.9895 | 0.9765 | 0.9778 | 0.9048 |
| 15 | 0.9916 | 0.9767 | 0.9781 | 0.9327 |
| 20 | 0.9927 | 0.9769 | 0.9782 | 0.9473 |

**关键发现**：
- **item_id 是唯一真正重要的 facet** — 从 n=1 的 0.50 到 n=50 的 0.975，影响巨大
- **prompt_template 次之** — n=1→3 有明显提升 (0.935→0.975)，之后收益递减
- **seed 和 ordering 几乎无影响** — 即使 n=1 也已 >0.97，增加复制数收益极小

## 3. 最低复制数

| 目标 G | prompt_template | seed | ordering | item_id |
|--------|----------------|------|----------|---------|
| ≥ 0.80 | 1 | 1 | 1 | **5** |
| ≥ 0.85 | 1 | 1 | 1 | **6** |
| ≥ 0.90 | 1 | 1 | 1 | **10** |
| ≥ 0.95 | 2 | 1 | 1 | **22** |
| ≥ 0.99 | 11 | >100 | >100 | >100 |

G≥0.90 只需 1 prompt × 1 seed × 1 ordering × 10 items。G≥0.99 对 seed/ordering/item_id 单独增加都不够（>100），需多 facet 联合提升。

## 4. 最优 facet 分配方案

| 方案 | prompts | seeds | orderings | items | G |
|------|---------|-------|-----------|-------|---|
| 当前 MVP | 3 | 3 | 2 | 50 | 0.9749 |
| 经济型 G≥0.90 | **1** | **1** | **1** | **10** | 0.905 |
| 推荐 G≥0.95 | **2** | **1** | **1** | **25** | ~0.95 |
| 高可靠 G≥0.99 | 10 | 5 | 3 | 100 | 0.9945 |
| 极致 | 20 | 15 | 10 | 200 | 0.9978 |

**推荐**：当前 MVP 设计已非常充裕。如需降低成本，可缩减到 2 prompts × 1 seed × 1 ordering × 25 items 即可达 G≥0.95。

## 5. text_exact_match vs correct 对比解读

| 维度 | text_exact_match (G=0.975) | correct (G=0.357) |
|------|---------------------------|-------------------|
| 可靠性 | 优秀，模型差异主导 | 极差，误差主导 |
| item 依赖 | 高（最大方差源） | 同样高 |
| prompt 敏感度 | 中等，n=3 足够 | 极高，是主要不稳定源 |
| seed/ordering | 几乎无影响 | 可能贡献更多方差 |
| 瓶颈 | 无（当前设计已足够） | prompt×model 交互方差过大 |

**核心差异原因**：text_exact_match 的模型间方差 (σ²τ = 0.027) 相对误差方差 (σ²δ = 0.0007) 大 39 倍，所以信噪比极高。correct 指标中模型间真实差异被评估噪声淹没，导致 G 极低。这意味着 text_exact_match 在区分模型能力方面远比 correct 可靠，correct 指标需要大幅增加复制数（尤其是 prompt 和 item）才能获得可接受的测量精度。

---
