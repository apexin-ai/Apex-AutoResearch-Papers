# analysis phase1 r4 results

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase1-r4-results_20260513T204708_result.json`
- **Structured JSON:** [`28117633b678a5b7406b.json`](../../sessions/28/28117633b678a5b7406b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是结论摘要：

---

## Phase 1 GRPO Pilot 结果：NEGATIVE

### 最终指标

| | Phase 0 Baseline | exec-only | exec+STA | Δ |
|---|---|---|---|---|
| prove_rate | 0.120 | 0.151 | 0.158 | +0.006 |
| mean_isr | 0.064 | 0.148 | 0.153 | +0.005 |

### MVP 判定：3/4 PASS，核心标准 FAIL

- **#1 ISR 可靠运行** ✅ — solver 100% 成功，~1.1s/sample
- **#2 ISR 有区分度** ✅ — GT ISR=0.559 vs base ISR=0.064
- **#3 ISR 趋势分离** ❌ — last-20 ISR 差异仅 0.016，不显著
- **#4 accuracy 无降幅** ✅ — exec+STA 反而略高 +0.6pp

### 根因

**ISR 在 GRPO 训练中退化为 prove_rate 的冗余信号**。100 步中，ISR≈prove_rate（仅 step 24 例外）。原因：unprovable samples ISR=0，provable samples 的 premises 几乎全部参与 proof → ISR≈1.0/sample。batch-level 平均后 ISR≈prove_rate。

100 步太短，模型未学会 reward hacking，ISR 的"保护"作用无从体现。

### 下一步选项
1. 延长训练到 500-1000 steps 观察 reward hacking 是否出现
2. 增大 batch_size 让 ISR 信号更细粒度
3. 人工检查 checkpoint 输出是否有 trivial formalization
4. 考虑 soft ISR（partial proof score）替代二值 ISR

已更新 registry（两个实验均标记 DONE/negative）和 memory.md。

---
