# analysis alpha sweep a025 v3

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a025_v3_20260515T012002_result.json`
- **Structured JSON:** [`8a6a3ff830e4620e372f.json`](../../sessions/8a/8a6a3ff830e4620e372f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整，分析结果如下：

---

## α=0.25 实验结果分析

### conclusion: **success**

### Metrics (gen0 → gen10)

| 指标 | gen0 | gen10 | drift% | α=0.00 drift% | 对比 |
|------|------|-------|--------|---------------|------|
| token_entropy | 3.2342 | 3.1017 | **-4.1%** | -5.1% | 相近 |
| ECE | 0.01080 | 0.01942 | **+79.7%** | +51.7% | **更强** |
| perplexity | 26.95 | 22.32 | **-17.2%** | -21.7% | 相近 |
| distinct_1 | 0.0982 | 0.0586 | **-40.3%** | -13.8% | **远更强** |
| distinct_2 | 0.5178 | 0.2219 | **-57.1%** | — | — |
| distinct_3 | 0.8127 | 0.3263 | **-59.9%** | — | — |
| mauve | 0.0341 | 0.0163 | **-52.2%** | — | — |
| effective_rank | 46.61 | 45.30 | -2.8% | — | — |

### 分析要点

1. **Diversity collapse 在 α=0.25 下剧烈加速**：distinct_1 下降 40.3%（α=0.00 仅 13.8%），distinct_2/3 均超过 57% 下降，确认合成数据污染率越高 collapse 越严重。
2. **ECE canary 信号更强**：ECE drift +79.7% vs baseline +51.7%，ECE 作为早期预警指标在高 α 下响应更灵敏，支持 canary 假设。
3. **Token entropy drift 大致持平**（-4.1% vs -5.1%），说明 token_entropy 对 α 变化不如 ECE 和 diversity 指标敏感。

### 路径

- **log_path**: `~/runs/distrib_canary_collapse/alpha_sweep_a025_s42_v3.log`
- **checkpoint_path**: `/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s42/gen_10/checkpoint/`
- **metrics_path**: `/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s42/all_metrics.json`

---
