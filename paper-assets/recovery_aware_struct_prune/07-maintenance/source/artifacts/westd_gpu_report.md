# westd-11672 GPU 状态报告

**时间**: 2026-05-17 17:48 UTC+8

## nvidia-smi 快照

| GPU | 进程 PID | 显存占用 | GPU-Util | 温度 |
|-----|----------|----------|----------|------|
| 0 | 3331 | 17658MiB / 97887MiB | 91% | 54°C |
| 1 | 14556 | 29610MiB / 97887MiB | 99% | 80°C |
| 2 | 3333 | 13144MiB / 97887MiB | 88% | 53°C |
| 3 | 11896 | 30078MiB / 97887MiB | 96% | 73°C |

## 各 GPU 任务详情

| GPU | exp_id | 模型 | 进度 | 当前 Acc | 预估完成时间 |
|-----|--------|------|------|----------|-------------|
| 0 | eval_math500_unpruned | DeepSeek-R1-Distill-Qwen-7B | 357/500 (71%) | 0.7343 | ~19:00 今天 |
| 1 | eval_math500_grpo_standard_20 | grpo_stage2_standard_20_v8/checkpoint-50 | 9/500 (2%) | N/A | ~07:00 明天 |
| 2 | eval_math500_sft_standard_20 | sft_standard_20_westd | 484/500 (97%) | 0.2511 | ~18:00 今天 |
| 3 | eval_math500_grpo_rasp_20_v2 | grpo_stage2_rasp_20_v9 | 55/500 (11%) | 0.3400 | ~03:30 明天 |

### 进度分析
- **GPU 2 (sft_standard_20)**: 还剩 16 个样本，约 10-15 分钟完成
- **GPU 0 (unpruned)**: 还剩 143 个样本，平均 ~30s/it，约 70 分钟完成
- **GPU 3 (grpo_rasp_20)**: 平均 ~80s/it（部分样本 200+s），还需 ~9-10 小时
- **GPU 1 (grpo_standard_20)**: 刚启动 22 分钟，平均 ~140s/it，还需 ~13-16 小时

注: GRPO 模型生成极长（30GB 显存），推理速度远慢于 SFT 模型（13GB 显存）。

## 已完成的 MATH-500 结果

| 文件 | 完成时间 | Accuracy |
|------|----------|----------|
| eval_math500_sft_rasp_20.json | May 17 17:19 | **0.242** |

## tmux sessions

```
eval_math500_grpo_rasp_20_v2  (created 16:34)
eval_math500_sft_standard     (created 14:20)
eval_math500_unpruned         (created 14:20)
```

注: grpo_standard_20 不在 tmux 中，通过 cron/后台进程运行。

## 磁盘状态

| 分区 | 使用 | 总量 | 使用率 |
|------|------|------|--------|
| 根分区 (/) | 5.2G | 30G | 18% |
| 数据盘 (/dev/sda2) | 17G | 879G | 3% |
| autodl-tmp 项目目录 | 689G | - | - |

磁盘状态健康，无需清理。

## 结论

**当前无空闲 GPU。预计释放顺序：**

1. **GPU 2** — ~18:00 今天（约 10-15 分钟后）
2. **GPU 0** — ~19:00 今天（约 70 分钟后）
3. **GPU 3** — ~03:30 明天
4. **GPU 1** — ~07:00 明天

如需立即使用 GPU，GPU 2 即将释放，可等待片刻后使用。
