# ops check perdof norm02 spatial gap

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-perdof-norm02-spatial-gap_20260515T213743_result.json`
- **Structured JSON:** [`2f19d585ec4c1d839bd7.json`](../../sessions/2f/2f19d585ec4c1d839bd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### Registry 数据 (`eval-mag-perdof-norm02`)

**已完成 6/10 tasks (T0-T5):**

| Task | SR |
|------|-----|
| T0 between_plate_ramekin | 60% |
| T1 next_to_ramekin | 90% |
| T2 table_center | 0% |
| T3 on_cookie_box | 20% |
| T4 top_drawer | 0% |
| T5 on_ramekin | 0% |
| **6-task avg** | **28.3%** |

**缺失 4 个 tasks:**
- T6: next_to_cookie_box
- T7: on_stove
- T8: next_to_plate
- T9: on_wooden_cabinet

### 服务器状态

**无 partial JSON 结果可利用** — 服务器上只有启动日志，没有 JSON 输出文件。进程在完成 T5 后崩溃/被杀，没来得及写结果。

**bjb2-28827 全部 6 卡被占满**（都在跑 object 评估）：

| GPU | 实验 | 显存 |
|-----|------|------|
| 0 | perdof-norm003-object | 4268 MiB |
| 1 | perdof-norm005-object | 4736 MiB |
| 2 | perdof-norm03-object-r3 | 5201 MiB |
| 3 | perdof-norm02-seed43-object-r3 | 5200 MiB |
| 4 | obsonly-norm005-object | 4269 MiB |
| 5 | obsonly-norm03-object | 4268 MiB |

### 补跑方案

`evaluate.py` **没有 `start_task` 参数**，task 列表是顺序遍历 `[0..9]`。两个选项：

**选项 A — 全量重跑 (10 tasks)**：
```bash
cd /root/acr-vla-conformal-refinement && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=X nohup python src/evaluate.py \
  --benchmark spatial \
  --mode acr_vla \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt \
  --n_rollouts 10 --max_steps 300 --seed 42 --K 10 \
  --max_correction_norm 0.2 \
  --output_file logs/eval_spatial_perdof_norm02_full.json \
  > logs/nohup_eval_spatial_perdof_norm02_full.log 2>&1 &
```

**选项 B — 改脚本加 `start_task` 参数，只跑 T6-T9**（省 ~60% 时间，但需要手动合并结果）

**当前 bjb2-28827 没有空闲 GPU**，需要等现有 object 评估完成，或者在其他有空闲卡的服务器（如 bjb2-40593）上跑。

---
