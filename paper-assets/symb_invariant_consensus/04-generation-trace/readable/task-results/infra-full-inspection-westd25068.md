# infra full inspection westd25068

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_full-inspection-westd25068_20260521T190444_result.json`
- **Structured JSON:** [`48b24669e10122d4d3da.json`](../../sessions/48/48b24669e10122d4d3da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-25068 巡检报告（2026-05-22 03:05 CST）

### GPU 状态

| GPU | 型号 | 显存占用 | 利用率 | 分配 |
|-----|------|---------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 89.3/97.9 GB (91%) | 94% | vLLM 72B AWQ tp=4 |
| 1 | RTX PRO 6000 Blackwell | 89.3/97.9 GB (91%) | 88% | vLLM 72B AWQ tp=4 |
| 2 | RTX PRO 6000 Blackwell | 89.3/97.9 GB (91%) | 94% | vLLM 72B AWQ tp=4 |
| 3 | RTX PRO 6000 Blackwell | 89.3/97.9 GB (91%) | 94% | vLLM 72B AWQ tp=4 |

**空闲 GPU: 0**

---

### 实验状态

| 实验 | 进程 | 状态 | 进度 | ETA | 备注 |
|------|------|------|------|-----|------|
| **70B AWQ SICA** (vLLM) | PID 39013 | ALIVE | — | — | port 8002, Qwen2.5-72B-Instruct-AWQ, tp=4 |
| **70B AWQ SICA** (pipeline) | PID 40007 | ALIVE | **52/204** (25.5%) | **~2.6h** | 正在跑 folio_51, avg 61.8s/prob, 153 remaining |
| **Gemini-2.5-pro SC** | PID 19972 | ALIVE | **80/204** (39.2%) | **~6.0h** | sc_acc=88.75% (71/80), avg ~175s/prob, 124 remaining |

### 70B SICA 详情
- 02:23 启动，当前本轮完成 folio_12→folio_50（39个），加上之前 resume 的 12 个，共 52/204
- vLLM 吞吐：~150-466 tokens/s，prefix cache hit 70%，KV cache 用量极低 (0.2-0.6%)
- 最新日志（folio_50）: SICA=False, SC=False, 82 constraints→13 unique, solve 0.6ms

### Gemini SC 详情
- 进程活着但无独立日志文件（logs/ 下无 gemini 文件）
- results.json 最后更新 02:57（~8min 前），正常——应在处理下一个 problem 后批量写入
- wall_time 已达 14041s（~3.9h）

### 磁盘

| 分区 | 容量 | 已用 | 剩余 |
|------|------|------|------|
| / (根) | 30G | 19G (61%) | 12G |
| /root/autodl-tmp | 250G | 60G (24%) | 191G |

---
