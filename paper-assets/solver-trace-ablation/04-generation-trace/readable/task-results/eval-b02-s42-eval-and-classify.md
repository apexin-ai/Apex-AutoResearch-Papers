# eval b02 s42 eval and classify

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_b02-s42-eval-and-classify_20260516T045643_result.json`
- **Structured JSON:** [`8f588476f4f104f179bb.json`](../../sessions/8f/8f588476f4f104f179bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是结构化报告。

---

## sweep-isr-b02-s42 Eval 结果

### Eval Metrics (eval_sta.py, proofwriter_fol_100.jsonl)

| 指标 | 值 |
|---|---|
| prove_rate | **100%** (100/100) |
| mean_isr | **0.602** |
| median_isr | 0.500 |
| isr_std | 0.197 |
| isr_range | [0.333, 1.000] |
| ISR=1.0 | 18% |

### Hacking Taxonomy (classify_h7.py)

| 类别 | 数量 | 占比 |
|---|---|---|
| H7a (text-match tautology) | 100 | **100%** |
| H7b (obfuscated tautology) | 0 | 0% |
| H1 (conclusion embedding) | 0 | 0% |
| H8 (conjunction collapse) | 0 | 0% |
| **Genuine** | **0** | **0%** |
| Content-independent predicates | 99 | 99% |
| Single premise | 100 | 100% |

### 剂量响应对比表

| β | prove_rate | mean_isr | genuine% | dominant hack | 行为模式 |
|---|---|---|---|---|---|
| 0.05 | 92% | 0.749 | ~36% | H7a ~50% | 高 ISR 但有部分 genuine |
| **0.20** | **100%** | **0.602** | **0%** | **H7a 100%** | **完全 tautology hacking** |
| 0.30 | 100% | ~0 | 0% | ISR 崩塌 | 完全退化 |

### 关键发现

β=0.2 呈现一个极端 Goodhart 效应点：模型学会了 100% 单前提 tautology 策略（将结论作为唯一前提），在形式上维持 ISR≈0.5（删掉唯一前提就证不了），但 **genuine=0**。这与 β=0.05（部分 genuine 存活）和 β=0.3（ISR 直接崩塌到 0）形成了清晰的三阶段剂量响应：

- β=0.05: ISR bonus 不够强，策略多样化，genuine 存活
- β=0.20: ISR bonus 足够强驱动 hacking，但 ISR 本身不崩塌（tautology 维持 ISR=0.5）
- β=0.30: ISR bonus 过强，policy 过度优化到 ISR→0 的退化模式

---
