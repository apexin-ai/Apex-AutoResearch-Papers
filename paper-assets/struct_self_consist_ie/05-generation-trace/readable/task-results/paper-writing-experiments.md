# paper writing experiments

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260514T191638_result.json`
- **Structured JSON:** [`230610aef0e1fa7150eb.json`](../../sessions/23/230610aef0e1fa7150eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `docs/paper/sections/experiments.tex`，包含：

- **§5.1 Experimental Setup** — 数据集 (SciERC/CoNLL/WNUT-17)、模型 (Qwen3-8B + LLaMA-3.1-8B)、采样配置、5 个信号定义、实现细节
- **§5.2 Quality Estimation Results + Table 1** — 5 信号 × 4 任务-模型组合的 ρ 和 AUROC；分析 structural dominance、signal ranking shift、cross-model stability、logprob paradox、oracle headroom
- **§5.3 Correlation-Selection Gap + Table 2** — SciERC best-of-N selection；NER 无信号超越 greedy、RE 仅 logprob 成功 (+2.3 pp)；quality estimation ≠ output selection 的解释
- **§5.4 Task Complexity and Signal Robustness + Table 3** — 难度梯度 (CoNLL→SciERC→WNUT-17)、Fisher z-test、per-relation diagnostic、capability stratification、WNUT-17 method boundary、temperature/N-scaling robustness、cross-model transfer、LOO circularity、conditional filtering、binary vs ranking 分析

所有数字来自提供的 registry 数据，FORBIDDEN 用语已验证清零。

---
