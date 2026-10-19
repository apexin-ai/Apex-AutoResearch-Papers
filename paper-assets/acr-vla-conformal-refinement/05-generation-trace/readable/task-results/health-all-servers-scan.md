# health all servers scan

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_health_all-servers-scan_20260524T080059_result.json`
- **Structured JSON:** [`3b9212b8aaf15c611fde.json`](../../sessions/3b/3b9212b8aaf15c611fde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 健康检查总结

**总览**: 23/23 GPU 占用，22 个实验在跑，1 个已完成并已收割。

---

### 服务器: bjb2-28827 (6 GPU, 全部进程存活)
| GPU | 进程 | PID | 显存 | 利用率 | 状态 |
|-----|------|-----|------|--------|------|
| 0 | crm-norm005-spatial-s46 | 121241 | 4190 MiB | 31% | 跑中 (started 15:14) |
| 1 | OpenVLA object vla-only s42 v3 | **114990** | 18211 MiB | 81% | etime 55:50, **任务 2 rollout 15/20 success 0/15 ⚠️** |
| 2 | vla-only-spatial-s45 | 96831 | 3560 MiB | 16% | 任务 1 rollout 10/20 success 0/10 |
| 3 | adapt-tau025-spatial-s45 | 97307 | 3660 MiB | 31% | 任务 1 rollout 10/20 success 0/10 |
| 4 | crm-norm005-spatial-s45 | 97070 | 3566 MiB | 14% | 跑中 |
| 5 | vla-only-spatial-s46 | 97550 | 3560 MiB | 17% | 跑中 |

⚠️ **OpenVLA v3 警报**：跑了 55 分钟，任务 1 (cream cheese) 0/20，任务 2 (salad dressing) 0/15。loader 改动可能破坏了行为，与 v2 ~69% 严重不符。等完成后核对。
⚠️ Spatial s45 第一个任务 0/10 — 可能是任务难度（之前 s45 vla-only 81%），需要后续任务确认。

---

### 服务器: bjb1-32546 (6 GPU, 全部进程存活)
| GPU | 进程 | PID | 显存 | 利用率 | 状态 |
|-----|------|-----|------|--------|------|
| 0 | long-adapt-s46 | (已完成) | 1876 MiB | 22% | **✅ DONE SR=58.5%** |
| 1 | long-crm-s46 | (262x) | 1970 MiB | 29% | 任务 6 rollout 10/20 (低显存可疑) |
| 2 | long-reconvla-s46 | 262529 | 1932 MiB | 35% | 任务 6 rollout 15/20 |
| 3 | long-k2mean-s46 | 263191 | 1874 MiB | 24% | 任务 6 rollout 10/20 |
| 4 | long-reconvla-s47 | 316673 | 4993 MiB | 28% | 任务 4 rollout 5/20 |
| 5 | long-crm-s47 | 316940 | 5031 MiB | 30% | 任务 4 rollout 5/20 |

**已收割**: `eval-supp-long-adapt-tau025-s46` → SR=58.5% (117/200)，registry 状态 DONE，conclusion=success。
注意 Long s46 跑了 4+ 小时仅到 6/10 任务，K=10 比平常慢，但 GPU 显存只有 ~1.9GB 略可疑（可能是 K=10 多采样的并行机制）。继续监控。

---

### 服务器: cqa1-32758 (6 GPU, 6 进程活跃)
| GPU | 进程 | PID | 显存 | 利用率 | 状态 |
|-----|------|-----|------|--------|------|
| 0 | spatial-vla-s47 | 731721 | 4338 MiB | 0% | 任务 2 rollout 5/20 success 5/5 (任务 1 95%) |
| 1 | spatial-adapt-s47 | 731987 | 4884 MiB | 15% | 任务 2 rollout 10/20 success 9/10 (任务 1 100%) |
| 2 | spatial-reconvla-s47 | 732063 | 4912 MiB | 26% | 跑中 |
| 3 | spatial-k2mean-s47 | 732418 | 4884 MiB | 15% | 跑中 |
| 4 | long-adapt-s47 | 715967 | 5872 MiB | 15% | 任务 2 rollout 15/20 success 10/15 |
| 5 | long-vla-s47(k2mean) | 716236 | 5872 MiB | 25% | 任务 2 rollout 15/20 success 11/15 |

⚠️ `long-adapt-s46-r2` tmux 任务有日志（任务 1 rollout 5/20 success 0/5）但 ps 未见对应 python 进程，可能早已退出。需核实是否需要重启。
Spatial s47 进展非常好（任务 1 90-100%）。

---

### 服务器: bjb1-18228 (4 GPU, 全部进程存活)
| GPU | 进程 | PID | 显存 | 利用率 | 状态 |
|-----|------|-----|------|--------|------|
| 0 | pi05 object precompute | 113456 | 9884 MiB | 37% | **94.9% (68800/72507), ~115 min 剩** |
| 1 | long-vla-s47-r2 | 278846 | 5606 MiB | 26% | 任务 2 rollout 10/20 success 7/10 |
| 2 | goal-vla-s47 | 279117 | 3704 MiB | 21% | 任务 2 完成 60%, 继续 |
| 3 | pi05 long precompute | 114507 | 9883 MiB | 24% | 48.9% (66500/136090), ~37 hr 剩 |

pi05 object 即将完成（< 2 小时）。

---

### 服务器: bjb2-40593 (1 GPU)
| GPU | 进程 | PID | 显存 | 利用率 | 状态 |
|-----|------|-----|------|--------|------|
| 0 | spatial-crm-s47 | 235730 | 4420 MiB | 25% | 任务 3 rollout 15/20 success 12/15 (任务 2 100%) |

---

## 已完成实验（已收割）
- **eval-supp-long-adapt-tau025-s46**: SR=58.5% (117/200), 10 tasks. Registry: status=DONE, conclusion=success.

## 异常关注
1. **OpenVLA v3 (bjb2-28827 cuda:1)**: 55 min 运行，前 2 任务 0% 成功。可能 loader 重构破坏了模型行为。**建议等完整结果出来后立即对比 v2 (69%)。如果确认回归，loader 需回滚。**
2. **cqa1-32758 long-adapt-s46-r2**: tmux 残留但 python 已退出。日志停在任务 1 rollout 5/20。需用户决定是否重启。
3. **Long s46 三件套** (reconvla/k2mean/crm) 跑 4 小时到 6/10 任务，进度比预期慢。GPU 显存偏低（1.9 GB）但 CPU 时间高，应该是 K=10 推理特性。继续监控。

---
