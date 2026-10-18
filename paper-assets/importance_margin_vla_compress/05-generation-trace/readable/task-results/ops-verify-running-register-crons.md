# ops verify running register crons

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-running-register-crons_20260521T223320_result.json`
- **Structured JSON:** [`9356cc721236ef62c1e2.json`](../../sessions/93/9356cc721236ef62c1e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 利用率
- **westd-41074**: GPU0=0% (10GB/98GB), GPU1=52% (11GB/98GB), GPU2=0% (29GB/98GB), GPU3=0% (28GB/98GB)
- **cqa1-33015**: GPU0=21% (10GB/25GB), GPU1=53% (10GB/25GB), GPU2=61% (10GB/25GB), GPU3=5% (10GB/25GB)
- **westd-38929**: GPU0=34% (10GB/98GB), GPU1=17% (11GB/98GB), GPU2=0% (0GB/98GB), GPU3=27% (11GB/98GB)

## 实验进程状态

| exp_id | server | PID | 状态 | 操作 |
|--------|--------|-----|------|------|
| eval_pi05_random_k095_object_seed43 | westd-41074 | 730309 | ALIVE (GPU1) | cron 75830f33 已注册 (每小时:13) |
| eval_pi05_random_k0925_object_seed42 | westd-41074 | 715307 | ALIVE (GPU0) | cron 2990f141 已注册 (每小时:17) |
| eval_pi05_random_k03_object_seed43 | cqa1-33015 | 716134 | ALIVE (GPU3) | cron c3c96fc3 已注册 (每小时:21) |
| eval_pi05_l2norm_k085_object_seed42 | cqa1-33015 | 716056 | ALIVE (GPU2) | cron ddb5cafa 已注册 (每小时:25) |
| eval_pi05_l2norm_k07_spatial_seed42 | westd-38929 | 829120 | ALIVE (GPU1) | cron 73bc91fd 已注册 (每小时:29) |

5 个实验全部存活，5 个 cron 监控已注册，每小时交错检查（:13/:17/:21/:25/:29），进程死亡后自动将 registry 状态更新为 ANALYZING。

---
