# analysis exception only bootstrap

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exception_only_bootstrap_20260515T093628_result.json`
- **Structured JSON:** [`d303aa8c63436b514cf3.json`](../../sessions/d3/d303aa8c63436b514cf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### Bootstrap 对比结果

| 对比 | Δacc (pp) | 95% CI | p-value | 显著 |
|------|-----------|--------|---------|------|
| exception_only vs vota | **+0.67** | [+0.17, +1.26] | 0.010 | YES |
| exception_only vs full_trace | **+18.07** | [+15.88, +20.34] | <0.001 | YES |
| exception_only vs no_trace | **+24.71** | [+22.27, +27.14] | <0.001 | YES |

z-test 交叉验证 (exception_only vs vota): z=2.32, p=0.021

**结论**: exception_only (99.83%) 三对比较在 α=0.05 下全部显著。尽管 vs VOTA 仅差 0.67pp (8 errors vs 2 errors on 1190 samples)，CI 下界仍 >0。这是 unpaired bootstrap，CI 偏保守，实际差异可能更显著。

report.md 已更新，反映了 bootstrap 数据、loop_only (step 296/444 on cuda:0) 和 ae_only (刚启动 cuda:1) 的运行状态。结果 JSON 已存到服务器 `/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final/bootstrap_compare.json`。

---
