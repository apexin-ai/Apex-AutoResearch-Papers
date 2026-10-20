# code exp003 figure table

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp003_figure_table_20260513T210000_result.json`
- **Structured JSON:** [`8f170516c1a308acbd0c.json`](../../sessions/8f/8f170516c1a308acbd0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。三个产物已生成：

| 文件 | 大小 |
|------|------|
| `artifacts/exp003_decoding_ablation.pdf` | 22K |
| `artifacts/exp003_decoding_ablation.png` | 53K |
| `artifacts/exp003_decoding_ablation.tex` | 628B |

Summary table 输出：

```
Config                 Decoding                1v2 AUC  K*(θ=.60) Top-3 Features
--------------------------------------------------------------------------------
Config1-Greedy         greedy                   0.6893          2 self_bleu, hapax_ratio, ttr
Config2-Nuc09          nucleus p=0.9, T=1.0     0.6866          2 hapax_ratio, ttr, surp_skew
Config3-T07            nucleus p=0.95, T=0.7    0.6887          2 hapax_ratio, ttr, low_freq_ratio
Config4-T12            nucleus p=0.95, T=1.2    0.7039          2 hapax_ratio, ttr, surp_skew
```

脚本从 `artifacts/exp003_analysis.json` 读取完整数据，也有硬编码 fallback。样式：serif 字体、无网格线、colorblind-safe 4 色 Tableau palette、深色边框浅色填充、θ=0.60 和 chance 虚线标注、单栏宽 3.5×2.5 inch。

---
