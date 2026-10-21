# paper writing results

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_results_20260515T175043_result.json`
- **Structured JSON:** [`e78a53fcee7e0580deef.json`](../../sessions/e7/e78a53fcee7e0580deef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

§4 Results 已写入 `docs/paper/results.tex`。结构：

- **§4.1** Count curves: NER/RE 单调下降，MAVEN 反向上升（不 claim universal degradation）
- **§4.2** Pairwise SCS→confusion: r²=1.3–1.7%，framed as "modest but robust, first empirically isolated"，含 tab\_pairwise（有 r² 列）
- **§4.3** BCS-controlled: 9.1pp→31.2pp（3.4× amplification），含 tab\_bcs\_controlled（有 CI）
- **§4.4** Multi-channel: IntraSub 与 BCS 近完美单调（ρ≥0.954），missed rate flat，两通道正交。含 tab\_error\_taxonomy
- **§4.5** Centrality confound: MAVEN per-type ρ 反向（+0.189/+0.208），归因于 same-domain cluster isotropy \cite{cai-isotropy-clusters-2021}，pairwise 信号完好，Few-NERD per-type ρ=−0.293 方向正确

所有关键数字附 bootstrap CI，r² 贯穿全文，无未经检验的 "significantly"。

---
