# paper zeroshot section draft

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_zeroshot-section-draft_20260519T170646_result.json`
- **Structured JSON:** [`3056594b6cbf85b0535a.json`](../../sessions/30/3056594b6cbf85b0535a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

草稿已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex`。

**段落摘要**: 72B zero-shot 下 LP ρ 趋近零（三数据集均<0.12），而结构信号 VC/SJ 仍保持中等相关（0.22-0.42），表明 LP 依赖 fine-tuning 校准。Construction 效果与 degeneracy 单调相关（SciERC 21% degen → +1.53pp, p=0.008；majority vote 也 +1.39pp）。结论：gap 与 self-consistency 在结构化 IE 中的内在属性一致，非 LoRA-specific artifact。

**注意事项**:
- Few-NERD 8B FT 的 VC ρ 缺失（标记为 `---`），需 Paper Agent 补全
- LP selection 数字仅引用 SciERC/CoNLL（FewNERD ZS LP selection 精确值未在 registry 中）
- 7B/14B/32B 占位已预留

---
