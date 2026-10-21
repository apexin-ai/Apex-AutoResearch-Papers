# eval check and evaluate all

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check-and-evaluate-all_20260514T213122_result.json`
- **Structured JSON:** [`33ba6048bd58edb49d91.json`](../../sessions/33/33ba6048bd58edb49d91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三组完整结果如下：

## 训练最终状态

| 条件 | 状态 | train_loss | eval_loss | eval_mean_token_accuracy | 耗时 |
|------|------|-----------|-----------|--------------------------|------|
| vota | EXIT_CODE=0 ✓ | 0.046 | 0.085 | 0.983 | 2h17m |
| full_trace | EXIT_CODE=0 ✓ | 0.037 | 0.084 | 0.984 | 2h11m |

## 三组评估对比 (n=1190)

| 条件 | Accuracy | Lift over majority | Lift 95% CI | fail_F1 | pass_F1 |
|------|----------|-------------------|-------------|---------|---------|
| no_trace | 75.1% | +3.6pp | [+0.4, +7.1] | 0.63 | 0.81 |
| **vota** | **99.2%** | **+27.6pp** | **[+25.2, +30.2]** | **0.99** | **0.99** |
| full_trace | 28.4% | -43.1pp | [-47.4, -38.6] | 0.57 | 0.16 |

## 条件间差值

| 对比 | Accuracy Δ | fail_F1 Δ |
|------|-----------|-----------|
| vota vs no_trace | **+24.1pp** | +0.36 |
| full_trace vs no_trace | -46.7pp | -0.06 |

## MVP 判断

**VOTA: PASS** — VOTA (99.2%) 大幅超过 no_trace (75.1%)，差值 +24.1pp，远超 2pp 阈值，bootstrap 95% CI [+25.2, +30.2] 不含 0。

**full_trace: FAIL** — 28.4% 低于 majority baseline，模型几乎总是预测 "fail"（pass_recall=0.08）。原因：full_trace 输入序列长度 69413 tokens 远超模型上下文窗口 32768，被截断后丢失关键信息，模型无法正确分类。

## 产出路径
- vota: `/root/autodl-tmp/trace-verdict-study-checkpoints/vota/final/eval_results.json`
- full_trace: `/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace/final/eval_results.json`

**结论：VOTA 条件压倒性胜出。full_trace 因上下文溢出导致性能崩塌，需要截断/摘要策略才能使用完整 trace。**

---
