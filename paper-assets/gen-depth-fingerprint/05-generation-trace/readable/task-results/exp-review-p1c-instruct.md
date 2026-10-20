# exp review p1c instruct

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_review-p1c-instruct_20260515T134100_result.json`
- **Structured JSON:** [`aeffc108f861de59a68b.json`](../../sessions/ae/aeffc108f861de59a68b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

P1-C instruct 实验已启动：

- **模型**: Qwen3-1.7B (Instruct，从 ModelScope 下载)
- **脚本**: `generate_chain_instruct.py` — 使用 `apply_chat_template` + `enable_thinking=False`
- **Pipeline**: 生成 → 特征提取 (Pythia-410M ref model) → 分析 (Spearman ρ + base model 对比)
- **GPU**: cuda:1, PID 211197
- **预计耗时**: ~80-90 分钟（生成 ~70min + 特征提取 ~15min）

20 分钟后自动检查进度。

---
