# diagnose exp029 seed3 episode

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp029_seed3_episode_20260520T170945_result.json`
- **Structured JSON:** [`e663e28f28800039cfb5.json`](../../sessions/e6/e663e28f28800039cfb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**失败原因**：Hydra override `seed=42` 将 `config.seed` 设为 `int`，但 `es_manager.py:44` 调用 `seed_cfg.get(mode, None)` 期望 dict 类型 → `AttributeError: 'int' object has no attribute 'get'`。启动阶段即 crash，无训练产出。

**已修复**：v2 实验已将 seed 改为 `{train: 42, val: 123}` 并正在运行（W&B run ID: `0t58u17b`，GPU 2,3 正常占用）。

报告已写入 `artifacts/diagnose_exp029_seed3.md`。

---
