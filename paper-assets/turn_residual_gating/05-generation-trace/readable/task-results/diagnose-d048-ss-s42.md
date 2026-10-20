# diagnose d048 ss s42

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_d048_ss_s42_20260522T155358_result.json`
- **Structured JSON:** [`a05ba5501e381a855a62.json`](../../sessions/a0/a05ba5501e381a855a62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

```json
{"root_cause":"GPU 内存争用 - 进程 30899 占 68.62 GiB（已死亡），训练进程被挤压至 26.13 GiB 后 OOM","error_type":"resource","training_progress":"Epoch 1 / Step 7800（共 3 epochs，epoch 0 已完成）","has_checkpoint":true,"checkpoint_path":"/root/turn_residual_gating/runs/d048_ss_s42/epoch_0/","competing_process":"进程 30899 已不存在，GPU 当前完全空闲（0 MiB / 97887 MiB）","fix_steps":["GPU 已空闲，竞争进程已消失","epoch_0 checkpoint 存在（lora/adapter_model.safetensors + gate_params.pt），epoch_1 未保存","检查 train_phase2_v8b.py 是否支持 --resume 从 epoch_0 恢复，避免从头重训","若不支持 resume，直接重跑 bash scripts/d048_ss_s42.sh"],"can_auto_fix":true}
```

**关键发现：**

| 项目 | 状态 |
|------|------|
| 进程 30899 | **已死亡**，GPU 完全空闲（0 MiB，0%利用率） |
| 训练进度 | Epoch 1 Step 7800，正常内存 53.0-53.1 GB，SS ratio 已到 max 0.300 |
| Checkpoint | epoch_0 已保存（`runs/d048_ss_s42/epoch_0/`），epoch_1 **未保存** |
| OOM 位置 | `Qwen2 eager_attention_forward` → `softmax`，申请 424 MiB 但仅剩 218.56 MiB |
| 脚本配置 | `--output-dir runs/d048_ss_s42`，无 `--resume` 参数 |

训练本身内存正常（53 GiB / 95 GiB），纯粹是外部进程争抢导致 OOM。GPU 已空闲，可直接重跑。需要确认训练代码是否能从 epoch_0 checkpoint 恢复，否则需要从头跑 3 个 epoch。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "GPU 内存争用 - 进程 30899 占 68.62 GiB（已死亡），训练进程被挤压至 26.13 GiB 后 OOM",
    "error_type": "resource",
    "training_progress": "Epoch 1 / Step 7800（共 3 epochs，epoch 0 已完成）",
    "has_checkpoint": true,
    "checkpoint_path": "/root/turn_residual_gating/runs/d048_ss_s42/epoch_0/",
    "competing_process": "进程 30899 已不存在，GPU 当前完全空闲（0 MiB / 97887 MiB）",
    "fix_steps": [
      "GPU 已空闲，竞争进程已消失",
      "epoch_0 checkpoint 存在（lora/adapter_model.safetensors + gate_params.pt），epoch_1 未保存",
      "检查 train_phase2_v8b.py 是否支持 --resume 从 epoch_0 恢复，避免从头重训",
      "若不支持 resume，直接重跑 bash scripts/d048_ss_s42.sh"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
