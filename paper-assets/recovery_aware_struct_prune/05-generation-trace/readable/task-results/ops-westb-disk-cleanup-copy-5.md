# ops westb disk cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_disk_cleanup_20260515T201023_result.json`
- **Structured JSON:** [`2d704de68106dadd7bd6.json`](../../sessions/2d/2d704de68106dadd7bd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 清理前磁盘状态
| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| 根分区 `/` | 30G | 8.6G | 22G | 29% |
| 数据盘 `/root/autodl-tmp` | 250G | 177G | **74G** | 71% |

### 空间占用明细
| 目录 | 大小 | 状态 |
|------|------|------|
| sft_rasp_20 | 81G | 保留 |
| sft_standard_20 | 81G | 保留（v8 base model） |
| DeepSeek-R1-Distill-Qwen-7B | 15G | 保留 |
| data | 1.5G | 保留 |
| GRPO v1-v7 所有目录 | **< 500K 合计** | 无实质 checkpoint |
| `recovered_*` | 不存在 | 已被清理过 |

### 无需清理
旧 GRPO 目录（v1-v7）全部为空或仅含配置文件（最大 172K），`recovered_*` 目录已不存在。**没有可清理的大文件。** 74G 空闲远超 checkpoint 需求（~15-25G），v8 可以安全保存。

### GRPO v8 进程健康
- **PID 534667**: 运行中，已跑 5h28m
- **GPU 1**: 71701/97887 MiB (73%), 利用率 98%
- **GPU 0**: 空闲
- **命令**: `train_grpo_v5.py`, output_dir 指向 `grpo_stage2_standard_20_v8`, save_steps=50, max_steps=100

**结论：磁盘空间充足，无需清理。GRPO v8 进程健康运行中。**

---
