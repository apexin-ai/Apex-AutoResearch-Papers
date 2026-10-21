# analysis 016e collapse deep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_016e-collapse-deep_20260515T222551_result.json`
- **Structured JSON:** [`569de6f5a0c87be22459.json`](../../sessions/56/569de6f5a0c87be22459.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新（status=DONE, conclusion=negative）。

## 核心发现

**016e vs 008d 逐步对比表：**

| Step | 016e eval | 008d eval | 016e value | 008d value | 016e entropy | 008d entropy |
|------|-----------|-----------|------------|------------|-------------|-------------|
| 5K   | 31        | 31        | 0.001      | 0.001      | 8.16        | 8.16        |
| 15K  | 140       | 154       | 3.1        | 3.4        | 1.05        | 0.48        |
| 25K  | 142       | 167       | 23.0       | 25.9       | -1.55       | -1.86       |
| 35K  | 173       | 146↓      | 53.5       | 60.2       | -2.12       | **-3.47**   |
| 45K  | 184       | 141↓      | 85.3       | 97.5       | -3.46       | -4.58       |
| 55K  | 154       | **83↓↓**  | 115.6      | 137.9      | -3.62       | -4.88       |
| 65K  | **324↑↑** | —         | 152.3      | —          | -4.55       | —           |
| 75K  | **327**   | —         | 190.0      | —          | -4.06       | —           |
| 85K  | 256↓      | —         | 215.4      | —          | -3.83       | —           |
| 95K  | **32↓↓↓** | —         | 208.9      | —          | -4.65       | —           |

**5 个关键结论：**

1. **Onset 差 ~50K steps**：008d 从 25K 开始衰退，016e 一直稳定到 75K peak 后才崩
2. **SGS 核心机制是保留 entropy**：35K 时 016e entropy 比 008d 高 1.35 nats（-2.12 vs -3.47），探索更充分 → 2x 更高的 peak（327 vs 167）
3. **Actor loss sign flip 是崩溃标志**：016e 在 95K 翻正（+0.014），value critic 开始把 actor 推向更差动作。008d 从未翻正
4. **Value 完全脱钩**：016e@95K value=209 但 eval=32，value function 处于"完全幻觉"状态（disconnect ratio 6.58x vs 008d 的 1.67x）
5. **SGS 治标不治本**：延迟了 CIVO 发作但让积累的 value overestimation 更高（215 vs 138），崩溃更惨烈（NVE 10.42x vs 4.12x）。Gate 始终锁死在 dt=2，SGS 未解锁时间抽象。CIVO 根因是 value dynamics，非 reward-head 梯度污染

---
