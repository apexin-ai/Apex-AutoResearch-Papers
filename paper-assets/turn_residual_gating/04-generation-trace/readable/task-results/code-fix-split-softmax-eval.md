# code fix split softmax eval

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_split_softmax_eval_20260523T075930_result.json`
- **Structured JSON:** [`37a76b3b19f47ac28266.json`](../../sessions/37/37a76b3b19f47ac28266.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both fixes verified — syntax checks pass.

**修复总结：**

**Bug 1** (`eval_split_softmax.py` L373): `ss.activate(system_prompt_len=0)` → 改为从实际数据动态计算 `init_sp_len`：TF 模式从第一条 conversation 提取，gen 模式从第一个 system prompt 提取。

**Bug 2** (`split_softmax.py` L127-134): NaN 根因是 bfloat16 精度不足——`1 - 1e-8` 在 bfloat16 下舍入为 `1.0`，导致 `pi.clamp(max=1-1e-8)` 无效。当 query 位于 system prompt 范围内时 `pi=1.0`，`conv_scale = 0/0 = NaN`。修复：将 `pi` 提升到 float32 计算，clamp 上界改为 `1 - 1e-6`，计算完 scale 后再转回原 dtype。

GPU 被占用，实际运行验证需等训练完成后再做。

---
