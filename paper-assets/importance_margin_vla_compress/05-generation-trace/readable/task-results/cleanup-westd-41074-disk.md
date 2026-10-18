# cleanup westd 41074 disk

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_westd-41074-disk_20260525T180952_result.json`
- **Structured JSON:** [`83f1f7787400313b50f3.json`](../../sessions/83/83f1f7787400313b50f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理完成

| | 清理前 | 清理后 |
|---|---|---|
| 已用 | 249GB | 57GB |
| 可用 | **1.9GB** | **194GB** |

**释放 192GB**，清理内容：
- HF datasets 处理缓存 (66GB)
- HF lerobot hub 下载缓存 (33GB)
- 未引用的模型缓存：SmolVLM2 backbone/Instruct, X-VLA, SmolVLA official (19GB)
- 未引用的 openvla baseline 模型：libero-goal, libero-spatial, libero-10 (45GB)
- Checkpoint 中间步骤：m64 的 step 70k/80k/90k, m96 的重复 step99999 (33GB)
- pip cache, clip 模型等小文件 (~1GB)

**保留不动**：`openvla-libero-object/` (pretrained 基座), `smolvla_base/`, `libero_data/`, 所有 results/eval_results/脚本, 两个实验的 final checkpoint。

---
