# code fewrel 40rel

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fewrel_40rel_20260515T160555_result.json`
- **Structured JSON:** [`8c2e2b04ca322cca5e12.json`](../../sessions/8c/8c2e2b04ca322cca5e12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

推理已开始！第一个 batch `count_1_random_0` 正在处理（12 samples, BCS=0.0000），速度正常。

实验成功运行。总结：

- **脚本**: `src/run_fewrel_40rel.py`（从 `run_fewrel_formal.py` 复制，`EXP1_COUNTS` 改为 `[1, 4, 8, 16, 32, 40]`）
- **启动脚本**: `scripts/run_fewrel_40rel.sh`（加了 `FLASHINFER_DISABLE_VERSION_CHECK=1` 绕过版本不匹配）
- **Registry**: `exp_fewrel_40rel` → RUNNING
- **配置**: 80 active relations, 960 samples (12/rel), 105 batches, 6960 inferences
- **预计时长**: ~174 min（~3 小时）
- **日志**: `/tmp/fewrel_40rel.log`
- **tmux session**: `fewrel_40rel`

---
