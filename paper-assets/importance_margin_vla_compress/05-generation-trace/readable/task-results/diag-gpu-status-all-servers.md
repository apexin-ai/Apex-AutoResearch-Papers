# diag gpu status all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu-status-all-servers_20260526T203910_result.json`
- **Structured JSON:** [`20e9fec4e919110951a2.json`](../../sessions/20/20e9fec4e919110951a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**14 GPU 总计，11 活跃，3 空闲。13 个实验在跑。**

### 空闲 GPU (3 个)

| 服务器 | GPU | 状态 |
|--------|-----|------|
| westd-27271 | cuda:0 | 空闲 (0%, 1 MiB) |
| cqa1-33015 | cuda:3 | 空闲 (**不是** cuda:0，cuda:0 在跑 pi05 l2norm k0.7) |
| westd-38929 | cuda:3 | 空闲 (0%, 1 MiB) |

### Cron 跟踪的 5 个 OpenVLA 实验 — 全部存活

全部在跑，日志最后更新均在 04:33-04:42 (刚刚)。进度：Task 3-7/10 不等。

### Registry 中 6 个非 cron 实验 — 全部是 zombie

`eval_pi05_l2norm_k075_long`, `eval_pi05_random_k085_long_seed43_postfix`, `eval_pi05_random_k09_long_seed43_postfix`, `eval_pi05_l2norm_k05_spatial_postfix`, `eval_pi05_l2norm_k03_long_postfix`, `eval_xvla_random_k05_spatial_seed43` — 4 台服务器上均无对应 GPU 进程，应清理 registry。

### 额外发现的实验 (不在 cron/zombie 列表中)

- **cqa1-33015**: 3 个 Pi0.5 实验 (l2norm k0.7, attention k0.7, attention k0.5) 占 GPU 0-2
- **westd-41074**: 5 个 OpenVLA object/long 实验，GPU 0 和 1 各跑 2 个实验 (98GB 放得下)

报告已写入 `artifacts/gpu_diagnostic_20260527.md`。

---
