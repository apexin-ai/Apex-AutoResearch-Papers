# deploy westd38929 refill gpu013

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929_refill_gpu013_20260526T054445_result.json`
- **Structured JSON:** [`7e07f493f4e372315c5f.json`](../../sessions/7e/7e07f493f4e372315c5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**westd-38929 全部 4 GPU 在跑，且你要部署的 3 个实验已经全部在运行中：**

| GPU | PID | 运行时长 | 实验 |
|-----|--------|---------|------|
| 0 | 285940 | 24min | **Random k=0.85 Object** (已在跑) |
| 1 | 279274 | 42min | **Random k=0.5 Long** (已在跑) |
| 2 | 252246 | 2h04m | L2norm k=0.7 Object |
| 3 | 288325 | 20min | **Attn k=0.85 Object** (已在跑) |

3 个目标实验（Random k=0.85 Object、Attn k=0.85 Object、Random k=0.5 Long）均已部署且正在执行，无需重复提交。模型路径注意：Object 模型实际在 `/root/autodl-tmp/openvla-libero-object`（无 `models/` 前缀）。

---
