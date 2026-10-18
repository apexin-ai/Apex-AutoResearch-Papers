# audit gpu status all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_gpu_status_all_servers_20260526T131651_result.json`
- **Structured JSON:** [`a7eaadd67bf8afd67633.json`](../../sessions/a7/a7eaadd67bf8afd67633.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。

---

## GPU 进程审计报告

### COMPLETED（2 个）

**eval_pi05_l2norm_k075_long_seed42 | cqa1-33015:cuda:0 | COMPLETED | SR=73.4%**

| Task | Description | SR |
|------|-------------|-----|
| T0 | open the bottom drawer... | 96.0% (48/50) |
| T1 | put both cream cheese... | 94.0% (47/50) |
| T2 | turn on the stove... | 82.0% (41/50) |
| T3 | turn on the stove... (v2) | 70.0% (35/50) |
| T4 | put the black bowl... | 68.0% (34/50) |
| T5 | pick up the book... | 84.0% (42/50) |
| T6 | put the white mug... | 52.0% (26/50) |
| T7 | put both alphabet soup... | 76.0% (38/50) |
| T8 | put both moka pots... | 28.0% (14/50) |
| T9 | put yellow/white mug... | 84.0% (42/50) |
| **Overall** | | **73.4% (367/500)** |

**eval_openvla_attn_k085_goal_seed42_v3 | westd-38929:cuda:2 | COMPLETED | SR=74.6%**

| Task | Description | SR |
|------|-------------|-----|
| T1 | open the middle drawer of the cabinet | 52.0% (26/50) |
| T2 | put the bowl on the stove | 88.0% (44/50) |
| T3 | put the wine bottle on top of the cabinet | 76.0% (38/50) |
| T4 | open the top drawer and put the bowl inside | 44.0% (22/50) |
| T5 | put the bowl on top of the cabinet | 98.0% (49/50) |
| T6 | push the plate to the front of the stove | 84.0% (42/50) |
| T7 | put the cream cheese in the bowl | 74.0% (37/50) |
| T8 | turn on the stove | 94.0% (47/50) |
| T9 | put the bowl on the plate | 78.0% (39/50) |
| T10 | put the wine bottle on the rack | 58.0% (29/50) |
| **Overall** | | **74.6% (373/500)** |

---

### RUNNING（6 个）

```
exp_id                                    | server:gpu         | status  | progress            | 备注
eval_pi05_attention_k075_long_seed42_v2   | cqa1-33015:cuda:1  | RUNNING | T9 ep20/50, ~49.6%  | PID 213212, 运行 4h03m
eval_pi05_attention_k05_long_seed42_v2    | cqa1-33015:cuda:2  | RUNNING | T6 ep40/50, ~58.0%  | PID 262562, 运行 2h51m
eval_pi05_attention_k085_long_seed42_v2   | cqa1-33015:cuda:3  | RUNNING | T2 ep20/50 (early)  | PID 337364, 运行 1h14m
eval_openvla_random_k085_goal_seed42      | westd-38929:cuda:0 | RUNNING | T10 ep40/50, 即将完成 | PID 467961, 运行 3h10m
eval_openvla_random_k05_long_seed42_v2    | westd-38929:cuda:1 | RUNNING | T9 ep10/50          | PID 279274, 运行 8h14m
eval_openvla_attn_k085_long_seed42_v5     | westd-38929:cuda:3 | RUNNING | T3 ep30/50 (early)  | PID 514347, 运行 2h07m
```

---

### 新发现的进程（未在审计清单中）

```
PID 384775 | cqa1-33015:cuda:0 | eval_pi05_random_k085_long_seed42      | 刚启动 ~4min
PID 601124 | westd-38929:cuda:2 | eval_openvla_attn_k07_goal_seed42     | 刚启动 ~5min
```

这两个是已完成实验腾出 GPU 后被新启动的实验。

---

**总结**：8 个审计目标中，2 个 COMPLETED（已提取完整 SR），6 个 RUNNING（无崩溃），0 个 CRASHED。两台服务器 8 张 GPU 全部满载。

---
