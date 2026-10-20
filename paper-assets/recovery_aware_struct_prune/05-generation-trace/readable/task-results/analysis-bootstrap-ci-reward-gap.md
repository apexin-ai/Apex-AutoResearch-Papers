# analysis bootstrap ci reward gap

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap_ci_reward_gap_20260519T030900_result.json`
- **Structured JSON:** [`1628a4e54af282da2f2c.json`](../../sessions/16/1628a4e54af282da2f2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| Pair | Mean Gap | 95% CI | n | Sig? |
|---|---|---|---|---|
| CKA-only vs Random | +0.114 | [0.088, 0.145] | 9 | **YES** |
| CKA-only vs Standard | +0.235 | [0.200, 0.272] | 10 | **YES** |
| CKA-only vs RASP | +0.254 | [0.229, 0.281] | 10 | **YES** |
| Random vs Standard | +0.115 | [0.096, 0.134] | 9 | **YES** |
| Random vs RASP | +0.131 | [0.122, 0.141] | 9 | **YES** |
| Standard vs RASP | +0.019 | [-0.000, 0.036] | 10 | NO |

方法均值：CKA-only 0.2845 > Random 0.1642 > Standard 0.0494 > RASP 0.0306

5/6 pair 显著，唯一不显著的是 Standard vs RASP（两者均 collapsed，CI 下界刚好碰到 0）。

数据来源说明：每 10 步记录一次 reward mean，CKA-only/Standard/RASP 各 10 个点（steps 10-100），Random 9 个点（训练在 step 97 超时终止）。

文件已保存至本地 `artifacts/bootstrap_ci_results.json` 和 `artifacts/bootstrap_ci_plot.png`，远端脚本在 `/root/recovery_aware_struct_prune/src/bootstrap_ci_analysis.py`。

---
