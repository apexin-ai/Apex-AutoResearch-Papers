# audit dose response data

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_dose-response-data_20260523T102128_result.json`
- **Structured JSON:** [`4a483d92623affa0aad7.json`](../../sessions/4a/4a483d92623affa0aad7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。关键发现：

**🔴 Critical — Figure 2 + Figure 3 MMLU 列数据过期**

`gen_baseline_vulnerability.py` 和 `gen_cross_benchmark_heatmap.py` 中有 4 个模型的数据与 Table 1 / Figure 1 严重不一致：

| Model | Fig 2/3 Δacc | Table 1 Δacc | 问题 |
|-------|-------------|-------------|------|
| Qwen-7B | **+2.90** | **-1.78** | 符号反转，Benefit vs V-recovery |
| Gemma-2 | **+1.21** | **+3.76** | 低估 62% |
| Phi-4 | x=70.69 | x=76.44 | x 位置偏 5.75pp |
| Qwen-14B | x=72.17 | x=69.44 | x 位置偏 2.73pp |

OLMo-2 和 Falcon3 两个模型的数据一致。

**🟡 Medium — Figure 3 Qwen-7B GSM8K**：heatmap 中 +16.24pp，论文正文说 +10.1pp（s42=+11.07）。来源不明。

**🟡 Medium — CI bounds**：6 个模型的 95% CI 未追溯到具体 bootstrap 输出文件。

**Table 1 和 Figure 1 之间完全一致**，所有数值验证通过。

报告已写入 `artifacts/data_audit_part1_dose_response.md`。

---
