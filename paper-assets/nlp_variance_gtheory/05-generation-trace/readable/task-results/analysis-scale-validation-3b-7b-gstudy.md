# analysis scale validation 3b 7b gstudy

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scale_validation_3b_7b_gstudy_20260522T070132_result.json`
- **Structured JSON:** [`1a737dcbe5922321bce1.json`](../../sessions/1a/1a737dcbe5922321bce1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果摘要：

| | **Qwen2.5-3B** | **Qwen2.5-7B** | **exp001 ref (Llama)** |
|---|---|---|---|
| grand_mean | 0.682 | 0.742 | — |
| item_id% | 75.32% | 73.37% | ~68% |
| prompt_template:item_id% | 8.83% | 12.20% | — |
| residual% | 11.02% | 9.71% | — |
| ordering:item_id% | 1.81% | 2.96% | — |
| **item_related_total** | **88.90%** | **90.21%** | **68.45%** |
| **G_item** | **0.963** | **0.956** | **0.937** |

关键发现：
- 3B/7B 单模型的 item_related 方差（~89-90%）远高于 exp001 8-model 参考值（68.45%），因为 exp001 含 precision facet 分散了部分 item 方差
- G_item 两个模型都 >0.95，高于参考值 0.937，说明 200 items 的测量信度很高
- Ranking 在 #2/#3 位有差异：3B 是 residual > prompt:item，7B 是 prompt:item > residual。7B 对 prompt 模板更敏感
- 所有验证通过：pct sum = 100%，D-study 单调递增，G_item 在合理范围

输出文件：
- 服务器：`results/exp003_scale_gstudy.json`
- 本地：`artifacts/exp004/data/exp003_scale_gstudy.json`
- 脚本：`scripts/exp003_scale_gstudy.py`

---
