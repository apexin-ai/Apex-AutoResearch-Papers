# run pooled irt 05b 15b n13

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_pooled_irt_05b_15b_n13_20260516T085630_result.json`
- **Structured JSON:** [`24f0288158abafd06bfc.json`](../../sessions/24/24f0288158abafd06bfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

```
================================================================================
POOLED IRT RESULTS (4PL+γ, RRF signal exposure, N_items=300 subsampled)
================================================================================
Bench            N_mod  N_item    γ̂           95% CI        R̂     ESS   PPP   rawMAE calMAE  ΔMAE
─────────────────────────────────────────────────────────────────────────────────
gsm8k              11     300  0.0128  [-0.990, 1.019]  1.0072  1300  0.663  0.1501 0.0373 +0.1128
arc_challenge       5     300  1.2259  [-0.271, 2.857]  1.0072  1480  0.000  0.0042 0.0682 -0.0640
```

**解读**：

- **GSM8K** (N=11, 0.5B+1.5B)：γ̂≈0，CI 宽且包含 0 — RRF signal 未检测到 GSM8K 上的显著 contamination effect。收敛良好（R̂<1.01, ESS>400, 0 divergences）。IRT 校准将 MAE 从 0.150 降至 0.037。

- **ARC** (N=5, 1.5B only per D045)：γ̂=1.23 正向趋势但 CI 包含 0。PPP=0.000 表明 N=5 下 4PL 模型严重拟合不足（参数过多/样本过少），结果不可靠。

**注意事项**：
- 实际可用模型数 GSM8K=11、ARC=5（部分 s123 模型缺少 RRF gsm8k/arc exposure）
- Items 从 1319/1172 子采样到 300（4PL 在全量 items 上 MCMC 不可行）
- 这是 pipeline validation；N≥16 最终版待 s123 signals 全部完成后重跑

---
