# ops urgent disk cleanup

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-disk-cleanup_20260512T185945_result.json`
- **Structured JSON:** [`4d9ab49e87ec8591ba0c.json`](../../sessions/4d/4d9ab49e87ec8591ba0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

情况汇报：

**HF cache 中 Qwen3 目录只有 4K（空壳），删除无意义。** 实际空间占用：

| 目录 | 大小 | 状态 |
|------|------|------|
| `structfuse/` | 88GB | 无进程占用，不同项目 |
| `models/Qwen2.5-7B-Instruct-DPO-merged/` | 15GB | 无进程占用 |
| `models/Mistral-7B-Instruct-v0.3/` | 14GB | 无进程占用，与本项目无关 |
| `models/Qwen/` | 15GB | **dpo-003 正在使用，不能删** |

好消息：LoRA checkpoint 只有 ~64MB，3.9GB 暂时够用，不会立即写入失败。

**建议立即删除 Mistral-7B（14GB，与本项目完全无关），释放到 ~18GB。** 要不要也删 `Qwen2.5-7B-Instruct-DPO-merged`（15GB）或 `structfuse`（88GB）？

---
