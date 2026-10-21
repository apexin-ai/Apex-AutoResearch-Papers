# analyze d154 8b exec s42 k8

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_d154-8b-exec-s42-k8_20260522T063100_result.json`
- **Structured JSON:** [`3db753d6ff467725095e.json`](../../sessions/3d/3db753d6ff467725095e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结：d154-8b-exec-s42-k8

### 训练状态
**完成 500/500 步**，总耗时 1h41m（12:45→14:27 UTC）。无 OOM 或 error。

### 核心结论：训练完全失败 — 零梯度信号

整个 500 步训练中 **loss=0.0, grad_norm=0.0**，模型权重本质上没有更新。

**根因**：`frac_reward_zero_std=1.0` — 每个 batch 内所有 K=8 个 completion 获得相同 reward（全 0 或全 1），GRPO advantage=0，无梯度。8B 模型太确定性，K=8 没能增加组内 reward 方差。

### 训练指标轨迹
| 阶段 | reward | prove_rate | ISR | 特征 |
|------|--------|------------|-----|------|
| Step 1-50 | 零星非零（0.06-0.5） | 0-50% | 0-0.4 | 基础模型能力的波动 |
| Step 50-450 | 绝大多数为 0 | ~0% | ~0% | 完全 stagnation |
| Step 450-500 | 偶发 spike（476: 0.81, 488: 0.75） | 大多为 0 | ~0 | 未恢复 |

**Final reward stats**（训练结束时的评估）：parse_rate=1.0, prove_rate=0.159, mean_isr=0.083 — 基本是 base model 水平。

**train_loss=0.017**（仅来自前几步有 reward 的 batch）。

### 与 K=4v2 对比
K=8 与 K=4v2 呈现相同 stagnation 模式。增大 K 未能解决问题 — 8B 模型在 exec-only 下太确定性，所有 K 个 completion 趋同。

**Hypothesis 被否决**：Qwen3-8B exec-only 未出现 Goodhart collapse（高 prove_rate + 低 ISR），而是 complete stagnation（无学习）。

### 关键信息
| 项目 | 值 |
|------|-----|
| W&B | **无**（未集成） |
| Checkpoint | `/root/autodl-tmp/outputs/8b_exec_only_s42_k8/`（31GB） |
| 也存于 | `/root/runs/solver-trace-ablation/d154-8b-exec-s42-k8.log` |
| Registry | **无条目** |
| Eval | **未单独跑 eval** |

### 建议
这个 checkpoint 本质是 base Qwen3-8B（未经有效训练），单独跑 eval 意义不大。31GB 的 checkpoint 可以考虑清理。如需 8B exec-only 数据点，可能需要换策略（如增大 batch size、温度调参、或混合 reward）来打破 zero-variance 问题。

---
