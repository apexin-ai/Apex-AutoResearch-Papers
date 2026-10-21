# prep object eval commands

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_object-eval-commands_20260514T031605_result.json`
- **Structured JSON:** [`b20f6fef0b415d8fb3ff.json`](../../sessions/b2/b20f6fef0b415d8fb3ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 组 object eval 命令已准备好，写入 `artifacts/object_eval_commands.md` 并注册。

命令模式直接从 running spatial 实验镜像而来，`--benchmark spatial` → `--benchmark object`：

| exp_id | mode | Server / GPU | 依赖 |
|--------|------|-------------|------|
| eval-acr-object | acr_vla, K=10, per-DOF CRM | bjb1 GPU 0 | spatial evals done |
| eval-reconvla-object | reconvla, K=10 | bjb1 GPU 1 | spatial evals done |
| eval-scalar-unc-object | crm_scalar, K=10 | bjb1 GPU 2 | spatial evals done |
| eval-vla-mean-object | vla_only, baseline_mode=mean | bjb2 GPU 0 | eval-vla-mean-spatial done |
| eval-k5-object | crm_perdof, K=5 | bjb1 GPU 3 | crm-train-k5 done |

VLA-only K=1 baseline 已有结果（13%），无需重跑。eval-k5-object 需等 crm-train-k5 出 checkpoint。

---
