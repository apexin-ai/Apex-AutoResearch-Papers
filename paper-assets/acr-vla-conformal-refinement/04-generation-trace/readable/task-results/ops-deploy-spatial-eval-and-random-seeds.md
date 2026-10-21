# ops deploy spatial eval and random seeds

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-spatial-eval-and-random-seeds_20260519T013257_result.json`
- **Structured JSON:** [`55da869a7c0c6ac01bc9.json`](../../sessions/55/55da869a7c0c6ac01bc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Task A: Spatial CRM — 不存在

两台服务器（bjb1-32546, bjb2-28827）均无 spatial 专用 CRM checkpoint:
- `find ... -path "*spatial*"` 返回空
- 现有 CRM 仅在 `crm_v3_norm/` 下有 `obs_only/`, `perdof/`, `scalar_unc/` 三个变体，无 benchmark 维度区分
- `evaluate.py` 已支持 `--benchmark spatial`，代码侧无障碍

**结论**: 审稿 M2 要求的 Spatial obs_only ε=0.2 多 seed 实验无法部署，需要先确认是否需要训练 Spatial 专用 CRM，还是可以复用现有 `obs_only/crm_best.pt`（该模型可能是在 LIBERO-Object 数据上训练的）。

### Task B: Random Selection 补 seed

| 实验 | 状态 | 服务器 | GPU |
|------|------|--------|-----|
| seed45 (`eval-random-selection-object-seed45`) | **已在运行**, 跳过 | bjb2-28827 | - |
| seed46 (`eval-random-seed46-t16`) | **已部署** | bjb2-28827 | GPU 2 |

---
