# fix s46 preparing status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_s46_preparing_status_20260528T085823_result.json`
- **Structured JSON:** [`4dfc134de2cb8a7b7a92.json`](../../sessions/4d/4dfc134de2cb8a7b7a92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

**实验 1** `eval_pi05_l2norm_k095_long_seed46_strict_w27` — westd-27271, PID 616102 存活，已运行 ~4min。Registry 已修复为 RUNNING。Cron 0b8e5bbb 每 12min 监控。

**实验 2** `eval_pi05_random_k095_long_seed46_strict_w41` — westd-41074, PID 898746 存活，已运行 ~4min。Registry 已修复为 RUNNING。Cron 178744cd 每 12min 监控。

**实验 3** `eval_pi05_l2norm_k07_long_seed46_strict_w38_v2` — **无法立即部署**。westd-38929 cuda:3 当前被 PID 457266 占用（`attention k=0.95 seed46`，运行 ~4min，刚启动的实验）。该实验预计运行 ~3h，cuda:3 短期内不会释放。

需要你决定：
- 等 cuda:3 上的 attention 实验结束后再部署（~3h 后）
- 换一台有空闲 GPU 的服务器部署

---
