# analysis gpt2m full 5method leadlag

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpt2m_full_5method_leadlag_20260515T222426_result.json`
- **Structured JSON:** [`1a3e0d56dbf8323817d2.json`](../../sessions/1a/1a3e0d56dbf8323817d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册 (`art_20260515_bce78c`)。核心结果：

**Forward（canary→diversity）：6/6 pairs 达成 4/5 方法共识**
- Naive xcorr（|r|>0.98）、differenced xcorr（p_fdr<0.001）、threshold onset（Δ=+1~+2 gen）、permutation Granger（p_fdr=0.003）一致支持
- TY Granger 0/6 显著——entropy pairs 的 df_resid=1，ECE pairs 的 df_resid=4，检验力不足（与 Pythia T=10 一致，符合 C001 约束）

**Reverse（diversity→canary）：0/6 pairs 达成共识**
- 仅 naive xcorr（inflated by shared trends）和 permutation Granger（d→ece 3 pairs, 效应量仅为 forward 的 1/10）部分显著
- Differenced xcorr 彻底区分方向：forward 全部 p<0.001，reverse 全部 p>0.18

**Threshold onset** 显示 entropy 是最早的 canary（gen 1），ECE 次之（gen 1–2），diversity 一致在 gen 3 才 onset。

---
