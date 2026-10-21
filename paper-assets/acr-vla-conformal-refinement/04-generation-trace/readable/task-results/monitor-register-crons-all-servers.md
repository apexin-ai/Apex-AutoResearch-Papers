# monitor register crons all servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_register-crons-all-servers_20260523T222703_result.json`
- **Structured JSON:** [`f64a0537c2129f64fad8.json`](../../sessions/f6/f64a0537c2129f64fad8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## 1. 确认在跑的实验及 PID（15 个）

**bjb1-32546**（5 个，cuda:0-4）:
| GPU | 实验 | PID |
|-----|------|-----|
| cuda:0 | eval-supp-crm-norm005-obj-s46 | 102927 |
| cuda:1 | eval-supp-long-vla-only-s45 | 103128 |
| cuda:2 | eval-supp-long-adapt-tau025-s45 | 103397 |
| cuda:3 | eval-supp-long-crm-norm005-s45 | 103675 |
| cuda:4 | eval-supp-long-reconvla-s45 | 103942 |

**bjb2-28827**（6 个，cuda:0-5）:
| GPU | 实验 | PID |
|-----|------|-----|
| cuda:0 | eval-supp-goal-vla-only-s45 | 926766 |
| cuda:1 | eval-supp-goal-crm-norm005-s45 | 927030 |
| cuda:2 | eval-supp-goal-reconvla-s45 | 927237 |
| cuda:3 | eval-supp-long-reconvla-s44 | 849677 |
| cuda:4 | eval-supp-long-k2mean-s45 | 924226 |
| cuda:5 | eval-supp-long-k2mean-s44 | 850410 |

**cqa1-32758**（5 个，cuda:0-1,3-5）:
| GPU | 实验 | PID |
|-----|------|-----|
| cuda:0 | eval-supp-goal-k2mean-s45 | 456787 |
| cuda:1 | eval-supp-spatial-vla-only-s45 | 456947 |
| cuda:3 | eval-supp-spatial-crm-norm005-s45 | 457405 |
| cuda:4 | eval-supp-spatial-adapt-tau025-s45 | 502816 |
| cuda:5 | eval-supp-spatial-reconvla-s45 | 457485 |

## 2. 已注册 cron（16 个，含上述 15 个 + spatial-adapt）

全部 16 个 cron 注册成功，interval=120s。

## 3. 已完成但之前标记为 RUNNING 的实验（3 个）

| 实验 | 服务器 | SR | 状态已更新 |
|------|--------|-----|-----------|
| eval-supp-goal-adapt-tau025-s45 | bjb1-32546:cuda:5 | **81.0%** (162/200), trigger_rate=9.4% | → DONE |
| eval-supp-reconvla-obj-s46 | cqa1-32758:cuda:2 | **80.0%** (160/200) | → DONE |
| eval-supp-crm-norm005-obj-s45 | bjb2-40593:cuda:0 | **76.5%** (153/200) | → DONE |

## 4. 异常/特殊情况

- **bjb2-40593**: 完全空闲，无任何 eval 进程和 tmux session（eval-supp-crm-norm005-obj-s45 已完成）
- **bjb1-32546:cuda:5**: 已空闲（eval-supp-goal-adapt-tau025-s45 已完成）
- **cqa1-32758:cuda:2**: 已空闲（eval-supp-reconvla-obj-s46 已完成）
- **eval-supp-spatial-adapt-tau025-s45**: 状态已从 PREPARING → RUNNING，进程确认在跑（PID 502816/502821）

---
