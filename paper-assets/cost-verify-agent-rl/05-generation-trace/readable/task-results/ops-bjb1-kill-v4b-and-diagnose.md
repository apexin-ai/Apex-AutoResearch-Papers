# ops bjb1 kill v4b and diagnose

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1_kill_v4b_and_diagnose_20260522T094714_result.json`
- **Structured JSON:** [`6fe42f970597e014600d.json`](../../sessions/6f/6fe42f970597e014600d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 3. v5 Config 已就绪，关键变更

| 参数 | v4/v4c | v5 | 理由 |
|------|--------|-----|------|
| **kl_loss_coef** | 0.01 | **0.05** | 5x 增强 KL 约束，防止一步内策略漂移 |
| **max_turn** | 100 | **20** | 硬性截断 episode 长度，512×20=10240 上限，阻断 response inflation |
| **collapse_detection.multi_turn_enabled** | false | **true** | 启用 multi-turn collapse 检测，早期预警 |
| env_groups | 8 (v4) / 1 (v4c) | **8** | 恢复 v4 的 8 组训练多样性 |
| lr | 1e-6 | 1e-6 | 未超 1e-6，保持不变 |
| 其余参数 | — | 不变 | group_size=16, 512 per-turn, etc. |

v5 config 路径：`/root/cost-verify-agent-rl/RAGEN/config/_scienceworld_cell_c_grpo_v5.yaml`

**未启动，等待审批。**

---
