# diag mcmc progress check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_mcmc-progress-check_20260515T005659_result.json`
- **Structured JSON:** [`282c39cfbc13e6b01647.json`](../../sessions/28/282c39cfbc13e6b01647.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 1. exp006-pooled-s1only-arc — **已完成**

| 指标 | 值 | 状态 |
|------|-----|------|
| max rhat | 1.0098 | OK (< 1.01) |
| min ESS | 769.6 | OK (> 400) |
| divergences | 0 | OK |
| PPP | 0.9677 | 优秀 |
| gamma | **-1.4637** [-2.51, -0.41] | CI 排除 0 |
| 运行时间 | 1244s (~21min) | — |

gamma 显著为负，意味着 S1 embedding 信号与污染效应**反向关联**。模型拟合优秀。

---

### 2. exp006-pooled-s1only-gsm8k — **失败**

4 条 chain 在采样 55-65% 时全部崩溃：
```
Chain [1-4] error: code '1' Operation not permitted
```
原因是 CmdStan 子进程被系统 nproc/security limits 杀掉（与 oracle-extended 相同问题）。需要重新运行。

---

### 3. exp006-oracle-gsm8k-extended — **部分完成**

- **IRT (4PL) 拟合失败**：同样的 "Operation not permitted" 错误，retcodes=[0,1,1,1]
- **非 IRT baselines 成功完成**（16 个模型，含 seed 123 + non-aligned）:

| Method | MAE | C50 | C80 | C95 | tau |
|--------|-----|-----|-----|-----|-----|
| B0_raw | 0.005 | 0.88 | 0.94 | **1.00** | 0.838 |
| B1_remove_rescore | 0.005 | 0.88 | 0.94 | 1.00 | 0.838 |
| B4_linear_regression | 0.008 | 0.81 | 0.94 | 1.00 | 0.746 |
| B6_dcr_fuzzy | 0.138 | 0.56 | 0.56 | 0.56 | 0.415 |

B0_raw 在 16 模型 oracle-extended 设置下 C95=1.00, C80=0.94，coverage 远好于之前的 20-33%。但 IRT 部分未跑出来。

---

### 4. 2PL 消融 — **已完成**（v1，baselines-only 模式）+ **v3 运行中**

**已完成结果**（保存在 `results_pooled_05B_15B_2pl_ablation/`）：

**GSM8K 2PL+gamma：**
| 指标 | 值 |
|------|-----|
| gamma | 0.422 [-0.145, 0.998] |
| CI excludes 0 | **否** |
| max rhat | 1.0085 |
| min ESS | 445.1 |
| PPP | 0.076 |

**ARC 2PL+gamma：**
| 指标 | 值 |
|------|-----|
| gamma | 4.361 [3.585, 5.167] |
| CI excludes 0 | 是 |
| max rhat | 1.0066 |
| min ESS | 1026.8 |
| PPP | **0.0**（拟合极差） |

ARC 2PL 模型拟合彻底失败（PPP=0），calibrated scores 被极端压缩（d5→0.07, d25→0.10, d100→0.02 vs raw ~0.33）。

**v3 仍在运行中**：chains 在 80%，预估剩余 ~9 分钟（基于 1.3s/it 的速度，剩余 400 samples/chain）。

---

### 根因判断的关键发现

1. **S1-only ARC 收敛了**，但 gamma 为负——S1 信号方向不对，不是 exposure 有问题，而是 S1 embedding 本身不是好的污染指标
2. **2PL ARC**: PPP=0.0，2PL 也无法拟合 ARC——不是 4PL+gamma 过参数化的问题
3. **Oracle-extended baselines 表现很好**（C95=1.00），说明模型指定可能没问题，问题在 signal quality 和 benchmark 特性
4. **GSM8K 的 IRT 结果全部被 "Operation not permitted" 阻断**——这是最需要修复的瓶颈。建议检查服务器的 `ulimit -u`（nproc limit），CmdStan fork 时超限被 kill

---
