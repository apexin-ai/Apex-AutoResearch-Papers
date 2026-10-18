# ops westd38929 fill 4gpu

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-fill-4gpu_20260521T050148_result.json`
- **Structured JSON:** [`f8931e08bae419c49862.json`](../../sessions/f8/f8931e08bae419c49862.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 GPU 全部成功启动并运行，日志确认参数正确。

### 产出汇总

| GPU | 实验 | PID | 日志确认 |
|-----|------|-----|---------|
| cuda:0 | OpenVLA **L2norm k=0.5** seed42 libero_object | 568225 | `[*] L2 norm pruning: k=0.5` ✓ |
| cuda:1 | OpenVLA **Random k=0.3** seed42 libero_object | 568905 | `[*] Random pruning: k=0.3` ✓ |
| cuda:2 | OpenVLA **L2norm k=0.7** seed42 libero_object | 569611 | `[*] L2 norm pruning: k=0.7` ✓ |
| cuda:3 | OpenVLA **L2norm k=0.3** seed42 libero_object | 570309 | `[*] L2 norm pruning: k=0.3` ✓ |

**X-VLA checkpoint 不存在于 westd-38929**（仅有 lerobot 源码目录，无模型权重）。4 GPU 全部改用 OpenVLA 实验填充。

GPU 显存占用 ~16GB/卡，GPU-Util 66-80%，全部正常运行。

---
