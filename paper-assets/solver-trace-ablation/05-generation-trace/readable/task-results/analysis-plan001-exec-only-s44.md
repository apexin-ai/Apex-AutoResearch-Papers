# analysis plan001 exec only s44

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan001-exec-only-s44_20260514T050751_result.json`
- **Structured JSON:** [`603b1e552ab46c1767c3.json`](../../sessions/60/603b1e552ab46c1767c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan001-exec-only-s44 结果报告

### 1. 训练状态
正常完成 500/500 步，EXIT_CODE=0，训练耗时 36m50s。

### 2. 训练指标轨迹

| Window | PR | ISR | n |
|--------|------|------|---|
| Steps 1-50 | 0.095 | 0.048 | 50 |
| Steps 51-100 | 0.320 | 0.112 | 50 |
| Steps 101-200 | 0.778 | 0.329 | 100 |
| Steps 201-300 | 0.975 | 0.562 | 100 |
| Steps 301-400 | 0.983 | 0.567 | 100 |
| Steps 401-500 | 0.999 | 0.561 | 100 |

- **Last100**: PR=0.9988, ISR=0.5611, loss=0.000419
- Steps PR≥0.85: 352/500（first at step 80）

### 3. eval_sta.py 结果（统一评估）

| 指标 | 值 |
|------|-----|
| prove_rate | **97%** (97/100) |
| mean_isr | **0.550** ± 0.195 |
| median_isr | 0.500 |
| proved_only_isr | 0.567 |
| by type: false | 25/25, ISR=0.620 |
| by type: unknown | 40/41, ISR=0.524 |
| by type: true | 32/34, ISR=0.529 |

### 4. 跨 seed 对比

| Seed | eval PR | eval mean_ISR | proved_only_ISR | 判定 |
|------|---------|---------------|-----------------|------|
| s42 | 93% | 0.1232 | — | 成功（高PR低ISR） |
| s43-r4 | 14% | 0 | — | 失败（退化） |
| **s44** | **97%** | **0.550** | **0.567** | **成功（最好）** |

**s44 明显属于成功 seed**，更像 s42 而非 s43。PR 甚至超过 s42（97% vs 93%）。ISR 显著高于 s42（0.55 vs 0.12），但需注意 exec-only 模型的形式化普遍退化为 trivial pattern（Premises: P, Conclusion: P），ISR≈0.5 是这种 trivial 形式化的预期值（2 components 中 1 个 necessary）。

### 5. 路径确认
- checkpoint: `/root/autodl-tmp/outputs/plan001_exec_only_s44`
- train log: `~/runs/solver-trace-ablation/plan001-exec-only-s44.log`
- eval result: `/root/autodl-tmp/outputs/eval_sta_plan001_exec_only_s44.json`
- reward log: `/root/autodl-tmp/outputs/plan001_exec_only_s44/reward_log.jsonl`

---
