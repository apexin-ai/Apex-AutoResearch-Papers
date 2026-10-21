# paper figure2 norm sweep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure2-norm-sweep_20260521T043537_result.json`
- **Structured JSON:** [`9abd6e45d3413532ee8a.json`](../../sessions/9a/9abd6e45d3413532ee8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure 2 生成完成。

**数据汇总：**

| ε | obs_only (n, mean±std) | perdof (n, mean±std) |
|---|---|---|
| 0.03 | 11 seeds, 15.2±1.1% | 4 seeds, 12.5±2.2% |
| 0.05 | 14 seeds, 13.9±1.3% | 5 seeds, 10.6±1.4% |
| 0.1 | 18 seeds, 15.7±2.2% | 3 seeds, 11.7±0.5% |
| 0.2 | 9 seeds, 16.6±1.8% | 5 seeds, 10.0±1.9% |
| 0.3 | 3 seeds, 15.7±1.2% | 3 seeds, 4.7±0.5% |

obs_only 在所有 ε 值下保持 ~14-17%（稳定），perdof 从 12.5% 骤降至 4.7%（progressive collapse），低于 VLA-only baseline (10.8%)。Claim 2 得到支持。

**产出文件：**
- `artifacts/figure2_norm_sweep.pdf`
- `artifacts/figure2_norm_sweep.png`

**注意：** obs_only ε=0.3 和 perdof 各 ε 组 seed 数偏少（3-5），ε=0.3 obs_only 仅 3 seeds，论文中可标注。

---
