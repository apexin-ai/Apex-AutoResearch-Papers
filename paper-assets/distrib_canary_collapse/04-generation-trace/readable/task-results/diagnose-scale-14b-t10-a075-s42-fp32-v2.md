# diagnose scale 14b t10 a075 s42 fp32 v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scale_14b_t10_a075_s42_fp32_v2_20260522T200658_result.json`
- **Structured JSON:** [`06f67b5831af969b6e0a.json`](../../sessions/06/06f67b5831af969b6e0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验验证完成，D102 分析已运行。结果汇总：

## 实验状态

| 项目 | 结果 |
|------|------|
| EXIT_CODE | **0** (成功) |
| Checkpoints | gen_9, gen_10 存在 (5.3GB each) |
| all_metrics.json | 11 条 (gen 0-10) |

## D102 5-Method Lead-Lag 分析 (1.4B, T=10, α=0.75, seed=42)

| 指标 | 值 |
|------|------|
| **PermG_fwd** | **5/8** |
| PermG_rev | 0/8 |
| diff_xcorr_fdr_fwd | 7/8 |
| naive_xcorr_fwd_D111 | 6/8 |
| threshold_onset_3sigma | 0/8 (downstream onset 全为 None) |
| TY_granger | 0/8 |
| **K≥3** | **5/8** |
| K≥4 | 0/8 |

## Drift Statistics (gen0 → gen10)

| Metric | gen0 | gen10 | Change |
|--------|------|-------|--------|
| perplexity | 19.83 | 89.37 | +350.7% |
| ece | 0.008 | 0.266 | +3179.7% |
| token_entropy | 2.97 | 1.97 | -33.8% |
| distinct_1 | 0.099 | 0.081 | -18.8% |
| distinct_2 | 0.522 | 0.407 | -22.1% |
| distinct_3 | 0.821 | 0.670 | -18.4% |
| effective_rank | 52.7 | 99.9 | +89.7% |
| mauve | null | 0.031 | — |

## 对比 410M 基线

410M PermG=6/8，1.4B PermG=**5/8**——方向一致，信号略弱。5 个 forward-significant pair 的共识分布：5 个 K=3（naive+diff+perm），2 个 K=1，1 个 K=0。mauve pair 在两个 canary 上均无信号。

结果已保存至服务器 `/root/autodl-tmp/distrib_canary_collapse/D102_14b_t10_a075_s42_fp32_11gen.json`。

---
