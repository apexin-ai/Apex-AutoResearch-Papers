# urgent westd38929 disk cleanup

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_westd38929_disk_cleanup_20260525T135530_result.json`
- **Structured JSON:** [`7a1a384aae590cbade7b.json`](../../sessions/7a/7a1a384aae590cbade7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**磁盘使用对比：**

| | Used | Avail | Use% |
|---|---|---|---|
| 清理前 | 247G | 3.2G | 99% |
| 清理后 | 240G | 11G | 96% |

**释放 ~7.8G，可用空间从 3.2G → 11G。**

清理内容：
- `.cache/huggingface/` 下载缓存（6个目录共 ~5G）— 模型已提取，缓存纯冗余
- `lora_adapter_bak/` — 925M 备份adapter
- `libero_plus_dl/.cache/` — 1.8G
- pip cache — 635个文件（在root分区）
- `__pycache__` + `.pyc` + 备份文件 + build目录

11G 可用空间足够 2 个运行中实验保存结果 JSON（单个 JSON <1MB）。eval_results/ 目录未触碰。

---
