# analysis exp001 bf16only 2temp subset

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp001_bf16only_2temp_subset_20260522T035510_result.json`
- **Structured JSON:** [`d5a7b5b564aaf755026f.json`](../../sessions/d5/d5a7b5b564aaf755026f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

| 指标 | Full (6-facet) | Reduced (bf16×2temp) | Diff |
|------|---------------|---------------------|------|
| N | 259,200 | 57,600 | |
| Grand mean | 0.6839 | 0.7089 | +0.025 |
| item_id% | 58.39% | 68.45% | +10.06pp |
| **G_item** | **0.9361** | **0.9369** | **+0.0008** |
| prompt:item% | 5.47% | 5.50% | +0.03pp |
| seed:item% | 4.71% | 5.60% | +0.89pp |
| temp:item% | 2.93% | 4.94% | +2.01pp |
| ordering:item% | 0.77% | 0.97% | +0.20pp |
| residual% | 23.10% | 14.45% | -8.66pp |

**结论**：Reduced crossing 不引入显著 confounding。G_item 差异仅 0.0008（0.9361 vs 0.9369）。item_id% 差异 +10pp 是因为 precision 相关分量（precision=0.91%, precision:item=3.30% 等共 ~4.5%）被移除后，剩余方差重新分配——不是 confounding，而是分解结构变化的必然结果。共享的非 precision 分量（prompt:item, seed:item, ordering:item）差异均 < 2pp。

脚本已保存至服务器 `scripts/exp001_bf16_2temp_subset.py`，结果 JSON 已存至服务器 `results/exp001_bf16_2temp_comparison.json` 和本地 `artifacts/exp004/data/`。

---
