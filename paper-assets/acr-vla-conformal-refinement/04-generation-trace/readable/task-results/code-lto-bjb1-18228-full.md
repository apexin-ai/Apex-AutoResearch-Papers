# code lto bjb1 18228 full

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lto-bjb1-18228-full_20260519T030408_result.json`
- **Structured JSON:** [`12c77e5306cfe6ae183f.json`](../../sessions/12/12c77e5306cfe6ae183f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Split A 训练已成功启动并在运行中。汇报如下：

---

## 完成状态

### 1. 修改了哪些文件

| 文件 | 修改内容 |
|------|----------|
| `src/build_task_ids.py` | **新建** — 从 HDF5 demos 重建 `task_ids.pt`，映射每个缓存样本到 task index |
| `src/train_crm.py` | 添加 `--task_indices` 参数（line 84-85）；训练时按 task_ids 过滤缓存数据（lines 327-344） |
| `src/evaluate.py` | 添加 `--task_indices` 参数（line 80-81）；按 index 过滤 LIBERO 任务环境（lines 393-397） |

### 2. LIBERO-Object 10 个 task names（按排序顺序）

| Index | Task name | Split A 样本数 |
|-------|-----------|---------------|
| 0 | pick up the alphabet soup and place it in the basket | 1516 |
| 1 | pick up the bbq sauce and place it in the basket | 1479 |
| 2 | pick up the butter and place it in the basket | 1522 |
| 3 | pick up the chocolate pudding and place it in the basket | 1520 |
| 4 | pick up the cream cheese and place it in the basket | 1462 |
| 5 | pick up the ketchup and place it in the basket | 1575 |
| 6 | pick up the milk and place it in the basket | 1279 → *Split B eval* |
| 7 | pick up the orange juice and place it in the basket | 1279 |
| 8 | pick up the salad dressing and place it in the basket | 1363 |
| 9 | pick up the tomato sauce and place it in the basket | 1414 |

**Split A**: Train on 0-4 (7499 samples), Eval on 5-9 (held-out)
**Split B**: Train on 5-9, Eval on 0-4

### 3. Split A 训练状态

- **exp_id**: `crm-lto-splitA-train`
- **GPU**: cuda:2 (RTX 4090, 536MiB used)
- **Config**: `input_mode=obs_only`, batch_size=256, lr=0.008, epochs=50, seed=42
- **Data**: 7499 train+val samples from crm_cache_v3/object (tasks 0-4)
- **进度**: Epoch 2/50, val_loss=0.112 (improving), ~30s/epoch
- **预估完成时间**: ~25 min

### 4. Split A 训练完成后的 eval 命令

在 held-out tasks 5-9 上评测：
```bash
source /root/miniconda3/bin/activate base && cd /root/acr-vla-conformal-refinement/src && \
CUDA_VISIBLE_DEVICES=2 python evaluate.py \
  --benchmark object \
  --mode crm_obs_only \
  --checkpoint /root/autodl-tmp/checkpoints/crm_lto_splitA/obs_only/crm_best.pt \
  --task_indices 5,6,7,8,9 \
  --n_rollouts 20 \
  --seed 42 \
  --output_file logs/eval_lto_splitA_heldout_5-9.json
```

VLA-only baseline（同样只在 held-out tasks 上评测）：
```bash
CUDA_VISIBLE_DEVICES=2 python evaluate.py \
  --benchmark object \
  --mode vla_only \
  --task_indices 5,6,7,8,9 \
  --n_rollouts 20 \
  --seed 42 \
  --output_file logs/eval_lto_splitA_vla_only_5-9.json
```

---
