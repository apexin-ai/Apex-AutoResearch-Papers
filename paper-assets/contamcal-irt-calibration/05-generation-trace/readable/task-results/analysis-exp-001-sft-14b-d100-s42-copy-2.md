# analysis exp 001 sft 14b d100 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_sft_14b_d100_s42_20260519T001713_result.json`
- **Structured JSON:** [`5061f2526cc0171a1bdf.json`](../../sessions/50/5061f2526cc0171a1bdf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**14B d100 训练结果：success**

核心数据：
- train_loss=0.9682, token_acc=0.7488, 4159 steps, 3h46m
- Checkpoint 已保存，`.done` sentinel 存在，EXIT_CODE=0
- 无 W&B 集成

**14B dosage sweep 全部完成** (d000/d005/d025/d050/d100)：
- Loss 随 dosage 单调递增：0.909 → 0.968
- Token accuracy 整体递减：0.776 → 0.749（d005 异常高 0.797）
- Entropy 随 dosage 单调递增：0.949 → 1.142

分析报告已写入 artifacts 并注册。下一步需要对 5 个 checkpoint 跑 eval 和 compute_signals。

---
