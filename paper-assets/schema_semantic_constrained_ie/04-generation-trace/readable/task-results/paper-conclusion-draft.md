# paper conclusion draft

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_conclusion_draft_20260514T061814_result.json`
- **Structured JSON:** [`0a54740c989cd81ceec2.json`](../../sessions/0a/0a54740c989cd81ceec2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 工具不在当前可用工具列表中，无法注册。文件已写入：

`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section7_conclusion.tex`

**内容概要（~400 words）：**

- **Para 1 — 三个贡献**：(1) Violation landscape study，发现 DR 由 constraint tightness 驱动而非 ontology size；(2) 两层 constraint 架构（grammar + semantic），grammar 是 semantic 的 enabling prerequisite；(3) SciERC 实证验证 DR 15.37%→0.93%（↓94%），RV/ET→0%，F1-neutral。DocRED 用 `\placeholder{}` 占位。
- **Para 2 — Limitations**：CF 从 0.08%→9.90%，归因于 per-relation independent type enforcement 导致的 EVR drift，grammar 层不引入 CF（0.08%=baseline），明确为 open challenge。单模型、两数据集、zero-shot only。
- **Para 3 — Future Work**：cross-model validation、global entity type consensus 解决 CF、fine-tuned model integration、跨语言 IE。

所有定量 claim 均附 `% exp_id:` 注释。需要你手动执行 `register_artifact` 或告诉我替代注册方式。

---
