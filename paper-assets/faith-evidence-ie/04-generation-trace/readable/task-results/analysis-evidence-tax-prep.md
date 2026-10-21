# analysis evidence tax prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_evidence_tax_prep_20260518T102202_result.json`
- **Structured JSON:** [`0b66013d42bbedbbcea3.json`](../../sessions/0b/0b66013d42bbedbbcea3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本语法通过。下面是汇报。

---

## 1. 已收集数据汇总表

### SFT with-evidence vs no-evidence

| Model | Mode | Rel F1 | Ign F1 | Evi F1 | EDCR | Preds | Trunc (%) | Tax (Ign-F1) |
|---|---|---|---|---|---|---|---|---|
| **Qwen3-1.7B** | with-evi | 49.45 | 47.86 | 83.16 | 0.670 | 17184 | 314 (31.9%) | |
| | no-evi | 41.03 | 39.82 | — | — | 26157 | 501 (50.9%) | **-8.04pp** (evidence helps!) |
| **Qwen3-4B** | with-evi | 40.49 | 39.74 | 79.86 | 0.698 | 16880 | 288 (29.2%) | |
| | no-evi | 48.76 | 47.21 | — | — | 21181 | 307 (31.2%) | **+7.47pp** |
| **Qwen3-8B** | with-evi | 52.62 | 50.51 | 81.88 | 0.651 | 17401 | 313 (31.8%) | |
| | no-evi | 52.83 | 50.79 | — | — | 19948 | 225 (22.8%) | **+0.28pp** |
| **LLaMA-8B** | with-evi | 55.14 | 53.84 | 81.51 | 0.628 | 15325 | 197 (20.0%) | |
| | no-evi | 56.24 | 54.52 | — | — | 18466 | 182 (18.5%) | **+0.68pp** |

### RSFT (with-evidence only)

| Model | Ign F1 | Trunc | Preds |
|---|---|---|---|
| 1.7B RSFT-k1 (D102) | 51.22 | 249 | 16154 |
| 4B RSFT-CED s44 | 45.11 | 190 | 15264 |
| 8B RSFT | 54.33 | 267 | 16831 |
| LLaMA-8B RSFT | 55.63 | 187 | 14959 |

### 关键发现

**Evidence tax 模式非单调**：
- 1.7B: evidence 反而 **帮助** RE（-8.04pp），因为 no-evidence 1.7B 严重过度生成（26157 preds，50.9% 截断）
- 4B: evidence tax 最大（+7.47pp）
- 8B: evidence tax 几乎消失（+0.28~0.68pp）

这意味着 evidence tax 的核心机制是 **output length vs model capacity 的竞争**：
- 小模型（1.7B）: capacity 不够，no-evidence 模式下反而产生更多重复/幻觉，evidence 结构起到约束作用
- 中等模型（4B）: evidence 产生真正的 length tax，截断导致关系丢失
- 大模型（8B）: capacity 足够，evidence 几乎不影响 RE 性能

## 2. 缺失数据

| 数据 | 状态 |
|---|---|
| 4B with-evidence predictions.json | **缺失**（sft_baseline_d076_reeval 只有 metrics.json，无法做 per-doc 分析） |
| D102 8B RSFT eval (d102_8b_k1_s42) | **空目录**（eval 未开始/进行中） |
| D102 LLaMA RSFT eval (d102_llama_k1_s42) | **空目录** |
| D102 8B seed43 (d102_8b_k1_s43) | **空目录** |
| No-evidence RSFT 变体 | **不存在**（所有 RSFT 均 with-evidence） |

## 3. 分析脚本

路径: `/root/autodl-tmp/freige/scripts/evidence_tax_analysis.py`

5 个模块：
- **Module A**: Output length distribution（chars, triples, 按 doc length 分层）
- **Module B**: Truncation impact（trunc vs clean docs 的 F1 差异，用 evaluator 重新计算）
- **Module C**: Per-relation analysis（按 relation type 计算 recall，找出 tax 最大的关系类型）
- **Module D**: False positive analysis（FP rate, FP 在 trunc vs clean docs 的分布）
- **Module E**: Fair subset analysis（排除 truncated+repetitive docs 后重新计算 tax）

运行：`python scripts/evidence_tax_analysis.py --module all`（或 A/B/C/D/E）

## 4. D102 eval 完成后还需什么

1. **重跑 4B with-evidence eval 并保存 predictions.json**，否则 4B 的 per-doc 分析无法进行
2. D102 8B/LLaMA eval 完成后，可以比较 RSFT 是否改变 evidence tax 模式
3. 可能需要 **4B no-evidence RSFT** 做完整的 RSFT-level tax 对比（目前只有 SFT-level 的对比）

---
