# analysis rho paper impact list

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rho_paper_impact_list_20260515T132710_result.json`
- **Structured JSON:** [`b1df63f7c40998749985.json`](../../sessions/b1/b1df63f7c40998749985.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出：

**本地**: `artifacts/rho_paper_impact_list.md` (详细版，269 行)
**服务器**: `/root/autodl-tmp/struct_self_consist_ie/analysis_rho_unification/` 下:
- `paper_impact_list.md` (精简版)
- `analysis_unified_rho.json` (已同步)

核心结论：

1. **论文核心贡献（correlation-selection gap）不受影响** — 基于 SciERC N=8，不在修正范围内
2. **主要影响在 appendix**: tab:robustness (LLaMA CoNLL N=16 全部 5 signal 偏低 ~0.015)、tab:n-scaling (FK N-scaling 可能从 +0.030 降至 +0.005)
3. **FK N-scaling claim 可能失效** — seed456 FK 从 0.345→0.272，是唯一可能受实质影响的 claim
4. **Structural advantage over LP 反而加强** — 统一管道下 SJ-LP Δ 从 +0.153 增至 ~+0.170
5. **关键缺口**: JSON 不含 N=8 数据和 seed123，Table 1 (N=8 LLaMA CoNLL) 及多处正文引用需用统一管道补算后才能确定是否需更新

---
