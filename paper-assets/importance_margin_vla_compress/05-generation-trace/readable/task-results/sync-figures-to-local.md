# sync figures to local

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_sync_figures_to_local_20260518T181044_result.json`
- **Structured JSON:** [`232b621b9553a409888e.json`](../../sessions/23/232b621b9553a409888e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 8 个 figure PDF 已就位。下面是完整报告：

## Figure 同步状态

| .tex 引用路径 | 引用位置 | 本地状态 |
|---|---|---|
| `figures/paper/fig_architecture.pdf` | background.tex, experimental_setup.tex, sections/background.tex | ✅ 已有 |
| `figures/paper/fig_degradation_curve.pdf` | results.tex:77 | ✅ 已有 |
| `figures/paper/fig_compression_curve.pdf` | results.tex:83 | ✅ 已有 |
| `figures/paper/fig_pixel_shuffle.pdf` | analysis.tex:11 | ✅ 已有 |
| `figures/paper/fig_entropy_layers.pdf` | analysis.tex:20 | ✅ 已有 |
| `figures/paper/fig_attention_heatmap.pdf` | sections/analysis.tex:41 | ✅ 已补充（从 `figures/paper/` 复制） |
| `figures/paper/fig_action_divergence.pdf` | sections/analysis.tex:71 | ✅ 已补充（从 `figures/paper/` 复制） |
| `figures/paper/fig_cliff_edge.pdf` | sections/experiments.tex:72 | ✅ 已补充（从 `figures/paper/` 复制） |

## 注意事项

1. **命名差异**：任务中提到的文件名（`degradation_curve.pdf` 等）与 .tex 实际引用的文件名（`fig_degradation_curve.pdf` 等）不同。.tex 统一使用 `fig_` 前缀。`docs/paper/figures/` 下还有一组旧命名的文件（无 `fig_` 前缀），这些不被 .tex 引用。

2. **远程最新版问题**：cqa1-33015 上只有一个 `degradation_curve.pdf`（无 `fig_` 前缀），与本地 `docs/paper/figures/paper/fig_degradation_curve.pdf` 是否为同一版本需确认。如果 cqa1 上的是最新版（3 条曲线，official 4 个数据点），可能需要替换本地版本。

3. **所有 `\includegraphics` 路径现在都能在 `docs/paper/figures/paper/` 下找到对应文件**，编译应无缺失图片错误。

---
