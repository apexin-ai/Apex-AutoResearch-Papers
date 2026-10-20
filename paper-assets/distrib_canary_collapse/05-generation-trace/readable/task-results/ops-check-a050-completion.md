# ops check a050 completion

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-a050-completion_20260515T051335_result.json`
- **Structured JSON:** [`d468fd99f0f0536b278a.json`](../../sessions/d4/d468fd99f0f0536b278a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### a050_s42 (PID 73737, 运行 3h54m)
- **未完成**，gen_9 正在训练中：**85% (4230/5000 steps)**，~50秒完成训练
- 训练完还需跑评估生成 metrics，预计 **几分钟内完成**
- 当前 loss: 0.9378 (step 4200)
- 无 EXIT_CODE

### plan_006_s42 (PID 68368, 运行 5h33m)
- gen_0 ~ gen_11 已完成（12/20 代）
- 当前训练 gen_12：**25% (2532/10000 steps)**，剩余 ~7m50s
- 当前 loss: 0.0517
- 按每代 ~10min 估算，还需 **~80 分钟**完成全部 20 代

### GPU
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 89% | 12.5 / 95.6 GB |
| 1 | 90% | 12.5 / 95.6 GB |

a050_s42 几分钟后应该就能拿到 gen_9 metrics，届时可计算 distinct_1 drift。

---
