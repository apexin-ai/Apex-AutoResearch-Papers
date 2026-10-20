# fix cuda0 zombie

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cuda0_zombie_20260513T061610_result.json`
- **Structured JSON:** [`be536e6691376f78e0aa.json`](../../sessions/be/be536e6691376f78e0aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出

### 1. 占用进程
cuda:0 上**无任何进程**。nvidia-smi、fuser、lsof 均未检测到持有 GPU 0 的进程。

### 2. 清理操作和结果
| 操作 | 结果 |
|------|------|
| `nvidia-smi --gpu-reset -i 0` | **Not Supported**（容器环境不允许） |
| `torch.cuda.empty_cache()` | 无效（无进程持有显存） |
| Python 分配+释放大块显存 | 无效，幽灵显存未回收 |
| lsof/fuser 查找隐藏进程 | 未发现任何进程 |

**结论：** 49GB 幽灵显存是驱动层面泄漏（可能是之前进程崩溃后未释放），在当前容器环境下无法通过用户态操作清理。**需要重启实例才能彻底释放。**

### 3. cuda:0 最终状态：**可用（受限）**
cuda:0 功能正常，可以分配和计算，但可用显存减半。

### 4. 显存状态
| GPU | Used | Free | Total |
|-----|------|------|-------|
| cuda:0 | 49,175 MiB (幽灵) | **46.3 GiB** | 95.0 GiB |
| cuda:1 | 21,687 MiB (PID 170483 Phase 2) | ~74.2 GiB | 95.0 GiB |

**cuda:0 仍有 46.3 GiB 可用**，足以运行 GPT-2 级别的实验。如需完整 95 GiB，需等 Phase 2 训练结束后重启实例。

---
