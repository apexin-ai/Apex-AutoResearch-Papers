# monitor factorial step3plus

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_factorial_step3plus_20260518T000857_result.json`
- **Structured JSON:** [`9b2f746564529d3b81a2.json`](../../sessions/9b/9b2f746564529d3b81a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整，已获取 step 0-4。进程仍在运行（step 5 正在 rollout）。

## 结果汇总

| Step | Train Success | Pass@8 | Action Valid | Entropy | KL Loss | Grad Norm | PG Loss |
|------|--------------|--------|-------------|---------|---------|-----------|---------|
| 0 (val) | 2.24% (OOD) | — | 37.8% | — | — | — | — |
| 1 | **20.31%** | 68.75% | 85.64% | 0.359 | 0.238 | 18.27 | 0.0121 |
| 2 | 6.25% | 31.25% | 83.96% | 0.569 | 0.208 | 14.73 | 0.0118 |
| 3 | 5.47% | 31.25% | 79.54% | 0.567 | **1.077** | 12.73 | 0.0126 |
| 4 | **3.13%** | **18.75%** | 83.70% | 0.617 | 0.638 | 11.33 | 0.0114 |

## 判断：场景 B（持续下降/训练崩溃）

关键证据：
1. **Success 单调下降**：20.3% → 6.25% → 5.47% → 3.13%，没有任何回升迹象
2. **Pass@8 同步恶化**：68.75% → 31.25% → 31.25% → 18.75%，表明即使 best-of-8 也在退化
3. **KL loss 在 step 3 异常飙升**（1.077 vs 正常 0.2），说明 policy 一度剧烈偏移 reference
4. **Entropy 增加**（0.359 → 0.617）但 success 下降：模型变得更随机但更差，不是在探索有用行为
5. **Grad norm 递减**（18.3 → 11.3）：有效学习信号在枯竭

结论：episode-level advantage 在 h=2 multi-step 设置下未能正确归因 reward 到各 step。step 1 高 success 可能只是初始 policy 质量，之后 PPO 更新方向错误导致持续退化。这排除了 sign misattribution 作为唯一原因（场景 A 预期 step 3+ 回升），问题更可能是 episode-level advantage 本身的 credit assignment 失败。

---
