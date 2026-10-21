# ops bjb2 scalar unc check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb2-scalar-unc-check_20260515T013447_result.json`
- **Structured JSON:** [`0ae6a93dbe1ed52e37d9.json`](../../sessions/0a/0ae6a93dbe1ed52e37d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，汇报如下：

---

## 1. eval-vla-mean-spatial-t10 残留

- **tmux**: 无残留 session（no server running）
- **结果文件**: 已生成 `/root/autodl-tmp/eval_results/eval-vla-mean-spatial-t10.json`，内容：
  - mode=vla_only, baseline_mode=mean, benchmark=spatial, n_rollouts=10
  - **overall_success_rate = 0.1**（1/10 成功，单任务 pick_up_black_bowl）
  - 实验已正常结束

## 2. eval-acr-spatial-v4-scalar 就绪检查

| 项目 | 状态 | 说明 |
|------|------|------|
| CRM checkpoint `crm_v3/scalar_unc/crm_best.pt` | ✅ 存在 | 1.3MB, 2026-05-15 02:25 |
| Precompute cache v5 `crm_cache_v5/spatial/` | ❌ 不存在 | bjb2 只有 `/root/autodl-tmp/crm_cache/spatial/`（无版本号目录名），manifest 无 version 字段，K=10, n_samples=2402 |
| `evaluate.py` | ✅ 存在 | 14489 bytes, 修改于 2026-05-15 06:26 |
| Git repo | ❌ 不是 git 仓库 | `.git` 不存在，无法确认代码版本 |
| Python/PyTorch | ✅ | torch 2.10.0+cu128, CUDA 可用 |

## 3. 缺少的内容

需要从 bjb1 同步或确认：

1. **crm_cache_v5**: bjb2 上的 cache 在 `/root/autodl-tmp/crm_cache/spatial/`，路径不匹配 `crm_cache_v5`。需要确认：
   - 这个 cache 是否就是 v5（只是路径不同），可以通过软链接解决
   - 还是需要重新从 bjb1 同步 v5 版本的 cache
2. **代码同步**: bjb2 上没有 `.git`，无法确认 evaluate.py 版本是否最新。建议从 bjb1 同步代码或重新 git clone。

---
