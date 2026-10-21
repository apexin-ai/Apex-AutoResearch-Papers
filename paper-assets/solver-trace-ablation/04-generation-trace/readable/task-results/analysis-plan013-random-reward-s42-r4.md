# analysis plan013 random reward s42 r4

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan013-random-reward-s42-r4_20260514T022117_result.json`
- **Structured JSON:** [`8931d64293304b26ad29.json`](../../sessions/89/8931d64293304b26ad29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## plan013-random-reward-s42-r4 分析总结

### 核心指标

| 指标 | plan013 (random reward) | plan001 (exec-only) | plan005 (real STA) |
|------|------------------------|--------------------|--------------------|
| last100 PR | **0.9663** | 0.865 | 0.7725 |
| last100 ISR | **0.9663** | 0.8612 | 0.2299 |
| ISR/PR ratio | **1.000** | ~1.0 | 0.298 |
| ISR < PR 次数 (last100) | **0/100** | — | 99/100 |
| ISR-PR 相关性 | **0.994** | ~1.0 | 低 |

### 训练趋势 (100-step windows)

| 窗口 | plan013 PR | plan013 ISR | plan001 PR | plan005 PR |
|------|-----------|-------------|-----------|-----------|
| 1-100 | 0.136 | 0.130 | 0.185* | 0.178 |
| 101-200 | 0.415 | 0.410 | 0.663 | 0.506 |
| 201-300 | 0.899 | 0.894 | 0.784 | 0.671 |
| 301-400 | 0.958 | 0.953 | 0.849 | 0.701 |
| 401-500 | 0.966 | 0.966 | 0.865 | 0.773 |

### 关键结论

1. **prove_rate**：random reward (0.966) 显著高于 exec-only (0.865) 和 real-STA (0.773)。随机噪声作为第二目标反而提升了 PR，可能因为额外 exploration signal 防止了过早收敛。

2. **ISR 行为**：random reward 下 ISR 完全跟随 PR（ratio=1.000，相关性 0.994），与 exec-only 一致。这与 real-STA 的持续分离（ratio=0.298）形成鲜明对比。

3. **核心发现**：real STA (plan005) 是唯一导致 ISR/PR 分离的配置。random reward 不产生分离，说明 **ISR 的结构化信号是 specific 的**——不是任意第二目标的 multi-objective regularization 效果，而是 ISR 评估的结构质量确实对训练施加了有方向性的约束。plan005 中 ISR 被压低到 0.23 而 PR 仍在 0.77，说明 real STA 迫使模型在"能证对"和"结构好"之间做权衡。

4. **Conclusion = success**：random reward baseline 验证了 ISR signal 的特异性。

---
