# analysis gpu status check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpu-status-check_20260522T145445_result.json`
- **Structured JSON:** [`8d874f315a7ca48cb397.json`](../../sessions/8d/8d874f315a7ca48cb397.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-16639 GPU 状态汇总

### GPU 0 — Qwen2.5-14B × ProofWriter (port 8005)
| 项目 | 值 |
|------|-----|
| vLLM PID | 551459, 90GB VRAM, 97% util |
| 状态 | **全部完成** |
| 进度 | seed 123 ✅ / seed 456 ✅ / seed 789 ✅ (3/3) |
| GPU 空闲 | vLLM 服务仍在运行，无活跃实验 |

### GPU 1 — LLaMA-3.1-8B × FOLIO (port 8002)
| 项目 | 值 |
|------|-----|
| vLLM PID | 595559, 88GB VRAM, 96% util |
| 当前任务 | seed 456: **184/204** (20 remaining) |
| ETA | **~12 min** |
| 已完成 | seed 123 ✅ |
| 待运行 | seed 789 |

### GPU 2 — Mistral-7B × ProofWriter (port 8003)
| 项目 | 值 |
|------|-----|
| vLLM PID | 510289, 90GB VRAM, 96% util |
| 当前任务 | seed 456: **184/600** (416 remaining) |
| ETA | **~206 min (~3.4h)** |
| 已完成 | seed 42 ✅ / seed 123 ✅ |

### GPU 3 — LLaMA-3.1-8B × ProofWriter (port 8004)
| 项目 | 值 |
|------|-----|
| vLLM PID | 613436, 88GB VRAM, 96% util |
| 当前任务 | seed 42: **95/600** (505 remaining) |
| ETA | **~493 min (~8.2h)** |
| 待运行 | seed 123, seed 456 |

### PID 存活检查
- **510987**: ✅ 存活
- **596151**: ✅ 存活 (LLaMA FOLIO 主脚本)
- **614142**: ✅ 存活 (LLaMA PW tmux session)

### 总体进度
- **Qwen2.5 PW**: 3/3 seeds 完成，GPU 0 可释放或复用
- **LLaMA FOLIO**: ~12 min 后 seed 456 完成，还剩 seed 789（预计再 ~2h）
- **Mistral PW**: seed 456 进行中，~3.4h 后全部完成
- **LLaMA PW**: 刚开始 seed 42，3 个 seed 全跑完预计 ~24h+

---
