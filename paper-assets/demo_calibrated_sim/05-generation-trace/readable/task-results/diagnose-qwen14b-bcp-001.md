# diagnose qwen14b bcp 001

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_qwen14b-bcp-001_20260513T151615_result.json`
- **Structured JSON:** [`69bd1d0f67e62f4a7a66.json`](../../sessions/69/69bd1d0f67e62f4a7a66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**qwen14b-bcp-001 结果：成功完成，BCP 失败机制在 14B scale 复现。**

| Run | Completion | Politeness | Question Rate | H1 | H2 | H3 | Overall |
|-----|-----------|------------|---------------|----|----|----|----|
| 1 | 73.7% | 0.470 | 0.037 | ✅ | ❌ | ✅ | ❌ |
| 2 | 55.0% | 0.588 | 0.035 | ✅ | ✅ | ✅ | ✅ |
| 3 | 57.9% | 0.497 | 0.054 | ✅ | ❌ | ✅ | ❌ |
| 4 | 60.0% | 0.536 | 0.041 | ✅ | ❌ | ✅ | ❌ |

- **Mean completion: 61.6%**
- **H2（校准改进门）仅 1/4 passes** — 模型无法有效向目标行为 profile 校准
- H1（基线质量）和 H3（任务完成保持）全部通过
- 与 7B 模型一致：BCP 失败的核心瓶颈在 H2

Registry 已更新为 DONE/success，cron 已清除。

---
