# paper figure1 tex verify

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure1_tex_verify_20260517T005325_result.json`
- **Structured JSON:** [`653ba98d252a1e1c944a.json`](../../sessions/65/653ba98d252a1e1c944a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完毕，报告如下：

**`\includegraphics` 路径:** `fig1_ii_scatter.pdf`（results.tex:73）
- 文件存在：`artifacts/_project/paper/fig1_ii_scatter.pdf` ✓（同时有 .png 版本）

**`\label`:** `fig:hero`（results.tex:75）

**`\ref` 出现位置:**
- `results.tex:29` — `Figure~\ref{fig:hero} visualizes the dose-response relationship for both models.`
- `discussion.tex:11` — `the dose-response curves (Figure~\ref{fig:hero}) provide target operating points...`

**问题: 无**
- label/ref 名称一致，无 typo
- 文件路径正确且实际存在
- caption 描述与当前数据一致：描述的是 paired median difference Δ 作为 sparsity 函数的 dose-response 曲线，DeepSeek n=496、Qwen n=475，与 results.tex 正文数据吻合（正文同样报告 Δ 从 0.39 到 8.48 for DeepSeek，0.07 到 3.16 for Qwen）

注意：caption 中样本量为 n=496/475（非 n=500），这与正文一致（是实际有效样本数），不是错误。

---
