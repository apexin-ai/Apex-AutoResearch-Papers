# paper gold section draft

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_gold-section-draft_20260515T084122_result.json`
- **Structured JSON:** [`4832b9766d12ff42a5a4.json`](../../sessions/48/4832b9766d12ff42a5a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已写入 `artifacts/gold_set/paper_draft_gold_section.md`。

框架包含 7 个部分：
- **Annotation Protocol** — 描述标注流程，`[KAPPA_PLACEHOLDER]` 留给 batch 2/3 的 inter-annotator agreement
- **Gold Label Distribution** — SWE 近平衡 (52.3% progress)，OH 极度偏斜 (98.4%)
- **Model vs Gold 表格** — TWV probe 0.768 领先 SWE-only 子集，structural GB 0.760 领先全集；所有模型超过对应 silver labels
- **MV–Gold Agreement** — conf=1 → conf≥2 从 69.6% 升至 82.5%，验证 confidence stratification
- **OH False-Stagnation Bias** — MV 在 OH 上 93% 的 stagnation 标注为假阳性，与 SWE 的 false-progress 方向相反，关联 C2 中 cmd_rep 的 firing rate 差异
- **GRU 污染检查** — train-set 0.844 vs test-set 0.871，无记忆优势
- **Limitations** — 单标注者、OH 类别偏斜、N=195 统计功效、采样偏差、窗口级标注局限

所有待填数字均标记为 `[PLACEHOLDER]` / `[CI_PLACEHOLDER]` / `[KAPPA_PLACEHOLDER]`。

---
