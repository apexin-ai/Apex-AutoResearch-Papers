# ops gpu audit and deploy loop16

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-audit-and-deploy-loop16_20260516T153732_result.json`
- **Structured JSON:** [`21d6be3691dfa979ad08.json`](../../sessions/21/21d6be3691dfa979ad08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署成功，GPU 3 已被占用（5664MiB，PID 507989）。

最终审计全部完成。最终状态汇总：

## bjb1-18228 审计
- cuda:0: 占用 by eval_object_obs_only_norm01_seed45 (PID 474319, mode=crm_obs_only, norm=0.1, seed=45)
- cuda:1: 占用 by eval-perdof-object-seed44 (PID 452987, mode=crm_perdof, norm=0.1, seed=44)
- cuda:2: 占用 by eval-perdof-object-norm03-seed44 (PID 505419, mode=crm_perdof, norm=0.3, seed=44) — **已在运行，无需重新部署**
- cuda:3: 占用 by eval-obs-only-object-norm03-seed45-r2 (PID 507989, 刚部署)

## bjb2-40593 审计
- cuda:0: 占用 by eval-perdof-object-default-seed44 (PID 316387, mode=crm_perdof, seed=44, no norm flag)
- 处理措施: **无冲突**。registry 误报 PID 452982 在 bjb2 上，实际该进程在 bjb1:GPU1。bjb2 仅有一个实验正常运行。

## 部署结果
- eval-perdof-object-norm03-seed44: **已在运行**，bjb1:GPU 2, PID=505419（submit_training_job 已部署，n_rollouts=10, --K 10）
- eval-obs-only-object-norm03-seed45-r2: bjb1:GPU 3, PID=507989, 已验证（5664MiB, 20% util）

## 剩余空闲 GPU
- **无**。bjb1-18228 四张卡全部占满。

## 需要你确认的问题
1. **Registry 修正**：eval-perdof-object-seed44 (PID 452982) 实际在 bjb1 而非 bjb2，需要更新 registry 服务器字段。
2. **eval-perdof-object-norm03-seed44 参数差异**：已运行版本用 `n_rollouts=10`，你的模板是 `n_rollouts=20`。此外输出路径是 `logs/eval_object_perdof_norm03_seed44.json` 而非 `/root/autodl-tmp/libero_data/`。是否需要 kill 重新部署？
3. **eval-obs-only-object-norm03-seed45-r2**：我用 `n_rollouts=20` 部署到了 `/root/autodl-tmp/libero_data/crm_eval_obs_only_object_norm03_seed45.json`，与你指定一致。注意脚本用的是 `src/evaluate.py`（`eval_crm_libero.py` 不存在）。

---
