# code tex d091 corrections

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tex-d091-corrections_20260515T170707_result.json`
- **Structured JSON:** [`e629680b061c67e49ada.json`](../../sessions/e6/e629680b061c67e49ada.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 项修改全部正确应用，编译无错误。

**结果：**
- **experiments.tex L32**: `≤3% non-hacking` → `0% non-hacking (3 samples escape text-match classifiers but are functionally degenerate; see Appendix)`
- **introduction.tex L27**: 添加 "at 500 steps" 限定（`69.7% of proved samples at 500 steps ... versus 0% under matched random at 500 steps`）
- **appendix.tex 表格**:
  - s44-1000 行 N-H: `3` → `0‡`
  - 3-seed mean N-H: `1.0±1.7` → `0.0±0.0`
  - 表格标题新增 `‡` 脚注，说明 3 个样本的退化性质（disjunctive conclusions bypass H8, commuted premises bypass H1, ISR=0）
- PDF 编译成功：17 页，536KB，无新增 warning

---
