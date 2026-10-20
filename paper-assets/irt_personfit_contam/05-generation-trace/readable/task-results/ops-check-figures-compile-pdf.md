# ops check figures compile pdf

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-figures-compile-pdf_20260523T163042_result.json`
- **Structured JSON:** [`27a7a420e7360d77f304.json`](../../sessions/27/27a7a420e7360d77f304.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

---

## Task A: Figure 更新状态

| Figure | 生成脚本 | 状态 |
|--------|----------|------|
| **fig_heatmap.pdf** | `figures/paper/gen_fig_heatmap.py:35` | **需要更新** — Llama 行硬编码旧值 `[nan, 2.27, 2.97, 2.50, nan, nan]`，CI 也是旧的 `['', '[1.6, 4.6]', '[2.0, 6.1]', '[1.8, 5.2]', '', '']` |
| **fig_theta_scatter.pdf** | `figures/paper/gen_fig_theta_scatter.py:33,40,44` | **需要更新** — Llama d 值硬编码旧值：15% `2.27`→应为 `2.11`，25% `2.97`→`1.99`，50% `2.50`→`2.33`；CI 也需更新 |
| **fig_grpo.pdf** | 未找到生成脚本（可能手动制作或脚本未提交） | **不需要更新** — 该图仅涉及 Qwen GRPO trajectory，不含 Llama d 值 |

论文正文 (`results.tex`) 已使用新值 `2.11/1.99/2.33`，但两个 figure 仍显示旧值 `2.27/2.97/2.50`，**figure 与正文不一致**。

---

## Task B: 编译结果

- **编译状态**: 成功（修复了 `results.tex:69` 的 `\ell_z^*_{\text{fixed}}` double subscript 错误，改为 `{\ell_z^*}_{\text{fixed}}`）
- **总页数**: 15 页
- **正文页数**: **8 页**（pages 1–8，含 limitations）— 恰好在 EMNLP Long paper 8 页限制上
- **References**: pages 9–10
- **Appendix**: pages 11–15

### 警告

| 严重度 | 位置 | 详情 |
|--------|------|------|
| **高** | `results.tex:79-100` (Table 3) | Overfull hbox **22.96pt** — 表格超出列宽，需要缩窄 |
| 低 | `appendix.tex:200-208` | Overfull hbox 0.79pt — 可忽略 |
| 低 | `appendix.tex:347-363` | Overfull hbox 0.89pt — 可忽略 |
| 低 | `appendix.tex:396-409` | Overfull hbox 4.58pt — 轻微 |
| — | 全文 | 20 个 underfull hbox — 正常范围 |

---
