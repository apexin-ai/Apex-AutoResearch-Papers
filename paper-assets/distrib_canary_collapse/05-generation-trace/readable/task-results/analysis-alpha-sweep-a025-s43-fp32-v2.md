# analysis alpha sweep a025 s43 fp32 v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a025_s43_fp32_v2_20260519T142213_result.json`
- **Structured JSON:** [`27df2bc5dc2c8693722d.json`](../../sessions/27/27df2bc5dc2c8693722d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 **正常完成**。完整结果如下：

## 状态

- **进程**: 123809 已退出，EXIT_CODE=0
- **完成度**: gen 0→10 全部完成，all_metrics.json + analysis_results.json 均已写入

## 核心指标

| 指标 | gen 0 | gen 10 | drift_pct |
|------|-------|--------|-----------|
| distinct_1 | 0.0983 | 0.0595 | **-38.95%** |
| distinct_2 | 0.5146 | 0.2330 | -53.35% |
| distinct_3 | 0.8140 | 0.3511 | -54.80% |
| token_entropy | 3.234 | 3.069 | -4.94% |
| perplexity | 26.95 | 21.95 | -18.38% |
| effective_rank | 46.61 | 44.91 | -1.99% |
| mauve | 0.0315 | 0.0207 | -35.59% |
| ece | 0.0108 | 0.0218 | +64.77% |

## Lead-lag 分析

| 方法 | forward sig / total |
|------|-------------------|
| PermG (fwd) | **0/8** |
| PermG (rev) | 0/8 |
| consensus_k≥4 | **0/8** |
| MMCT detection_rate | **0.0** |
| TY Granger | 6/8 (但 C003 约束：低α下 TY 不可信) |
| naive_xcorr | 8/8 |
| threshold_onset | 4/8 |

最高 consensus vote = 3 (token_entropy→d1/d2/d3 各 3 票: naive+thresh+ty)，均未达 K≥4 阈值。

## 与 bf16 s43 对比

| | bf16 s43 | fp32 s43 |
|--|----------|----------|
| d1_drift_pct | -40.5% | -38.95% |
| PermG | 0/8 | 0/8 |
| consensus_k≥4 | 0/8 | 0/8 |

fp32 和 bf16 结果高度一致：d1 drift 幅度相近（-39% vs -40.5%），PermG 和 consensus 均为 0/8。

## 对 dose-response map 的影响

α=0.25 fp32 s43 确认了 s42 的结论：
- **drift 幅度跨 seed 稳定**（d1 ≈ -39~-40%），precision 格式（fp32 vs bf16）无显著影响
- **PermG=0/8 跨 seed 稳定**——α=0.25 处于 lead-lag 信号不可检出区域
- dose-response map 中 α=0.25 可标记为 "drift present, no detectable lead-lag"，与 α=0.50 形成对照

---
