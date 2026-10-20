# ssh n17 api judges launch

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n17_api_judges_launch_20260523T143930_result.json`
- **Structured JSON:** [`27c11a85498f1c3373da.json`](../../sessions/27/27c11a85498f1c3373da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

API 调用正常，结果格式正确。

## 启动状态汇总

**4 个 API judge 全部启动成功，正在通过 TUM proxy (`http://47.94.22.126/v1`) 收集评测数据。**

| Judge | tmux session | 已完成 | 总量 | 剩余 | 预估时间 (30 RPM) |
|-------|-------------|--------|------|------|-------------------|
| Claude Sonnet 4.6 | `judge_sonnet` | 8,803 | 18,000 | ~9,197 | ~5.1h |
| Gemini 2.5 Pro | `judge_gemini` | 6,845 | 18,000 | ~11,155 | ~6.2h |
| DeepSeek V4 Pro | `judge_deepseek` | 6,137 | 18,000 | ~11,863 | ~6.6h |
| Qwen3-235B | `judge_qwen3` | 7,253 | 18,000 | ~10,747 | ~6.0h |

**注意**：config 中 target_models 有 18 个（含 gpt-4-0314 reference），500 prompts × 18 models × 2 positions = 18,000 total。实际数据为 500 prompts（非 176），总量比预期大。如果需要只跑 9 个新模型，需要调整 config。

---
