# analysis maven confused pairs case study

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_maven_confused_pairs_case_study_20260515T152151_result.json`
- **Structured JSON:** [`39879bf50d70058f6ff2.json`](../../sessions/39/39879bf50d70058f6ff2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成。结果如下：

---

## Top-10 Confused Pairs (MAVEN exp-004)

| Rank | Type A | Type B | Conf | MiniLM SCS | Qwen3 SCS | Category | Relation |
|------|--------|--------|------|-----------|-----------|----------|----------|
| 1 | Achieve | Getting | 73 | 0.4504 | 0.7496 | centrality | causative-resultative |
| 2 | Departing | Escaping | 49 | 0.3146 | 0.7334 | confusable | manner-of |
| 3 | Death | Killing | 34 | 0.7363 | 0.7041 | centrality | causative pair |
| 4 | Attack | Use_firearm | 33 | 0.2877 | 0.4853 | confusable | instrument-of |
| 5 | Action | Removing | 29 | 0.3740 | 0.9061 | centrality | hypernym-hyponym |
| 6 | Arriving | Conquering | 27 | 0.2572 | 0.6618 | centrality | script-adjacent |
| 7 | Communication | Expressing_publicly | 25 | 0.4395 | 0.3120 | confusable | hypernym-hyponym |
| 8 | Motion | Motion_directional | 24 | 0.7308 | 0.5298 | confusable | hypernym-hyponym |
| 9 | Arriving | Process_start | 24 | 0.3094 | 0.6927 | centrality | metaphorical overlap |
| 10 | Expressing_publicly | Statement | 23 | 0.2906 | 0.3875 | confusable | near-synonym |

## Top-10 MiniLM SCS Pairs

| Rank | Type A | Type B | SCS | Confusion |
|------|--------|--------|-----|-----------|
| 1 | Commerce_buy | Commerce_sell | 0.8368 | **0** |
| 2 | Choosing | Deciding | 0.8179 | **0** |
| 3 | Motion | Self_motion | 0.7900 | 8 |
| 4 | Death | Killing | 0.7363 | 34 |
| 5 | Motion | Motion_directional | 0.7308 | 24 |
| 6 | Robbery | Theft | 0.7092 | **0** |
| 7 | Process_end | Process_start | 0.7078 | **0** |
| 8 | Coming_to_be | Coming_to_believe | 0.6891 | **0** |
| 9 | Legal_rulings | Legality | 0.6822 | **0** |
| 10 | Being_in_operation | Military_operation | 0.6704 | **0** |

## Centrality Confound 分析

**Category breakdown**: centrality 5/10, confusable 5/10

**Overlap top-10 SCS vs top-10 confused**: 仅 2/10（Death↔Killing, Motion↔Motion_directional）

**Centrality stats**: top-10 confused types 平均 centrality = 0.2385, 全体 = 0.2161 (1.10x)。18 个涉及类型中 11 个在 top-quartile centrality。

**Spearman ρ (MiniLM SCS vs confusion)**: 0.1926 (p=8.6e-7), 652 nonzero pairs — 显著但弱。

## 核心发现：为什么 SCS 在 MAVEN 上 captures centrality 而非 confusability

**Top-SCS pairs 几乎不产生 confusion。** Commerce_buy↔Commerce_sell (SCS=0.84)、Choosing↔Deciding (0.82)、Robbery↔Theft (0.71) 等最高 SCS pairs 的 confusion count 全是 0。这些 pair 虽然语义极相似，但 trigger words 截然不同（buy/sell, choose/decide, rob/steal），LLM 不会混淆。

**真正 confused 的 pairs 源于 trigger ambiguity + type centrality，而非 embedding 相似度。** Achieve↔Getting (confusion=73) 的 MiniLM SCS 只有 0.45，远低于 Commerce_buy↔Commerce_sell 的 0.84。但 "won"/"gained" 等 trigger 在叙事语境中既可描述获取过程也可描述成就结果——这是 **trigger 多义性**，不是 type embedding 相似度能捕捉的。

**Centrality confound 机制**：在 MAVEN 这类 homogeneous event schema（168 types 全来自 FrameNet event domain）中，embedding SCS 本质上度量 **type 在语义空间的位置** 而非 **pair-wise confusability**。"Action"（centrality=0.313, 最高）出现在 3 个 top-20 confused pairs 中，因为它是最泛化的原型类型——它的高 SCS 反映的是它位于 embedding 空间中心，而不是它与具体类型（Removing/Arranging/Competition）真正 confusable。这导致 SCS 与 F1 呈正相关（ρ=+0.19）：central types 既有高 mean-SCS，又因为更 prototypical 而被 LLM 更好地识别。

JSON 已保存至 `artifacts/maven_case_study.json`。

---
