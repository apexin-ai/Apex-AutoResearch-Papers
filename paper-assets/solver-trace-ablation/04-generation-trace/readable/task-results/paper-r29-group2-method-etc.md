# paper r29 group2 method etc

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r29-group2-method-etc_20260522T142617_result.json`
- **Structured JSON:** [`a9d8e980235854eb807a.json`](../../sessions/a9/a9d8e980235854eb807a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 项完成。汇总：

### B. ISR vs Shapley（method.tex:44-45）
- 在 ISR 定义段（eq:isr 后）插入 2 行：ISR = Shapley $(n{-}1)$-coalition 退化、$O(2^n) \to O(n)$ 复杂度对比、binary framing 的设计取舍。引用 `lundberg2017unified`。

### M. ISR unproved（method.tex:44）
- 同一位置，在 ISR 定义后加 "Unproved samples receive ISR=0 by definition"。

### C. Discussion 扩展（conclusion.tex:2-4）
- 原文 1 句扩展为 4 句：STA 泛化性（formal verifiers / test suites）、Goldilocks hypothesis（capacity narrow band + 50% non-convergence）、ISR 局限性与 per-sample mode 诊断路径。

### E. Survivorship bias（limitations.tex:6）
- seed power 段后插入 1 句：degeneration conditional on convergence，3/6 exec-only seeds 不收敛保留 85-87% genuine，指向 `app:seed-convergence`。

### N. Missing references（references.bib + related_work.tex:20）
- `references.bib` 添加 3 条：`lundberg2017unified`（NeurIPS 2017）、`coste2023reward`（ICLR 2024）、`moskovitz2023confronting`（ICLR 2024），后两条含 arXiv note。
- `related_work.tex` reward hacking 段加半句引用 ensembles + constrained optimization，对比 STA 在 output level 诊断。

---
