# analysis a1 heatmap

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a1_heatmap_20260512T145218_result.json`
- **Structured JSON:** [`baa6e5048f19434ab30f.json`](../../sessions/ba/baa6e5048f19434ab30f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 张图已生成并注册。

**输出文件**（均在 westd-16980 的 `/root/carc/figures/`）：

| 文件 | 内容 |
|------|------|
| `a1_ema_perturbation_corr.png` (114KB) | Layer-wise EMA–Perturbation Pearson r 热力图，3行（seed42, seed1337, mean） |
| `a1_perturbation_diff.png` (167KB) | 扰动敏感度剖面：redundant/novel 均值 + diff + 跨 seed 对比 |
| `a1_spatial_decoupling.png` (466KB) | 三面板叠加图：(a) 双轴线图 correlation vs diff, (b) 归一化解耦分数热力图, (c) 层分类色条 |

**数据发现**：
- **Layer 0** 反常：正相关 (r≈+0.33)，且 diff 为负值（redundant 扰动 > novel）
- **Layers 3-9**：correlation 接近 0，但 diff 极大（layer 4 的 diff≈0.66）—— 典型的空间解耦
- **Layers 25-46**：强负相关 (r≈-0.25~-0.37)，diff 为正但较小 —— correlation 和 diff 同向
- **Layer 47**（最后一层）：correlation 回到接近 0，near_zero_frac 异常高（~0.83）

绘图脚本：`/root/carc/plot_a1_heatmap.py`

---
