# ops disk cleanup execute

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-execute_20260512T161843_result.json`
- **Structured JSON:** [`3eabac46ddbdcad2bc97.json`](../../sessions/3e/3eabac46ddbdcad2bc97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理报告

| 删除项 | 大小 |
|--------|------|
| GPT-2 缓存 ×3（models--gpt2 + openai-community--gpt2 + hub/models--gpt2） | 8.4G |
| SWE-smith 数据集缓存（hub + arrow + metadata.jsonl） | 5.2G |
| v3 有毒轨迹数据（trajectories_v3 + trajectories_v3_test） | 400K |
| Qwen2.5-7B HF cache 重复元数据 | 4K |

**总回收：~13.6G**

| 分区 | 清理前 | 清理后 |
|------|--------|--------|
| `/root/autodl-tmp` | 169G/169G (100%, 496K 可用) | 156G/169G (93%, **14G 可用**) |
| `/` (根分区) | 12G/30G (39%) | 不变 |

数据盘从满盘恢复到 14G 可用空间，够 fix Worker 写新样本。保留了 `models/Qwen2.5-7B-Instruct`（552M）、structfuse 目录、所有 Qwen3 相关文件均未动。

---
