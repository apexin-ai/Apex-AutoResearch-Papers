# ops westd quick status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-quick-status-check_20260518T083431_result.json`
- **Structured JSON:** [`c4687f6712feeb08fe1d.json`](../../sessions/c4/c4687f6712feeb08fe1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载状态（2026-05-18 16:34 CST）：

| 模型 | 大小 | incomplete 文件 | safetensors | 状态 |
|------|------|----------------|-------------|------|
| **Qwen2.5-7B** | 11G | **2** | 2 | 下载中 |
| Qwen2.5-14B | 15G | 6 | 2 | 下载中 |
| gemma-2-9b | 8.0G | 8 | 0 | 下载中 |
| phi-4 | 1.2G | 6 | 0 | 下载中 |
| OLMo-2-1124-7B | 13G | 6 | 0 | 下载中 |

**Qwen2.5-7B 尚未完成**，还有 2 个 incomplete 文件。

5 个模型全部在活跃下载中：
- Qwen2.5-7B / Qwen2.5-14B 由 `download_all.sh` 脚本驱动
- gemma-2-9b / phi-4 / OLMo-2-1124-7B 各有独立 screen 会话（`dl_gemma`, `dl_phi4`, `dl_olmo2`）

磁盘剩余：**203G**。GPU 全部空闲（0 MiB used），GPU 3 utilization 显示 100% 但无显存占用，可能是残留状态。

---
