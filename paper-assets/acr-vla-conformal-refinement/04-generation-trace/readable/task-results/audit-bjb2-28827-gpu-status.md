# audit bjb2 28827 gpu status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_bjb2-28827-gpu-status_20260520T140249_result.json`
- **Structured JSON:** [`abbe72961d0208f455c0.json`](../../sessions/ab/abbe72961d0208f455c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，汇总如下：

---

## bjb2-28827 GPU 审计报告

### GPU 总览

| GPU | 显存占用 | 实际进程 |
|-----|---------|---------|
| **0** | 1 MiB — **空闲** | 无 |
| **1** | 1 MiB — **空闲** | 无 |
| **2** | 4190 MiB | PID 357304 — `evaluate.py --mode crm_obs_only --benchmark spatial --seed 49` (21:27 启动) |
| **3** | 22651 MiB | PID 365151 — `precompute_openvla.py --device cuda:0 --cache_dir .../crm_cache_k1_openvla/` (21:49 启动) |
| **4** | 1 MiB — **空闲** | 无 |
| **5** | 5731 MiB | PID 367998 — `evaluate.py --mode adaptive_k --benchmark spatial --seed 44` (21:50 启动) |

---

### 表中 6 个实验的状态

| exp_id | GPU | 状态 | JSON | 详情 | 推荐 |
|--------|-----|------|------|------|------|
| eval-crm-k1-object-seed42-plan702 | 0 | **CRASHED** | NOT_FOUND | `UnboundLocalError: unc_dim`，13:50 退出 | **fix code + redeploy** |
| eval-latency-profiling-v1 | 1 | **COMPLETED** | **COMPLETE** | `latency_profiling_v1.json` (2893B)，K=1/5/10/20 全有 | **harvest** |
| eval-crm-k1-object-seed43-plan702 | 3 | **CRASHED** | NOT_FOUND | 同 unc_dim 错误，13:50 退出；GPU 3 现被 precompute 占用 | **fix code + redeploy 到空闲 GPU** |
| eval-crm-k1-object-seed44-plan702 | 4 | **CRASHED** | NOT_FOUND | 同 unc_dim 错误，13:50 退出 | **fix code + redeploy** |
| eval-adaptive-k-spatial-p90-seed44-bjb2 | 5 | **RUNNING** | 进行中 | PID 367998（非原 PID 367984），已完成 task 4/10，当前 SR ~80%-100% | **continue** |
| eval-adaptive-k-spatial-p90-seed42 | 2 | **COMPLETED** | **COMPLETE** | SR=31%, fast_path=80.6%, avg_k=3.5；GPU 2 已被 seed49 eval 占用 | **harvest** |

---

### 幽灵进程确认

表中列出的原始 PID 全部已死：
- PID 367510 (latency) → 已退出
- PID 366294 (crm-k1-seed44) → 已退出
- PID 367984 (adaptive-seed44) → 已退出，但新 PID 367998 在跑同任务
- PID 308030 (adaptive-seed42) → 已退出（exit code 129 SIGHUP）

---

### 未在表中但正在运行的进程

1. **PID 357304** (GPU 2) — `crm_obs_only spatial seed49`，21:27 启动，正在评估中
2. **PID 365151** (GPU 3) — `precompute_openvla.py object benchmark`，21:49 启动，已生成 4620 个 sample，仍在运行

---

### 旧 RUNNING 实验 JSON 检查（均已完成，可 harvest）

| 文件 | 状态 |
|------|------|
| eval_spatial_obs_only_norm02_seed46_r2.json | **COMPLETE** (crm_obs_only/spatial) |
| eval_goal_vla_only_seed44_r2.json | **COMPLETE** (vla_only/goal) |
| eval_object_argmin_k5_seed44_r2.json | **COMPLETE** (reconvla/object) |
| eval_object_perdof_norm02_seed48.json | **COMPLETE** |
| eval_object_obs_only_norm005_seed43.json | **COMPLETE** |

---

### OpenVLA Precompute

- `data/openvla_precomputed_*.pt` → NOT_FOUND（输出在 `/root/autodl-tmp/crm_cache_k1_openvla/object/`）
- 已生成 4620 个 .pt 文件，PID 365151 仍在 GPU 3 上运行

---

### 关键发现

1. **3 个 crm-k1-object 实验全崩**：`evaluate.py:466` 的 `unc_dim` 变量未定义，代码 bug，需修复后重新部署
2. **3 张 GPU 空闲** (0/1/4)，可立即部署新任务
3. **5 个旧实验** JSON 已完成但未 harvest
4. **latency_profiling_v1** 已完成可 harvest，包含 K=1/5/10/20 全部延迟数据

---
