# analyze train pi05 lora baseline s2 resume

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_train_pi05_lora_baseline_s2_resume_20260527T130943_result.json`
- **Structured JSON:** [`1c78b1a930dd9999dbd0.json`](../../sessions/1c/1c78b1a930dd9999dbd0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

项目配置中没有 W&B entity。日志中也没有 wandb 相关输出，说明这次 resume 训练的 wandb 可能未正常连接（日志中无 wandb URL）。不过 wandb_id.txt 存在（来自原始 run），可以尝试用已知 entity 查询。

从日志已能获取所有关键信息，汇总如下：

---

## 训练结果汇总：`train_pi05_lora_baseline_s2_resume`

| 项目 | 值 |
|------|------|
| **训练是否完成** | 是，正常退出 (EXIT_CODE=0) |
| **最终 step** | 30000 (100%) |
| **恢复起点** | step 22000 |
| **最终 loss** | 0.0117 (step 30000) |
| **最终 lr** | 2.50e-06 |
| **best loss** | 0.008163 @ step 26000 |
| **resume 段耗时** | ~10h18m (22000→30000, ~4.64s/step) |
| **W&B run ID** | `9sfus56z` |
| **W&B 状态** | 日志中无 wandb 输出，可能 resume 时未成功连接 W&B（需确认） |

### Checkpoint 路径
```
/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed2/
├── 29999/    (含 model.safetensors 7.0GB + optimizer.pt 124MB)
├── 30000/    (含 model.safetensors 7.0GB + optimizer.pt 124MB)
├── best/     (best loss 0.008163 @ step 26000)
├── best_loss.txt
└── wandb_id.txt
```

### 异常
- W&B 日志中无任何 wandb 相关输出，resume 训练可能未成功上报指标到 W&B（原始 run 的 wandb_id.txt 存在但 resume 段的 W&B 连接状态不明）
- 项目配置 (`diff_collision_sdf.yaml`) 中缺少 `wandb` entity/project 配置，导致 `fetch_wandb_metrics` 工具无法查询
- 其余一切正常，无报错

---
