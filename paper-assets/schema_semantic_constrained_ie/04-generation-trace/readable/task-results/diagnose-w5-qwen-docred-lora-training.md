# diagnose w5 qwen docred lora training

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w5_qwen_docred_lora_training_20260515T175743_result.json`
- **Structured JSON:** [`1fde614e3715898203f7.json`](../../sessions/1f/1fde614e3715898203f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**找到根因了。**

GPU 0 上有 **两个** `train_lora_docred.py` 实例同时运行：
- PID 293601 (`python`): 56492 MiB
- PID 294205 (`python3`): 32386 MiB
- 合计 88892 / 97887 MiB (91%)，GPU 1 完全空闲

第一次失败原因：训练脚本未设 `CUDA_VISIBLE_DEVICES`，`device_map="auto"` 跨双 GPU 分布模型。当并发进程占 GPU 显存时，forward/backward 分配激活内存失败导致 CUDA OOM。进程被杀时无 Python traceback（stderr 中的 CUDA 错误随日志被重试覆盖）。

当前重试也有风险：两个训练实例共享 GPU 0 几乎满载，随时可能再次 OOM。

```json
{
  "root_cause": "GPU contention: duplicate train_lora_docred.py instances (PID 293601 + 294205) sharing GPU 0 at 91% VRAM; device_map='auto' without CUDA_VISIBLE_DEVICES causes cross-GPU allocation conflicts with concurrent jobs",
  "error_type": "resource",
  "fix_steps": [
    "Kill duplicate process: kill PID 294205 (or 293601, keep one)",
    "Relaunch with CUDA_VISIBLE_DEVICES=1 (GPU 1 is empty) pinning to single GPU: CUDA_VISIBLE_DEVICES=1 python scripts/train_lora_docred.py",
    "Alternatively: add CUDA_VISIBLE_DEVICES to the job submission config to prevent recurrence"
  ],
  "can_auto_fix": true,
  "sft_data_exists": true
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "GPU contention: duplicate train_lora_docred.py instances (PID 293601 + 294205) sharing GPU 0 at 91% VRAM; device_map='auto' without CUDA_VISIBLE_DEVICES causes cross-GPU allocation conflicts with concurrent jobs",
    "error_type": "resource",
    "fix_steps": [
      "Kill duplicate process: kill PID 294205 (or 293601, keep one)",
      "Relaunch with CUDA_VISIBLE_DEVICES=1 (GPU 1 is empty) pinning to single GPU: CUDA_VISIBLE_DEVICES=1 python scripts/train_lora_docred.py",
      "Alternatively: add CUDA_VISIBLE_DEVICES to the job submission config to prevent recurrence"
    ],
    "can_auto_fix": true,
    "sft_data_exists": true
  }
}
```

</details>

---
