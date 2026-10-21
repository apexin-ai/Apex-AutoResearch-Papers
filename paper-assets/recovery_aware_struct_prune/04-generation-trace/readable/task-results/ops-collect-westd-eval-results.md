# ops collect westd eval results

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-westd-eval-results_20260515T192852_result.json`
- **Structured JSON:** [`c827d35b832757f8b64f.json`](../../sessions/c8/c827d35b832757f8b64f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 cron 需要清理。

## 结果汇总

| Model | westd N=100 | westb 预期 | 偏差 |
|-------|-------------|-----------|------|
| **RASP 20%** | **67%** (±4.7%, eos=0.99, avg_len=182) | ~57% | **+10pp** ⚠️ |
| **Standard 20%** | **63%** (±4.8%, eos=0.97, avg_len=260) | ~64% | -1pp ✓ |

关键发现：
- **Standard**: westd 63% ≈ westb 64%，cross-server reproducibility 确认
- **RASP**: westd 67% >> westb 57%，偏差 10pp，**RASP 在 westd 上反超 Standard 4pp**（westb 上 Standard 领先），cross-server reproducibility 未确认
- 两个 registry 条目已更新为 DONE，metrics 和偏差分析已记录

RASP 在 westd 表现异常好，需要 N=1319 full eval 确认是 N=100 采样方差还是真实差异。

---
