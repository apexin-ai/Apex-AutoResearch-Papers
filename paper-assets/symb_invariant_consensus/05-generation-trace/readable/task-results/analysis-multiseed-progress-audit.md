# analysis multiseed progress audit

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multiseed-progress-audit_20260522T165940_result.json`
- **Structured JSON:** [`f79ff3b0204f80d1a8ff.json`](../../sessions/f7/f79ff3b0204f80d1a8ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Multi-seed 进度总览

**根分区 100% 满 (30G/30G)**，导致两个实验写文件时崩溃。数据盘 `/root/autodl-tmp` 还有 137GB 空闲。

### cuda:1 LLaMA-8B FOLIO (204 problems/seed) — vLLM port 8002
| seed | 状态 | 详情 |
|------|------|------|
| 123 | **完成** 204/204 | |
| 456 | **完成** 204/204 | |
| 789 | **崩溃** 189/204 | `OSError: No space left on device` — 根分区满 |

### cuda:2 Mistral-7B PW (600 problems/seed) — vLLM port 8003
| seed | 状态 | 详情 |
|------|------|------|
| 42 | **完成** 600/600 | |
| 123 | **完成** 600/600 | |
| 456 | **在跑** 440/600 | ETA ~79 min (~160 remaining) |
| 789 | **未开始** | |

### cuda:3 LLaMA-8B PW (600 problems/seed) — vLLM port 8004
| seed | 状态 | 详情 |
|------|------|------|
| 42 | **崩溃** 223/600 | `OSError: No space left on device` — 根分区满 |
| 123 | **未开始** | 无结果目录 |
| 456 | **未开始** | 无结果目录 |

### 额外已完成（非用户问的三组，但在 multi_seed 目录下）
- Qwen2.5 FOLIO: seed 123/456/789 全部 204/204 ✓
- Qwen2.5 PW: seed 123/456/789 全部 600/600 ✓
- Mistral FOLIO: seed 123/456/789 全部 204/204 ✓

### 阻塞问题
**根分区 `/` 已满 (30G used / 30G total)**。cuda:1 和 cuda:3 的实验都因此崩溃。需要清理根分区空间或将结果目录改写到 `/root/autodl-tmp/`，否则恢复运行后仍会崩。

### 可分流到 westd-14391 的任务
- LLaMA-8B FOLIO seed=789（仅剩 15 problems，但需先解决磁盘问题）
- LLaMA-8B PW seed=123, seed=456（未开始，各 600 problems）
- Mistral-7B PW seed=789（未开始，600 problems）

---
