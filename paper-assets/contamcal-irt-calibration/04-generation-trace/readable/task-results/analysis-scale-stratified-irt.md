# analysis scale stratified irt

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scale_stratified_irt_20260516T112105_result.json`
- **Structured JSON:** [`e5f742c90ee2693fd595.json`](../../sessions/e5/e5f742c90ee2693fd595.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

## Scale-Stratified IRT 结果

| Scale | Benchmark | N | γ | 95% CI | PPP | ΔMAE |
|-------|-----------|---|---|--------|-----|------|
| **0.5B** | gsm8k | 7 | 0.61 | [-0.19, 1.39] | 0.163 | +0.002 |
| **1.5B** | mmlu | 8 | -0.30 | [-1.66, 1.04] | 0.441 | +0.005 |
| **1.5B** | gsm8k | 6 | -0.35 | [-1.24, 0.52] | 0.704 | +0.004 |
| **1.5B** | arc | 6 | 1.17 | [0.17, 2.21] | 0.013 | -0.027 |
| **3B** | mmlu | 7 | 0.45 | [-1.05, 1.92] | 0.263 | +0.000 |
| **3B** | gsm8k | 7 | 0.42 | [-0.42, 1.26] | 0.245 | **+0.155** |
| **3B** | arc | 7 | 0.76 | [-0.84, 2.36] | 0.088 | -0.019 |

**关键结论**：
1. **γ 不是 scale-dependent** — 没有单调趋势，大多数 CI 包含 0
2. **3B GSM8K 贡献了几乎全部校准增益** (ΔMAE=0.155 ≈ pooled 的 0.155)
3. 原因是 N=6-8 统计功效不足；pooled (N=23) 仍是更可靠的估计
4. 1.5B ARC 虽然 γ 显著 (CI 不含 0)，但 PPP=0.013 说明模型拟合差

**论文建议**：pooled 作为主结果，scale-stratified 作为补充材料。不宜声称 γ 随 scale 增大。

---
