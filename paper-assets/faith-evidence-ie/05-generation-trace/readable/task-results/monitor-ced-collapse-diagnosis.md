# monitor ced collapse diagnosis

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_ced-collapse-diagnosis_20260514T101856_result.json`
- **Structured JSON:** [`b5ed4803f78b5b4de407.json`](../../sessions/b5/b5ed4803f78b5b4de407.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整诊断报告。

---

## 诊断结果

### 优先级 1: Checkpoint — **无**
`/root/autodl-tmp/grpo_s3/` 为空。`save_strategy="epoch"` 且 189 步才完成一个 epoch，所以**没有任何中间 checkpoint**。

### 优先级 2: 训练状态 — 确认退化，建议 kill

当前 step 80/189，完整指标趋势：

| Step | Format | F1 | CED | Total Reward | Clipped% | Mean Len | frac_zero_std |
|------|--------|----|-----|-------------|----------|----------|---------------|
| 5 | 0.554 | 0.008 | 0.085 | 0.648 | 18.1% | 668 | 12.5% |
| 10 | 0.886 | 0.012 | 0.048 | 0.946 | 6.9% | 562 | 32.5% |
| 15 | 0.853 | 0.043 | 0.427 | 1.323 | 13.8% | 631 | 5.0% |
| 65 | 0.980 | 0.005 | 0.756 | 1.741 | 0.3% | 112 | 6.3% |
| 70 | 0.977 | 0.006 | 0.546 | 1.529 | 0.0% | 104 | 16.3% |
| 75 | 0.992 | 0.003 | 0.449 | 1.443 | 0.0% | 136 | 16.3% |
| **80** | **0.966** | **0.001** | **0.346** | **1.313** | 0.0% | 156 | **28.8%** |

**早停判断**: step 80, total_reward=1.31 (距阈值 1.3 仅差 0.01), f1=0.0006 (实质归零)。每 5 步 total_reward 下降约 0.1，**step 85 必然跌破阈值**。且 F1 已完全丧失，无恢复可能。**建议立即 kill。**

### 优先级 3: clip_ratio=0 根因

- TRL 默认 `epsilon=0.2`，**未被代码或 DeepSpeed 覆盖**，配置正常
- clip_ratio=0 不是 bug — QLoRA 下每步可训练参数少，单步 policy ratio 变化小于 ε=0.2，PPO 裁剪从未触发
- **但问题在于：PPO clip 只约束单步，无 KL penalty 导致累积漂移不受限**

### 优先级 4: 根因分析 + 修复方案

**根因：format reward hacking + 无 KL 约束**

训练轨迹：
1. Step 5-15: 模型学格式 (0.55→0.85)，mean_length 仍 600+
2. Step 15-65: 模型发现**短输出+正确 JSON 格式**即可拿 format≈1.0，mean_length 从 600 压缩到 112
3. Step 65-80: CED 持续衰减 (0.76→0.35)，F1 归零 (0.005→0.001)，frac_zero_std 从 6%→29% (越来越多样本 reward 方差=0，GRPO 无法学习)

模型本质上学会了输出格式完美但内容空洞的短 JSON，靠 format_reward≈1.0 吃饱。

**属于情况 C (无 checkpoint) + 情况 B (cliprange 正常但 collapse)**。需从 SFT 重跑。

**修复方案（按重要性排序）：**

1. **加 KL penalty**: `GRPOConfig` 加 `kl_coef=0.05`，约束策略不要偏离 reference 太远
2. **加 `save_steps=20`**: 替换 `save_strategy="epoch"`，保留中间 checkpoint
3. **降低 format reward 权重或上限**: format_reward 贡献占 total reward 的 60-70%，主导了优化方向。选项：
   - reward 加权：format×0.3 + f1×1.0 + ced×1.0
   - 或 format 用 binary gate（格式合格则不额外奖励）
4. **降 lr**: 5e-5 → 2e-5，减缓漂移速度
5. **减 num_generations**: 降低 reward variance（次要）

**是否现在 kill 训练？** 鉴于 F1 已归零且无 checkpoint，继续跑没有价值。确认后我执行 kill。

---
