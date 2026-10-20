# fix seed456 eval and gpu cleanup

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_seed456_eval_and_gpu_cleanup_20260518T221637_result.json`
- **Structured JSON:** [`35ddf1973e51d71e07a7.json`](../../sessions/35/35ddf1973e51d71e07a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常推进到 step 17/444，无 OOM。

---

**汇总：**

```
GPU0 CLEANUP: 无泄漏进程需清理（49GB 是 driver/runtime 固定开销，非泄漏）
SEED456 EVAL: 训练中 (17/444 steps, ~4s/step, 预计 ~30min 训练 + ~15min eval)
             修复: 加 --gradient_checkpointing 解决 OOM (23GB vs 之前 50GB)
SEED123:     同样 OOM 失败 (step 3/444)，目录已清理
SEED123_V2:  未启动，registry 中不存在。需等 seed456 完成后在 GPU0 上启动（同样需要 --gradient_checkpointing）
GPU0 STATUS: 在用 (seed456 训练中, 72GB/98GB used, 100% util)
GPU1 STATUS: 在用 (codellama13b_full_trace_tail512_seed123 训练中, 47GB/98GB, 100%)
```

**根因**: GPU 0 有 ~49GB 不可释放的 driver 级固定开销（不是进程泄漏，nvidia-smi reset 也不支持），导致可用显存仅 ~48GB。1.5B 模型无 gradient_checkpointing 时峰值需 ~50GB，差 2GB 触发 OOM。seed42 之前成功可能是因为当时 GPU 开销更小。

**待做**: seed456 完成后需手动启动 seed123_v2（同样加 `--gradient_checkpointing`）。

---
