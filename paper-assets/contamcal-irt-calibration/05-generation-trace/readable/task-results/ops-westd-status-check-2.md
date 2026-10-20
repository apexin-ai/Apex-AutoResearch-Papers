# ops westd status check 2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-status-check-2_20260518T084154_result.json`
- **Structured JSON:** [`33c5b9019561aa37430c.json`](../../sessions/33/33c5b9019561aa37430c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载状态汇总：

| 模型 | 大小 | incomplete | safetensors | 状态 |
|------|------|-----------|-------------|------|
| Qwen2.5-7B | 12G | **2** | 2 | 未完成 |
| Qwen2.5-14B | 15G | 6 | 2 | 未完成 |
| gemma-2-9b | 9.9G | 8 | 0 | 未完成 |
| phi-4 | 1.6G | 6 | 0 | 未完成 |
| OLMo-2-1124-7B | 13G | 5 | 1 | 未完成 |

- 磁盘可用：200G
- GPU：4 卡全部空闲（0 MiB）

**Qwen2.5-7B 未完成**：仍有 2 个 `.incomplete` 文件，只有 2/4 个 safetensors。所有模型都还在下载中或下载中断。需要检查下载进程是否还在运行。

---
