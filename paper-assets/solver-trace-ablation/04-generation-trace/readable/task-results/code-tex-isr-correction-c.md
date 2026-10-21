# code tex isr correction c

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tex-isr-correction-c_20260515T171800_result.json`
- **Structured JSON:** [`118af7e829b6652f8ce0.json`](../../sessions/11/118af7e829b6652f8ce0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译通过，18 页，无错误。

修改汇总：

| 位置 | 原值 | 新值 |
|------|------|------|
| appendix.tex:420 — s43-1000 ISR | `0.531` | `0.465$^\S$` |
| appendix.tex:425 — 1000-step 3-seed mean±std ISR | `$0.18{\pm}0.31$` | `$0.16{\pm}0.27$` |
| appendix.tex:394 — 表格 caption | — | 新增 `$^\S$` 脚注说明 decompose_fol() +12% inflation artifact |

experiments.tex 和 main.tex 中无 `0.531` 引用，无需改动。Prolog 表中的 `0.53` 是 Prolog PR mean，与此无关。

---
