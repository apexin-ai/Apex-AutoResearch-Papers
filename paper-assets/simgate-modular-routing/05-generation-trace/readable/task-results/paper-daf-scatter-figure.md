# paper daf scatter figure

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_daf-scatter-figure_20260514T112313_result.json`
- **Structured JSON:** [`1f37cbc420b3df56440c.json`](../../sessions/1f/1f37cbc420b3df56440c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已生成并注册。

**产出文件（服务器 westb-13313）：**
- PDF: `/root/autodl-tmp/simgate-modular-routing/figures/fig1_daf_scatter.pdf`
- PNG: `/root/autodl-tmp/simgate-modular-routing/figures/fig1_daf_scatter.png`
- 生成脚本: `/root/autodl-tmp/simgate-modular-routing/figures/gen_fig1.py`

**图表内容：**
- X 轴：per-task death rate differential (internal − deterministic)，范围 0.0–0.45
- Y 轴：Δ_full (deterministic − internal)，范围 ~10–48
- 11 个点（task types），点大小按 episode 数缩放（20–40 episodes）
- 红色回归线 + 95% CI band
- 左上角标注 r=0.9698, p=8.09e-07
- find-non-living-thing 标注为异常点（零死亡差异但 Δ=+9.58）
- 双列宽度 6.75 inch，去掉 top/right spines，符合 ACL/EMNLP 风格

**数据验证通过：**

| Task | N | IntDR | DetDR | DeathDiff | Δ_full |
|------|---|-------|-------|-----------|--------|
| identify-life-stages-1 | 20 | 0.550 | 0.100 | 0.450 | +47.50 |
| lifespan-longest-lived | 25 | 0.560 | 0.160 | 0.400 | +44.00 |
| lifespan-longest-lived-then-shortest | 20 | 0.450 | 0.100 | 0.350 | +40.80 |
| inclined-plane-determine-angle | 20 | 0.550 | 0.200 | 0.350 | +36.00 |
| freeze | 20 | 0.550 | 0.250 | 0.300 | +30.50 |
| measure-melting-point | 20 | 0.550 | 0.250 | 0.300 | +30.05 |
| identify-life-stages-2 | 20 | 0.500 | 0.200 | 0.300 | +30.00 |
| find-animal | 20 | 0.500 | 0.250 | 0.250 | +26.65 |
| grow-fruit | 20 | 0.450 | 0.200 | 0.250 | +25.10 |
| chemistry-mix | 20 | 0.450 | 0.250 | 0.200 | +21.80 |
| find-non-living-thing | 40 | 0.000 | 0.000 | 0.000 | +9.58 |

---
