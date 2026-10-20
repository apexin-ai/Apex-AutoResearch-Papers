# ops check gradient accumulation

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_gradient_accumulation_20260515T191234_result.json`
- **Structured JSON:** [`c68c3142f9f75a1fd162.json`](../../sessions/c6/c68c3142f9f75a1fd162.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数学验证完成。

## 结论

| 参数 | 值 | 来源 |
|------|-----|------|
| `per_device_train_batch_size` | **4** | 代码第149行硬编码 + trainer_state 确认 |
| `gradient_accumulation_steps` | **8** | 代码第151行硬编码 |
| 命令行覆盖 | **无** | argparse 中没有 gradient_accumulation 参数 |
| n_gpus | **1** | `device_map={"": 0}` + 单卡 CUDA_VISIBLE_DEVICES |

**数学验证**：
- 训练样本数 = 4720
- steps_per_epoch = ceil(4720 / (4 × 8 × 1)) = ceil(147.5) = **148** ✓（与所有 checkpoint 的 148/296/444 步完全吻合）
- 如果 gradient_accumulation=4，steps_per_epoch 应为 295，与实际不符 ✗

**Effective batch size = 4 × 8 × 1 = 32**

**结论：论文写的 gradient_accumulation=8 (effective batch=32) 是正确的。paper_provenance 记录的 4 是错误/过时的，应更新。** W&B 目录在服务器上不存在，无法从 W&B config 交叉验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "": 0
  }
}
```

</details>

---
