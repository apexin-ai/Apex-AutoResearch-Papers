# analysis qwen theta fixed consistent

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen-theta-fixed-consistent_20260521T171114_result.json`
- **Structured JSON:** [`bedb0633d67a13c3980c.json`](../../sessions/be/bedb0633d67a13c3980c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

### 验证
- free-θ lz(s1) = **8.0101**，与 registry 完全一致 ✓
- 使用的是 `compute_lz_drasgow`（Drasgow 1985，无 Snijders 校正），即 `theta_fixed_lzstar.py` 中的同源函数

### θ_fixed = -0.1022（10 个 clean seeds 的 mean θ_MLE）

### Table: Qwen MMLU θ-fixed (registry-consistent)

| Condition | θ_MLE | lz_free (registry) | lz_fixed |
|-----------|-------|---------------------|----------|
| clean_s1 | -0.0987 | 8.010 | 8.114 |
| clean_s2 | -0.0842 | 5.944 | 6.459 |
| clean_s3 | -0.1068 | 8.081 | 7.947 |
| clean_s4 | -0.1092 | 7.609 | 7.407 |
| clean_s5 | -0.0875 | 7.196 | 7.621 |
| clean_s6 | -0.1036 | 6.985 | 6.946 |
| clean_s7 | -0.0892 | 7.400 | 7.777 |
| clean_s8 | -0.1035 | 7.719 | 7.682 |
| clean_s9 | -0.1242 | 7.680 | 7.032 |
| clean_s10 | -0.1156 | 6.927 | 6.537 |
| **contam_15** | **0.1971** | **3.005** | **10.120** |
| **contam_50** | **0.3703** | **5.448** | **15.778** |

### Cohen's d + 95% Bootstrap CI

| Metric | d(15%) | 95% CI | d(50%) | 95% CI |
|--------|--------|--------|--------|--------|
| lz_fixed | -5.27 | [-7.79, -3.97] | -16.09 | [-24.79, -12.10] |
| lz_free | 8.38 | [4.75, 15.65] | 3.71 | [1.89, 7.29] |

### 关键发现
- **θ-fixed 恢复了 dose-response 单调性**：|d(50%)| = 16.09 > |d(15%)| = 5.27，ratio ≈ 3.1×
- free-θ 下 dose-response 反转（d(50%) = 3.71 < d(15%) = 8.38），因为 θ 膨胀部分吸收了 contamination 信号
- θ-fixed 时 contam 的 lz **升高**（10.12, 15.78 vs clean 均值 7.35），因为固定 θ 后 response pattern 偏离更大

结果已保存到 `/root/autodl-tmp/qwen_theta_fixed_consistent.json`。

---
