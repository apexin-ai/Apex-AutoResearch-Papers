# diagnose v2 rebuild crash

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_v2_rebuild_crash_20260525T134307_result.json`
- **Structured JSON:** [`2cc4473ded5aaefa7a27.json`](../../sessions/2c/2cc4473ded5aaefa7a27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 关键错误行（3 个日志完全一致）

```
finetune.py: error: unrecognized arguments: --occ_norm_type bn
```

exitcode=2（argparse 参数错误），不是 OOM 也不是 CUDA 冲突。

### 根因

**`finetune.py` 不支持 `--occ_norm_type` 参数。** v2 rebuild 实验的启动配置中传了 `--occ_norm_type bn`，但当前服务器上的代码版本没有这个 CLI 参数定义。需要在 `finetune.py` 的 argparse 中添加 `--occ_norm_type` 参数，或者确认服务器代码是否已同步到包含该参数的版本。

### GPU 状态

4 张 GPU 全部被 dose-response 实验占满（各 ~62GB/98GB, 74-99% util），但这不是本次崩溃的原因——3 个实验在 argparse 阶段就挂了，根本没走到 GPU 分配。

### 重试建议

1. **先修代码**：在 `finetune.py` 的 argparse 中加入 `--occ_norm_type` 参数，或同步最新代码到 westd-34685
2. **等 GPU 释放后再重试**：dose-response 实验占满了 cuda:0-3，即使修复参数问题现在也没 GPU 可用。等 dose-response 完成（~20:30 UTC 预估）后重提交

---
