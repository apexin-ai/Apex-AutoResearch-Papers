# 诊断报告: batchsize16_nmin8_seed42

## 结论：训练已成功完成，监控误判为失败

## 根本原因

脚本通过 `bash scripts/run_batchsize16_nmin8_seed42.sh` 直接启动（日志写到 `/tmp/batchsize16_nmin8_seed42.log`），未使用 `submit_training_job` 包装器，因此没有生成 `/tmp/agent-ml-exit/batchsize16_nmin8_seed42.exit` sentinel 文件。同时 `WANDB_MODE=disabled` 禁用了 W&B 心跳。监控系统 5 次探测进程已退出 + 无 sentinel + 无 W&B，自动判定失败。

## 关键证据

- 日志尾部确认完成：
  ```
  100%|██████████| 6103/6103 [13:00:00<00:00, 7.67s/it]
  Training complete. Model saved to output/models/batchsize16_nmin8_seed42/final
  DONE: batchsize16 seed42
  train_runtime: 46800.93s, train_loss: 2.6308
  ```
- Final model 文件时间戳: `2026-05-17 22:02:39`（约 13 小时训练）
- 输出目录包含 checkpoint-5500, checkpoint-6000, checkpoint-6103, final/
- step_metrics.jsonl 记录到 step 6102（0-indexed 最后一步）
- lm_eval 已在评估 final model（PID 97397, arc_easy task）

## 修复建议

无需重新训练。模型已完整保存，评估已在进行中。

如需补充评估，模型路径：
```
/root/provenance_weight_training/output/models/batchsize16_nmin8_seed42/final
```

未来避免误判：使用 `submit_training_job` 提交任务（会自动创建 sentinel 文件），或脚本中手动写 sentinel：
```bash
echo "0|$(date -u +%Y-%m-%dT%H:%M:%SZ)" > /tmp/agent-ml-exit/batchsize16_nmin8_seed42.exit
```
