# code results summary csv

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_results_summary_csv_20260514T031526_result.json`
- **Structured JSON:** [`818fba038aeedbb3453b.json`](../../sessions/81/818fba038aeedbb3453b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CSV 验证通过，20 行数据完整。

---

## 结果汇总

### 任务 1: results_summary.csv ✓

已在 `/root/ratekv/results_summary.csv` 创建，共 20 行数据覆盖全部 9 组实验：

| 实验组 | 行数 | 关键结果 |
|--------|------|----------|
| exp_c_constrained_mckp | 1 | MCKP=11.23 vs uniform=15.45 (+4.21) |
| exp_d_no_l0_exclusion | 1 | solver 自动回避 L0，与 exp_c 完全一致 |
| exp_e_hires_profile | 1 | hires PPL=9.57(bf16)，退化仅+0.75 vs baseline |
| budget_sweep | 3 | 2x 无优势 / 4x sweet spot / 8x collapse protection |
| compounding_sweep | 10 | U 型曲线，k=8 最优 (11.23) |
| c4_cross_dataset | 1 | 98.2% allocation 一致性 |
| ratequant_greedy | 1 | greedy=32.45 vs MCKP=11.23 |
| llama_full_pipeline | 1 | MCKP=8.70 > uniform=8.47 (lowres 失效) |
| mistral_full_pipeline | 1 | MCKP=7.56 > uniform=7.13 (lowres 失效) |

注意：exp_e 的 uniform_ppl=15.4454 是 fp16 参考值（bf16 未单独测量），已在 conclusion 标注。

### 任务 2: Hires 进度

**Llama hires**: profiling 进行中，198/768 步 (25.8%)，对应 66/256 heads 完成，当前在 L8H1。

**Mistral hires**: 刚完成模型加载，尚未开始 hires profiling（日志显示 "Loading model in bf16 on cuda:0..."）。

---
