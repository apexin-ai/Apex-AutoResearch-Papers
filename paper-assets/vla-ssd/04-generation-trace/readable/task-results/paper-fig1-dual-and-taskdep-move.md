# paper fig1 dual and taskdep move

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fig1_dual_and_taskdep_move_20260519T155504_result.json`
- **Structured JSON:** [`7a51b3b58bf9c8e94f94.json`](../../sessions/7a/7a51b3b58bf9c8e94f94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

**任务 1 — Fig 1 双面板**
- `experiments.tex:104-117`: 替换为 minipage 双面板布局，panel (a) 32-layer attention + panel (b) dose-response
- `\label{fig:attention_profile}` 保留，正文引用不变
- Appendix `fig:dose_response`（appendix.tex:157-162）未动，`\ref{fig:dose_response}` 引用仍指向 appendix 详细版

**任务 2 — Task-dependent routing 移入 Experiments**
- `experiments.tex:119-121`: 在 §4.3 末尾（Fig 1 之后）新增 `\paragraph{Task-dependent routing modulation.}`，含 2.5×/p=0.033、6.5×/p=0.008 数据
- `discussion.tex:19-21 → 17-18`: 删除原 `\paragraph{Task-dependent routing.}` 整段，将 deployment 建议句合并至 "Functional stages and predictions" 段尾
- Introduction line 18 的 "2.5× stronger" 现在对应 experiments.tex 中的段落

**编译验证**
- 0 errors, 0 undefined references
- 正文 ≤8 页（References 从 page 8 开始）
- 总 27 页

---
