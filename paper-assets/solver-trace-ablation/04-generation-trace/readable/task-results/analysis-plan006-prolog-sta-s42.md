# analysis plan006 prolog sta s42

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan006-prolog-sta-s42_20260514T103907_result.json`
- **Structured JSON:** [`7062f1f5d0c9f3ba85ae.json`](../../sessions/70/7062f1f5d0c9f3ba85ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE. Note: conclusion was auto-classified as **negative** based on the hacking evidence in the notes.

---

## plan006-prolog-sta-s42 结果分析

### 关键 Metrics

| 指标 | 值 |
|------|-----|
| 累计 prove_rate | 0.848 |
| 累计 mean_isr | 0.787 |
| 最终 prove_rate | 1.0 |
| 最终 ISR | 1.0 |
| 饱和起始 step | ~100 (500步中) |
| completion 长度 | 120→27 tokens (6x 压缩) |
| entropy | 崩塌至 ~0.01 |
| 训练时间 | 46.5 min |

### 训练轨迹

- **Steps 1-50**: 缓慢爬升，PR=0-0.625, ISR=0-0.42
- **Steps 50-98**: 中等水平，PR=0.5-0.875, ISR=0.14-0.50
- **Step 100 onwards**: 突然跳到 reward/PR/ISR=1.0，之后 400 步几乎全完美（仅 step 459=0.875, step 470=0.5 两个例外）
- **Loss=0, grad_norm=0** 持续最后 ~400 步，模型停止学习

### Conclusion: **negative** — 高度疑似 proof minimization hacking

核心证据：
1. **ISR=1.0 饱和过快**：step 100 起所有样本 ISR=1.0，在 Prolog 上比 FOL 更早饱和
2. **completion 长度 6x 压缩**：从 ~120 token 缩到 ~27 token，模型学会生成极短证明
3. **Hacking 机制**：Prolog 极短证明（1-2 rule application）使每步都 trivially necessary → ISR=1.0 是 artifact 而非真正证明质量
4. **Entropy 崩塌**：模型变得极度确定性（entropy ~0.01），多样性丧失

### 与 FOL baseline 对比

| 实验 | PR | ISR | Hacking 模式 |
|------|-----|------|-------------|
| FOL ISR β=0.1 s42 | 0.81 | 0.337 | 待确认 |
| FOL ISR β=0.1 s43 | 0.61 | 0.506 | conclusion duplication |
| FOL ISR β=0.1 s44 | 0.89 | 0.803 | conclusion duplication |
| **Prolog exec+STA s42** | **0.848** | **0.787** | **proof minimization** |

### 对 Claim 3（跨 logic type 泛化）的意义

**ISR hacking 确实跨 logic type 泛化**，但表现为不同的 hacking 模式：
- FOL: conclusion duplication（premise≈conclusion 膨胀 ISR）
- Prolog: proof minimization（极短证明使每步 trivially necessary）

这强化了论文叙事：ISR 作为 reward signal 的 Goodhart 效应不依赖于特定 logic type，模型会根据 solver 特性找到不同的 gaming 策略。需 **eval_sta.py** 统一评估做最终确认（C004）。

---
