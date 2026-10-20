# ops westd disk cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_disk_cleanup_20260520T092839_result.json`
- **Structured JSON:** [`c7a85852a607a6be0a7c.json`](../../sessions/c7/c7a85852a607a6be0a7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

## 磁盘清理报告

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 数据盘已用 | 594G (96%) | 550G (89%) |
| 数据盘可用 | 26G | **70G** |

### 删除明细

| 文件 | 大小 |
|------|------|
| `grpo_stage2_standard_20_fair/checkpoint-100/optimizer.pt` | 15G |
| `grpo_standard_20_seed123/checkpoint-100/optimizer.pt` | 15G |
| `grpo_standard_20_seed456/checkpoint-100/optimizer.pt` | 15G |
| **总计释放** | **~44G** |

### 备注
- seed123/seed456 无中间 checkpoint 可删（只有 final checkpoint-100）
- `grpo_stage2_rasp_20_fair` 的 optimizer.pt 不存在（已清理过）
- 所有模型权重（model.safetensors）、配置、日志均保留完整
- **70G 可用空间**，超额完成 ≥30GB 目标

---
