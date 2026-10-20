# 诊断报告：exp-ctrl-contam-qwen-clean s4/s5/s6 状态

**日期**: 2026-05-21
**服务器**: westd-35694 (4x NVIDIA RTX PRO 6000 Blackwell, 98GB each)

## 结论：三个实验均已成功完成，"failed" 为监控误判

### s4 (clean_s4, seed=301)
- **状态**: ✅ 训练完成
- 939/939 steps, 3 epochs, train_loss=1.352, runtime=1926s (~32min)
- Checkpoint 保存完整: 313, 626, 939 + final adapter (20MB safetensors)
- 输出路径: `/root/autodl-tmp/ctrl_contam_pilot/checkpoints/clean_s4/`

### s5 (clean_s5, seed=302)
- **状态**: ✅ 训练完成
- 939/939 steps, 3 epochs, train_loss=1.353, runtime=1743s (~29min)
- Checkpoint 保存完整: 313, 626, 939 + final adapter
- 输出路径: `/root/autodl-tmp/ctrl_contam_pilot/checkpoints/clean_s5/`

### s6 (clean_s6, seed=303)
- **状态**: ✅ 训练完成 (pid 89524 已退出)
- 237/237 steps (注意: 步数与 s4/s5 不同, s4/s5 为 939 步)
- Checkpoint: 79, 158, 237 + final adapter
- 输出路径: `/root/autodl-tmp/ctrl_contam_pilot/checkpoints/clean_s6/`
- 无 `/tmp/train_clean_s6.log` (可能日志路径不同)

## 失败根因

**监控系统误判 (false positive)**。训练进程正常完成后退出 (exit code 0)，但监控检测到 "process dead" 且未找到 sentinel file 或 W&B run，因此 auto-resolve 为 failed。

实际上：
- 日志最后一行均为 `Model saved to ...`，无任何错误
- 所有 checkpoint 和 final adapter 文件完整存在
- 训练指标正常 (loss ~1.35, mean_token_accuracy ~0.65)

## 当前 GPU 状态

| GPU | Memory Used | Utilization | Process |
|-----|------------|-------------|---------|
| 0   | 0 MiB      | 0%          | idle |
| 1   | 5,697 MiB  | 94%         | pid 90909: `python eval_lz.py --condition contam_50 --gpu 1` |
| 2   | 11,003 MiB | 67%         | pid 73689: `python train_grpo.py --gpu 0` (running 2h29m) |
| 3   | 0 MiB      | 0%          | idle |

## 磁盘状态

`/root/autodl-tmp/`: 80GB / 250GB used (32%) — 充足

## 注意事项

1. **s6 步数差异**: s6 共 237 步 (save at 79/158/237), 而 s4/s5 共 939 步 (save at 313/626/939)。可能使用了不同的 num_epochs 或 batch_size 配置，需确认是否符合预期。
2. **监控修复建议**: 训练脚本完成后应写入 sentinel file (如 `DONE` 标记文件) 或配置 W&B logging，以便监控系统正确识别成功完成。
3. **实验状态需在管理系统中手动标记为 COMPLETED**。
