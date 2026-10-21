# write paper figures

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_paper-figures_20260514T231318_result.json`
- **Structured JSON:** [`98f7d9b22873a3be2b01.json`](../../sessions/98/98f7d9b22873a3be2b01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 PDF 矢量图全部生成：

| 文件 | 大小 | 内容 |
|------|------|------|
| `fig1_sta_overview.pdf` | 39K | STA 概念三面板图（pipeline / LOO ablation / Goodhart） |
| `fig2_isr_collapse.pdf` | 17K | ISR 崩塌轨迹双 Y 轴图（PR↑ vs ISR↓，100→500→1000 步） |
| `fig3_hacking_composition.pdf` | 22K | Hacking 模式堆叠柱状图（4 条件 × H7/H1/genuine） |
| `fig4_prolog_comparison.pdf` | 32K | Prolog 双面板（FOL vs Prolog ISR + 3 种 gaming mode） |

所有数据来自 registry，关键数值：
- Fig2: PR=[32%, 93%, 96%], ISR=[0.642, 0.132, 0.003]
- Fig3: ISR 条件 H7=64.5%（加权 3-seed 均值），Random H7=0%，SFT genuine=92.9%
- Fig4: Prolog exec-only ISR 全面低于 FOL；STA 三个 seed 分别展示 H7/H1/query-as-fact 三种不同 gaming mode

文件路径：`/root/solver-trace-ablation/paper/figures/`，可直接在 LaTeX 中 `\includegraphics` 引用。

---
