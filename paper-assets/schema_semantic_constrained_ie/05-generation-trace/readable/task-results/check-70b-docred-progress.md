# check 70b docred progress

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_70b_docred_progress_20260521T115430_result.json`
- **Structured JSON:** [`cb6461bd0aa843e249d5.json`](../../sessions/cb/cb6461bd0aa843e249d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 70B DocRED ZS 实验进度

**服务器**: westd-21461

### Unconstrained 运行状态
| 指标 | 值 |
|------|-----|
| PID | 247853 (运行中) |
| 已运行 | 6h49m |
| 进度 | **758 / 998** (75.9%) |
| 速度 | ~1.85 samples/min (~32.4 sec/sample) |
| GPU | GPU 1: 39.8GB / 95.8GB, 93% 利用率 |

### S1 (Constrained) 状态
- **未开始** — s1.jsonl 不存在
- 启动脚本 `run_70b_docred_zs.sh` 是串行执行：先跑 unconstrained，完成后自动跑 s1
- 当前 s1.log 实际是整个脚本的 nohup 输出

### 预估完成时间
| 阶段 | 剩余 | 预估完成 |
|------|------|----------|
| Unconstrained | 240 samples ≈ **2h10m** | ~22:05 今晚 |
| S1 (Constrained) | 998 samples ≈ **9h+** | ~明早 07:00+ (May 22) |

约束解码可能比 unconstrained 更慢，S1 实际耗时可能更长。两个 jsonl 全部完成预计 **5月22日上午**。

---
