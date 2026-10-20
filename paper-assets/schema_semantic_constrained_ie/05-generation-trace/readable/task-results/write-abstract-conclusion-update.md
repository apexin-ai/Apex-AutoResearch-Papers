# write abstract conclusion update

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_abstract_conclusion_update_20260514T201909_result.json`
- **Structured JSON:** [`070487bc066a49e81a3c.json`](../../sessions/07/070487bc066a49e81a3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已更新完毕。变更摘要：

**abstract.tex**:
- 替换 DocRED placeholder 为实际结果（DR↓45%, 18.46%→10.21%, Rel F1 +0.50pp, Ent F1 +1.23pp）
- 添加 constraint tightness τ̄ 数据（SciERC 0.333, DocRED 0.842）
- 更新 SciERC 结果含 p=0.58 标注"not significant"
- 添加 cross-model 验证（Qwen3-8B + Llama-3.1-8B-Instruct）
- 添加 post-hoc filtering 对比
- 移除旧的 prompting 段落和 CF 细节以控制篇幅

**section7_conclusion.tex**:
- DocRED baseline 18.70% → 18.46%
- 第一贡献添加 τ̄ 具体数值及"DR reduction scales inversely with τ̄"
- DocRED placeholder 替换为完整结果 + post-hoc comparison
- Limitations 更新为双模型验证，标注 `[LLAMA-DOCRED-TBD]`
- Future Work 第(1)条更新为扩展至更大模型 + 完成 Llama DocRED 验证

---
