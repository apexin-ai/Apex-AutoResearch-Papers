# analysis exp003 bootstrap ci

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp003_bootstrap_ci_20260516T023635_result.json`
- **Structured JSON:** [`09ab75eba84613d832ab.json`](../../sessions/09/09ab75eba84613d832ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W4 任务完成。总结：

**脚本**: `scripts/exp003_bootstrap_ci.py` 在远程服务器运行完毕（10K bootstrap + 10K permutation, 耗时 ~27 分钟）

**输出**: `artifacts/exp003_bootstrap_ci.json`，4 config × 5 pairs = 20 条目

**关键结果**:

| Config | 2v3 AUC | 95% CI | CI upper vs θ=0.60 |
|--------|---------|--------|---------------------|
| config1_greedy | 0.5612 | [0.5517, 0.5705] | 远低于 θ |
| **config2_nuc09** | **0.5917** | **[0.5824, 0.6010]** | **跨过 θ** |
| config3_t07 | 0.5901 | [0.5806, 0.5996] | 差 0.04pp |
| config4_t12 | 0.5820 | [0.5722, 0.5917] | 远低于 θ |

- **config2_nuc09 的 2v3 CI 上界 0.6010 跨过 θ=0.60**，K*=2 在该 config 下存在边界模糊性
- config3_t07 的 CI 上界 0.5996 极接近但未跨过
- 所有 config 的 0v1 和 1v2 permutation p=0（10K 次中零次超过观测值），K*≥2 判定稳健
- config2 的 4v5 perm_p=0.12，不显著（接近 chance）

Artifact 已注册，registry 已更新。

---
