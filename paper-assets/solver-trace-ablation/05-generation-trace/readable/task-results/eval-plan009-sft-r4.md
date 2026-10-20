# eval plan009 sft r4

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan009-sft-r4_20260514T133910_result.json`
- **Structured JSON:** [`eb550635d26426b3028b.json`](../../sessions/eb/eb550635d26426b3028b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。完整分析报告如下。

---

## Plan009 SFT Baseline 评估报告

### 实验配置
- **模型**: Qwen3-4B, SFT 500 steps, seed=42
- **训练数据**: data/train_500_seed42.jsonl (500 samples)
- **评估数据**: data/proofwriter_fol_100.jsonl (100 samples)
- **Checkpoint**: `/root/autodl-tmp/outputs/plan009_sft_baseline_s42/checkpoint-500`
- **训练日志**: `~/runs/solver-trace-ablation/plan009-sft-baseline-s42-r4.log`
- **评估结果**: `/root/autodl-tmp/outputs/plan009_sft_baseline_s42/eval_results.json`

### 训练指标
| 指标 | 值 |
|------|-----|
| Final loss | 0.0287 |
| Token accuracy | 99.35% |
| Epoch | 7.94 |
| Training time | 789.6s (13.2 min) |

### 评估指标

| 指标 | SFT baseline | Base (zero-shot) | GRPO exec-only | GRPO ISR β=0.1 |
|------|-------------|------------------|----------------|----------------|
| **Prove Rate** | **0.14** | 0.12 | 0.93 | 0.81 |
| **Mean ISR** | **0.080** | 0.064 | 0.123 | 0.337 |
| ISR Std | 0.214 | — | — | — |
| Median ISR | 0.0 | — | — | — |
| **Proved-only ISR** | **0.571** | — | ~0.132† | — |
| Max ISR | 0.833 | — | — | — |

†推算值：mean_isr(0.123) / prove_rate(0.93) ≈ 0.132

### By answer type 分解

| Type | Count | Proved | PR | Mean ISR |
|------|-------|--------|------|----------|
| true | 34 | 13 | 38.2% | 0.226 |
| unknown | 41 | 1 | 2.4% | 0.008 |
| false | 25 | 0 | 0.0% | 0.000 |

### 关键发现

**1. SFT 对 prove rate 几乎无提升**

PR: 0.12 (base) → 0.14 (SFT) → 0.93 (GRPO exec-only)。SFT 仅提升 2 个百分点，而 GRPO 提升 81 个百分点。这证实 prove rate 的大幅跃升来自 RL reward signal，不是训练数据曝光。

**2. SFT 无 hacking 模式**

- 无 ISR=1.0 的 tautological collapse
- Max ISR = 0.833，分布合理
- Proved-only ISR = 0.571 — 当 SFT 成功证明时，57% 的组件是必要的，说明形式化质量健康

**3. GRPO exec-only 呈现明显 padding 行为**

对比 proved-only ISR：
- SFT: 0.571（proved 时大部分组件必要）
- GRPO exec-only: ~0.132（proved 时仅 13% 组件必要）

GRPO exec-only 模型大幅提升 PR 但代价是加入大量冗余组件（不影响正确性但不必要），表明模型学会了"安全padding"策略来最大化 exec reward。

**4. SFT 存在严重的 answer type 偏斜**

只能证明 "true" 类问题（38.2%），完全不能处理 "false"（0%）和 "unknown"（2.4%）。这说明 SFT 学到的是浅层的"肯定确认"模式，不是真正的逻辑推理。

### 对论文 story 的影响

这是审稿人要求的关键对照实验，结论清晰：

1. **Hacking 是 RL-reward-specific，不是 finetuning 通用问题**。SFT 不 hack（proved-only ISR = 0.571），GRPO exec-only 表现出 padding（proved-only ISR = 0.132）。这支持论文的核心论点：exec-only reward 导致 Goodhart 效应。

2. **SFT 作为 "data exposure" 控制组**。PR 从 0.12 到 0.14 的微弱提升证明：模型看到训练数据本身不足以学会 FOL 形式化，RL 的探索-利用循环是关键。

3. **SFT 的 answer type 偏斜是有价值的补充发现**。可用于论文讨论"为什么 RL 比 SFT 更有效"——SFT 只学到表面模式（偏向 true），RL 通过 solver feedback 学到了更通用的形式化策略。

---
