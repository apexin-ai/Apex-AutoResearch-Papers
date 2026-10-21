# diagnose a3 spatial definitive

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_a3_spatial_definitive_20260521T171637_result.json`
- **Structured JSON:** [`320bf3dd694004fff121.json`](../../sessions/32/320bf3dd694004fff121.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### GPU 0 — spatial_bowl (PID 191747) ✅ 存活
- **Step**: 7894 / 30000 (26%)
- **Loss**: 0.0568, LR: 2.20e-05
- **速度**: ~4.0 s/it
- **已运行**: 8h06m
- **剩余**: ~24.5h（约 748 步 × ... 实际是 22106 步 × 4s ≈ 24.5h）
- **预估完成**: ~5月22日 25:30 → **5月23日 ~01:30**

### GPU 1 — object_pudding (PID 165990) ✅ 存活，即将完成
- **Step**: 29252 / 30000 (98%)
- **Loss**: 0.0206, LR: 2.54e-06
- **速度**: ~4.0 s/it
- **剩余**: 748 steps × 4s ≈ **~50 分钟**
- **预估完成**: **5月22日 ~02:10**

### Cron 报失败的原因
`/root/autodl-tmp/colliforce-outputs/a3_spa_s0/train_resume3.log` 内容是旧的失败记录——`SyntaxError` 在 `train_a3_hook.py:243`（corrupted code）。这是之前的失败尝试。Cron 一直在检测这些旧日志并报告失败。

当前实际运行的进程日志在 `/tmp/spatial_bowl.log`，训练正常进行中，没有报错。

### 结论
- 两个实验均正常运行，无需干预
- object_pudding 约 50 分钟后完成
- spatial_bowl 还需约 24.5 小时
- Cron 误报是因为它检测的日志路径指向旧的失败日志，不是当前运行的日志

---
