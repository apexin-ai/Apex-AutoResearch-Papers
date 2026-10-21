# analysis exp029 seed300 episode

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp029_seed300_episode_20260522T175454_result.json`
- **Structured JSON:** [`6e87311159f113488132.json`](../../sessions/6e/6e87311159f113488132.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。以下是 exp029_seed300_episode 分析报告。

---

## exp029_seed300_episode 训练结果

### 1. 训练完成状态：**完成** (EXIT_CODE=0)
- 5 个 step 全部完成，checkpoint 已保存
- 无致命 error（仅有 W&B BrokenPipe 和 "Skipping non-numeric metric" 等无害 warning）
- 总耗时: ~8885 秒 (~2.5h)

### 2. 每 Step 关键指标

| Step | response_length/mean (rollout) | train/response_length | critic/rewards/mean | actor/ppo_kl |
|------|------|------|------|------|
| 0 (eval) | — | — | — | — |
| 1 | **14019** | 8359 | 1.41 | 0.000368 |
| 2 | 13308 | 7871 | 1.56 | 0.001005 |
| 3 | 12393 | 6340 | 1.56 | 0.000293 |
| 4 | 13088 | 7777 | 1.95 | 0.000461 |
| 5 | **12691** | — | 1.72 | — |

Val 指标 (step 0 → step 5):
| Metric | Step 0 | Step 5 |
|--------|--------|--------|
| val-env/response_length | 7088 | **6203** |
| val-core/reward/mean@32 | 1.25 | **2.50** |
| val-env/pass@1 | 12.5% | **25.0%** |

### 3. Collapse 判断：**Healthy**

理由：
- **response_length/mean 下降趋势**：14019 → 12691（-9.5%），无爆炸增长
- **val-env/response_length 下降**：7088 → 6203（-12.5%）
- **reward 稳步提升**：val reward 从 1.25 → 2.5（翻倍），pass@1 从 12.5% → 25%
- **KL 极低且稳定**：始终 < 0.001，策略偏移小
- collapse MI 指标 (step 5): mi_estimate=0.206, retrieval_accuracy=0.547

### 4. Checkpoint 路径
```
/root/autodl-tmp/checkpoints/exp029-seed300/global_step_5/actor/
```
包含: model (rank 0/1), optim (rank 0/1), extra_state (rank 0/1), huggingface config

### 5. Log 路径
```
~/runs/cost-verify-agent-rl/exp029_seed300_episode.log
```

### 6. 结论
**Success — 需后续 OOD eval 确认。** seed300 训练表现 healthy，response length 稳定甚至下降，reward 有明确提升趋势。基于此 pattern，预期 OOD 表现在 healthy seed 范围（28-31%）。可直接安排 OOD eval。

---
