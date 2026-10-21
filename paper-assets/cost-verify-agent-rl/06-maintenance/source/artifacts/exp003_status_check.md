# exp003 状态检查 — 2026-05-13

## 进程状态
- **PID 157852**: 存活，运行 02:09:34
- **命令**: `python train.py --config-name=_alfworld_exp003`（CUDA_VISIBLE_DEVICES=0,1）
- **模型**: Qwen3-1.7B（full fine-tune, no LoRA）

## 训练进度
- **当前 step**: 1/100（1%）
- **每步耗时**: ~5743s（~96 分钟）
- **预计剩余**: ~158 小时（~6.6 天）
- **吞吐量**: ~40 tokens/s

## GPU 利用率
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0   | 97%    | 48375 / 97887 MiB (49%) |
| 1   | 97%    | 48341 / 97887 MiB (49%) |

## Step 1 关键指标
| 指标 | 值 | 说明 |
|------|-----|------|
| success | 0.78% (1/128) | 极低 |
| pass@8 | 6.25% | |
| manager_invalid_action | **95.3%** | 绝大多数动作无效 |
| action_is_valid | 1.9% | |
| action_is_effective | 4.7% | |
| num_actions | 2.14 | 每 episode 动作数极少 |
| raw_reward | 0.0 | |
| episodic_return | 0.0 | |
| response_length (mean) | 3584 tokens | |

### Actor 指标
| 指标 | 值 |
|------|-----|
| entropy | 0.088 |
| pg_loss | 0.000176 |
| ppo_kl | 0.003 |
| kl_loss | -0.0038 |
| grad_norm | 2.50 |
| pg_clipfrac | 0.57% |

### Critic 指标
| 指标 | 值 |
|------|-----|
| score/mean | -4.68 |
| score/max | 9.80 |
| score/min | -5.00 |
| advantages/mean | 0.0087 |

## Checkpoint
- **无 checkpoint 产出**（checkpoints 目录不存在，step 1 刚完成）

## W&B
- 日志中未发现 W&B run URL（可能未启用或 run 未初始化）

## 诊断备注
- 95.3% invalid_action 率表明模型在 step 1 几乎完全无法生成合法 ALFWorld 动作
- 每 episode 仅 2.14 个动作，说明大部分 trajectory 很早就因无效动作终止
- 这在训练初期是预期行为（Qwen3-1.7B 基座模型未见过 ALFWorld 格式）
- 需要持续监控后续 step 的 invalid_action 是否下降、success 是否上升
