# d062_full_ft_scierc 实验诊断报告

**诊断时间**: 2026-05-19 13:15 UTC+8 (更新)
**服务器**: westd-21461
**GPU**: 2x NVIDIA RTX PRO 6000 Blackwell (96GB each)

## 结论：实验全流程已完成，cron 误报

训练、推理、评估全流程均已正常完成。Cron 报告的 "process dead 5x with no sentinel/W&B" 是误报。

## 失败原因分析

### 原始失败 (04:50 cron 报告)

训练过程中，最后一个 epoch 结束时 checkpoint 保存因磁盘空间不足失败：

```
safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```

原因：`save_strategy="no"` 未阻止 `eval_strategy="epoch"` 末尾触发的 save。此时 `/dev/md0` 250GB 磁盘空间紧张。

### 恢复过程

Checkpoint 后续被成功保存（疑似手动清理磁盘后重试），然后推理也完成了。

## 最终状态：全流程完成

### Checkpoint

```
/root/autodl-tmp/checkpoints/qwen_full_ft_scierc/
  model.safetensors  16,381,517,208 bytes  (May 19 12:09)
  config.json, tokenizer.json, training_args.bin  均存在
```

### 推理输出 (551/551 samples)

| 文件 | 行数 | 时间 |
|------|------|------|
| re_qwen_full_ft_scierc_unconstrained.jsonl | 551 | May 19 12:36 |
| re_qwen_full_ft_scierc_full_s1.jsonl | 551 | May 19 13:09 |

### 质量指标

| 指标 | Unconstrained | Constrained (full_s1) |
|------|--------------|----------------------|
| Entity F1 | 0.6478 | 0.6478 |
| Relation F1 | 0.3789 | 0.3789 |
| Domain-range violation rate | **2.74%** | **0.0%** |
| Relation vocab violation rate | 0.18% | 0.0% |
| Cross-field consistency violation | 0.0% | 1.31% |
| JSON parse rate | 100% | 100% |

Constrained decoding 成功将 domain-range violation 从 2.74% 降至 0%。

### 训练指标 (来自旧诊断)

| 指标 | 值 |
|------|------|
| 总步数 | 333/333 (100%) |
| Epochs | 3 |
| Final eval_loss | 0.09459 |
| Mean token accuracy | 97.61% |
| 训练耗时 | ~21 min |
| GPU 显存占用 | ~19GB / 96GB |

## 时间线

| 时间 | 事件 |
|------|------|
| 03:15 | 实验创建 |
| ~11:25 | 训练脚本启动 |
| ~11:47 | 训练完成，checkpoint 保存失败 (No space left on device) |
| 04:50 | Cron 误报 failed (5x 无 sentinel/W&B) |
| 12:09 | Checkpoint 成功保存 |
| 12:36 | Unconstrained 推理完成 |
| 12:38 | 首次 constrained 推理被 Terminated |
| 13:09 | Constrained 推理重跑完成，violation report 生成 |

## Cron 误报原因

脚本设置了 `WANDB_DISABLED=true` + `report_to="none"`，无 sentinel 文件写入。Cron 监控仅依赖 W&B 心跳或 sentinel 文件判断存活。

## 修复建议

1. **无需重新训练或推理**：全流程已完成
2. **实验状态应更新为 completed**
3. **磁盘空间**：250GB 磁盘已用 65%，建议清理旧 checkpoints（如 `llama_lora_scierc_merged`）
4. **Cron 监控改进**：
   - 短期：脚本中加入 sentinel 文件写入
   - 长期：支持通过进程存在性或 GPU 占用率判断存活
5. **save_strategy bug**：`save_strategy="no"` 未阻止末尾 epoch save，建议额外设置 `load_best_model_at_end=False`
