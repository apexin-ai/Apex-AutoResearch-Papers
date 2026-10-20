# paper fix rebuttal prep data

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-rebuttal-prep-data_20260524T102134_result.json`
- **Structured JSON:** [`06d9f413c78c55eac67b.json`](../../sessions/06/06d9f413c78c55eac67b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修正完成。逐项 before → after：

| # | 位置 | Before | After | 来源 |
|---|------|--------|-------|------|
| 1 | Q1 L9 | `恢复 13.4× 检测力` | `恢复 2.4× 检测力（Qwen 50% 污染: free-θ \|d\|=5.08 → fixed-θ \|d\|=12.32; Table 2 / results.tex:54,94）` | results.tex:54,94 (`tab:theta_fixed`) |
| 2 | Q2 L15 | `Qwen 83% 吸收强 vs Llama 59% 吸收弱` | `Qwen 67.8% 吸收强 vs Llama 59.4% 吸收弱（results.tex:70,72）` | results.tex:70 (Qwen), :72 (Llama) |
| 3 | Q2 L15 | `acc=89.5%` | `acc=89.7%（results.tex:59）` | results.tex:59 |
| 4 | Q2 L15 | `baseline accuracy range 59%-83%` | `baseline accuracy range 59.4%–67.8%` | 同上两个来源 |
| 5 | Q3 L21 | `detection frontier 框架（Table 1）` | `detection frontier 框架（§1 Introduction, introduction.tex:12）` | Table 1 实为 `tab:cohens_d`（Cohen's d 表）；detection frontier 仅在 introduction.tex:12 文本中出现，`tab:frontier` 在 background.tex 中但未被编译进论文 |

---
