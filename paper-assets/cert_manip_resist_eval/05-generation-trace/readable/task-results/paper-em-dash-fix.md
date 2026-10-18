# paper em dash fix

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_em-dash-fix_20260523T015250_result.json`
- **Structured JSON:** [`baea28983783cb2949ed.json`](../../sessions/ba/baea28983783cb2949ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**修复完成。**

- **appendix.tex:50**：修复 2 处 em-dash
  - `conditions---stronger` → `conditions, stronger`
  - `retains---indeed improves---its` → `retains (indeed improves) its`
- **未修改的 `---`**（共 3 处，均为非 em-dash 用途）：
  - `appendix_attacks.tex:29` — 攻击模板字面量（`\texttt` 内容）
  - `results.tex:47` — 表格中缺失值占位符（2 处）

全部 `.tex` 文件中不再有需要修复的 em-dash。

---
