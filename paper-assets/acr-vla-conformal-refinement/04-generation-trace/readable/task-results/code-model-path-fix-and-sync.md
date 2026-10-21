# code model path fix and sync

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_model-path-fix-and-sync_20260513T113849_result.json`
- **Structured JSON:** [`66de70b1e06feaa94fb2.json`](../../sessions/66/66de70b1e06feaa94fb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器验证都通过。总结：

### 完成状态

| 项目 | 状态 |
|------|------|
| **Step 1**: smolvla_wrapper.py 默认路径 → smolvla_libero | **已完成** |
| **Step 2**: train_crm.py 加 HF_OFFLINE | **已完成** |
| **Step 3**: evaluate.py 合并 crash protection (try/except + SIGSEGV handler) | **已完成** |
| **Step 4**: 代码同步到 autodl-4090 (utils/cgs/smolvla_wrapper/evaluate/train_crm) | **已完成** |
| **Step 5**: 两台服务器验证 FULL=7, CORR=6, 默认路径=smolvla_libero | **已完成** |

### 需要注意

**autodl-4090 上没有 smolvla_libero 模型**，只有 `smolvla_base`。4090x4 上有 `/root/autodl-tmp/models/smolvla_libero/`（865MB）。如果要在 4090 上跑 precompute 或 evaluate，需要先把模型复制过去，或用 `--smolvla_path /root/autodl-tmp/models/smolvla_base` 覆盖。

### train_crm.py 模型路径参数

参数名是 `--smolvla_path`，默认值已改为 `/root/autodl-tmp/models/smolvla_libero/`。precompute 时如需指定不同路径：
```bash
python train_crm.py --precompute --benchmark spatial --smolvla_path /path/to/model
```

---
