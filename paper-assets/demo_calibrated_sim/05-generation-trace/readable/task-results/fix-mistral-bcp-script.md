# fix mistral bcp script

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_mistral-bcp-script_20260512T230230_result.json`
- **Structured JSON:** [`40dc2b52f6cf0cb4e1c7.json`](../../sessions/40/40dc2b52f6cf0cb4e1c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

### 修改内容

**`eval_mistral_bcp.sh`**（第 11-15 行）：
- `GPU_ID=${GPU_ID:-0}` → `GPU_ID=${GPU_ID:?"ERROR: GPU_ID must be set (2 or 3)"}` — 去掉默认值 0，未设置时直接报错退出
- 新增 if 检查：`GPU_ID` 不是 2 或 3 时报错退出

**`run_mvp_experiment.py`** — 无需修改。

### SERVED_MODEL_NAME 传递链路

```
eval_mistral_bcp.sh:  MODEL_NAME="democalib-mistral"
                      export SERVED_MODEL_NAME="$MODEL_NAME"
                      vLLM --served-model-name "$MODEL_NAME"
         ↓
run_mvp_experiment.py:  SERVED_MODEL_NAME = os.environ.get("SERVED_MODEL_NAME", "democalib-qwen")
                        → 获得 "democalib-mistral"
                        model_name = SERVED_MODEL_NAME  (第284行)
                        → 传入 run_single_experiment() 的 model_name/agent_model_name 参数
```

链路完整，vLLM 注册的模型名与 Python API 调用的模型名一致。fallback "democalib-qwen" 仅在不设环境变量直接运行 Python 脚本时生效（Qwen 场景），不影响 Mistral eval。

---
