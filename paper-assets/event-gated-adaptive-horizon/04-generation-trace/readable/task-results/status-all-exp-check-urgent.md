# status all exp check urgent

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_all_exp_check_urgent_20260521T194036_result.json`
- **Structured JSON:** [`c45bcfe7b90fa99c274f.json`](../../sessions/c4/c45bcfe7b90fa99c274f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集。汇总如下：

---

## 全局结论：所有实验 CIVO 均未触发，gate_dt 始终锁死在 2.0

所有 4 个实验中 `civo/alert` 始终 = 0，`gate_dt_2_frac` 始终 = 1.0，horizon 从未自适应调整。

---

## 1. exp_036_dual_critic_pickcube — 已完成 ❌ Negative

| 项目 | 值 |
|---|---|
| 状态 | **DEAD**，EXIT_CODE=0，正常完成 |
| 最终步数 | ~212,447 / 210k |
| 服务器 | bjb1-45299:cuda:0, GPU 空闲 (0%) |

**eval_return 轨迹：**
| Step | eval |
|------|------|
| 2.5k | 2.0 |
| 12.5k | 17.5 |
| 22.5k | 17.5 |
| 32.5k | 11.6 |
| 42.5k | 15.6 |
| 52.5k | 11.7 |
| 62.5k | 18.8 |
| 72.5k | 5.4 |
| 82.5k | 22.5 |
| 92.5k | 18.1 |
| 102.5k | 8.4 |
| 112.5k | 7.1 |
| 122.5k | 9.1 |
| 132.5k | 12.8 |
| 142.5k | 14.0 |
| 152.5k | 13.1 |
| 162.5k | 16.2 |
| 172.5k | 19.7 |
| 182.5k | 16.8 |
| 192.5k | 13.7 |
| **202.5k** | **27.7** |

**ve_ratio 轨迹（可见点）：**
12.5k→0.2, 22.5k→1.0, 32.5k→2.3, ...(中段截断)..., 182.5k→0.4, 192.5k→0.4, 202.5k→0.2

**结论：** PickCube 任务 eval 始终在 2~28 之间波动，无学习趋势。最终 27.7 是最高点但仍然很低。CIVO 未触发。完全 negative。

---

## 2. exp_037_wide_critic_cheetah — 已完成 ⚠️ 衰退

| 项目 | 值 |
|---|---|
| 状态 | **DEAD**，EXIT_CODE=0，正常完成 |
| 最终步数 | ~224,000 / 210k |
| 服务器 | bjb1-45299:cuda:1, GPU 空闲 (0%) |

**eval_return 轨迹：**
| Step | eval |
|------|------|
| 5k | 8.3 |
| 15k | 32.3 |
| 25k | 107.9 |
| 35k | 123.4 |
| 45k | 19.1 |
| 55k | 22.7 |
| 65k | 23.0 |
| 75k | 186.1 |
| 85k | 95.4 |
| 95k | 48.5 |
| **105k** | **350.1** ← peak |
| 115k | 256.7 |
| 125k | 286.8 |
| 135k | 238.9 |
| 145k | 186.5 |
| 155k | 182.4 |
| 165k | 167.3 |
| 175k | 260.8 |
| 185k | 191.5 |
| 195k | 151.7 |
| 205k | 150.7 |
| **215k** | **146.1** ← final |

**ve_ratio 轨迹（可见点）：**
15k→0.1, 25k→0.2, 35k→0.4, **45k→3.6** (spike), ...(中段截断)..., 195k→0.1, 205k→0.1, 215k→0.1

**结论：** 峰值 350 在 105k，之后持续衰退至 146。ve_ratio 在 45k 有一次大 spike (3.6) 但 CIVO 未触发。后半程 eval 稳步下降。gate_dt 始终 2.0。

---

## 3. exp_038_dual_critic_walker_s2 — 运行中 ⚠️ 严重衰退

| 项目 | 值 |
|---|---|
| 状态 | **ALIVE**，PID 175633，已运行 7h23m |
| 当前步数 | 205,000 / 210k (97.6%) |
| 服务器 | bjb1-40020:cuda:0, GPU 27%, 3830 MiB |

**eval_return 轨迹：**
| Step | eval |
|------|------|
| 5k | 35.2 |
| 15k | 149.3 |
| 25k | 194.5 |
| 35k | 176.5 |
| 45k | 119.6 |
| 55k | 251.5 |
| 65k | 310.5 |
| 75k | 249.0 |
| 85k | 344.7 |
| 95k | 311.8 |
| 105k | 283.1 |
| 115k | 300.5 |
| 125k | 278.2 |
| 135k | 308.7 |
| 145k | 297.4 |
| **155k** | **354.0** ← peak |
| 165k | 226.6 |
| **175k** | **99.6** ← collapse |
| 185k | 109.4 |
| 195k | 107.0 |
| 205k | 120.9 |

**ve_ratio 轨迹（可见点）：**
15k→0.0, 25k→0.1, 35k→0.3, ..., 185k→0.3, 195k→0.3, 205k→0.3

**结论：** 峰值 354 在 155k，175k 发生断崖式崩溃 (354→99.6)，之后稳定在 ~107-121 无法恢复。ve_ratio 始终 ≤0.3，CIVO 未触发。gate_dt 始终 2.0。即将完成。

---

## 4. exp_039_narrow_dual_critic_walker_s1 — 运行中 ⚠️ 正在崩溃

| 项目 | 值 |
|---|---|
| 状态 | **ALIVE**，PID 198771，已运行 3h10m |
| 当前步数 | ~92,000 / 210k (43.8%) |
| 服务器 | bjb1-40020:cuda:1, GPU 15%, 2597 MiB |

**eval_return 轨迹：**
| Step | eval |
|------|------|
| 5k | 36.7 |
| 15k | 155.3 |
| 25k | 159.7 |
| 35k | 189.0 |
| 45k | 258.3 |
| 55k | 253.1 |
| 65k | 339.2 |
| **75k** | **463.5** ← peak |
| **85k** | **136.0** ← collapse |

**ve_ratio 轨迹：**
15k→0.0, 25k→0.1, 35k→0.2, 65k→0.3, 75k→0.3, **85k→1.3** (spike post-collapse)

**结论：** 75k 时 eval 达到 463.5（所有 Walker 实验最高），随即 85k 崩溃至 136。ve_ratio 在崩溃后升至 1.3 但 CIVO 仍未触发 alert。当前在 92k，train_return 在 37-134 之间波动，很可能无法恢复。

---

## GPU 状态

| 服务器 | GPU | 利用率 | 显存 |
|--------|-----|--------|------|
| bjb1-45299 | 0: RTX PRO 6000 Blackwell | 0% | 0/98GB |
| bjb1-45299 | 1: RTX PRO 6000 Blackwell | 0% | 0/98GB |
| bjb1-40020 | 0: RTX 4090 | 27% | 3.8/24GB |
| bjb1-40020 | 1: RTX 4090 | 15% | 2.5/24GB |

**bjb1-45299 双卡完全空闲**，exp_036/037 已完成。

---

## 总体判断

所有 4 个实验的核心问题一致：**CIVO 机制形同虚设**。
- `civo/alert` 全程 = 0，从未触发
- `gate_dt` 全程 = 2.0，`gate_dt_2_frac` = 1.0，horizon 从未自适应
- `gate_empirical_entropy` = 0.0，gate 网络完全没有探索
- 3/4 个实验出现严重性能崩溃（exp_037/038/039），但 CIVO 均未检测到

---
