# diagnose plan 006 deep internal

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan-006-deep-internal_20260515T161622_result.json`
- **Structured JSON:** [`d347ab56747f6b40c6f7.json`](../../sessions/d3/d347ab56747f6b40c6f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写入 `artifacts/plan-006-deep-internal/failure_diagnosis.md`。

**核心结论**：

- **根因**：两个并行进程都用了 `CUDA_VISIBLE_DEVICES=0`，在同一块 32GB GPU 上跑两个 vLLM 实例（各要 85% 显存），GPU 1 全程空闲。Process 1 还错误地包含了全部 6 个任务而非计划的 2 个。
- **死亡方式**：GPU 显存竞争导致 vLLM EngineCore 崩溃（`Engine core proc EngineCore died unexpectedly`），进程在 chemistry-mix 未完成时终止，无 sentinel 文件。
- **数据现状**：117/120 episodes 已收集（97.5%），chemistry-mix 差 3 集，补充进程正在跑。但两进程同写一目录，需去重检查。
- **当前风险**：服务器上两个补充进程又在 GPU 0 上竞争，重演相同模式，建议 kill 一个。

---
