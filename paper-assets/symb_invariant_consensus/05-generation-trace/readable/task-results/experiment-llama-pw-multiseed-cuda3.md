# experiment llama pw multiseed cuda3

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_llama-pw-multiseed-cuda3_20260522T132013_result.json`
- **Structured JSON:** [`29be35d75ffb99fb8eb9.json`](../../sessions/29/29be35d75ffb99fb8eb9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**产出汇总：**

| 项目 | 值 |
|------|-----|
| 模型路径 | `/root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct` |
| vLLM PID | 613151 (worker 613156), port 8004, cuda:3 |
| Sanity check | PASSED (回复 "4") |
| 脚本路径 | `/root/symb_invariant_consensus/scripts/multiseed_llama8b_pw_cuda3.sh` |
| GPU 确认 | cuda:3 已占用 88259 MiB / 97887 MiB, utilization 0%（待实验启动） |

脚本使用 seeds 42/123/456，参数与现有 Qwen25 PW 脚本一致（`run_full_mvp.py`, k=12, temp=0.7, max-tokens=2048）。脚本已创建但未启动，等 Agent 用 `submit_training_job` 提交。

---
