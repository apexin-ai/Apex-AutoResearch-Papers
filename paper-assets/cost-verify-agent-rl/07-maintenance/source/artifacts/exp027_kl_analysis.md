# exp027 KL 监控报告 — 2026-05-16 01:05 (UTC+8)

## 当前训练进度
- 当前 step: 0→1 过渡中（step 1 policy update 进行中）
- 运行时间: ~2.5h（22:33 启动）
- 训练进度: 0/50 steps (0%)
- W&B run: y7jiibqk (`exp027-alfworld-stable-grpo`)
- 进程状态: **存活** (PID 793046)，双 GPU 100% 利用率

## Step 0 初始验证指标（16 episodes）
| 指标 | 值 |
|------|-----|
| val-env/AlfworldSG/success | **6.25%** (1/16) |
| val-env/AlfworldSG/num_actions | 42.375 |
| val-env/AlfworldSG/episodic_return | 0.0 |
| val-env/AlfworldSG/raw_reward | 0.0 |
| val-env/response_length | 114.67 |
| val-core/unknown/reward/mean@775 | 0.3226 |

## KL 指标
**尚无 KL 数据。** 训练仍在 step 1 的 policy update 阶段（compute_policy_loss 已触发），首个 KL 指标需等 step 1 完成后才记录到 W&B。

| Step | KL | Entropy | Reward | Success |
|------|-----|---------|--------|---------|
| 0 (val) | N/A | N/A | 0.3226 | 6.25% |
| 1 | 计算中 | 计算中 | 计算中 | 计算中 |

## 判定
- [ ] KL 正常 (< 0.005)
- [ ] 需要告警
- [x] **数据不足，无法判定** — 训练尚未完成 step 1

## 详细分析

### 时间线
| 时间 (UTC+8) | 事件 |
|--------------|------|
| 22:33 | 训练启动，W&B 初始化 |
| 22:34-22:42 | Step 0 验证 rollout（502s） |
| 22:42 | Step 0 验证完成：success=6.25% |
| 22:50 | Step 1 训练 rollout 开始 |
| 00:14 | Step 1 rollout 完成，进入 policy update（最后日志输出） |
| 00:14-now | Step 1 policy update 进行中（无日志输出，GPU 100%） |

### 当前状态评估
1. **进程健康**: GPU 双卡 100% 利用率(50.5GB/97.9GB each)，进程存活，正在做 ref_log_probs + policy gradient 计算
2. **Step 0 基线**: success=6.25% 与 exp026 step 0 可比，属正常初始水平
3. **速度**: step 1 rollout 耗时 ~1.4h（128 trajectories x 50 max_actions），policy update 已进行 ~47min——首个 step 因 torch.compile 预热会更慢
4. **日志刷屏**: 10736/12458 行(86%)是 anchor_obs warning，正常现象但影响日志可读性

### 与 exp026 对比
- exp026 step 4 出现死亡螺旋（success 归零）
- exp027 新增保护措施：kl_loss_coef=0.005, entropy_coeff=0.01, low_var_kl
- 需等 step 1-5 KL 数据出来后才能判断保护是否有效

### 建议下次检查时间
Step 1 完成预计还需 ~30-60min（policy update + log_prob 计算）。建议 **1 小时后** 再次检查，届时应有 step 1 的完整训练指标和可能的 step 2 rollout 数据。

### 配置确认
- kl_loss_coef: 0.005
- kl_loss_type: low_var_kl
- use_kl_loss: True
- entropy_coeff: 0.01
- clip_ratio: 0.2 (low: 0.2, high: 0.28)
- ppo_kl_coef: 0.1
- lr: 5e-07 (constant schedule)
- ppo_epochs: 1
- model: Qwen3 1.72B (qwen3_exp021_ragen_sft_v4)
- CUDA_VISIBLE_DEVICES: 0,1
