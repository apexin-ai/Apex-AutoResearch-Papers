# ops gpu0 orphan cleanup

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu0_orphan_cleanup_20260521T051516_result.json`
- **Structured JSON:** [`715eb082eb134b0532e7.json`](../../sessions/71/715eb082eb134b0532e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**原因**：某个已退出的进程（大概率是之前的训练任务）崩溃或被 kill 后未正确释放 CUDA 显存，导致 49175 MiB 残留在驱动层。无任何用户进程持有该显存。

**已尝试的清理方法及结果**：

| 方法 | 结果 |
|------|------|
| `torch.cuda.empty_cache()` | 无效（仅清理 PyTorch 缓存，驱动层分配不受影响） |
| `nvidia-smi --gpu-reset -i 0` | 不支持（容器环境限制） |
| Kill nvidia-persistenced | 无效（显存不由 persistenced 管理） |
| 卸载 nvidia 内核模块 | 不可行（246 引用计数） |

**结论**：这是 NVIDIA 驱动层的孤儿分配，在容器环境中无法通过用户态操作释放。**需要重启实例**才能清除。

**当前可用显存**：
- cuda:0 — 48712 MiB 可用（97887 - 49175）
- cuda:1 — 97887 MiB 可用

如果当前不方便重启，cuda:0 仍有 ~48 GiB 可用，足够运行 7B 模型的推理或 LoRA 微调。需要我重启实例吗？

---
