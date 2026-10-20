# analysis qwen35 08b wiki a100 s42 v2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen35_08b_wiki_a100_s42_v2_20260519T131606_result.json`
- **Structured JSON:** [`7e45a3e5a2f35a907a34.json`](../../sessions/7e/7e45a3e5a2f35a907a34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果总结

- **conclusion: success**
- PermG (FDR): **8/8** fwd, **0/8** rev — 完美单向因果
- K≥4 consensus: **8/8**
- MMCT (uniform_fwd): **1.0** (8/8)
- TY Granger: 6/8
- distinct_1 drift: **-32.50%**
- distinct_2 drift: -45.99%
- distinct_3 drift: -47.21%
- token_entropy drift: **-54.03%**
- ece drift: **+5643.53%**
- mauve drift: -22.89%
- perplexity: 20.55 → 1247.19 (+5969%)
- GPU hours: 12.8h

**关键发现**: Qwen3.5-0.8B (第5个独立架构族) 在 fp32 α=1.0 下展现出所有架构中最强的 canary→downstream lead-lag 信号——8/8 pair 全部 PermG 正向显著且 0/8 反向显著，跨架构泛化完全确认。与 Pythia-410M (~75% PermG) 相比，Qwen3.5 的信号更为清晰。

---
