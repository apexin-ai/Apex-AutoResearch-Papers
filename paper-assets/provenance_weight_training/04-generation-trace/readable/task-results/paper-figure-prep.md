# paper figure prep

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure-prep_20260516T025916_result.json`
- **Structured JSON:** [`412e81b6ae10c8ea7525.json`](../../sessions/41/412e81b6ae10c8ea7525.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。生成了 3 个论文图表：

**服务器路径** `westd-47453:/root/provenance_weight_training/output/figures/`

| 图表 | 文件 | 关键数据 |
|------|------|----------|
| Fig 1: τ sweep | `fig1_tau_sweep.{pdf,png}` (28K/123K) | τ*=0.8 (PPL=17.653), safe range [0.5,0.8] 全优于 uniform (17.694) |
| Fig 2: b curve | `fig2_b_curve.{pdf,png}` (22K/122K) | Grid-b 多 seed 均值±std, adaptive b* (17.651) 参考线 |
| Fig 3: 方法对比 | `fig3_method_comparison.{pdf,png}` (24K/84K) | Adaptive=17.651 vs Uniform=17.694 vs ESS-only=17.723 |

**脚本 & 数据**：
- `scripts/generate_figures.py` — 支持 `--figures tau/b_curve/comparison/all` 和 `--data` 参数
- `scripts/figure_data.json` — 所有数据集中管理，b=0.1/0.3 完成后更新 JSON 重跑即可

**注意**：registry 中 tau_09/tau_095 结论为 `negative`（非 `success`），已用其 eval_ppl 数据。seed456 的 b≥2.0 因 checkpoint resume artifact 被排除，仅用 2 seeds。

---
