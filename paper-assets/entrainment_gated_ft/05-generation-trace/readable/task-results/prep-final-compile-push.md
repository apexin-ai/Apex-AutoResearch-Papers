# prep final compile push

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_final-compile-push_20260524T045337_result.json`
- **Structured JSON:** [`e61c948450ae8bbe0d40.json`](../../sessions/e6/e61c948450ae8bbe0d40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**Figure 2**：`gen_fig2.py` 中 HellaSwag ρ 硬编码为 0.4/0.517，已改为 0.3/0.683 并重新生成图。论文 PDF 中 Figure 2 已正确显示 ρ=0.3, p=0.6830。

**编译**：22 页（主文 8 页 + Limitations + References + Appendix），0 undefined references/citations，无 critical warnings。

**匿名仓库**：`figures/gen_fig2.py` 已更新并 push 到 `anonymous-nlp-2026-2/entrainment_gated_ft` main 分支（`3b74292`）。`data/convergence_table.csv` 已是正确值无需改动。

注意：论文源文件（experiments.tex, appendix.tex, main.pdf）不在匿名仓库中（之前已移除，PDF 通过 OpenReview 单独提交），因此本次 push 只包含 `gen_fig2.py` 的修复。

---
