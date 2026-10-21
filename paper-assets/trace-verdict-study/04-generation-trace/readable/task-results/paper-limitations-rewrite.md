# paper limitations rewrite

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_limitations-rewrite_20260525T124530_result.json`
- **Structured JSON:** [`958c85a2c2f317016441.json`](../../sessions/95/958c85a2c2f317016441.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

替换完成。对比如下：

**旧文本**（15 行，3 个 `\paragraph{}`）：
- `\paragraph{Scope.}` — 4 句，涵盖 Python-only、语言差异、模型规模、human-written code
- `\paragraph{Variance and robustness.}` — 2 句，涵盖 seed 数量、VOTA tokenizer truncation
- `\paragraph{Mechanistic analysis.}` — 3 句，涵盖 gradient masking、CodeLlama head-2048 proxy、VOTA 阈值敏感性

**新文本**（4 行，1 段连续文本）：
1. Scope：Python-only, code-specialized models 1.5B–13B, 未验证其他语言/human-written code/30B+
2. 泛化性：Python 结构化异常使 exception 信号特别丰富，其他语言可能不同
3. 机制分析：gradient masking 只隔离 backward-pass，forward-pass attention 未量化

去掉了 VOTA tokenizer sensitivity、CodeLlama head-2048 proxy、阈值敏感性等过细的点。

---
