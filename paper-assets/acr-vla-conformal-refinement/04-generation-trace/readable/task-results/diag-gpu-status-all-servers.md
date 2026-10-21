# diag gpu status all servers

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu-status-all-servers_20260525T182416_result.json`
- **Structured JSON:** [`e343709995e0a965f778.json`](../../sessions/e3/e343709995e0a965f778.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

# 全服务器 GPU 状态诊断

## 1. cqa1-32758 (6 GPU)

| GPU | 显存 | 利用率 | 实验 |
|---|---|---|---|
| 0 | 1 MiB | 0% | **空闲** |
| 1 | 13956 | 62% | pi05 crm_obs_only K=2 **goal s42** |
| 2 | 13956 | 23% | pi05 crm_obs_only K=2 **goal s43** |
| 3 | 13956 | 21% | pi05 crm_obs_only K=2 **goal s44** |
| 4 | 14653 | 24% | pi05 crm_obs_only K=2 **spatial s42** |
| 5 | 13879 | 6% | pi05 crm_obs_only K=2 **spatial s43** |

- 空闲: **GPU 0**
- 异常: `/root/acr-vla-conformal-refinement/results/` **目录不存在**；之前的 `eval-pi05-vla-goal-s42` 进程消失且无结果文件 → 需排查输出位置 (`logs/eval_goal_vla_only_seed42_pi05.json`?)

## 2. bjb1-32546 (6 GPU)

| GPU | 显存 | 利用率 | 实验 |
|---|---|---|---|
| 0 | 14700 | 23% | pi05 crm_obs_only K=2 **spatial s44** |
| 1 | 14125 | 26% | pi05 crm_obs_only K=2 **object s42** |
| 2 | 14125 | 26% | pi05 crm_obs_only K=2 **object s43** |
| 3 | 14125 | 24% | pi05 crm_obs_only K=2 **object s44** |
| 4 | 1876 | 20% | SmolVLA **adaptive_conformal_crm K=2 long s43** |
| 5 | 2 MiB | 0% | **空闲** |

- 空闲: **GPU 5**
- 4 个 pi05 K=2 实验全部健康运行

## 3. bjb1-18228 (4 GPU)

| GPU | 显存 | 利用率 | 实验 |
|---|---|---|---|
| 0 | 0 | 0% | **空闲** |
| 1 | 0 | 0% | **空闲** |
| 2 | 0 | 0% | **空闲** |
| 3 | 9883 | 23% | `train_crm.py --precompute pi05 long K=10` |

- 空闲: **GPU 0, 1, 2** (3 个！)
- K=10 释放后没有部署新实验

## 4. bjb2-28827 (6 GPU) ⚠️ 严重故障

| GPU | 显存 | 利用率 | 实验 |
|---|---|---|---|
| 0 | 1 | 0% | **空闲** |
| 1 | 1 | 0% | **空闲** |
| 2 | 1815 | 26% | SmolVLA **crm_obs_only K=10 long s44** |
| 3 | 1 | 0% | **空闲** |
| 4 | 1 | 0% | **空闲** |
| 5 | 1721 | 19% | SmolVLA **adaptive_conformal_crm K=2 long s43** |

- 空闲: **GPU 0, 1, 3, 4** (4 个！)
- **3 个 pi05 CRM K=2 Long 失败原因已查明**：3 个日志 (`s42/s43/s44`) 全部报同样错误：
  ```
  evaluate.py: error: argument --benchmark: invalid choice: 'long_horizon'
  (choose from 'object', 'spatial', 'goal', 'long', '90')
  ```
  **启动脚本传了 `--benchmark long_horizon`，正确应为 `long`**。Bug fix 后重启即可。
- 注意：bjb1-32546 GPU 4 和本机 GPU 5 都在跑 `adaptive_conformal_crm K=2 long seed43` —— **同一实验重复部署**，需确认是否冗余。

## 5. bjb2-40593 (1 GPU)

| GPU | 显存 | 利用率 | 实验 |
|---|---|---|---|
| 0 | 6544 | 11% | SmolVLA `vla_only single long s43` (baseline) |

- 空闲: 无

---

## 汇总

| 服务器 | 总 GPU | 活跃 | 空闲 | 空闲位置 |
|---|---|---|---|---|
| cqa1-32758 | 6 | 5 | **1** | GPU 0 |
| bjb1-32546 | 6 | 5 | **1** | GPU 5 |
| bjb1-18228 | 4 | 1 | **3** | GPU 0, 1, 2 |
| bjb2-28827 | 6 | 2 | **4** | GPU 0, 1, 3, 4 |
| bjb2-40593 | 1 | 1 | 0 | — |
| **总计** | **23** | **14** | **9** | |

## 关键行动项

1. **bjb2-28827 启动脚本 bug**: `--benchmark long_horizon` → 改为 `long`，可在 4 个空闲 GPU 上重启 pi05 CRM K=2 Long s42/s43/s44 (还多 1 个 GPU 空闲)
2. **bjb1-18228**: 3 个 GPU 完全闲置，可立即部署新实验
3. **cqa1-32758 GPU 0**: 排查 `eval-pi05-vla-goal-s42` 消失原因，确认结果是否生成 (results 目录不存在 → 输出可能在 `logs/`)
4. **重复实验**: bjb1-32546 GPU 4 与 bjb2-28827 GPU 5 都在跑 SmolVLA adaptive K=2 long s43，需 dedupe
5. **附注**: 工具限制 (`tmux`/`ps`/`pgrep` 全被 ssh_read_only 拦截)，session 列表无法获取；需用 ssh_execute 才能查 tmux

---
