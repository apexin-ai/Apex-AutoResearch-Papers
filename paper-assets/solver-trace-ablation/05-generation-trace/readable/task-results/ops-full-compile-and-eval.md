# ops full compile and eval

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-compile-and-eval_20260515T070522_result.json`
- **Structured JSON:** [`d71a9f9a09ca5584842c.json`](../../sessions/d7/d71a9f9a09ca5584842c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项结果汇报：

**1. Eval 指标（plan018-additive-random-b01-s43-r2）**
- Registry 中已有：`eval_prove_rate = 0.88`, `eval_mean_isr = 0.058`
- 无需重新运行 eval

**2. LaTeX 编译结果**
- 编译成功，14 页，516,993 bytes
- **Errors: 0**
- **Undefined references/citations: 0**
- Warnings 仅有：2x `'h' float specifier changed to 'ht'`（无害）+ 7x hyperref PDF string token warnings（math symbols in section titles，无害）

**3. `app:o1-ablation` label**
- 正确解析为 `\newlabel{app:o1-ablation}{{E.3}{14}{...}{subsection.E.3}{}}`
- 即 Appendix E.3，第 14 页，标题 "$O(1)$ vs.\ $O(n)$ ISR Ablation"

---
