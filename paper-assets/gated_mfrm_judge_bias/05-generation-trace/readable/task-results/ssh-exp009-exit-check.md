# ssh exp009 exit check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp009_exit_check_20260522T233253_result.json`
- **Structured JSON:** [`c57b16e6cb8a587ceff6.json`](../../sessions/c5/c57b16e6cb8a587ceff6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-009 汇报

### 退出状态：正常完成
- 无 Traceback，无错误
- Part A 耗时 70078s (~19.5h)，Part B 耗时 10527s (~2.9h)
- 输出文件在 `/root/gated_mfrm_judge_bias/exp009/`（不是 `results/` 子目录）

### Part A: bias_slope vs ρ — **完成 (400/400 行)**

| method | ρ=0.0 | ρ=0.3 | ρ=0.6 | ρ=0.9 |
|--------|-------|-------|-------|-------|
| **sequential** bias_slope | 0.1982±0.055 | 0.1950±0.056 | 0.1910±0.057 | 0.1855±0.058 |
| **sequential** RMSE | 0.2119 | 0.2111 | 0.2094 | 0.2044 |
| **joint** bias_slope | 0.0558±0.024 | 0.0574±0.028 | 0.0595±0.030 | 0.0644±0.028 |
| **joint** RMSE | 0.1205 | 0.1229 | 0.1257 | 0.1265 |

关键发现：
- **joint 方法 bias_slope 约为 sequential 的 1/3**（~0.06 vs ~0.19），OVB 修正效果显著
- ρ 对 sequential 影响微弱（0.198→0.186，随 ρ 增大 bias 略降）
- ρ 对 joint 影响也很小但方向相反（0.056→0.064，随 ρ 增大 bias 略升）
- 两种方法的 bias_slope 对 ρ 都不敏感，符合预期——confounding correlation 不是 bias 的主要驱动因素

### Part B: c_n recovery — **完成 (2500/2500 行, 50 seeds × 50 items)**

| 指标 | 值 |
|------|-----|
| Coverage 95% | **0.7100** |
| RMSE | 0.6484 ± 0.2386 |
| Correlation | 0.8114 ± 0.2003 |

关键发现：
- Coverage 71% < 名义 95%，置信区间偏窄（under-coverage）
- Correlation 0.81 表明 c_n 排序大致可恢复，但绝对值 RMSE 较大

### 结论：**Success（实验成功完成，结果为正面）**

joint 方法在所有 ρ 水平上一致性地将 bias_slope 压低至 sequential 的 ~30%，且 c_n 可恢复（corr=0.81）。Coverage 不足是需要在论文中讨论的 limitation。

---
