# infra gpu status and s2 50k eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-status-and-s2-50k-eval_20260521T162802_result.json`
- **Structured JSON:** [`b5fb067374dc8d3ea977.json`](../../sessions/b5/b5fb067374dc8d3ea977.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### GPU 任务分配（4/4 全部占满）

| GPU | 利用率 | 显存 | 任务 |
|-----|--------|------|------|
| 0 | 99% | 62203/97887 MiB | occ_s1_fresh finetune（CUDA_VISIBLE_DEVICES=0） |
| 1 | ~0% | 16778/97887 MiB | occ_s0 47500 50r rerun eval（CUDA_VISIBLE_DEVICES=1） |
| 2 | 30% | 16778/97887 MiB | **occ_s2 50K 50r eval**（刚启动，CUDA_VISIBLE_DEVICES=2） |
| 3 | ~0% | 16211/97887 MiB | occ_s0 50K eval |

### s0 47500 rerun 碰撞检测

**正常。** CAR 值明显小于 1.0（如 Task 3 CAR=0.200，Task 5 CAR=0.260，Task 6 CAR=0.360），确认碰撞被正确检测。当前进度 T7 94%，接近完成。

### s2 50K eval 启动结果

- **PID: 673918**（实际 python 进程；外层 bash PID 673916）
- 模型已加载，正在跑 T0 rollouts（~3.8s/it）
- 日志：`/root/eval_logs/occ_s2_50k_50r_eval.log`

### 备注

这台机器是 **4 GPU**（非 8 GPU），4/4 全部有任务在跑。

---
