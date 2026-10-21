# analysis convergence dynamics figure

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_convergence_dynamics_figure_20260519T120142_result.json`
- **Structured JSON:** [`14646231d7ae26279b50.json`](../../sessions/14/14646231d7ae26279b50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。输出文件：

- **PDF**: `artifacts/_project/chart/fig_convergence_dynamics.pdf` (26 KB)
- **PNG**: `artifacts/_project/chart/fig_convergence_dynamics.png` (188 KB)
- **Caption**: `artifacts/_project/chart/fig_convergence_dynamics_caption.tex`

**指数拟合结果**（drifting 特征）：
| Feature | λ (convergence rate) |
|---|---|
| Entropy (mean) | 0.12 (slow drift) |
| TTR | 0.47 (fast) |
| Hapax ratio | 0.60 (fastest) |

词汇多样性特征（TTR、hapax ratio）在 2 步内快速收敛，entropy mean 衰减较慢，而 distributional shape 特征（entropy max/min、tail decay）跨所有 depth 保持稳定。

---
