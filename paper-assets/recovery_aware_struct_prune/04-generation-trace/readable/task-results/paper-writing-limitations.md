# paper writing limitations

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_limitations_20260515T052115_result.json`
- **Structured JSON:** [`ec7fca7003aa3e279a40.json`](../../sessions/ec/ec7fca7003aa3e279a40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`paper/limitations.tex` 已写入，约 270 词，覆盖四个 Dream 三档一致的结构性问题：

1. **Single model and architecture** — 仅在 DeepSeek-R1-Distill-Qwen-7B 验证，GQA 动态可能因架构不同而异
2. **Single benchmark and sparsity ratio** — 仅 GSM8K + 20% sparsity，未覆盖其他推理模态和更高剪枝率
3. **No inference speedup measurement** — 结构化剪枝但未报告实际推理延迟/吞吐
4. **Limited seed diversity** — 单一 seed=42，未捕获 calibration 和 GRPO 训练的随机性方差

语气坦诚但不自我否定，每项说明了限制存在的原因（计算资源、scope）和 future work 方向。引用了 `references.bib` 中的 `deepseek2025r1`、`cobbe2021gsm8k`、`hendrycks2021mmlu`、`chen2021humaneval`，使用了 `\rasp{}` 宏。

---
