# ops cqa1 disk cleanup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-disk-cleanup_20260519T214031_result.json`
- **Structured JSON:** [`d996168b7692f165c069.json`](../../sessions/d9/d996168b7692f165c069.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GSM8K eval (PID 285390) 仍正常运行。

**清理结果：**

| 阶段 | 删除内容 | 释放空间 |
|------|---------|---------|
| Phase 1 | `.hf_cache/models--Qwen--Qwen2.5-3B/`, `models--Qwen--Qwen2.5-0.5B/`, `models--sentence-transformers--*` × 2 | ~8GB |
| Phase 2 | `Llama-3.2-3B_d{000,005,025,100}_s42/merged/` × 4 | ~24GB |
| Phase 3 | `structfuse/m1_extraction/` | ~13GB |
| **总计** | | **~45GB** |

**磁盘状态：** 98% (4.7GB free) → **72% (49GB free)**

未删除：所有 eval 结果、所有 lora_adapter、所有基模型（被 adapter_config 引用的路径完整保留）、所有 .log 文件。Llama merged 模型如需要可从 base + adapter 重建。

---
