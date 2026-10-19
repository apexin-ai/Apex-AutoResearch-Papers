# diagnose pi05 crm k2 long s43 cqa1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pi05-crm-k2-long-s43-cqa1_20260526T131123_result.json`
- **Structured JSON:** [`53c31966b49ff1556839.json`](../../sessions/53/53c31966b49ff1556839.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 失败原因

s43 实验命令**缺少三个关键参数**：
- `--crm_checkpoint`（或 `--checkpoint`）
- `--obs_dim 2048`
- `--unified_obs_dim 2088`

日志确认 args 中 `checkpoint: None, crm_checkpoint: None`，触发 line 583 的 ValueError。

### s44 实验状态

**s44 正在正常运行**（PID 216649，CPU 539%），它的命令包含了所有必要参数：
```
--crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088
```
s44 没有同样的风险。

### Checkpoint 确认

`/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt` 存在（2.4MB，May 25 16:41）。

### 参数说明

evaluate.py 支持 `--checkpoint` 和 `--crm_checkpoint`（line 69-72），后者是前者的别名（line 535-537）。两者均可。

### 重新提交的完整命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/acr-vla-conformal-refinement && \
CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py \
  --model pi05 \
  --mode crm_obs_only \
  --K 2 \
  --max_correction_norm 0.05 \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt \
  --obs_dim 2048 \
  --unified_obs_dim 2088 \
  --benchmark long \
  --seed 43 \
  --n_rollouts 20 \
  --output_file logs/eval_long_crm_k2_pi05_seed43.json
```

注意：output_file 名也建议对齐 s44 的命名格式（`eval_long_crm_k2_pi05_seed43.json` 而非原来的 `eval_long_crm_obs_only_norm0.05_seed43_pi05_K2_cqa1.json`），方便后续批量分析。

---
