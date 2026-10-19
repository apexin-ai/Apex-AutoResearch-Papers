# paper figure fig theoretical sign probability

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig-theoretical-sign-probability_20260518T212424_result.json`
- **Structured JSON:** [`2cc12027d72b4624ba08.json`](../../sessions/2c/2cc12027d72b4624ba08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图已生成，PDF 和 PNG 均已保存。

**输出文件：**
- PDF: `figures/paper/fig_theoretical_sign_probability.pdf`
- PNG: `figures/paper/fig_theoretical_sign_probability.png`

**关键读数：**

| p | K=2 | K=4 | K=8 | K=16 |
|---|-----|-----|-----|------|
| 0.05 | 51.3% | 27.0% | 14.9% | 8.9% |
| 0.10 | 52.6% | 29.1% | 17.6% | 12.3% |
| **0.125** | 53.3% | 30.2% | **19.0%** | 14.2% |
| 0.20 | 55.6% | 33.9% | 24.0% | 20.6% |
| 0.50 | 66.7% | 53.3% | 50.2% | 50.0% |

核心结论可视化验证：K=8, p=12.5% 时只有 19% 的 gradient update 方向正确；K 越大，低 success rate 区域的 sign accuracy 越差，趋近 y=p 对角线。K=16 在 p=0.05 时仅 8.9%，几乎是纯噪声。

---
