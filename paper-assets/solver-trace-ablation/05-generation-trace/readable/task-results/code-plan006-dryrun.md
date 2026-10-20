# code plan006 dryrun

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan006-dryrun_20260514T081656_result.json`
- **Structured JSON:** [`7dcee924b9b74b2b0101.json`](../../sessions/7d/7dcee924b9b74b2b0101.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**DRYRUN PASS**

| 指标 | Step 1 | Step 2 | Step 3 |
|------|--------|--------|--------|
| reward | 0.125 | 0.000 | 0.000 |
| prove_rate | 0.125 | 0.000 | 0.000 |
| ISR | 0.018 | 0.000 | 0.000 |
| parse_rate | 1.000 | 1.000 | 1.000 |
| step_time (s) | 3.84 | 7.21 | ~7.1 |

结果分析：
- **全链路无报错**：PrologSolver → swipl 子进程 → rule ablation ISR 计算正常
- **parse_rate = 1.0**：base model 输出全部可解析（Prolog 格式解析正常）
- **prove_rate > 0**：Step 1 有 1/8 样本可证明（12.5%），符合预期（base model 不擅长 Prolog，但不是零）
- **ISR = 0.018**：rule ablation 正常工作，至少有一个样本产生了非零 ISR
- **训练速度**：~4-7s/step，比 FOL (Prover9) 快得多
- **唯一 warning**：vLLM 版本兼容性警告（0.18.1 vs 支持到 0.17.1），不影响训练

---
