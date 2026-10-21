# analysis collect qwen7b gsm8k cqa1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_collect-qwen7b-gsm8k-cqa1_20260521T034751_result.json`
- **Structured JSON:** [`8612e5fa0656a4780fa3.json`](../../sessions/86/8612e5fa0656a4780fa3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**eval 状态：STILL RUNNING**（不是 failed）

PID 435752 正在 GPU 0 上跑 `d025_s0` GSM8K eval（已运行 35 分钟），脚本按 d000→d005→d025→d050→d100 顺序执行。

### 已完成的 GSM8K accuracy (s0)

| Dosage | Accuracy | Correct/Total | Δ vs d000 |
|--------|----------|--------------|-----------|
| d000 | 73.31% | 967/1319 | — |
| d005 | 78.32% | 1033/1319 | **+5.00pp** |
| d025 | *running* | — | — |
| d050 | pending | — | — |
| d100 | pending | — | — |

### GPU 状态

| GPU | Memory | Util | Process |
|-----|--------|------|---------|
| 0 | 17125/24564 MiB | 83% | PID 435752 — d025_s0 GSM8K eval |

### 建议

- Registry 应改为 RUNNING（进程仍活跃），不需要干预
- d005 的 +5.00pp 在 7B 模型上是显著的 contamination effect
- 按 d000/d005 各约 40 分钟推算，d025/d050/d100 预计还需 ~2 小时完成

---
