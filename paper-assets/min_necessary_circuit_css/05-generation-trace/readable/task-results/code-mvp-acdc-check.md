# code mvp acdc check

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-acdc-check_20260512T123510_result.json`
- **Structured JSON:** [`e1e9b5b4ab2d4a769fa4.json`](../../sessions/e1/e1e9b5b4ab2d4a769fa4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

**进程状态：FAILED（已崩溃）**

| 项目 | 详情 |
|------|------|
| GPU 5 | 完全空闲（0MiB, 0% util），无进程 |
| `mvp_output.log` | 672 bytes，最后修改 20:16（服务器时间），只有 EAP-IG 阶段的输出 |
| 结果文件 | 无 `mvp_results*.json` |

**日志分析：**
- EAP-IG 完成（4/4 batches, ~10s） ✅
- 输出最后一行是 `` `torch_dtype` is deprecated! Use `dtype` instead! ``
- 之后日志截断，无 Edge Pruning / ACDC 的任何输出
- 进程在 EAP-IG 完成后、Edge Pruning 启动前静默崩溃（无 traceback 被捕获到日志）

**前次运行（killed log）参考：** ACDC 曾跑到 23227/32491（~71.5%），在被 kill 前以 4.74 it/s 运行。

**可能原因：** stderr 没有重定向到日志文件，实际错误（可能是 Edge Pruning 初始化时的 import error 或 CUDA 错误）丢失了。需要重新启动时将 stderr 也重定向（`2>&1`），或者先检查 `run_mvp.py` 中 Edge Pruning 阶段的代码逻辑。

---
