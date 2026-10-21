# eval plan017 eval sta

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan017-eval-sta_20260514T051825_result.json`
- **Structured JSON:** [`138a5897cdc006e6c6b3.json`](../../sessions/13/138a5897cdc006e6c6b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据完整。以下是最终结果。

---

## 1. plan017 完整 eval 指标

| 指标 | 值 |
|------|-----|
| n_problems | 100 |
| n_proved | 48 |
| **prove_rate** | **0.48** |
| **mean_isr** | **0.0453** |
| isr_std | 0.0759 |
| median_isr | 0.0 |
| max_isr | 0.2857 |
| proved_only_mean_isr | 0.0943 |
| isr_pr_ratio | 0.0943 |
| component_count_mean (proved) | **~9.6** |
| 2-component ratio | **0%** |
| elapsed | 542.3s (5.4s/sample) |
| by_type: false | n=25, proved=8 (32%), ISR=0.0254 |
| by_type: unknown | n=41, proved=21 (51%), ISR=0.0518 |
| by_type: true | n=34, proved=19 (56%), ISR=0.0520 |

## 2. Tautological Collapse 判断

**plan017 没有 tautological collapse。** n_components 范围 4-18，均值 9.6，零个 2-component proof。与 plan013（96% 2-component）完全不同。exec 信号作为主奖励有效阻止了坍缩。

## 3. 对比表

| 指标 | plan001-s42 (exec-only) | plan017 (add random β=0.3) | plan002 (add ISR β=0.3) | plan013 (pure random) |
|------|:-:|:-:|:-:|:-:|
| **reward** | r_exec | r_exec·(1+0.3·rand) | r_exec·(1+0.3·ISR) | random |
| **prove_rate** | **0.93** | 0.48 | 0.18 | 1.00 |
| **mean_isr** | **0.1232** | 0.0453 | 0.0257 | 0.535* |
| isr_std | 0.1887 | 0.0759 | 0.0742 | 0.1282* |
| median_isr | 0.0 | 0.0 | 0.0 | 0.5* |
| proved_only_ISR | 0.1324 | 0.0943 | 0.1427 | 0.535* |
| component_mean | ~7.1 | ~9.6 | ~10.7 | ~2.0* |
| 2-comp ratio | 0% | 0% | 0% | ~96%* |
| **collapsed?** | **No** | **No** | **No** | **YES** |

\* plan013 指标因 tautological collapse 无意义（ISR 高是假象）

## 4. Hypothesis 结论

**exec-only >> additive random > additive ISR >> pure random (collapsed)**

核心发现：
- **additive random (plan017) 没有坍缩**，但 prove_rate 从 0.93 降至 0.48（-48%）——随机噪声作为 reward perturbation 显著伤害了证明能力
- **additive ISR (plan002) 比 additive random 更差**：prove_rate 0.18 vs 0.48。ISR 信号不仅没有提供有用的结构指导，反而比纯随机噪声更具破坏性
- **proved_only ISR 对比**：plan002 (0.1427) > plan001 (0.1324) > plan017 (0.0943)——plan002 在少数成功证明中 ISR 稍高，但代价是丧失了 80%+ 的证明能力
- **ISR ≈ random 的假设不成立**：ISR 信号明确比 random 更差（0.18 vs 0.48 prove_rate），这意味着 ISR additive reward 是 actively misleading，不仅仅是 noisy

**结论：ISR 作为 additive reward 信号是反生产力的。exec-only baseline 仍然是最优策略。任何 additive perturbation（无论是 ISR 还是 random）都伤害 prove_rate，且 ISR 的伤害大于 random。**

---
