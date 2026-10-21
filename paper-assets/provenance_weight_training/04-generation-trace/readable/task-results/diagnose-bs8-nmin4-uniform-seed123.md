# diagnose bs8 nmin4 uniform seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bs8_nmin4_uniform_seed123_20260523T032450_result.json`
- **Structured JSON:** [`8f6a1bf231d8a240c97b.json`](../../sessions/8f/8f6a1bf231d8a240c97b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完毕。

**根因**：三个实验都指定 `--resume_from_checkpoint .../checkpoint-1000`，但 checkpoint-1000 根本不存在。前两个目录只有 checkpoint-500，第三个连 checkpoint-500 都没有。

- **bs8_nmin4_uniform_seed123** 和 **bs8_nmin4_adaptive_seed123**：safetensors 报 `Error while deserializing header: incomplete metadata, file not fully covered`——实际上是因为 checkpoint-1000 目录不存在，transformers 回退到了某个错误路径
- **rho03_adaptive_seed456**：更直白，`FileNotFoundError: .../checkpoint-1000/trainer_state.json`

```json
{"root_cause":"checkpoint-1000 directories do not exist (only checkpoint-500 available for bs8 runs, no checkpoint at all for rho03). safetensors_rust.SafetensorError: Error while deserializing header: incomplete metadata / FileNotFoundError: trainer_state.json","error_type":"infrastructure","fix_steps":["对 bs8_nmin4_uniform_seed123 和 bs8_nmin4_adaptive_seed123：将 --resume_from_checkpoint 改为 checkpoint-500","对 rho03_adaptive_seed456：移除 --resume_from_checkpoint（无可用 checkpoint），或从头训练","检查之前训练为何只保存了 checkpoint-500 而没有 checkpoint-1000（可能 save_steps=500 但训练在 step 500~1000 之间中断）"],"can_auto_fix":true,"affects_all_three":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "checkpoint-1000 directories do not exist (only checkpoint-500 available for bs8 runs, no checkpoint at all for rho03). safetensors_rust.SafetensorError: Error while deserializing header: incomplete metadata / FileNotFoundError: trainer_state.json",
    "error_type": "infrastructure",
    "fix_steps": [
      "对 bs8_nmin4_uniform_seed123 和 bs8_nmin4_adaptive_seed123：将 --resume_from_checkpoint 改为 checkpoint-500",
      "对 rho03_adaptive_seed456：移除 --resume_from_checkpoint（无可用 checkpoint），或从头训练",
      "检查之前训练为何只保存了 checkpoint-500 而没有 checkpoint-1000（可能 save_steps=500 但训练在 step 500~1000 之间中断）"
    ],
    "can_auto_fix": true,
    "affects_all_three": true
  }
}
```

</details>

---
