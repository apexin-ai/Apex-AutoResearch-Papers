# paper 6point figures

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_6point_figures_20260514T093936_result.json`
- **Structured JSON:** [`4301a196467e75d3186e.json`](../../sessions/43/4301a196467e75d3186e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 figures generated and registered. All files at `/root/autodl-tmp/pacs/figures/`:

| 图表 | 文件 | 大小 |
|------|------|------|
| **Dose-Response 曲线** | `dose_response_6point.pdf/.png` | 22.5 / 159 KB |
| **Crossover Diagram** | `crossover_6point.pdf/.png` | 21.2 / 243 KB |
| **Cohen's d** | `cohens_d_6point.pdf/.png` | 20.8 / 168 KB |

关键设计：
- s=0.10 用**空心圆**标记 + **虚线**连接到 s=0.15，与 active zone 的实心/实线视觉区分
- 灰色竖线和浅灰色阴影标注 onset zone 区域
- Dose-response 用 log scale（数值跨越 0.015 → 28.8）
- Crossover 用 symlog scale（处理负值和多数量级跨度）
- Cohen's d 带 small/medium/large 阈值参考线和 bootstrap CI error bars
- 色盲友好配色（Okabe-Ito：#0072B2 / #D55E00）
- 300 DPI，DejaVu Sans

Cohen's d 计算结果（s010/s035 从 per-problem II 现场计算，s015-s030 用已有 paired bootstrap B=10000）：
- **DeepSeek**: 0.38 → 0.61 → 0.73 → 0.95 → 1.13 → 0.82
- **Qwen**: -0.05 → 0.37 → 0.72 → 1.23 → 1.44 → 1.10

---
