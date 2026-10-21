# analysis exp1 isr b03 s42 1000 r2 eval

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp1-isr-b03-s42-1000-r2-eval_20260515T113427_result.json`
- **Structured JSON:** [`c5ed7270b0a1af22e49d.json`](../../sessions/c5/c5ed7270b0a1af22e49d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。结果汇总：

## exp1-isr-b03-s42-1000-r2 (ISR β=0.3, 1000步, seed42)

| 指标 | 值 |
|------|-----|
| **prove_rate** | 0.95 (95/100) |
| **mean_isr** | 0.734 |
| **H7** | 0 (0%) |
| **H1** | 54 (56.8%) |
| **genuine** | 41 (43.2%) |
| **ISR=1.0** | 41 (43.2%) |
| **tautological_collapse** | false |
| **by_answer_type** | 34 true / 25 false / 41 unknown ✓ |

### 与 500 步 ISR β=0.3 (exp1-isr-b03-s43-r3) 对比

| 指标 | 500步 s43 | 1000步 s42 | 变化 |
|------|-----------|------------|------|
| PR | 0.86 | 0.95 | +9pp |
| mean_isr | 0.254 | 0.734 | +0.48 |
| H7 | 4 (4.7%) | 0 (0%) | ↓ |
| H1 | 59 (68.6%) | 54 (56.8%) | ↓ |
| genuine | 23 (26.7%) | 41 (43.2%) | +16.5pp |

**注意**：seed 不同（s42 vs s43），对比有 confound。

**结论改为 success**：原 registry 中 h7=41/genuine=0 是错误数据（可能把 ISR=1.0 count 误标为 H7）。实际 H7=0，genuine=41（43.2%），是所有 ISR β=0.3 实验中最高的 genuine rate。mean_isr=0.734 偏高（潜在 Goodhart），但 genuine 绝对数量和比例均有提升，H1 也略降。

---
