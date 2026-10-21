# infra exp058 deploy

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp058-deploy_20260519T031050_result.json`
- **Structured JSON:** [`2cc78c99264eb1db0cbb.json`](../../sessions/2c/2cc78c99264eb1db0cbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

**Phase 1 — Kill 遗留进程**
- cuda:3 上原运行 **Qwen3-14B** vLLM (PID 99897/100181, port 8003)，属于 `exp028b` tmux session
- 已 kill tmux session `exp028b`，cuda:3 释放至 0MiB

**Phase 2 — 部署 exp-058**
- vLLM: Mistral-7B-Instruct-v0.3，cuda:3，port 8003，tmux session `exp058_vllm`
- 实验: T=0.5, k=12, FOLIO-204, seed=42，tmux session `exp058_run`，已在活跃发送请求
- 输出: `results/exp058_mistral_folio204_t05/exp058_results.json`
- Registry: `exp-058-mistral-folio204-t05` → RUNNING

---
