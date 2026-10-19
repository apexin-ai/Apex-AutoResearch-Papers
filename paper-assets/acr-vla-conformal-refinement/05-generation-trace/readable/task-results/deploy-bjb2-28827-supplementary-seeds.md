# deploy bjb2 28827 supplementary seeds

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-supplementary-seeds_20260521T070803_result.json`
- **Structured JSON:** [`c14082fba6e1f7631ef9.json`](../../sessions/c1/c14082fba6e1f7631ef9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 部署结果

**bjb2-28827 GPU 状态：**

| GPU | 状态 | 实验 |
|-----|------|------|
| 0 | **已部署** | Spatial CRM obs_only seed45 (新) |
| 1 | 占用 | Object crm_obs_only seed77 norm003 (PID 979385) |
| 2 | 占用 | Object crm_obs_only seed78 norm003 (PID 980044) |
| 3 | 占用 | Object crm_obs_only seed76 norm005 (PID 981089) |
| 4 | 占用 | Object crm_obs_only seed77 norm005 (PID 982680) |
| 5 | 占用（保留） | K=20 Object seed45 (PID 23401) |

**新部署：**
- **GPU 0** → `eval-spatial-obs-only-seed45` — Spatial CRM obs_only, seed=45, K=10, norm=0.2
- tmux session: `spatial_obs_only_s45`
- 模型加载中，进程已启动
- Registry 已注册为 RUNNING，标记 low-priority

只有 1 张卡空闲，无法部署 seed46/47 或 vla_only 实验。

---
