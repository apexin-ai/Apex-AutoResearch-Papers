# code bootstrap ci plan005

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bootstrap-ci-plan005_20260513T153228_result.json`
- **Structured JSON:** [`278226fbf03130ff1980.json`](../../sessions/27/278226fbf03130ff1980.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**C1 (FM3 rebound)**: overcorrected_pol − baseline_pol = +0.071, CI [-0.017, 0.156]。方向一致（正向 rebound），但 CI 包含 0——4 runs pooled 后接近显著。

**C2 (FM4 reversal)**: 方向一致但未达统计显著：
- Base BCP AAVE gap = −0.091 (baseline 高于 variant)
- DPO+BCP AAVE gap = +0.064 (variant 反超 baseline)
- 两个 CI 都跨 0，因 7B base 只有 1 run (n≈19-20)

**C3 (7B vs 14B completion)**: **显著**。Overall 14B−7B = +0.411, CI [0.322, 0.495]。5/6 variants 的 CI 排除 0，14B 完成率系统性高于 7B。

**C4 (H2 calibration gap)**:
- 14B AAVE/Indian gap reduction **显著** (CI > 0)：分别 +0.070 [0.003, 0.136]、+0.072 [0.007, 0.137]
- 7B 的 gap reduction CI 跨 0（样本量不足）

输出文件在服务器 `/root/democalib/results/bootstrap_ci_results.json` 和 `bootstrap_ci_report.md`，实验注册为 `bootstrap-ci-001`。

---
