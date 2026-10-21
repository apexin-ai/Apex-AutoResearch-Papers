# deploy exp 079 icg logiqa 16639

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp-079-icg-logiqa-16639_20260519T185540_result.json`
- **Structured JSON:** [`cc4e3386b21ed231d8d4.json`](../../sessions/cc/cc4e3386b21ed231d8d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-079 已部署并运行中。

**部署摘要:**
- **服务器**: westd-16639, cuda:0, port 8010
- **tmux sessions**: `exp079_vllm` (vLLM), `exp079_run` (实验)
- **代码适配**: `run_icg.py` 新增 `--dataset logiqa` 支持（ICG_PROMPT_LOGIQA、multichoice domain、A/B/C/D 候选集）
- **Dry-run**: 3 题通过，SC=0.33, ICG=0.67, 无 crash
- **ETA**: ~110 min (200 problems)
- **输出**: `results/exp079_icg_mistral_logiqa200/results.json`

---
