# analysis alpha sweep a065 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a065_s42_fp32_20260521T005325_result.json`
- **Structured JSON:** [`4d5740a64bdbe94f9ef8.json`](../../sessions/4d/4d5740a64bdbe94f9ef8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。结果解读：

---

## α=0.65 s42 fp32 分析结果

### 核心指标（D105+D111 校正后）

| 指标 | α=0.50 | α=0.55 | α=0.60 | **α=0.65** | α=0.75 |
|------|--------|--------|--------|------------|--------|
| PermG_fwd | 6/8 | 0/8 | 0/8 | **0/8** | 6/8 |
| K≥3(3σ) | 6 | 1 | 0 | **1** | 6 |
| K≥4(3σ) | 3 | 0 | 0 | **0** | 0 |
| threshold_onset_3σ | - | - | - | **0/8** | - |
| diff_xcorr | - | - | - | **6/8** | - |

### 结论

1. **PermG_fwd = 0/8** — α=0.65 仍完全被压制，与 α=0.60 相同。Sync collapse dip 扩展至 **[0.55, 0.65]**，不限于 [0.55, 0.60]。

2. **恢复是突变而非渐进** — 从 α=0.65 (0/8) 到 α=0.75 (6/8) 是跳变。PermG 在 dip 区间内没有中间恢复值（0/8→0/8→0/8→6/8）。转折点在 (0.65, 0.75) 区间内。

3. **PermG 边缘效应** — ece→distinct 三对 p_raw=0.014–0.025（名义显著），但 FDR 校正后 p_fdr=0.067（不显著）。比 α=0.60 更接近恢复临界值，提示 α=0.70 可能是实际转折点。

4. **Drift 对比** — perplexity drift +123.75%（介于 α=0.60 和 α=0.75 之间），distinct 退化约 -30%~-37%，mauve 仅 -5.23%（显著弱于其他 α）。Downstream 退化幅度不足以触发 3σ 阈值，这解释了 threshold_onset_3sigma=0/8。

5. **D105 关键发现** — canary 在 gen1-2 就 onset，但 downstream 指标从未越过 3σ 门槛。退化存在但不够剧烈——canary-downstream 在 temporal scale 上同步（sync collapse），剥夺了 lead-lag 信号。

---
