# code token importance heatmap

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_token_importance_heatmap_20260522T064104_result.json`
- **Structured JSON:** [`acc86edd71b9cbafe7d3.json`](../../sessions/ac/acc86edd71b9cbafe7d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Here are the results:

## 结果

**脚本路径**: `/root/autodl-tmp/importance_margin_vla_compress/visualize_token_importance.py`

**Token spatial mapping**: image=224×224, patch=14×14, grid=16×16 = 256 tokens/image, feature dim=2048

**生成的 heatmap**:
- `artifacts/token_importance_heatmaps/step000_t0000.png` (~790KB)
- `artifacts/token_importance_heatmaps/step001_t0005.png`
- `artifacts/token_importance_heatmaps/step002_t0010.png`
- `artifacts/token_importance_heatmaps/summary_average.png`

## 空间分布分析

**Norm 统计**: range 170.95–283.95, mean=250.29, std=16.12, CV=0.065

**明确的 center-high, edge-low 模式**:

Row means 显示中心行 (7-9) norm 最高 (~265-267)，边缘行 (0, 14-15) 最低 (~235-236)：
```
Row 7:  267.5  ← 最高
Row 8:  266.5
Row 9:  265.1
  ...
Row 0:  236.3  ← 最低
Row 14: 235.3
```

Column means 同样：中心列 6-8 最高 (~261-265)，边缘列 1, 13 最低 (~239)。

**k=0.9 时被剪掉的 26 个 token 位置**:
- 集中在 **row 0 (上边缘)** 和 **rows 12-15 (下边缘)**
- **50% 的被剪 token 在图像最外圈** (edge tokens 只占总量 23%，被剪概率是 2 倍)
- 最低 norm=170.95 在 (12,1) — 图像左下角背景区域

**结论**: L2norm pruning 的空间选择 pattern 是清晰的 — 保留中心区域 (机器人手臂/目标物体)、剪掉边缘 (桌面/背景)。Random 选择则均匀散布剪掉的 token，有概率丢失中心关键区域的 token。这解释了为什么 k=0.9 时 L2norm 保持 98% SR 而 random 崩到 5% — random 有概率同时删除多个关键空间位置的 token。

---
