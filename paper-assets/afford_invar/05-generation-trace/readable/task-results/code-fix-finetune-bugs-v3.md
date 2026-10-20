# code fix finetune bugs v3

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-finetune-bugs-v3_20260519T210640_result.json`
- **Structured JSON:** [`b99e646dd559e5abc5be.json`](../../sessions/b9/b99e646dd559e5abc5be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 3 个验证通过。

---

## 修复总结

**文件**: `/root/afford_invar/openvla-oft/vla-scripts/finetune_afford.py`

### 修改 1 — Line 363
```python
# 修改前
layer18_orig = output.hidden_states[cfg.layer_idx][:, 1:1 + NUM_PATCHES, :].to(torch.bfloat16)
# 修改后
layer18_orig = output.hidden_states[cfg.layer_idx + 1][:, :NUM_PATCHES, :].to(torch.bfloat16)
```

### 修改 2 — Line 385
```python
# 修改前
feat = p_out.hidden_states[cfg.layer_idx][:, 1:1 + NUM_PATCHES, :].to(torch.bfloat16)
# 修改后
feat = p_out.hidden_states[cfg.layer_idx + 1][:, :NUM_PATCHES, :].to(torch.bfloat16)
```

### 无需修改
- `affordance_decoder.py` — 已用 GroupNorm，无 BatchNorm，无 hidden_states 引用
- 其他文件 — 全项目搜索无同类 bug

### 验证结果
1. Unit test 索引正确性 — PASSED (`hidden_states[18+1]` = layer 18 output = value 19.0)
2. Phase 0 一致性 — PASSED (`hs_index = layer_idx + 1`，与修复后一致)
3. AffordanceDecoder — PASSED（无 BatchNorm，forward shape (2,256,4096)→(2,1,128,128) 正确）

---
