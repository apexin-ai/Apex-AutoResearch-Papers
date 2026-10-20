# ops verify bootstrap true values

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-bootstrap-true-values_20260523T193944_result.json`
- **Structured JSON:** [`2d5b077699f88b78da42.json`](../../sessions/2d/2d5b077699f88b78da42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data needed. Here's the summary.

---

## Task 1: ARC-C Qwen 50% CI 上界

**Bootstrap 原始值** (`/root/autodl-tmp/bca_bootstrap_results.json`):
- Qwen ARC-C free-θ 50%, percentile CI = [3.6296, **15.1505**]

| 来源 | 值 | 正确？ |
|------|-----|--------|
| Table 1 (`results.tex:31`) | 15.2 | **正确** (15.15 → 15.2) |
| 本地 figure 脚本 (`figures/paper/gen_fig_theta_scatter.py:47`) | 15.20 | **正确** |
| 服务器 figure 脚本 (两个版本) | 15.49 | **错误** |

**结论**: Table 正确。服务器上的 figure 脚本是旧版本，值 15.49 没有来源依据。本地脚本已修正。

---

## Task 2: Mistral 50% CI 上界

**Bootstrap 原始值** (`bca_bootstrap_results.json`):
- Mistral MMLU free-θ 50%, percentile CI = [**-9.3858**, -2.0945]
- |d| CI 上界 = 9.3858 → 9.4

| 来源 | 值 | 正确？ |
|------|-----|--------|
| Table 1 (`results.tex:30`) | 9.4 | **正确** (9.39 → 9.4) |
| 本地 figure 脚本 (`:46`) | 9.40 | **正确** |
| 服务器 figure 脚本 (两个版本) | 9.59 | **错误** |

**结论**: Table 正确。服务器脚本的 9.59 是错误值。本地脚本已修正。

---

## Task 3: ARC-C Qwen baseline accuracy

**10-seed 原始数据** (`worker_code_arcc-collect-all-seeds` 日志):

| Seed | Accuracy | 正确数/295 |
|------|----------|-----------|
| s1 | 90.17% | 266 |
| s2 | 89.49% | 264 |
| s3 | 89.49% | 264 |
| s4 | 88.47% | 261 |
| s5 | 89.83% | 265 |
| s6 | 89.49% | 264 |
| s7 | 89.15% | 263 |
| s8 | 90.51% | 267 |
| s9 | 90.17% | 266 |
| s10 | 90.51% | 267 |

**Mean = 2647/2950 = 89.73%**

| 来源 | 值 | 正确？ |
|------|-----|--------|
| `results.tex:58-59` | 90.0% | **错误** |
| 本地 figure 脚本 (`:47`) | 89.9% | **错误** |
| 服务器 irt 脚本 | 89.9% | **错误** |
| 服务器 anon 脚本 | 90.2% | **错误** (看起来用了单个 s1=90.17%) |

**结论**: 真值是 **89.7%**。所有地方都需要修正。`results.tex` 中两处 "90.0%" 应改为 "89.7%"，figure 脚本中的 89.9 应改为 89.7。

---
