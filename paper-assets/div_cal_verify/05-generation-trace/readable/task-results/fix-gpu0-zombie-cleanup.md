# fix gpu0 zombie cleanup

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gpu0_zombie_cleanup_20260513T152208_result.json`
- **Structured JSON:** [`2f4ec6ea7e4137c75f55.json`](../../sessions/2f/2f4ec6ea7e4137c75f55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

容器内无 rmmod，无法重载内核模块。

## 结论

**GPU 0**: 49175 MiB 被驱动级孤儿内存占用（无任何用户进程持有）。实际可用 ~46 GB / 总计 ~95 GB。

**GPU 1**: 0 MiB 占用，完全空闲，~95 GB 可用。

**已尝试的清理方法（全部失败）**:
- `nvidia-smi --gpu-reset` → 硬件/容器不支持
- `torch.cuda.empty_cache()` + `ipc_collect()` → 无效（不是 PyTorch 管理的内存）
- 关闭/开启 persistence mode → 无效
- 内核模块重载 → 容器内无 rmmod/modprobe
- fuser/kill 进程 → 无进程可杀

**唯一解决办法**: 重启容器实例。这是容器环境下驱动级僵尸内存的唯一清理途径。如果当前不方便重启，GPU 0 仍有 ~46 GB 可用，GPU 1 完全空闲（~95 GB）。

---
