# ssh p1 ee check training alive

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p1_ee_check_training_alive_20260518T200014_result.json`
- **Structured JSON:** [`25407d5aa560b4e33008.json`](../../sessions/25/25407d5aa560b4e33008.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/p1_ee_training_check.md`。

**结论**: PID 55834 已崩溃，从未进入训练循环。

- 进程在模型加载完成后，`adjust_generation_fn()` 尝试从 HuggingFace Hub 下载 `custom_generate/generate.py` 时因网络不可达 (`Errno 101`) 崩溃
- GPU 0 完全空闲 (0% util, 0 MiB)，无 checkpoint 产出
- Log 显示进程仅存活约 9 分钟

**重启前需解决**: 设置 `TRANSFORMERS_OFFLINE=1` 环境变量，让 transformers 跳过远程下载，仅用本地缓存。是否现在重启训练？

---
