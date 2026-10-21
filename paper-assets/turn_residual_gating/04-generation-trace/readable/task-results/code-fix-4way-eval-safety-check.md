# code fix 4way eval safety check

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_4way_eval_safety_check_20260519T112104_result.json`
- **Structured JSON:** [`4741ecf7453682e61765.json`](../../sessions/47/4741ecf7453682e61765.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。语法检查通过，checkpoint 前置检查已插入变量定义之后、`mkdir -p` 之前。脚本原本就用变量引用路径，无需额外替换。现在如果 `lora/` 目录或 `gate_params.pt` 缺失，脚本会立即报错退出，不会静默 fallback 到 base model。

---
