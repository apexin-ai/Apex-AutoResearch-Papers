# diagnose exp012 llama 8b r2 final

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp012_llama_8b_r2_final_20260515T194608_result.json`
- **Structured JSON:** [`55d5dd0b6fb32c88fbcf.json`](../../sessions/55/55d5dd0b6fb32c88fbcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程仍在运行，未退出。** 

当前状态：
- exit 文件不存在（`/tmp/agent-ml-exit/exp012_llama_8b_r2.exit` → No such file）
- PID 319316 活跃（40% CPU），vLLM EngineCore PID 319623（105% CPU）
- **exp1 已完成**（02:38→03:39）
- **exp2 正在运行**：count_6 batches 进行中，已完成 low_bcs、high_bcs、random/0→17。当前 running count_6/random/17，之后还有 count_12 全部 batches

artifacts/exp012/ 中 00:45 的 exp2 文件是旧 run 遗留，本次 run 的 exp2 还没写出新结果。

**预估剩余时间**：count_6 random 即将完成（~18 batches done），count_12 还需 ~20 batches × ~15s ≈ 5-7 分钟。总计约 10 分钟内应结束。

不更新 registry、不删 cron——等进程完成后再操作。

---
