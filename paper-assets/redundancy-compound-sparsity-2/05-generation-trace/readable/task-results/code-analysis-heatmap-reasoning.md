# code analysis heatmap reasoning

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analysis_heatmap_reasoning_20260512T174847_result.json`
- **Structured JSON:** [`d927cce714111aa7a99f.json`](../../sessions/d9/d927cce714111aa7a99f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果摘要：

## Reasoning Traces EMA Heatmap 结果

**数据**: 4 个 MATH 问题生成 4220 tokens（截断至 4096），耗时 106s 生成 + 82s EMA 计算。

### Reasoning Traces 统计

| gamma | global mean | layer std | 最强层 | 最弱层 |
|-------|------------|-----------|--------|--------|
| 0.5 | 0.5968 | 0.0576 | [31, 30, 18, 19, 33] | [4, 3, 2, 1, 0] |
| 0.7 | 0.5965 | 0.0527 | [30, 31, 18, 19, 35] | [4, 3, 2, 1, 0] |
| 0.9 | 0.5793 | 0.0376 | [30, 31, 19, 18, 35] | [4, 3, 2, 1, 44] |

### WikiText vs Reasoning 关键差异

**整体 pattern 高度一致**：global mean 差异极小（<0.003），最强/最弱层几乎相同。

**局部差异最大的层**（所有 gamma 一致）：
- **Layer 1**: reasoning 比 WikiText 低 ~0.04（浅层 reasoning 的 EMA 更不稳定）
- **Layer 7, 10, 13**: reasoning 比 WikiText 高 ~0.03（中浅层 reasoning 信号更强）
- **Layer 47**: reasoning 在 gamma=0.9 时比 WikiText 高 0.019（最后一层差异）

Top-5 divergent layers: **[1, 2, 7, 10, 13]** — 集中在浅层和中浅层（0-13），说明 reasoning traces 和自然语言在**浅层表征**上差异最大，深层则趋同。

### 输出文件（westd-16980:/root/carc/results/）
- `heatmap_reasoning_data.pt` — 原始数据
- `ema_heatmap_reasoning_gamma{05,07,09}.pdf` — 单 gamma heatmap
- `ema_heatmap_reasoning_comparison.pdf` — 三 gamma 对比
- `ema_heatmap_wikitext_vs_reasoning.pdf` — WikiText vs Reasoning 折线图
- `analysis_heatmap_reasoning.py` — 脚本（支持 `--plot-only` 重绘）

---
