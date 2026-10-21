# deploy bjb1 18228 cuda2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-18228-cuda2_20260526T064435_result.json`
- **Structured JSON:** [`bb82b1e1d20a1bba62ed.json`](../../sessions/bb/bb82b1e1d20a1bba62ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-18228 报告

### 新部署
- **pi05-adaptive-goal-s43-bjb1-18228 on cuda:2**: 启动成功（tmux session 已建，PID 42110 加载 PI05 中，VRAM 尚未分配）

### GPU 状态

| GPU | 实验 | 进度 | VRAM | 预计完成 |
|-----|------|------|------|---------|
| 0 | pi05 crm_obs_only long s42 (norm=0.05) | task 4/10 (KITCHEN_SCENE4 100% 完成, SR=16/20) | 12793 MiB | ~4-5h |
| 1 | pi05 crm_obs_only long s43 (norm=0.05) | task 4/10 (KITCHEN_SCENE4 15/20, SR=12/15) | 13156 MiB | ~4-5h |
| 2 | **pi05-adaptive-goal-s43-bjb1-18228** | starting（loading PI05 weights） | 4 MiB | ~6-7h |
| 3 | pi05 adaptive_conformal_crm long s42 | task 4/10 完成（KITCHEN_SCENE4 SR=19/20） | 13120 MiB | ~4-5h |

### 已完成未 harvest
- 无新的完成实验（GPU 0/1/3 全部仍在 long benchmark KITCHEN_SCENE4 阶段，约 40% 进度）

注：3 个在跑实验皆为 `long` benchmark（10 个 KITCHEN_SCENE 任务），已运行约 7h。Director 描述与实际命令大致一致（GPU 0/1 是 `crm_obs_only` 模式而非纯"CRM"，参数 K=2/norm=0.05；GPU 3 是 adaptive_conformal_crm s42 = Adaptive Long s42 ✓）。

---
