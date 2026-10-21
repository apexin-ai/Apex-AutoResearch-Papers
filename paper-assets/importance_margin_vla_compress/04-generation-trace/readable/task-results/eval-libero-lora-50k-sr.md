# eval libero lora 50k sr

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_libero_lora_50k_sr_20260516T185313_result.json`
- **Structured JSON:** [`d47a34f55aaa904bece3.json`](../../sessions/d4/d47a34f55aaa904bece3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已出。汇总如下：

---

```
LoRA 50K: SR = 0/100 (0%), suite=libero_object
实际 checkpoint step: 50000 (libero_baseline/step_050000 from cqa1)

IMM two-stage cuda:0 状态: GPU util=0%, mem=2728 MiB
  PID 221824: train_twostage.py 正在运行（13min+）
  实际情况: 在从 HuggingFace 下载 LIBERO 数据集 (4/383 files, ~160s/file)
  预计下载完还需 ~16 小时才能开始实际训练
```

---

**关键发现：**

1. **LoRA 50K SR = 0%**（vs Full FT 50K = 33%）。LoRA rank=32 在 50K step 完全无法完成任务。差距极大，不是随机波动。

2. **IMM two-stage 未在真正训练。** 进程存活但 GPU util=0%，因为它卡在下载 LIBERO 数据集阶段。westd 上没有 HF 缓存，正以 ~160s/file 从 HuggingFace 下载 383 个 parquet 文件。cqa1 上有完整缓存（`/root/autodl-tmp/.hf_cache/lerobot/hub/datasets--HuggingFaceVLA--libero`），需要想办法同步过去或中止后配置本地数据路径。

---
