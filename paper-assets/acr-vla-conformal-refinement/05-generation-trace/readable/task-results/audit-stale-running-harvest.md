# audit stale running harvest

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_stale-running-harvest_20260526T145318_result.json`
- **Structured JSON:** [`5c9e034358b0f282aab7.json`](../../sessions/5c/5c9e034358b0f282aab7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 台服务器检查完毕。汇总报告：

---

## 收割结果汇总（22 个实验）

### cqa1-32758（5 个，全部完成）

```
pi05-adaptive-long-s44-cqa1:          COMPLETED | SR=0.0%  | 10 tasks x 20 rollouts 全部失败
pi05-adaptive-long-s43-cqa1:          COMPLETED | SR=0.0%  | 10 tasks x 20 rollouts 全部失败
pi05-adaptive-object-s44-cqa1:        COMPLETED | SR=88.0% | tau=0.25, trigger_rate=3.5%
eval-supp-spatial-reconvla-s46:       COMPLETED | SR=80.0% | PID 588065 已死，结果文件: eval_spatial_reconvla_seed46.json
eval-supp-spatial-adapt-tau025-s45-r3:COMPLETED | SR=80.0% | PID 502821 已死，trigger_rate=20.0%，结果文件: eval_spatial_adaptive_conformal_crm_norm0.2_tau0.25_seed45.json
```

### bjb1-32546（10 个，8 完成 / 2 失败）

```
eval-crm-spatial-s48-d149:            COMPLETED | SR=80.5% | eval_spatial_crm_seed48.json (May 25 20:35)
eval-crm-object-s44-d149:             COMPLETED | SR=74.0% | eval_object_crm_seed44.json (May 25 21:01)
eval-crm-object-s43-d149:             COMPLETED | SR=78.5% | eval_object_crm_seed43.json (May 25 20:55)
eval-crm-object-s42-d149:             COMPLETED | SR=77.0% | eval_object_crm_seed42.json (May 25 20:38)
eval-crm-goal-s44-d149:               COMPLETED | SR=82.0% | eval_goal_crm_seed44.json (May 25 20:16)
eval-crm-goal-s43-d149:               COMPLETED | SR=82.0% | eval_goal_crm_seed43.json (May 25 20:20)
eval-supp-spatial-k2mean-s46:         COMPLETED | SR=80.0% | PID 188432 已死，eval_spatial_k2mean_seed46.json (May 24 09:22)
eval-supp-reconvla-obj-s45:           COMPLETED | SR=78.0% | eval_object_reconvla_seed45.json (May 24 08:59)
eval-smolvla-lerobot-goal-seed43-v3:  CRASHED   | SR=N/A   | RuntimeError: state_dict size mismatch (input shape [990] vs [1030])
eval-smolvla-lerobot-spatial-seed43-v3:NO_TRACE  | SR=N/A   | 服务器上无任何日志或结果文件
```

### bjb2-28827（5 个，4 完成 / 1 无痕迹）

```
eval-supp-obj-reconvla-s47:           COMPLETED | SR=76.5% | eval_object_reconvla_seed47.json (May 24 20:26)
eval-supp-goal-reconvla-s47:          COMPLETED | SR=83.5% | eval_goal_reconvla_seed47.json (May 24 19:56)
eval-supp-goal-k2mean-s47:            NO_TRACE  | SR=N/A   | 无结果文件、无日志，可能从未启动
eval-supp-goal-crm-norm005-s47:       COMPLETED | SR=82.0% | eval_goal_crm_obs_only_norm0.05_seed47.json (May 24 19:58)
eval-supp-goal-adapt-tau025-s47:      COMPLETED | SR=82.0% | eval_goal_adaptive_conformal_crm_tau0.25_seed47.json (May 24 20:03)
```

### bjb1-18228（2 个，全部完成）

```
precompute-pi05-long-2048-r2:         COMPLETED | cache=2.5G | n=136,090 samples, manifest created May 26
precompute-pi05-object-2048-r2:       COMPLETED | cache=1.3G | n=72,507 samples, manifest created May 24
```

---

### 统计

| 状态 | 数量 |
|------|------|
| COMPLETED（有结果） | 19 |
| CRASHED | 1（smolvla-goal: state_dict mismatch） |
| NO_TRACE | 2（smolvla-spatial、goal-k2mean-s47） |

### ⚠️ C002 警告

- **pi05-adaptive-long-s43/s44**: SR=0.0%，200/200 rollouts 全部失败。long-horizon + pi05 adaptive 组合完全不工作。
- **smolvla 系列**: CRM checkpoint 与 SmolVLA obs_dim 不兼容（990 vs 1030），需要重新训练 CRM 或修改维度映射。

---
