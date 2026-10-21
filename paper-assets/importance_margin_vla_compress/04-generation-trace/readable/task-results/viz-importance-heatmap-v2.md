# viz importance heatmap v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_importance_heatmap_v2_20260524T195136_result.json`
- **Structured JSON:** [`40e130bc46d88c9108e9.json`](../../sessions/40/40e130bc46d88c9108e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 artifacts 已注册。总结：

### 产出

**westd-38929** 上 `/root/autodl-tmp/importance_margin_vla_compress/artifacts/figures/` 下已有 3 组有效图表（PDF+PNG）：

| 文件 | 尺寸 | 大小 | 内容 |
|------|------|------|------|
| `fig_importance_heatmap` | 3497×1602 | PDF 1580KB, PNG 1441KB | 2行×4列：Original \| Importance heatmap \| k=0.95 pruned \| k=0.85 pruned（task 22 + task 3）|
| `fig_importance_comparison` | 2823×1008 | PDF 302KB, PNG 267KB | 1行×3列：Original \| L2-Norm k=0.85 \| Random k=0.85 |
| `fig_importance_histogram` | 1581×898 | PDF 23KB, PNG 82KB | 重要性分布直方图 + cliff zone 标注 |

所有图片已通过 PIL 验证完整性，artifacts 已注册（`art_20260524_75d5a6`, `art_20260524_9d40e8`, `art_20260524_cebd13`）。

### 与任务要求的差异

现有图布局与任务 spec 略有不同：
- 任务要求 k=0.9，实际用了 k=0.95 和 k=0.85（更能展示不同压缩率的效果）
- Random 对比在独立图中而非合并到 heatmap 图中
- 现有布局实际上更适合论文呈现——heatmap 图展示压缩程度梯度，comparison 图专门对比 L2-norm vs Random

**未做视觉检查**：base64 传输到本地失败。如需视觉确认，可在远程服务器直接查看或用其他方式传输。

---
