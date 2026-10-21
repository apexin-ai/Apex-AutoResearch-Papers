# ssh check pythia410m generalize

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_pythia410m_generalize_20260517T112721_result.json`
- **Structured JSON:** [`d868c3fe2b7d030850a2.json`](../../sessions/d8/d868c3fe2b7d030850a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，分析结果：

**Drift**: 严重 model collapse — token_entropy -61.69%, distinct_1/2/3 下降 27-32%, ECE +3759%, perplexity +3369% (26.9 → 935.0)

**5-Method 因果分析** (58/80 = 72.5% sig rate):
- 7/16 pairs 达到 5/5 全票一致 (token_entropy→distinct_*, self_bleu→ppl, ece→distinct_*)
- 13/16 pairs 达到 consensus ≥ 3
- PermG: 10/16 pairs 显著 (62.5%)
- differenced_xcorr: 16/16 全部显著
- 最弱信号: effective_rank→perplexity (1/5)

Pythia-410M 在 WikiText-103 上确认了 GPT-2 Medium 实验中观察到的 canary collapse 模式，泛化性验证通过。

报告已保存到 `artifacts/generalize_pythia410m/analysis_report.md`。

---
