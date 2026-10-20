# analysis deepseek lomo cross benchmark

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_lomo_cross_benchmark_20260522T101628_result.json`
- **Structured JSON:** [`06101c1af568bb704f2c.json`](../../sessions/06/06101c1af568bb704f2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

| Benchmark | item_id% (7m) | Δ item_id | model:item% (7m) | Δ m:i | residual% (7m) | Δ res | G_item (7m) | ΔG |
|-----------|---------|-----------|----------|-------|----------|-------|---------|------|
| ARC | 41.34 | +3.45 | 31.70 | -2.03 | 13.79 | -1.65 | 0.8939 | +0.0022 |
| HellaSwag | 36.85 | +2.57 | 35.99 | -0.01 | 19.41 | -2.00 | 0.8655 | -0.0061 |
| GSM8K | 17.30 | +0.45 | 13.80 | -0.75 | 38.60 | -1.29 | 0.8541 | -0.0088 |

去掉 DeepSeek-7B 后，所有 benchmark 的 G_item 变化均 < 0.01（max |ΔG| = 0.0088），与 MMLU LOMO 结果一致，确认测量稳定性。跨 benchmark 的共同模式：item_id% 略升（DeepSeek 对 item 难度梯度贡献较小），residual% 略降。

输出文件：
- 服务器：`results/exp004_8model_analysis/deepseek_lomo_cross_benchmark.json`
- 本地：`artifacts/exp004/data/deepseek_lomo_cross_benchmark.json`

---
