# mvp_imm_v8b_twostage 诊断报告

## 结论：实验已成功完成，非失败

Cron 监控误报。训练进程在 14:57:22 正常退出，两个 stage 均完整执行。

## 详情

- **Stage1**: 10,000 steps 完成，checkpoint 保存于 `stage1_done/`
- **Stage2**: 20,000 steps 全部完成（step 19950 → "stage2 complete"），final checkpoint 已保存
- **最终 loss**: stage1=0.034, stage2=0.027; action_loss=0.027
- **训练速度**: 3.1 steps/sec (stage2 全程稳定)
- **Final checkpoint**: `checkpoints/imm_anchor_v8b_twostage/final/checkpoint.pt` (1.2GB)
- **Stage2 中间 checkpoints**: 每 2000 steps 一个，共 9 个 (step_002000 ~ step_018000)
- **W&B offline run**: `wandb/offline-run-20260516_122925-2t4p795u/` 完整，可 sync

## 误报原因

进程正常结束后退出，cron 监控检测到进程不存在且无 sentinel 文件，误判为异常退出。需要在训练脚本结束时写入 sentinel 文件（如 `.done`），或让 cron 监控检查日志末尾的完成标志。

## GPU 当前状态

cuda:1 上有另一个 python3 进程在运行（10.3GB VRAM, 95% util），非本实验残留。

## 下一步

1. 同步 W&B 数据：`wandb sync <offline-run-path>`
2. 用 final checkpoint 跑评估
3. 修复 cron 监控的 sentinel 检测逻辑，避免误报
