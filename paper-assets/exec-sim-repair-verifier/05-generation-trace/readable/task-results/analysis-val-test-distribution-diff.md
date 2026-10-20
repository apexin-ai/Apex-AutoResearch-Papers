# analysis val test distribution diff

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_val-test-distribution-diff_20260514T223002_result.json`
- **Structured JSON:** [`d53a4a49f63462106325.json`](../../sessions/d5/d53a4a49f63462106325.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/val_test_distribution_analysis.md`。核心发现：

## Root Cause: 多维度严重分布偏移

**最关键的三个因素：**

### 1. Mutation Type 组成剧变
- `operator_swap`: val 19.1% → test **34.3%**（+15pp，接近翻倍）
- `off_by_one`: val 10.0% → test **1.9%**（缩减 5 倍）
- 不同 mutation type 有完全不同的检测签名，val-best checkpoint 学到的 off_by_one/return_value 检测能力在 test 上几乎无用

### 2. Problem Instance 零重叠 + Per-Problem 难度异质
- Val 22 个 problem，Test 25 个，**重叠 = 0**
- 同 repo 不同 instance 难度天差地别：matplotlib val 3% label=0 vs test **50%** label=0
- 少数头部问题主导整体指标（top-5 各占 ~64%）

### 3. Repo 组成偏移
- **xarray 占 test 的 23.7%**，val 中完全没有 → val 选择无法评估 xarray 泛化
- pylint 占 val 12.1%，test 中没有；sympy 从 19.1% 降到 1.1%

**Reversal 机制**：不同 checkpoint 在不同 mutation type / repo 上的学习进度不同。Val-best 优化了 val 特有的信号分布（off_by_one 多、return_value 多、pylint/sympy 重），test 需要的能力（operator_swap 主导、xarray 泛化）恰好是 val 无法选择的维度。

**4B s123 有额外 confound**：val@5120 vs test@2048 的 seq_len 差异在长尾样本上影响显著（val code p95=18007 chars）。8B s42 的 8192→8192 是 clean comparison，排除了这个因素。

---
