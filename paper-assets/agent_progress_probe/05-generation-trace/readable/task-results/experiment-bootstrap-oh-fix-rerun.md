# experiment bootstrap oh fix rerun

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_bootstrap-oh-fix-rerun_20260515T092522_result.json`
- **Structured JSON:** [`04ed3264a7db56d1f5b3.json`](../../sessions/04/04ed3264a7db56d1f5b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。全部结果如下：

## 产出总结

### 1. OH 轨迹加载
- **Y** — SWE 轨迹 5000 条，OH 轨迹 5000 条

### 2. Windows source 字段检测
- 无 `source` 字段。通过 `trajectory_id` 中的 `__openhands__` 标识区分。

### 3. 特征矩阵 SWE/OH 窗口数
- 总计 205,461 non-abstain windows：**SWE=54,809, OH=150,652**

### 4. Bootstrap 测试完整结果

| Test | Model A | Model B | N | F1_A | F1_B | Delta | 95% CI | p-value | Sig? |
|------|---------|---------|---|------|------|-------|--------|---------|------|
| gb_vs_mv | GB | MV | 195 | 0.7644 | 0.7184 | +0.0460 | [+0.006, +0.088] | 0.0121 | **YES** |
| gb_vs_gru_probe | GB | GRU | 132 | 0.7847 | 0.7348 | +0.0499 | [-0.016, +0.120] | 0.0698 | NO |
| rf_vs_gb | RF | GB | 195 | 0.7516 | 0.7644 | -0.0127 | [-0.037, +0.009] | 0.1360 | NO |
| twv_probe_vs_gb | TWV | GB | 132 | 0.7684 | 0.7847 | -0.0163 | [-0.067, +0.031] | 0.2536 | NO |
| twv_probe_vs_gru | TWV | GRU | 132 | 0.7684 | 0.7348 | +0.0336 | [-0.029, +0.099] | 0.1499 | NO |

### 5. GB F1 一致性
- Bootstrap: **0.7644** vs eval_canonical: **0.764** → 差距 **0.0pp**（完全一致）

### 6. RF F1 一致性
- Bootstrap: **0.7516** vs eval_canonical: **0.752** → 差距 **0.0pp**（完全一致）

---
