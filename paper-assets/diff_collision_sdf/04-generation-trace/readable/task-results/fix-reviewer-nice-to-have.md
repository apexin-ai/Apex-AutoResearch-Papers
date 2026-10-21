# fix reviewer nice to have

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_reviewer_nice_to_have_20260527T205429_result.json`
- **Structured JSON:** [`cb92b8ea620542cc9c99.json`](../../sessions/cb/cb92b8ea620542cc9c99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。逐项汇报：

**N1. appendix 变量名格式化**
`appendix.tex:113` — `avg\_max\_obstacle\_displacement` 已用 `\texttt{}` 包裹。

**N2. per-task fingerprint 图加入 appendix**
- 图文件从 `artifacts/_project/chart/` 复制到 `artifacts/figures/fig_pertask_car_fingerprint.png`（与 `\graphicspath` 一致）
- `appendix.tex` Per-Task CAR Breakdown 节末尾（表格和描述文字之后、SSR 节之前）插入了 figure 环境，`\label{fig:pertask_fingerprint}`
- `claim3.tex:27` per-task ordering 描述处添加了 `Figure~\ref{fig:pertask_fingerprint}` 引用

**N3. stepwise caption 统计检验**
已检查：stepwise 表格 caption 和正文均已使用 "permutation test"，无 z-test 残留。跳过。

**N4. discussion 机制假设**
`discussion.tex:6` "Why EE-only SDF fails" 段落中，在 "These two causes are independent" 前插入了机制假设句。

---
