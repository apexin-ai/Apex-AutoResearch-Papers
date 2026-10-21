# research tatsu patch plan

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_tatsu_patch_plan_20260516T235416_result.json`
- **Structured JSON:** [`acc98105e374aeb00b31.json`](../../sessions/ac/acc98105e374aeb00b31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署方案已写入 `artifacts/exp029_episode_level/tatsu_patch_deploy_plan.md`。

核心改动 3 处:
1. 创建 `patches/__init__.py`（使其可 import）
2. `train.py` 顶部加 `import patches.tatsu_parallel_fix`
3. `config/envs.yaml` 中 `AlfworldSG` 设为 `parallel_friendly: true, max_workers: 4`

回滚只需把 `parallel_friendly` 改回 false，patch import 本身无副作用。

---
