# 诊断报告: perlayer_kl_k16_s42_v2 失败

## 错误信息（原文）

```
File "/root/distill_sparse_swiglu/src/train_perlayer_kl_k4.py", line 314, in main
    wandb.init(project=args.wandb_project, name=run_name, config=vars(args))
...
wandb.errors.errors.UsageError: No API key configured. Use `wandb login` to log in.
EXIT_CODE=1
```

脚本在第一行 wandb.init() 就崩溃了，**没有进入训练循环**，无 checkpoint 产生。

## 根因分析

`train_perlayer_kl_k4.py` 第 314 行无条件调用 `wandb.init()`，但服务器上 wandb 认证缺失：
- 无 `/root/.netrc`
- 无 `/root/.config/wandb/` 目录
- `.bashrc` 中无 `WANDB_API_KEY`

**K=4 为什么成功**：K=4 训练（perlayer_kl_k4_s123.log 等）在脚本加入 wandb 之前运行，日志中无 wandb 痕迹。wandb 集成是后来添加的，K=16 是第一个使用新版脚本的实验。

与 v1 失败原因不同（v1 是 argparse error `--loss_type kl_normalized`）。v2 修了 argparse 问题但触发了新的 wandb 认证问题。

## 修复建议

**方案 A（最快，推荐）**：启动命令前加 `WANDB_MODE=disabled`

```bash
WANDB_MODE=disabled python -u src/train_perlayer_kl_k4.py \
  --num_masked_layers 16 --seed 42 --num_steps 1000 --save_every 500 \
  --gradient_checkpointing \
  --output_dir /root/distill_sparse_swiglu/checkpoints/perlayer_kl_k16_s42_v2 \
  --gpu 0
```

**方案 B（如需 wandb logging）**：在服务器上配置 API key

```bash
wandb login <YOUR_API_KEY>
```

**方案 C（长期）**：修改脚本，使 wandb 在无 key 时自动 fallback 到 disabled

```python
# line 314 改为:
try:
    wandb.init(project=args.wandb_project, name=run_name, config=vars(args))
except wandb.errors.errors.UsageError:
    wandb.init(mode="disabled")
```
