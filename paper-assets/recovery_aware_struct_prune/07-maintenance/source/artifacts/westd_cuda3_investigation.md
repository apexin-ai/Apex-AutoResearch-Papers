# westd-29022 cuda:3 未注册进程调查报告

**调查时间**: 2026-05-19 10:47 UTC

## 进程状态：活跃

| 字段 | 值 |
|------|-----|
| PID | 59413 |
| GPU | cuda:3, 29610 MiB / 97887 MiB, 99% utilization |
| 启动时间 | 2026-05-19 10:18 |
| tmux session | `eval_gsm8k_standard_300` |
| 命令 | `python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300/ --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_extended_300.json` |

## 进度

- 207/1319 samples (16%), 已运行 ~22 min
- 当前速率 ~4 s/it
- 当前 accuracy: 0.63, eos_rate: 99%
- 预计剩余 ~74 min（总计约 96 min）
- 输出文件尚未生成（eval 完成后写入）

## 模型来源

`/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300/` 存在，含 checkpoint-280/290/300，创建于 2026-05-18 22:40。

## 结论

**有效实验，非 orphan。** 这是 grpo_standard_20_extended_300 模型在 GSM8K 上的评估任务，在 tmux session 中正常运行。仅因未注册到 registry 而被 reconcile_crons 标记。

## 建议

- **保留**：让评估自然完成（预计 ~74 min 后）
- 完成后将结果补录到 registry
- 同服务器其余 3 张 GPU 也都在跑 python 进程（PID 56151/56977/36703），均满载
