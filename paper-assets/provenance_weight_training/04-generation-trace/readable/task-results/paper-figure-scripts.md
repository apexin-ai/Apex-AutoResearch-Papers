# paper figure scripts

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure-scripts_20260516T075653_result.json`
- **Structured JSON:** [`7885c96e9951a97380b7.json`](../../sessions/78/7885c96e9951a97380b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个脚本已写入 `artifacts/figures/` 并注册：

| 文件 | 内容 |
|------|------|
| `plot_grid_b_sweep.py` | b-PPL 曲线，含 3 seed 点、uniform/adaptive 水平线、RUNNING 标注 |
| `plot_tau_ppl_curve.py` | τ-PPL 双线图，含 safe range 底纹、τ* 星号标注 |
| `plot_rho_comparison.py` | 4 方法 × 2 ρ 分组柱状图，含数值标签和 adaptive τ 注释 |

脚本均输出 PDF+PNG (300 DPI)，学术风格无标题。运行时从脚本所在目录或项目根目录执行 `python artifacts/figures/plot_*.py` 即可生成图片。

---
