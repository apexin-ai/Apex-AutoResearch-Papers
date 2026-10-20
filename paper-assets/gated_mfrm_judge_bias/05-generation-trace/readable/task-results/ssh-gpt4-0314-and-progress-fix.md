# ssh gpt4 0314 and progress fix

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpt4-0314-and-progress-fix_20260524T100059_result.json`
- **Structured JSON:** [`a16fb344713d7da94506.json`](../../sessions/a1/a16fb344713d7da94506.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本工作正常。6 个 `_n17` judges 中：
- **RUNNING (6个)**：claude-sonnet-4.6-proxy_n17, deepseek-v4-pro-proxy_n17, gemini-2.5-pro-proxy_n17, llama-3.3-70b-local_n17, qwen2.5-72b-local_n17, qwen3-235b-proxy_n17
- **STOPPED**：所有旧批次（无 `_n17` 后缀）和 mistral-large-2-local_n17（59min 前停写）

## 产出汇总

**任务 1 — gpt-4-0314**：**已覆盖**，在 `ARENA_ELO` 中，ELO=1206。无需加入 EXCLUDE_MODELS，无需修改 evaluation.py。

**任务 2 — check_progress.sh 修复**：

原 bug：脚本只做 `ps aux | grep collect.py`，不输出 per-judge RUNNING/STOPPED 状态。

修复 diff：
- 遍历 `results/` 下每个 judge 目录
- 检查 `arena_hard_judgments.jsonl` 是否在 5 分钟内有写入 → RUNNING
- 否则显示 STOPPED + 距上次写入的分钟数
- 保留 GPU/Disk 信息，增加进程列表

验证输出确认 6 个活跃 judge 正确显示 RUNNING。

---
