# paper d031 framing core

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d031-framing-core_20260520T112415_result.json`
- **Structured JSON:** [`68bd94496ec3ab276346.json`](../../sessions/68/68bd94496ec3ab276346.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 9 处修改完成：

**abstract.tex (3处)**
- **N1**: L3 — "Recursive LLM generation" → "Recursive generation by base (pretrained) LLMs"
- **W3**: L4 — "under standard decoding" → "under standard decoding (temperature $\leq 0.7$, nucleus $p{=}0.9$)"
- **N2**: L6 — "equivalence testing" → "preliminary equivalence testing (…; $n{=}3$ seeds)"

**introduction.tex (1处)**
- **N4**: L19-22 — 贡献列表重排为 DDR decomposition → task formulation → interpretable baseline + evaluation; 第3条同步加入 preliminary + n=3 seeds 限定

**discussion.tex (3处)**
- **W7**: L10 — 新增两个诊断场景 (batch auditing + provenance tracing)
- **W8**: L11 — 新增 generator-unknown 部署下的 conservative lower bound 说明
- **N1 instruct**: L21 — 新增 ρ 反转机制假说 + QLoRA recovery 解释

---
