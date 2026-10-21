# deploy bjb2 28827 4gpu crm long

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-4gpu-crm-long_20260519T190719_result.json`
- **Structured JSON:** [`9a4f26a3de00c7240d98.json`](../../sessions/9a/9a4f26a3de00c7240d98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部部署完成，registry 已更新为 RUNNING。

**bjb2-28827 GPU 分配汇总：**

| GPU | 实验 | 模式 | Suite | Seed | PID |
|-----|------|------|-------|------|-----|
| 0 | eval-vla-only-object-seed47 | vla_only (K=1) | LIBERO-Object | 47 | 959564 |
| 1 | eval-argmin-object-k5-seed44-r2 | reconvla (K=5) | LIBERO-Object | 44 | 901523 |
| 2 | eval-crm-long-seed42 | crm_obs_only (K=10, ε=0.2) | LIBERO-10 | 42 | 959637 |
| 3 | eval-crm-long-seed43 | crm_obs_only (K=10, ε=0.2) | LIBERO-10 | 43 | 959901 |
| 4 | eval-openvla-object-baseline-seed42 | OpenVLA baseline | LIBERO-Object | 42 | (running) |
| 5 | eval-crm-long-seed44 | crm_obs_only (K=10, ε=0.2) | LIBERO-10 | 44 | 960107 |

6 卡满载。CRM checkpoint: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`，benchmark 参数用 `--benchmark long`（映射到 `libero_10`）。

---
