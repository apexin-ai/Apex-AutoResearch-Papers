# eval s45r2 then submit 8b isr

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_s45r2-then-submit-8b-isr_20260516T092247_result.json`
- **Structured JSON:** [`0b7e60b8d4d7d784bcfa.json`](../../sessions/0b/0b7e60b8d4d7d784bcfa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

## 产出汇总

### 1. s45-r2 Eval 结果
| 指标 | 值 |
|------|-----|
| Prove rate | 99/100 (99.0%) |
| Mean ISR | 0.5012 ± 0.2055 |
| Median ISR | 0.5000 |

**Taxonomy (C013 标准):**
| 类别 | 数量 | 占比 |
|------|------|------|
| H7a (text-match tautology) | 93 | 93.9% |
| H1 (conclusion in premises) | 5 | 5.1% |
| H8 (conj-collapse) | 1 | 1.0% |
| **Genuine** | **1** | **1.0%** |

### 2. s45-r2 Train Metrics (后 500 步)
- prove_rate: final=1.0, mean=0.7402
- isr_mean: final=0.5, mean=0.3596
- reward_mean: final=1.0, mean=0.7402
- 首次 prove_rate=1.0: step offset 95

### 3. 8B ISR β=0.1 Pilot
- **Status**: 已启动，GPU 1 占用 49767 MiB (正常)
- **PID**: 798398
- **Session**: `w2-qwen3-8b-isr-pilot`
- **Model**: Qwen3-8B, 500 steps, num_generations=4
- **Log**: `~/runs/solver-trace-ablation/w2-qwen3-8b-isr-pilot.log`

### 4. 注意事项
s45-r2 genuine 只有 1%——和其他 exec-only seeds 一致，collapse 严重 (93.9% H7a)。8B pilot 正在跑第一步，无 OOM。

---
