# diagnose gsweep g080 h5 seed1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gsweep_g080_h5_seed1_20260518T092349_result.json`
- **Structured JSON:** [`75201e8ceda866984556.json`](../../sessions/75/75201e8ceda866984556.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

```json
{"root_cause":"SIGTERM killed at step 8 — γ=0.80 reward collapse: success=0.0, pass@8=0.0, entropy=0.168, advantages_min=-11.97. Watchdog detected collapse and killed the process, replaced with g095 experiment.","error_type":"hyperparameter","fix_steps":["No fix needed — γ=0.80 confirmed collapsed as D072 predicted","Watchdog already auto-rotated to gsweep-g095-h5-seed1 on cuda:2,3","Checkpoint exists at global_step_5 if post-mortem analysis needed"],"can_auto_fix":false,"gpu_2_3_free":false}
```

详细情况：
- **日志路径**：`/root/runs/cost-verify-agent-rl/gsweep-g080-h5-seed1.log`（文件名用连字符非下划线，cron 找错了路径）
- **死因**：watchdog 发送 SIGTERM（17:14:14），进程在 step 8 时 success=0.0 完全坍缩
- **关键指标**：entropy 0.168（极低，策略退化）、advantages_min -11.97（极端负值）、pass@8=0.0
- **checkpoint**：`/root/autodl-tmp/checkpoints/gsweep-g080-h5/global_step_5` 存在
- **GPU 2,3 当前状态**：被 g095 实验占用（~4.7GB/卡，刚启动 step 0），不空闲
- **磁盘**：30G 用了 24G（80%），偏紧但未满

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "SIGTERM killed at step 8 — γ=0.80 reward collapse: success=0.0, pass@8=0.0, entropy=0.168, advantages_min=-11.97. Watchdog detected collapse and killed the process, replaced with g095 experiment.",
    "error_type": "hyperparameter",
    "fix_steps": [
      "No fix needed — γ=0.80 confirmed collapsed as D072 predicted",
      "Watchdog already auto-rotated to gsweep-g095-h5-seed1 on cuda:2,3",
      "Checkpoint exists at global_step_5 if post-mortem analysis needed"
    ],
    "can_auto_fix": false,
    "gpu_2_3_free": false
  }
}
```

</details>

---
