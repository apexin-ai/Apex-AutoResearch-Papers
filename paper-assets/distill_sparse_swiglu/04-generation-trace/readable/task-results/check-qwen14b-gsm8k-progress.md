# check qwen14b gsm8k progress

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen14b_gsm8k_progress_20260522T074438_result.json`
- **Structured JSON:** [`2fedd2833ac1e75d3638.json`](../../sessions/2f/2fedd2833ac1e75d3638.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进度报告**

- **当前阶段**：Sparsity setup + tokenization 已完成，正在执行 generation
- **GSM8K 进度**：289/1319 (22%)，已运行 57:24
- **生成速度**：~9-13 秒/题（每 8 题一个 batch，约 80-100s/batch）
- **ETA**：剩余 1030 题，按当前节奏约 3:35-4:00 小时
- **状态**：进行中，未完成。无 gsm8k_exact_match_flex 指标可提取
- **模型 sparsity 验证**：Model-level 0.296（目标 0.30 ✓），逐层均匀 0.285-0.301

eval 仍需约 3.5-4 小时才能完成。

---
