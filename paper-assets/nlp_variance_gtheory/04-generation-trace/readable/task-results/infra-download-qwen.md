# infra download qwen

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_download_qwen_20260521T005242_result.json`
- **Structured JSON:** [`41726c6ec980f4ad269a.json`](../../sessions/41/41726c6ec980f4ad269a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态更新：

- **Qwen3-8B-Instruct 在 HuggingFace 上不存在**（401 返回，ModelScope 也是 404）。Qwen3 不区分 base/Instruct — `Qwen/Qwen3-8B` 本身就是对话模型（有 chat_template，标记 conversational）
- 已改为下载 **Qwen/Qwen3-8B**，PID 63161，15 个文件正在下载中
- 约 4.5 分钟后自动轮询进度

---
