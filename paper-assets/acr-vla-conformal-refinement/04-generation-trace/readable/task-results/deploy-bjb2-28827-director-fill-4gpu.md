# deploy bjb2 28827 director fill 4gpu

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-director-fill-4gpu_20260520T141758_result.json`
- **Structured JSON:** [`fb9d9551a151c831e5e8.json`](../../sessions/fb/fb9d9551a151c831e5e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

latency profiling 已正常跑完，输出了 JSON 结果。

4 个实验全部部署完毕，3 个 CRM 实验正在运行。汇总：

| GPU | exp_id | tmux session | Python PID | 状态 |
|-----|--------|-------------|------------|------|
| cuda:0 | eval-crm-k1-object-seed42-plan702 | eval-crm-k1-object-seed42-plan702 | 381023 | 运行中 |
| cuda:1 | eval-crm-k1-object-seed43-plan702 | eval-crm-k1-object-seed43-plan702 | 381299 | 运行中 |
| cuda:2 | eval-obs-only-spatial-norm02-seed49 | eval-obs-only-spatial-norm02-seed49 | 357304 | 已有实验（未动） |
| cuda:3 | openvla-precompute-k1 | openvla-precompute-k1 | — | 未动 |
| cuda:4 | eval-latency-profiling-v1 | — | — | **已完成** |
| cuda:5 | eval-crm-k1-object-seed44-plan702 | eval-crm-k1-object-seed44-plan702 | 381573 | 运行中 |

**修复了 `evaluate.py:457` 的 bug**：`crm_k1_accg` 模式下 `unc_dim` 未定义导致 `UnboundLocalError`。将 `ConformalRefinementModule` 初始化代码移入 `else` 分支，使其只在非 `crm_k1_accg` 模式下执行。备份在 `src/evaluate.py.bak`。

---
