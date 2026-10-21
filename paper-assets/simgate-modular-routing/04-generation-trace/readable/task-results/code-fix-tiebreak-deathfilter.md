# code fix tiebreak deathfilter

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-tiebreak-deathfilter_20260513T074437_result.json`
- **Structured JSON:** [`e00556dae8a077fd7b62.json`](../../sessions/e0/e00556dae8a077fd7b62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**修复 1 — Tie-break**: `phase1_signal.py:273` `>=` → `>`，相等 delta 时 oracle 选 deterministic

**修复 2 — 致死动作过滤**: 
- 新增 `is_lethal(fr)` 函数（line 44），检查 `done+score<0` 或 `score<=-100`
- **always-internal** (line 74-83): fork 检查 LLM 选出的 action，致死则移除重选，最多 3 次
- **always-deterministic** (line 149-167): fork 评估时跳过致死候选，fallback 到最佳全量候选
- **oracle** (line 230-267): 两条线都加过滤，fallback 逻辑一致

**实验 `mvp-p1-gpu1-v2`**: 已在 westb-13313 GPU1 上启动，正在运行 chemistry-mix-paint-secondary-color Episode 0。Registry 已更新为 RUNNING。

---
