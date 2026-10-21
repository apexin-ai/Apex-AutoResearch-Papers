# 状态检查 Loop 4 — 2026-05-15 07:10 UTC

## 进程总览

| PID | GPU | 任务 | 状态 | 运行时间 | 进度 | ETA |
|-----|-----|------|------|----------|------|-----|
| 90080 | cuda:0 | GRPO lr5e6_r1 训练 | ✅ 存活 | 3h25m | 113/200 (56.5%) | ~2h40m |
| 101842 | cuda:2 | ckpt-40 eval (r2) | ✅ 存活 | 1h40m | 60/62 (97%) | ~3min |
| 108185 | cuda:1 | ckpt-60 eval (r2) | ✅ 存活 | 35m42s | 23/62 (37%) | ~60min |
| 104979 | cuda:3 | SFT baseline eval | ✅ 存活 | 1h12m | 无日志可查 | ~36min (估) |

## 详细进度

### 1. PID 90080 — GRPO 训练 lr5e6_r1 (cuda:0)

- **进度**: step 113/200 (56.5%), ~100-112s/step
- **已保存 checkpoint**: 20, 40, 60, 80, 100
- **最新指标** (step ~80):
  - format_reward: 0.249
  - f1_reward: 0.016
  - ced_reward: 0.018
  - total reward: 0.283
  - KL: 0.0093
- **KL 警告**: steps 5/30/85/90/105 出现 KL divergence 爆炸 (最高 7e13), monitoring-only
- **GPU**: 13645 / 32607 MiB

### 2. PID 101842 — ckpt-40 eval r2 (cuda:2) — 即将完成

- **进度**: batch 60/62 (97%), ~98s/batch
- **预计 2-3 分钟内完成**
- **日志**: `/root/runs/faith-evidence-ie/mvp2_eval_lr5e6_r1_ckpt40.log`
- **输出**: `/root/autodl-tmp/eval_results/lr5e6_r1_ckpt40/checkpoint-40/` (完成时写入)
- **GPU**: 11243 / 32607 MiB

### 3. PID 108185 — ckpt-60 eval r2 (cuda:1)

- **进度**: batch 23/62 (37%), ~92s/batch
- **日志**: `/root/runs/faith-evidence-ie/mvp2_eval_lr5e6_r1_ckpt60_r2.log`
- **输出**: `/root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60/` (空)
- **GPU**: 9719 / 32607 MiB

### 4. PID 104979 — SFT baseline eval (cuda:3)

- **进度**: 无可读日志 (shell 脚本启动, stdout 到管道)
- 运行 1h12m, 参照 SFT eval r3 耗时 1h48m, 估计 ~65%
- **输出**: `/root/autodl-tmp/sft_baseline_eval_results/` (空)
- **GPU**: 9713 / 32607 MiB

## nvidia-smi

```
GPU 0: RTX 5090 | 50% util | 13645 / 32607 MiB  (GRPO 训练)
GPU 1: RTX 5090 | 87% util |  9719 / 32607 MiB  (ckpt-60 eval)
GPU 2: RTX 5090 | 66% util | 11243 / 32607 MiB  (ckpt-40 eval)
GPU 3: RTX 5090 | 67% util |  9713 / 32607 MiB  (SFT baseline eval)
```

## 已完成的 eval 结果 (参照)

### SFT eval r3 (已完成)
- **F1: 0.4057** | Ign-F1: 0.4057 | Evi-F1: 0.7979 | EDCR: 0.7118
- Format OK: 983/985 (99.8%) | Truncated: 367/985

### grpo_ced_lr5e6 ckpt-20 eval (已完成)
- **F1: 0.0077** (几乎为零) | Evi-F1: 0.6281 | EDCR: 0.9934
- Format OK: 976/985 (99.1%) | Truncated: 587/985
- field_compliance: 39.9% — 只有 393/985 格式完整
- 14440 predictions vs 12151 gold — 关系抽取精度极低

## 异常标记

- **ckpt-20 F1 = 0.008** — GRPO 早期 checkpoint 关系抽取能力崩溃, field compliance 仅 40%, 但 EDCR=0.99 说明证据引用质量高. 模型可能在学习证据引用但还没学会正确的关系抽取格式
- **KL 爆炸** — GRPO 训练 KL divergence 多次爆至 7e13, monitoring-only 但值得关注
- **SFT baseline eval 无日志** — 进程存活但无法追踪进度, 脚本直接启动没有重定向到文件
