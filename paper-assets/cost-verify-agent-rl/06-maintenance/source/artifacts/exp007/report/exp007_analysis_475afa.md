# exp007 Training Analysis Report

## 实验概要

| 项目 | 值 |
|------|-----|
| 实验ID | exp007 |
| 假设 | Parser fix + prompt enhancement + speed optimization (collapse_detection off) enables GRPO learning signal with <50% invalid_action |
| 模型 | Qwen3-1.7B |
| 训练方法 | GRPO (verl框架, FSDP) |
| 环境 | ALFWorld, 30 max_turns, 64 traj/step |
| 计划步数 | 30 steps |
| 实际完成 | 10/30 steps (33%) |
| 训练时长 | ~1h52m (6739s) |
| 服务器 | bjb1-17606, 2× RTX PRO 6000 (cuda:0,1) |
| 父实验 | exp003 (bootstrap失败, 95% invalid_action) |
| W&B | 未配置 |
| Checkpoint | 无 (目录为空) |

## 终止原因

**训练在 step 10 rollout 阶段崩溃**，错误：
```
OSError: [Errno 28] No space left on device: 
'/root/miniconda3/lib/python3.12/site-packages/fast_downward/libdownward.so' 
-> '/tmp/tmpf_bqbz28/libdownward.so'
```

Ray session 文件填满了根分区 /tmp（30GB overlay），导致 ALFWorld 环境的 fast_downward 库无法复制 .so 文件到临时目录。

## 关键指标表

### 训练指标趋势 (step 0-10)

| Step | Success | action_is_valid | manager_invalid | pass@8 | pg_loss | ppo_kl | entropy | grad_norm | score_mean |
|------|---------|-----------------|-----------------|--------|---------|--------|---------|-----------|------------|
| 0 (val) | 0.000 | 0.054 | 0.065 | 0.0¹ | - | - | - | - | - |
| 1 | 0.047 | 0.040 | 0.027 | 0.375 | 0.00127 | -0.00046 | 0.0668 | 5.72 | 0.389 |
| 2 | 0.000 | 0.090 | - | 0.000 | - | - | - | - | - |
| 3 | 0.000 | 0.080 | - | - | - | - | - | - | - |
| 4 | 0.063 | 0.113 | - | - | - | - | - | - | - |
| 5 | 0.016 | 0.084 | - | - | - | - | - | - | - |
| 6 | 0.016 | 0.118 | - | - | - | - | - | - | - |
| 7 | 0.000 | 0.066 | 0.016 | 0.000 | - | - | - | - | - |
| 8 | 0.000 | 0.049 | 0.010 | 0.000 | - | - | - | - | - |
| 9 | 0.000 | 0.080 | - | 0.000 | 0.00063 | 0.00186 | 0.0449 | 5.12 | -0.044 |
| 10 | 0.063 | 0.084 | 0.016 | 0.375 | 0.00117 | 0.00127 | 0.0570 | 8.48 | 0.578 |

¹ step 0 是 val-env 评估，使用 pass@1

注：steps 2-8 的 actor 指标因日志截断未完整提取，仅 step 1/9/10 有完整 actor 数据。

### Dryrun 基线对比

| 指标 | Dryrun 基线 | Step 1 | Step 10 | 变化 |
|------|-------------|--------|---------|------|
| invalid_action (manager) | 6.5% | 2.7% | 1.6% | 改善 ✓ |
| action_is_valid | 5.4% | 4.0% | 8.4% | 微弱改善 |
| success | - | 4.7% | 6.3% | 无显著趋势 |

## 趋势分析

### 1. action_is_valid
- 10步内在 4.0%-11.8% 之间波动，均值约 7.8%
- 无清晰上升趋势：step 4 达到峰值 11.3%，但 step 8 回落到 4.9%
- 相比 dryrun 基线 5.4% 有微弱改善，但远未达到期望水平
- **Phase A 判定标准：step 10 后 action_is_valid = 8.4% < 10%，触发 FAIL 条件**

### 2. Success Rate
- 绝大多数步骤 success=0（steps 2,3,7,8,9）
- 偶发成功（steps 1,4,10 有 4.7-6.3%）可能是随机噪声（64 条轨迹中 3-4 条）
- 远未达到 76% PASS 阈值

### 3. pg_loss（梯度信号）
- 非零但极小（0.0006-0.0013），说明有梯度但强度不足
- 梯度未带来有效学习：action_is_valid 无上升趋势

### 4. Entropy
- 下降趋势（0.0668 → 0.0449 → 0.0570）
- 模型在变得更确定性，但不是在学习正确行为

### 5. manager_invalid_action
- 从 exp003 的 95% 降到 1.6-2.7%——**parser fix 确实解决了动作解析问题**
- 但解决解析问题后暴露出更深层问题：模型生成的动作虽然格式正确，但语义无效

### 6. Collapse Detection
- first_turn_valid_rate: 0.64 (step 1) → 0.81 (step 5) → 0.78 (step 10)，未触发 collapse
- retrieval_accuracy 保持 1.0，模型输出有多样性

## 结论

**FAILED**

### 失败原因（双重）

1. **基础设施故障**：/tmp 磁盘空间耗尽导致训练在 step 10/30 崩溃，无 checkpoint 保存
2. **学习信号不足**：即使在完成的 10 步中，关键指标未呈现有意义的改善趋势
   - action_is_valid 在 step 10 仅为 8.4%，触发 Phase A FAIL 条件（<10%）
   - success rate 停滞在 0-6.3%，远离 76% 目标
   - parser fix 成功解决了格式问题（invalid_action 从 95%→1.6%），但未解决语义理解问题

### 关键洞察

- **Parser fix 有效**：manager_invalid_action 从 exp003 的 95% 降到 <3%
- **但学习信号仍然不足**：格式正确 ≠ 语义有效。模型能产出正确格式的动作，但这些动作在 ALFWorld 中无效
- **可能的根因**：Qwen3-1.7B 的基础能力不足以理解 ALFWorld 任务语义，或 GRPO 的 reward signal 过于稀疏（大部分轨迹 reward=0）导致无法有效学习

### 后续建议
- 修复 /tmp 磁盘问题（设置 TMPDIR 到数据盘）后可考虑重跑
- 但鉴于 10 步内无学习趋势，即使完成 30 步也难以达到 76% 目标
- 需要更根本的改进：更大模型、更密集的 reward shaping、或预训练 ALFWorld 行为
