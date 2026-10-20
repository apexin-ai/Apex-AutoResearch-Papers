# diagnose uniform 1 7b seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_uniform_1_7b_seed42_20260518T154539_result.json`
- **Structured JSON:** [`0e3510cb11a218c359ea.json`](../../sessions/0e/0e3510cb11a218c359ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**checkpoint-3000 状态：**
| 文件 | 状态 |
|------|------|
| `model.safetensors` (3.4GB) | 有效，310个tensor |
| `optimizer.pt` (6.7GB) | **损坏** — zip archive central directory 读取失败 |
| `trainer_state.json` (468B) | 存在但可疑 — 比模型文件晚52分钟写入，`log_history`为空 |
| `scheduler.pt` (1.4KB) | 有效，`last_epoch=3000` |
| `rng_state.pth` | 存在 |
| `training_args.bin` | 存在 |

**结论：** checkpoint-3000 的 `optimizer.pt` 损坏，无法完整 resume（optimizer state 和 momentum 无法恢复）。这是唯一的 checkpoint。

```json
{"valid_checkpoint": null, "checkpoint_step": null, "all_checkpoints": ["checkpoint-3000"], "recommendation": "train_from_scratch", "detail": "checkpoint-3000 的 optimizer.pt 损坏 (PytorchStreamReader failed reading zip archive)，无法恢复优化器状态。model.safetensors 可读(310 tensors)，如果接受 optimizer/LR reset 可考虑只加载模型权重从 step 3000 继续，但严格意义上无完整有效 checkpoint。"}
```

两个选项：
1. **从头训练** — 最干净，结果可复现
2. **只加载 model weights 继续** — 省约 49% 步数，但 optimizer momentum 和 LR schedule 会重置，训练曲线会有跳变，实验严谨性打折

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "valid_checkpoint": null,
    "checkpoint_step": null,
    "all_checkpoints": [
      "checkpoint-3000"
    ],
    "recommendation": "train_from_scratch",
    "detail": "checkpoint-3000 的 optimizer.pt 损坏 (PytorchStreamReader failed reading zip archive)，无法恢复优化器状态。model.safetensors 可读(310 tensors)，如果接受 optimizer/LR reset 可考虑只加载模型权重从 step 3000 继续，但严格意义上无完整有效 checkpoint。"
  }
}
```

</details>

---
