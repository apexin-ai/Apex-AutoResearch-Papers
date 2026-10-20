# code analysis pipeline p1p2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analysis_pipeline_p1p2_20260514T191147_result.json`
- **Structured JSON:** [`88f83c6962df2f2dde10.json`](../../sessions/88/88f83c6962df2f2dde10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功。结果汇总：

### P1: Mid-phase null rate

| Condition | Total | Null | Rate | Effective n |
|-----------|-------|------|------|-------------|
| ds_imp_s015 | 500 | 51 | 10.2% | 449 |
| ds_rand_s015 | 500 | 51 | 10.2% | 449 |
| qw_imp_s015 | 500 | 226 | **45.2%** | 274 ⚠ |
| qw_rand_s015 | 500 | 226 | **45.2%** | 274 ⚠ |

Qwen n=500 的 mid-phase null rate 从 n=50 时的 58% 降到 45.2%，但仍远超 30% 阈值。DeepSeek 只有 10.2%。

### P2: Paired gradient (ii_high - ii_low)

| Model | Sparsity | median_D | 95% CI | Wilcoxon p | Bonf. p | d_z |
|-------|----------|----------|--------|------------|---------|-----|
| DeepSeek | s015 | -0.4227 | [-0.4825, -0.3564] | 0.0000 | 0.0000 | -0.045 |
| Qwen | s015 | -0.0991 | [-0.1454, -0.0504] | 0.0000 | 0.0000 | 0.038 |

n=500 下两个模型 imp-vs-rand paired gradient 均显著（Bonferroni 校正后 p<0.0001），n=50 时不显著的问题已解决。d_z 接近 0 说明 effect size 很小（imp 和 rand 的 gradient 差异方向一致但幅度小）。

脚本已更新，两个新功能均验证通过。JSON 和 report.md 输出已包含新字段。

---
