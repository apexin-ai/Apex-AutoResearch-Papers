# ops check docred progress est

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_docred_progress_est_20260514T032245_result.json`
- **Structured JSON:** [`ab3e594ded3315585064.json`](../../sessions/ab/ab3e594ded3315585064.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## DocRED Phase 2 进度报告

| | **grammar_only** (GPU 0) | **full_s1** (GPU 1) |
|---|---|---|
| **完成** | **254 / 998** (25.5%) | **107 / 998** (10.7%) |
| **PID** | 150766 | 157047 |
| **启动时间** | 09:54 (+0800) | 11:16 (+0800)，刚重启 with `--resume` |
| **运行时长** | ~1h29m | ~7min（模型刚加载完） |
| **速度** | ~17s/doc ≈ **212 docs/hr**（近期） | 尚无新数据，预估 ~17-20s/doc |
| **剩余** | 744 docs | 891 docs |
| **预计完成** | ~**14:55 (+0800) / 06:55 UTC** | ~**16:00 (+0800) / 08:00 UTC** |
| **GPU 利用率** | 85%, 17.4GB VRAM | 81%, 17.1GB VRAM |

**备注**：
- grammar_only 无 tmux session（用 nohup 后台跑），进程正常运行中
- full_s1 刚从 doc 107 resume，模型加载完毕，即将开始推理
- Semantic masking fallback: **0 次触发**
- 两块 RTX PRO 6000 (98GB) 各占 ~17GB，运行正常

---
