# analysis w6 mistral docred unconstrained metrics

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w6_mistral_docred_unconstrained_metrics_20260516T085043_result.json`
- **Structured JSON:** [`1a74a750a7157e09fe09.json`](../../sessions/1a/1a74a750a7157e09fe09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。以下是完整 metrics 和三模型对比：

## w6_mistral_docred_unconstrained Metrics

| Metric | Value |
|--------|-------|
| ET_pct | 7.58% |
| **RV_pct** | **42.35%** |
| DR_pct | 33.10% |
| CF_pct | 34.94% |
| parse_fail_rate | 0.70% |
| E_F1 / E_P / E_R | 48.43 / 62.14 / 39.67 |
| R_F1 / R_P / R_R | 3.48 / 3.53 / 3.44 |
| total_entities | 12,580 |
| total_relations | 11,879 |
| total_samples | 998 |

## DocRED Unconstrained 三模型对比

| Metric | Qwen-2.5-7B | Llama-3.1-8B | Mistral-7B |
|--------|:-----------:|:------------:|:----------:|
| **RV_pct** | 29.66% | 16.03% | **42.35%** |
| **DR_pct** | 18.46% | 26.07% | **33.10%** |
| **ET_pct** | 2.48% | 0.13% | **7.58%** |
| CF_pct | — | — | 34.94% |
| E_F1 | — | — | 48.43 |
| R_F1 | — | — | 3.48 |

Mistral 在所有违规维度上都是最高的。RV=42.35% 是因为 Mistral 大量生成自然语言关系名（"located in", "cast_member", "place_of_birth" 等）而非 DocRED ontology 定义的名称。Top violators: `located in`(369), `cast_member`(100), `applies to`(81)。R_F1 仅 3.48%——关系几乎全部匹配失败。

对论文是好消息：约束效果越戏剧化，Mistral 作为"最不遵守 schema"的模型，constrained 版本的改善幅度会最大。

---
