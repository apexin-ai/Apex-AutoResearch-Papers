# ops fig radar chart

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fig-radar-chart_20260525T142321_result.json`
- **Structured JSON:** [`e558c833e6ef51fa097d.json`](../../sessions/e5/e558c833e6ef51fa097d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Output files delivered:
- **PDF**: `docs/paper/figures/fig_model_radar.pdf` (47 KB)
- **PNG**: `docs/paper/figures/fig_model_radar.png` (463 KB)

Key observations from the radar chart:
- **API models**: 7/9 have ASR < 5% across all attacks. Claude 3 Haiku is a major outlier (prompt injection ASR = 77%), GPT-4.1 Nano is moderately vulnerable (~10-17%)
- **Local models**: Position bias is universally the dominant attack vector (26-48% ASR). LLaMA 3.1-8B has uniformly high vulnerability across all 6 attacks (~16-48%)
- The sqrt radial scale preserves readability for both low-ASR clusters and high-ASR outliers

---
