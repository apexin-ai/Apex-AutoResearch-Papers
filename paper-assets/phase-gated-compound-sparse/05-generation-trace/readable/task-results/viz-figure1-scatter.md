# viz figure1 scatter

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_figure1_scatter_20260516T031846_result.json`
- **Structured JSON:** [`ac30a717c415a2b73c35.json`](../../sessions/ac/ac30a717c415a2b73c35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure 1 生成完成。

**输出文件**：
- `/root/autodl-tmp/pacs/artifacts/figure1_ii_scatter.pdf` (28 KB)
- `/root/autodl-tmp/pacs/artifacts/figure1_ii_scatter.png` (191 KB)

**图表配置**：
- 2 panel（左 DeepSeek-R1-Distill-Qwen-1.5B，右 Qwen2.5-1.5B-Instruct）
- X 轴：Sparsity Level (15%–30%)
- Y 轴：Interaction Index (median ΔII)
- 红色圆点 = Importance eviction，蓝色方块 = Random eviction
- 非对称 95% CI error bars
- serif 字体，无顶/右 spine

**数据摘要**：

| Model | Strategy | 15% | 20% | 25% | 30% |
|-------|----------|-----|-----|-----|-----|
| DeepSeek | Importance | 0.391 [0.350, 0.443] *** | 1.215 [1.109, 1.339] *** | 3.986 [3.534, 4.356] *** | 8.481 [7.754, 9.685] *** |
| DeepSeek | Random | 0.014 [-0.015, 0.039] ns | 0.031 [-0.013, 0.080] ns | 0.257 [0.126, 0.350] ** | 0.510 [0.260, 0.894] ** |
| Qwen | Importance | 0.066 [0.049, 0.092] *** | 0.307 [0.261, 0.356] *** | 1.074 [0.977, 1.179] *** | 3.155 [2.783, 3.558] *** |
| Qwen | Random | -0.011 [-0.039, 0.012] ns | 0.015 [-0.015, 0.068] ns | 0.393 [0.220, 0.546] *** | 0.913 [0.613, 1.250] *** |

两个模型都呈现相同趋势：importance eviction 的 ΔII 随 sparsity 指数级增长，random eviction 在低 sparsity 时接近零（ns），高 sparsity 时才出现小幅显著增长。DeepSeek 的 importance 效应幅度约为 Qwen 的 2.7× (30% sparsity)。

---
