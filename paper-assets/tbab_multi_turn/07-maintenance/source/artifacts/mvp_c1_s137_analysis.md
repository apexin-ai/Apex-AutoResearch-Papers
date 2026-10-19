# mvp_c1_s137 训练结果分析

## 训练指标

| 指标 | s137 | s42 | 差异 |
|------|------|-----|------|
| final_train_loss | 0.2471 | 0.2437 | +0.0034 |
| avg_train_loss | 0.4423 | 0.4426 | -0.0003 |
| train_runtime (s) | 8549 | 5761 | +48.4% |
| adapter_size (bytes) | 335,604,696 | ~335 MB | 一致 |
| epochs | 3 | 3 | 一致 |
| total_steps | 471 | 471 | 一致 |
| exit_code | 0 | 0 | 一致 |

## Checkpoint

- **路径**: `/root/tbab_multi_turn/checkpoints/c1_lora_only_seed137/`
- **文件**: adapter_model.safetensors (320 MB), adapter_config.json, tokenizer.json, tokenizer_config.json, chat_template.jinja, training_args.bin
- **中间 checkpoint**: checkpoint-157, checkpoint-314, checkpoint-471
- **保存时间**: 2026-05-18 21:13 UTC

## Loss 曲线趋势

- Epoch 1 (steps 1-157): loss 从 ~0.66 下降到 ~0.61
- Epoch 2 (steps 158-314): loss 从 ~0.45 下降到 ~0.34
- Epoch 3 (steps 315-471): loss 从 ~0.25 下降到 ~0.22，最终步 0.2471
- 收敛模式与 s42 高度一致

## W&B

- 目录: `/root/tbab_multi_turn/scripts/wandb/`
- s137 对应 run: `offline-run-20260518_185032-a28h9so6`（根据训练开始时间推断）
- 最新 run `offline-run-20260518_211605-90rbv856` 属于新启动的 mvp_c4_s42

## GPU 状态 (21:16 UTC)

- GPU: NVIDIA RTX PRO 6000, 17045/97887 MiB, 35% util
- **不空闲**，两个进程正在占用:
  1. PID 25961: C1_s42 eval（code task），占用 17036 MiB，从 18:54 开始运行
  2. PID 40217: **mvp_c4_s42 训练**（condition4_full_tbab.yaml, seed=42），21:16 刚启动

## C1_s42 eval 进程状态

- **仍在运行**，PID 25961
- 命令: `run_eval.py --model_path c1_lora_only_seed42 --tasks code --n_repeats 1 --min_shards 5`
- 输出目录: `/root/tbab_multi_turn/eval/results/c1_s42_code_n1/`
- CPU 时间: 104 分钟+

## 注意事项

1. **训练时长异常**: s137 耗时 8549s，比 s42 的 5761s 长 48%。可能原因是 s137 训练期间 eval 进程也在 GPU 上运行，争抢资源导致训练变慢。
2. **Loss 一致性好**: final_loss 和 avg_loss 两个 seed 几乎相同，说明训练过程稳定可复现。
3. **新训练已启动**: mvp_c4_s42（Condition 4 full TBAB）已在 21:16 启动，与 eval 共享 GPU。需要关注是否会因资源争抢导致 OOM 或训练缓慢。
