# audit bjb2 28827 and bjb1 18228 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_bjb2-28827-and-bjb1-18228-status_20260525T100119_result.json`
- **Structured JSON:** [`a2eab8fb10bb6a172740.json`](../../sessions/a2/a2eab8fb10bb6a172740.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== bjb2-28827 ===
GPU Status (6×RTX 4090, registry是STALE,实际进程与registry完全不匹配):
  GPU 0: 4699 MiB  | pid 730605 (55:50) | spatial crm_obs_only seed 47
  GPU 1: 13046 MiB | pid 732023 (55:20) | goal adaptive_conformal_crm pi05 seed 43
  GPU 2: 13606 MiB | pid 732469 (54:49) | object adaptive_conformal_crm pi05 seed 42
  GPU 3: 1 MiB     | IDLE — registry中eval-supp-goal-reconvla-s47未运行
  GPU 4: 13606 MiB | pid 733346 (53:48) | object adaptive_conformal_crm pi05 seed 43
  GPU 5: 1 MiB     | IDLE — registry未分配
  
Running experiments (无 tmux session, 全部 nohup 后台):
  - spatial_crm_s47          → task 1, rollout 20/20 (15/20 = 75%) 进行中
  - goal_adaptive_pi05_s43   → 当前任务 put_the_bowl_on_the_stove 20/20 (100%)
  - object_adaptive_pi05_s42 → cream_cheese 10/20 (9/10)
  - object_adaptive_pi05_s43 → cream_cheese 10/20 (7/10)
  
Idle GPUs: cuda:3, cuda:5
Completed but unclosed: registry 5 个条目全部与实际不符;特别是 reconvla-s47 (cuda:3) 进程已死但 registry 仍 RUNNING;另 4 个 registry 条目 (goal-adapt-tau025-s47/goal-crm-norm005-s47/goal-k2mean-s47/obj-reconvla-s47) 均无对应进程,需 registry 清理

=== bjb1-18228 ===
GPU Status (4×RTX 4090):
  GPU 0: 10411 MiB | pid 484291 (02:32:30) | spatial adaptive_conformal_crm pi05 seed 42 r2 (K=2)
  GPU 1: 1 MiB     | IDLE
  GPU 2: 12593 MiB | pid 524279 (01:22:13) | goal adaptive_conformal_crm pi05 seed 42
  GPU 3: 9874 MiB  | pid 114507 (2d 13h)   | precompute pi05 long K=10
  
Running experiments (无 tmux,全部 nohup):
  - spatial_adaptive_pi05_seed42_r2 → 当前 black_bowl_on_stove 20/20 (100%)
  - goal_adaptive_pi05_seed42       → 已写入 logs/eval_goal_adaptive_pi05_seed42.json, 总成功率 0.0% (0/200) ⚠️ 异常,进程将退出
  - precompute_pi05_long_2048       → 113600/136090 (83.5%), ETA ~12.3 小时
  
Idle GPUs: cuda:1
Completed but unclosed:
  - goal_adaptive_pi05_seed42 已完成 (0/200 结果异常,需调查),进程残留中,registry 未关闭
  - precompute-pi05-object-2048-r2 (registry RUNNING) 无对应进程,object cache 已有 150 个文件,可能已完成或中断
  - 新出现 2 个 eval job (spatial_r2_s42, goal_s42 pi05 adaptive) 未在 registry 中登记
```

关键告警:
1. **两台机器 registry 全部失同步**,需重建
2. **bjb1 goal_adaptive_pi05_seed42 结果 0.0% (0/200)** — 异常,需查 conformal_threshold/crm_checkpoint 配置
3. **bjb2 有 2 张空闲 GPU (cuda:3, cuda:5)**,bjb1 有 1 张空闲 (cuda:1) — DDL 5/29 前可立即补跑实验

---
