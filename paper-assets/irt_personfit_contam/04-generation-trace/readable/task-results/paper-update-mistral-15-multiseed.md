# paper update mistral 15 multiseed

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_update-mistral-15-multiseed_20260524T103345_result.json`
- **Structured JSON:** [`621b4e9ee4bf2d293dee.json`](../../sessions/62/621b4e9ee4bf2d293dee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 修改汇总

**results.tex** (3 层均已更新):

| 位置 | Before | After |
|------|--------|-------|
| 正文 prose (L10) | `Mistral ($\|d\|{=}2.64$/$3.50$)` | `Mistral ($\|d\|{=}3.37$/$3.50$)` |
| Table 1 (L30) | `Mistral & MMLU & --- & $-2.64$ [$-7.3$, $-1.5$]` | `Mistral$^{\dagger}$ & MMLU & --- & $-3.37$ ($\pm$0.68)` |
| Table 1 footnote (L33) | `Qwen and Llama MMLU 15%/25%/50%: multi-seed means...` | `Multi-seed conditions: means ($n{=}3$...) shown as $\pm$SD; remaining single-seed with bootstrap CIs` |
| Table 2 free-θ (L91) | `2.64 & 2.69 & 1.0×` | `3.37 & 2.69 & 0.8×` |
| Table 3 lz* (L151) | `Mistral & $\ell_z^*$ & $2.64$ [$1.5$, $7.3$]` | `Mistral$^\dagger$ & $\ell_z^*$ & $3.37$ ($\pm$0.68)` |
| Table 3 footnote (L155) | `Llama and Mistral are single-seed with bootstrap CIs` | `Remaining conditions are single-seed with bootstrap CIs` |

**limitations.tex**: `available for Qwen and Llama` → `available for Qwen, Llama, and Mistral`

**gen_fig_theta_scatter.py**: Mistral 15% `(52.4, 2.64, 1.49, 7.29)` → `(52.4, 3.37, 2.69, 4.05)`

**gen_fig_heatmap.py**: Mistral 15% `3.01` → `3.37`, CI `[1.8, 8.2]` → `(±0.68)`

编译 16 页（main text + appendix），anonymous repo 已 push: `892deca..5d29dce`。

---
