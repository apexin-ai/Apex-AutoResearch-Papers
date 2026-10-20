# ssh compute budget paragraph

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_compute_budget_paragraph_20260524T081508_result.json`
- **Structured JSON:** [`ae493bd9cccff25a1a85.json`](../../sessions/ae/ae493bd9cccff25a1a85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，无新错误。

### 汇报

**位置**: `appendix.tex` 末尾（第 472–480 行），新增 `\section{Compute Budget}` (`\label{app:compute}`)，位于 "Use of AI Assistants" 之后。

**段落全文**:
```latex
\section{Compute Budget}
\label{app:compute}

\paragraph{Compute budget.}
All experiments ran on a single machine with four NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs (96\,GB each).
MCMC inference (Stage~3) used NumPyro/JAX with 4 chains $\times$ 4{,}000 warmup + 4{,}000 sampling iterations;
the $N=8$ joint G-MFRM fit completed in approximately [X] minutes on one GPU.
Judge inference for local models (LLaMA-3.3-70B, Qwen2.5-72B, Mistral-Large-2; all AWQ-quantized)
used vLLM continuous batching, consuming approximately [Y] GPU-hours total across three GPUs.
API judge calls (GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Gemini-2.5-Pro, Qwen3-235B) cost approximately \$[ZZZ] in total.
Synthetic calibration experiments (exp-015, exp-018) required approximately [W] GPU-hours.
```

**编译结果**:
- 16 页，无编译错误
- 正文不受影响（compute budget 在 `\appendix` 之后，不计入 8 页限制）
- 9 个 overfull hbox（全部为已有的，无新增）
- 待填占位符：`[X]`（MCMC 运行时间）、`[Y]`（本地 judge GPU-hours）、`\$[ZZZ]`（API 费用）、`[W]`（合成实验 GPU-hours）

---
