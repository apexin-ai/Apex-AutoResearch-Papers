# code theta sensitivity figure

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_theta-sensitivity-figure_20260518T133210_result.json`
- **Structured JSON:** [`6c614fe5cc96198f4e26.json`](../../sessions/6c/6c614fe5cc96198f4e26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

输出完成。

**文件位置**：
- PDF: `artifacts/figures/fig_theta_sensitivity.pdf`
- PNG: `artifacts/figures/fig_theta_sensitivity.png`

**包含的模型配置**：

| Panel | Models |
|-------|--------|
| C4 (7) | Qwen2.5-1.5B, Pythia-1.4B, OLMo-1B, Qwen2.5-7B, LLaMA-3.1-8B, Mistral-7B, Qwen2.5-14B |
| arXiv (4) | Qwen2.5-1.5B, Pythia-1.4B, LLaMA-3.1-8B, Mistral-7B |
| Wiki (4) | Qwen2.5-7B, LLaMA-3.1-8B, Pythia-1.4B, OLMo-1B |

**关键观察**：
- θ=0.60 处 domain ordering 清晰：Wiki K*≈1, C4 K*≈2, arXiv K*≈3
- 该 ordering 在 θ∈[0.55, 0.70] 全范围内保持稳定
- 模型间差异远小于域间差异，验证 K* 主要由 domain 决定而非 model family/scale

---
