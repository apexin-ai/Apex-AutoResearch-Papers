# code exp002 analysis pipeline

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp002_analysis_pipeline_20260521T100021_result.json`
- **Structured JSON:** [`66baaa1a4fadb2a1a90b.json`](../../sessions/66/66baaa1a4fadb2a1a90b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6/6 脚本语法验证通过。

总结：

**完成状态**

| 脚本 | 本地 dry-run | 服务器传输 | 语法检查 |
|---|---|---|---|
| `per_benchmark_gstudy.py` | OK | OK (10865B) | OK |
| `gradient_permutation_test.py` | OK | OK (10580B) | OK |
| `leave_one_benchmark_out.py` | OK | OK (8430B) | OK |
| `within_format_gradient.py` | OK | OK (10215B) | OK |
| `gsm8k_answer_reextract.py` | OK | OK (6900B) | OK |
| `cross_benchmark_dstudy.py` | OK | OK (7923B) | OK |

**输出结构**（每个脚本的 JSON 结构已验证）：
- `exp002_per_benchmark_gstudy.json` — 每 benchmark 的 variance components + G_item + D-study curve
- `gradient_permutation_test.json` — item_id 递减 / model:item 递增的精确置换检验 (k!=24)
- `leave_one_benchmark_out.json` — 逐一移除 benchmark 后梯度是否保持
- `within_format_gradient.json` — MC 组内梯度 + MC vs free-form 方差结构对比
- `gsm8k_answer_reextract.json` — 停止序列截断重提取 + 准确率 delta
- `cross_benchmark_dstudy.json` — 跨 benchmark D-study 曲线 + G≥0.80/0.90/0.95 最低 item 数

脚本已就位在 `westd-32570:/root/nlp_variance_gtheory/scripts/exp002_analysis/`，等 exp-002 数据到齐后直接运行。

---
