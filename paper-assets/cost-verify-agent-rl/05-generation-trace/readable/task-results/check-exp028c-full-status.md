# check exp028c full status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp028c_full_status_20260516T025012_result.json`
- **Structured JSON:** [`f588cb0e9b668ac1b406.json`](../../sessions/f5/f588cb0e9b668ac1b406.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp028c 训练状态报告

### 进程状态
**存活** — PID 824675，运行 5h13m，入口 `python train.py --config-name _alfworld_exp028c_selfguide_recipe`

### W&B 信息
- **entity**: `xiaoyucorynne-`
- **project**: `cost-verify-agent-rl`
- **run_id**: `4yu6qz1m`
- **run name**: `exp028c-alfworld-selfguide-recipe`
- **state**: running

### 当前进度
- W&B 已记录到 **step 4**（summary step=4, runtime=15967s ≈ 4.4h）
- Checkpoint 已保存到 **step 5**（10:04 UTC）
- 日志显示 `compute_policy_loss` 正在执行 → 当前在 step 5+ 训练中
- 总目标：100 steps

### 每 step 关键 metrics

| Step | Phase | success | pass@8/1 | action_is_valid | entropy | kl_loss | ppo_kl | grad_norm | score/mean |
|------|-------|---------|----------|-----------------|---------|---------|--------|-----------|------------|
| 0 | **val** | **6.25%** | p@1=6.25% | 74.5% | — | — | — | — | — |
| 1 | train | 13.28% | p@8=37.5% | 76.4% | 0.263 | 0.013 | 0.019 | 16.9 | 0.843 |
| 2 | train | 6.25% | p@8=25.0% | 83.2% | 0.247 | 0.171 | 0.017 | 17.3 | 0.274 |
| 3 | train | 15.62% | p@8=68.75% | 86.0% | 0.249 | 0.112 | 0.019 | 12.6 | 0.661 |
| 4 | train | 18.75% | p@8=62.5% | 87.9% | 0.234 | 0.031 | 0.015 | 14.5 | 1.146 |

### GPU 利用率
| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX PRO 6000 Blackwell | **91%** | 33.2 / 97.9 GB |
| 1 | RTX PRO 6000 Blackwell | **95%** | 33.2 / 97.9 GB |

### 趋势分析
- **action_is_valid 持续上升**：74.5% → 87.9%（+13.4pp over 4 steps）— 正面信号
- **train success 震荡上升**：6.25% → 18.75%，但 step 2 回落到 6.25%
- **pass@8 波动大**：25%-68.75%，step 3 是峰值
- **kl_loss 有一次 spike**：step 2 突然跳到 0.171（正常 ~0.01-0.03），step 3-4 回落 — 暂时异常，已自行恢复
- **entropy 缓慢下降**：0.263 → 0.234，策略在收敛但还没 collapse

### 异常
- **速度偏慢**：4 train steps 耗 ~4.4h（~66min/step），比预期 50min/step 慢约 30%。env_groups=16 × group_size=8 = 128 rollouts/step 可能是主因
- **kl_loss step 2 spike 到 0.171**：比其他步高 5-13 倍，但已恢复，不需干预
- **无 step 5 val 数据**：checkpoint 已保存但 W&B 尚未收到 step 5 metrics，可能 val 正在运行或刚完成

### 预计完成时间
按 ~66min/step、100 steps 计算：约 **110 小时 ≈ 4.6 天**。已过 ~5h 完成 ~5 steps，预计剩余 ~4.3 天（~5月20日完成）。

---
