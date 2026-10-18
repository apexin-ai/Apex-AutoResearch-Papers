# check all servers pid scan

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all_servers_pid_scan_20260524T204703_result.json`
- **Structured JSON:** [`b4a41046b445bace2d8d.json`](../../sessions/b4/b4a41046b445bace2d8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完成。以下是全部结果：

## GPU 进程汇总表

| 服务器 | GPU | exp_id | PID (python) | GPU利用率 | 备注 |
|--------|-----|--------|-------------|-----------|------|
| **westd-41074** | 0 | eval_pi05_random_k09_goal_seed43_postfix | 830189 | 35% | 需注册 cron |
| westd-41074 | 1 | eval_pi05_l2norm_k09_object_seed43_postfix | 711648 | 39% | 需注册 cron |
| westd-41074 | 2 | eval_pi05_random_k09_object_seed43_postfix | 794748+796424 | 72% | ⚠️ **重复进程**，2个相同python占GPU2 |
| westd-41074 | 3 | (空) | — | 0% | ⚠️ **无进程！** l2norm_k09_goal 已挂/已完成 |
| **westd-38929** | 0 | eval_openvla_attn_k09_object_seed42_v3 | 692475 | 69% | ✅ 已有 cron (wrapper 692469) |
| westd-38929 | 1 | eval_openvla_attn_k085_object_seed42_v3 | 693434 | 66% | ✅ 已有 cron (wrapper 693429) |
| westd-38929 | 2 | eval_pi05_l2norm_k03_long_seed43_postfix_v2 | 756339 | 0% | ⚠️ **旧 cron PID 566653 已死**，需更新 cron 到新 PID 756339 |
| westd-38929 | 3 | eval_pi05_l2norm_k09_spatial_seed43_postfix | 763844 | 50% | 需注册 cron |
| **westd-27271** | 0 | eval_openvla_attn_k09_goal_seed42 | 958937 | 69% | 需注册 cron |
| westd-27271 | 1 | eval_openvla_attn_k09_spatial_seed42 | 959698 | 72% | 需注册 cron |
| **cqa1-33015** | 0 | eval_pi05_l2norm_k03_long_seed43_postfix_v2 | 566658 | 0% | 需注册 cron |
| cqa1-33015 | 1 | eval_pi05_random_k07_long_seed43_postfix | 600244 | 52% | 需注册 cron |
| cqa1-33015 | 2 | eval_pi05_random_k05_long_seed43_postfix | 600325 | 22% | 需注册 cron |
| cqa1-33015 | 3 | eval_pi05_random_k095_long_seed43_postfix | 600400 | 0% | 需注册 cron |

---

## 异常情况

1. **westd-41074 GPU3 无进程** — `eval_pi05_l2norm_k09_goal_seed43_postfix` 已崩溃或已完成，需查日志确认是否要重启
2. **westd-41074 GPU2 重复进程** — PID 794748 和 796424 运行完全相同的命令（random k0.9 object），疑似重复启动
3. **westd-38929 GPU2 cron 失效** — 旧 PID 566653 已不存在，当前实际进程为 756339（且 GPU 利用率 0%，可能在等待或卡住）

## 需注册 cron 的实验（11 个）

| 服务器 | PID | exp_id |
|--------|-----|--------|
| westd-41074 | 830189 | eval_pi05_random_k09_goal_seed43_postfix |
| westd-41074 | 711648 | eval_pi05_l2norm_k09_object_seed43_postfix |
| westd-41074 | 794748 | eval_pi05_random_k09_object_seed43_postfix |
| westd-38929 | 756339 | eval_pi05_l2norm_k03_long_seed43_postfix_v2 (更新旧cron) |
| westd-38929 | 763844 | eval_pi05_l2norm_k09_spatial_seed43_postfix |
| westd-27271 | 958937 | eval_openvla_attn_k09_goal_seed42 |
| westd-27271 | 959698 | eval_openvla_attn_k09_spatial_seed42 |
| cqa1-33015 | 566658 | eval_pi05_l2norm_k03_long_seed43_postfix_v2 |
| cqa1-33015 | 600244 | eval_pi05_random_k07_long_seed43_postfix |
| cqa1-33015 | 600325 | eval_pi05_random_k05_long_seed43_postfix |
| cqa1-33015 | 600400 | eval_pi05_random_k095_long_seed43_postfix |

**注意**：cqa1-33015 的 GPU 分配顺序与你预期不同（k07→GPU1, k05→GPU2, k095→GPU3），但实验本身都在正常运行。

---
