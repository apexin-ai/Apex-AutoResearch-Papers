# ops force kill all gpu

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_force-kill-all-gpu_20260528T110452_result.json`
- **Structured JSON:** [`75517375e420a7c6faf0.json`](../../sessions/75/75517375e420a7c6faf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 GPU 进程已经不存在，无需 kill。

## westd-10894 (4 张卡)
| GPU | Util | Memory |
|-----|------|--------|
| 0 | 0% | 0 MiB / 97887 MiB |
| 1 | 0% | 0 MiB / 97887 MiB |
| 2 | 0% | 0 MiB / 97887 MiB |
| 3 | 0% | 0 MiB / 97887 MiB |

## westd-34685 (4 张卡)
| GPU | Util | Memory |
|-----|------|--------|
| 0 | 0% | 0 MiB / 97887 MiB |
| 1 | 100% | 0 MiB / 97887 MiB |
| 2 | 0% | 0 MiB / 97887 MiB |
| 3 | 0% | 0 MiB / 97887 MiB |

## Kill 结果
- 共 kill 了 **0** 个进程（两台服务器均无 GPU 进程）
- 所有 GPU 已释放: **YES**

注：westd-34685 GPU 1 显示 100% utilization 但无进程且显存为 0，这是 nvidia-smi 的瞬态残留，会自行归零。

---
