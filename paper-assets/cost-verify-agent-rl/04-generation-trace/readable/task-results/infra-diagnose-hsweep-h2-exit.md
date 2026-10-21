# infra diagnose hsweep h2 exit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_diagnose-hsweep-h2-exit_20260517T143234_result.json`
- **Structured JSON:** [`52c7d8521dc8624335e9.json`](../../sessions/52/52c7d8521dc8624335e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## 诊断结果

**1. 退出原因：正常完成（15/15 steps）**
- 日志有 "Final validation metrics"，无 traceback/error
- 总训练时间：10.04 小时

**2. 最终 Metrics**

| Step | Success | Invalid Action |
|------|---------|---------------|
| 1 | 18.75% | 2.7% |
| 2 | 14.84% | 2.0% |
| 3 | 18.75% | 2.8% |
| 4 | **5.47%** | **26.4%** ← collapse onset |
| 5 | 1.56% | 36.9% |
| 6-8 | 1.6-4.7% | 47-54% |
| 9 | **0%** | 64.1% |
| 10 | 2.34% | - |
| 11-15 | **0%** | 97.2% (step 15) |

Final val: success=0%, invalid_action=99.9%, action_is_valid=0.06%

Step 15 actor metrics: entropy=0.342, kl_loss=0.777, grad_norm=1.611

**3. Checkpoint**
`/root/autodl-tmp/checkpoints/hsweep-h2/` (global_step_5, 10, 15)

**4. auto_next: seed2 已自动启动**
- PID 945877, wandb run `jhwyg4tc`
- 正在 bjb1-17606 cuda:0,1 上运行（各 ~36GB 占用）

**5. 清理完成**
- Registry: status=DONE, conclusion=success
- Cron: 已删除

---
