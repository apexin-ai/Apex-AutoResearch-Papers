# Eval Status Check — ced_kl001_r4
**Time:** 2026-05-15 ~03:05 UTC

## 1. 进程存活状态

| PID | 状态 | 运行时长 | 任务 | GPU |
|-----|------|---------|------|-----|
| 78850 | ALIVE | 1h21m | batch_eval parent (ckpt 10,20,30,40,60,70,80) | cuda:2 |
| 78857 | ALIVE | 1h21m | 子进程: ckpt-10 inference | GPU 2 |
| 80789 | ALIVE | 55m | batch_eval step100 | cuda:0 |
| 81962 | ALIVE | 47m | inference ckpt-60 (high task) | GPU 3 |
| 83207 | ALIVE | 31m | batch_eval step90 | cuda:1 |

**失败任务（非上述5个PID）：**
- `mvp2_eval_ced_kl001_r4_last.log` → EXIT_CODE=1, `No module named freige.eval.batch_eval`
- `mvp2_eval_ced_kl001_r4_ckpt90.log` → EXIT_CODE=1, `No module named freige.eval.batch_eval`

## 2. GPU 利用情况

| GPU | 利用率 | 显存占用 | 任务 |
|-----|--------|---------|------|
| GPU 0 | 65% | 10653/32607 MiB | step100 eval (PID 80799) |
| GPU 1 | 68% | 9071/32607 MiB | step90 eval (PID 83217) |
| GPU 2 | 76% | 10933/32607 MiB | multi batch_eval ckpt-10 (PID 78857) |
| GPU 3 | 73% | 10567/32607 MiB | ckpt-60 eval (PID 81962) |

**结论：4张卡全部在用，无空闲GPU。cuda:2 并未空闲。**

## 3. 已完成 Checkpoint 结果

### checkpoint-50 ✅ COMPLETE
| 指标 | 值 |
|------|-----|
| **F1** | **0.1563** |
| ign_F1 | 0.1563 |
| Precision | 0.2356 |
| Recall | 0.1169 |
| **Evi-F1** | **0.5643** |
| Evi-Precision | 0.4864 |
| Evi-Recall | 0.6721 |
| **EDCR** | **0.8858** |
| format_ok_rate | 0.9990 |
| n_truncated | 11 |
| inference_time | 4641.8s (~77min) |

**vs SFT baseline (F1=0.4057, Evi-F1=0.7979, EDCR=0.7118):**
- F1: 0.1563 vs 0.4057 → **大幅下降 (-61%)**
- Evi-F1: 0.5643 vs 0.7979 → **下降 (-29%)**
- EDCR: 0.8858 vs 0.7118 → **提升 (+24%)**，但代价是关系抽取质量严重劣化

## 4. 进行中任务进度估计

### multi batch_eval (GPU 2) — ckpt-10 当前
- 进度: 57/62 batches (92%)
- 当前速度: ~86s/batch
- ckpt-10 ETA: **~7 分钟**
- 之后还需评估: ckpt-20, 30, 40, 60, 70, 80（6个checkpoint）
- 每个 checkpoint 推理约 77-80 分钟
- **注意**: --resume 会跳过已有结果的 ckpt-50；ckpt-60 正在 GPU 3 上单独评估，multi 到 60 时若已完成也会跳过
- **总剩余预估**: 7min + 5×80min ≈ **6.7 小时**（如果 ckpt-60 也被跳过则 ~5.4 小时）

### step100 eval (GPU 0)
- 进度: 39/62 batches (63%)
- 当前速度: ~80s/batch
- **ETA: ~30 分钟**

### step90 eval (GPU 1)
- 进度: 22/62 batches (35%)
- 当前速度: ~80s/batch
- **ETA: ~53 分钟**

### ckpt-60 eval (GPU 3)
- 进度: 36/62 batches (58%)
- 当前速度: ~76s/batch
- **ETA: ~33 分钟**

## 5. Step 90 状态

- **独立 eval 任务 (PID 83207)** 在 GPU 1 上运行中，35% 完成，约 53 分钟后出结果
- 之前尝试用 `ckpt90.log` 启动的任务已失败（模块导入错误）
- step90 结果目录 `/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-90/` 已创建但为空

## 6. 预计结果交付时间线

| Checkpoint | 预计完成时间 (UTC) | 来源 |
|-----------|-------------------|------|
| ckpt-10 | ~03:12 | multi batch_eval (GPU 2) |
| ckpt-60 | ~03:38 | high task (GPU 3) |
| step-100 | ~03:35 | step100 task (GPU 0) |
| step-90 | ~03:58 | step90 task (GPU 1) |
| ckpt-20 | ~04:32 | multi batch_eval (GPU 2) |
| ckpt-30 | ~05:52 | multi batch_eval (GPU 2) |
| ckpt-40 | ~07:12 | multi batch_eval (GPU 2) |
| ckpt-70 | ~08:32 | multi batch_eval (GPU 2) |
| ckpt-80 | ~09:52 | multi batch_eval (GPU 2) |
