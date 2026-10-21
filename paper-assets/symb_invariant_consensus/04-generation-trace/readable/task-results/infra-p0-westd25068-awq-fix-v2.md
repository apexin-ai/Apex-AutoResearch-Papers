# infra p0 westd25068 awq fix v2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_p0-westd25068-awq-fix-v2_20260521T182723_result.json`
- **Structured JSON:** [`528be3d08df8584124b0.json`](../../sessions/52/528be3d08df8584124b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

一切已在运行中，前一个 Worker 实际上成功了（尽管日志损坏）。

**状态汇报：**

1. **AWQ 模型**：已完整下载在 `/root/autodl-tmp/models/Qwen/Qwen2___5-72B-Instruct-AWQ/`（ModelScope 格式），11/11 shards，~39GB，确认 `quant_method: "awq"` 4-bit

2. **vLLM** (PID 39013)：已运行，port 8002，tp=4，max-model-len 8192，`--quantization awq`。吞吐正常（prompt 188 tok/s, generation 408 tok/s），prefix cache hit 72.5%

3. **FOLIO pipeline** (PID 40007)：正在执行 `exp_70b_sica_awq_25068`，当前进度 **5/192 FOLIO 题**（overall 17/204），ETA ~137 min，avg 43.7s/prob。前 4 题正确率看起来正常（SC voting 12/12）

4. **额外进程**：Gemini 2.5 Pro frontier 实验 (PID 19972) 也在跑 `run_frontier_scb.py`

无需任何修复操作，所有任务已在正常运行。

---
