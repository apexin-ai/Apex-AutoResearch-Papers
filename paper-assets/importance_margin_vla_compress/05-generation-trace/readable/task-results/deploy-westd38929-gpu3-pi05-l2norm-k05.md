# deploy westd38929 gpu3 pi05 l2norm k05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929_gpu3_pi05_l2norm_k05_20260527T114946_result.json`
- **Structured JSON:** [`7c76bd639a86f5f7618f.json`](../../sessions/7c/7c76bd639a86f5f7618f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both tasks done. Summary:

---

### cqa1 Harvest: `eval_pi05_l2norm_k085_long_seed42_strict` → **DONE (success)**
- **Overall SR: 77.6%** (388/500), 224.8 min
- Per-task: T0=98%, T1=94%, T2=86%, T3=96%, T4=68%, T5=96%, **T6=8%**, T7=80%, T8=56%, T9=94%
- Registry updated with full metrics
- cqa1 GPU3: 9.8GB/24GB, 0% util — process still loaded but idle, **可用于下一个实验**

### westd-38929 Deploy: `eval_pi05_l2norm_k05_long_seed42_strict_w38` → **RUNNING**
- ⚠️ **GPU3 不空闲**（21GB, 92% util, 2 python processes）。改部署到 **GPU1**（实际空闲的）
- tmux session `pi05_l2n_k05`, CUDA_VISIBLE_DEVICES=1
- 模型正在加载，日志确认启动正常
- Registry: RUNNING

### westd-38929 GPU 状态
| GPU | Memory | Util | Status |
|-----|--------|------|--------|
| 0 | 16GB/98GB | 83% | busy |
| 1 | loading... | 0%→ | **刚部署 L2norm k=0.5** |
| 2 | 16GB/98GB | 72% | busy |
| 3 | 21GB/98GB | 91% | busy (2 processes) |

---
