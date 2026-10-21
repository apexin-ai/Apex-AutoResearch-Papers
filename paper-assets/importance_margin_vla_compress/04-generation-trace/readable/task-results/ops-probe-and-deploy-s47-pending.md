# ops probe and deploy s47 pending

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_probe_and_deploy_s47_pending_20260529T060229_result.json`
- **Structured JSON:** [`36a0c3f0a080c177ae66.json`](../../sessions/36/36a0c3f0a080c177ae66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有服务器探测完毕。

### GPU 状态汇总

| 服务器 | 状态 | GPU | 显存占用 | 利用率 |
|--------|------|-----|----------|--------|
| cqa1-33015 | 在线 | GPU 0 | 10689/24564 MiB | 66% |
| cqa1-33015 | 在线 | GPU 1 | 10572/24564 MiB | 20% |
| cqa1-33015 | 在线 | GPU 2 | 10531/24564 MiB | 39% |
| cqa1-33015 | 在线 | GPU 3 | 10525/24564 MiB | 21% |
| westd-38929 | 在线 | GPU 0 | 10926/97887 MiB | 57% |
| westd-41074 | 在线 | GPU 0 | 10762/97887 MiB | 38% |
| westd-27271 | **离线** | — | — | — |

### 结论

- **空闲 GPU: 0**。全部 6 张卡（cqa1 ×4, w38 ×1, w41 ×1）均在运行实验，显存占用 ~10.5GB+，利用率 20%-66%。
- **westd-27271 离线**，端口 27271 连接失败，无法使用。
- Director 提到的 8 张 GPU 目前无法确认来源——现有服务器只有 6 张可用卡，全部占满。

### 未部署实验

| 实验 | 原因 |
|------|------|
| `eval_pi05_l2norm_k095_long_seed47` | 无空闲 GPU |
| `eval_pi05_random_k05_long_seed47` | 无空闲 GPU |

需要等当前 s47 实验陆续完成后轮换部署，或确认 w27 是否有新端口/新服务器资源。

---
