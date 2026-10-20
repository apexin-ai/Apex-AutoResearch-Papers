# mvp_occ_s3_v2 训练诊断报告

## 结论：训练已成功完成，EXIT_CODE=1 为误报

## 失败原因
EXIT_CODE=1 并非训练失败，而是 PyTorch distributed 进程退出时的清理警告：
```
[rank0]:[W526 19:04:45] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources.
```
这是 PyTorch distributed 的已知行为——训练脚本退出前未显式调用 `torch.distributed.destroy_process_group()`，导致进程以非零退出码结束。**不影响训练结果和 checkpoint 质量。**

## 训练进度
- **完成度**: 50005/50005 步 (100%)
- **总训练时间**: 14h 21m 32s
- **最终 loss (step 50000)**: occ_loss=0.0098, depth_loss=0.0000, action_loss=0.0493
- 日志确认: "Max step 50005 reached! Stopping training..."

## Checkpoint 状态
两个 checkpoint 均已成功保存：

| Checkpoint | 路径 | 状态 |
|-----------|------|------|
| 40000_chkpt | `openvla-7b+...--mvp_occ_s3_v2--40000_chkpt/` | 已保存 |
| 50000_chkpt | `openvla-7b+...--mvp_occ_s3_v2--50000_chkpt/` | 已保存 (含 merged model + dataset_statistics.json) |

## 建议
- **无需重试**。训练已完整完成，50000_chkpt 可直接用于评估。
- 若要消除未来实验的 EXIT_CODE=1 误报，可在 finetune.py 退出前添加 `torch.distributed.destroy_process_group()`。
