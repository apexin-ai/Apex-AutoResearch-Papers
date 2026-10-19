# monitor status check both servers

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_status_check_both_servers_20260520T035956_result.json`
- **Structured JSON:** [`6e707c96b8bb5c39fd20.json`](../../sessions/6e/6e707c96b8bb5c39fd20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### westd-47453: v9d 训练

| 项目 | 状态 |
|------|------|
| **进程** | **存活** (PID 380305, 4 个 actor worker 380864-380867) |
| **进度** | **Step 2/30** (7%), ETA ~13h35m (每 step ~28min) |
| **Checkpoint** | 目录为空（save_freq=5，step 5 时才会保存第一个） |
| **磁盘** | 124G/250G (50%), 剩余 127G |

**GPU 利用率：**
| GPU | 利用率 | 显存 | 温度 | 功耗 |
|-----|--------|------|------|------|
| 0 | 100% | 79.6/97.9 GB | 55°C | 359W |
| 1 | 100% | 79.6/97.9 GB | 57°C | 372W |
| 2 | 100% | 79.7/97.9 GB | 54°C | 361W |
| 3 | 100% | 79.7/97.9 GB | 61°C | 401W |

**关键 Metrics (step 1 → step 2):**
| Metric | Step 1 | Step 2 |
|--------|--------|--------|
| success rate | 57.0% | **58.6%** |
| entropy | 0.0459 | 0.0449 ↓ |
| KL divergence | 0.00233 | 0.00357 ↑ |
| reward mean | 5.70 | 5.86 ↑ |
| pg_clipfrac | 0.0058 | 0.0075 |
| grad_norm | 1.13 | 1.19 |
| pass@8 | 1.0 | 1.0 |
| throughput | 169 tok/s | 149 tok/s |

---

### bjb1-17606: eval_v2

| 项目 | 状态 |
|------|------|
| **进程** | **存活** (PID 195853, 2 个 VLLM Worker) |
| **进度** | **783/1796 episodes** (43.6%) |
| **Success rate** | **241/783 = 30.8%** |
| **GPU** | 2x RTX PRO 6000, 84.2/97.9 GB 显存, 0% util（采样瞬间在 episode 间隙） |

最近 3 条结果（inclined-plane-friction-named-surfaces）: score 10 / -100 / 100，成功 1/3。

---
