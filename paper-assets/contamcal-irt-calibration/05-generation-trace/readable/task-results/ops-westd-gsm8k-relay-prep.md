# ops westd gsm8k relay prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-gsm8k-relay-prep_20260520T003146_result.json`
- **Structured JSON:** [`be4c5ef69a0d0654f658.json`](../../sessions/be/be4c5ef69a0d0654f658.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个脚本全部验证通过，s42 目录也已就绪。

```
GSM8K s123 脚本验证:
- Gemma-2:  CUDA=3 ✅  md5 gate: ✅  dosages: d000+d100 ✅
- Phi-4:    CUDA=0 ✅  md5 gate: ✅  dosages: d000+d100 ✅
- Qwen-14B: CUDA=1 ✅  md5 gate: ✅  dosages: d000+d100 ✅

s42 GSM8K 脚本状态: 存在 ✅ (5个: gemma2/olmo2/phi4/qwen14b/qwen7b)
```

所有 CUDA 分配与预期一致，md5 gate 均指向 `001a9bc23f808c47d25ef9eaeecb81f1`，checkpoint 路径均指向 `*_s123`，只跑 d000+d100 端点。无需修正。

---
