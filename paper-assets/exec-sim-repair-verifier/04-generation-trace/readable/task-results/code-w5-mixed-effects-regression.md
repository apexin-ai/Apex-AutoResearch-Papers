# code w5 mixed effects regression

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w5-mixed-effects-regression_20260520T023456_result.json`
- **Structured JSON:** [`1d2f3fbe7607b9cb0e8b.json`](../../sessions/1d/1d2f3fbe7607b9cb0e8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个模型都跑通了。结果汇总：

---

## 产出总结

### 1. 脚本
- 本地：`w5_mixed_effects.py`
- 服务器：`/home/sonny/exec-sim-repair-verifier/w5_mixed_effects.py`

### 2. 数据概况
- **78,272 observations**, 25 unique problem_ids, 8 个 eval 文件
- CLS: 5 runs (Qwen s42/s456 + DeepSeek s42/s123/s456)
- CWM: 3 runs (Qwen s42 + DeepSeek s42/s123)

### 3. Dry-run 结果

**GLMM (logit scale, baseline = CLS + DeepSeek):**

| Effect | Coef | z | 
|---|---|---|
| Intercept (CLS/DeepSeek) | +2.45 | 252.6 |
| CWM vs CLS | **-1.49** | **-106.7** |
| Qwen vs DeepSeek | +0.10 | 6.0 |
| CWM:Qwen interaction | +0.06 | 2.3 |

**LPM (probability scale, with p-values):**

| Effect | Coef | p |
|---|---|---|
| CWM vs CLS | **-0.221** | **<0.001** |
| Qwen vs DeepSeek | +0.011 | 0.002 |
| CWM:Qwen | +0.016 | 0.006 |
| Random (problem_id) var | 0.035 | — |

核心结论：formulation (CLS vs CWM) 是最强主效应，CWM 比 CLS 低约 22pp；model 效应显著但小（~1pp）；交互项显著（CWM 在 Qwen 上衰减略少）。

### 4. 缺失数据/待填路径

| 数据 | 状态 |
|---|---|
| Qwen CLS s123 | 缺少 repo-level test predictions |
| Qwen CWM s123 | 缺少 repo-level test predictions |
| **TRAJ 全部** | 只有 summary JSON (48 问题)，无 per-sample predictions；且 TRAJ 是 problem-level (48) vs CLS/CWM 的 test-case-level (9784)，粒度不同 |
| DeepSeek TRAJ repo | 未做 repo-level TRAJ eval |

要加入 TRAJ，需要：(a) 重跑 TRAJ eval 保存 per-sample predictions，(b) 决定是在 problem-level 聚合分析还是排除 TRAJ。

---
