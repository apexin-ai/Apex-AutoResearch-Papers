# code lto implementation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lto-implementation_20260519T024641_result.json`
- **Structured JSON:** [`acfd8c2d0f6730f49bfe.json`](../../sessions/ac/acfd8c2d0f6730f49bfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本都验证通过，新参数均已正确显示。

---

## 最终报告

### (1) 修改了哪些文件

| 文件 | 改动 |
|------|------|
| `src/train_crm.py` | 12 处修改：新增 `--task_names` 参数；precompute 阶段保存 `task_ids.pt` + manifest 写入 `task_names` 列表；train 阶段按 task name 过滤样本 |
| `src/evaluate.py` | 2 处修改：新增 `--task_indices` 参数；加载环境后按索引过滤 task，关闭未选中的环境 |

备份文件：`train_crm.py.bak`、`evaluate.py.bak`

### (2) manifest.json 结构（更新后）

```json
{
  "benchmark": "object",
  "n_samples": 14570,
  "K": 10,
  "obs_dim": 960,
  "action_dim": 6,
  "h_eff": 5,
  "task_names": ["task_0_name", "task_1_name", ...]  // NEW: sorted task name list
}
```

新增文件：`task_ids.pt` — 与 `obs_features.pt` 等长的 `torch.long` tensor，每个样本对应 `task_names` 列表中的索引。

### (3) 是否需要重新 precompute

**需要。** 当前缓存 `/root/autodl-tmp/crm_cache_v5/object/` 没有 `task_ids.pt`，也没有 `task_names` 字段。必须用更新后的脚本重新 precompute 才能使用 `--task_names` 过滤。

另外，HDF5 demo 数据 (`/root/autodl-tmp/libero_data/datasets/`) 目前在该服务器上为空，需要先传输数据。

### (4) 预估训练命令

**Step 1: 重新 precompute（生成 task_ids）**
```bash
/root/miniconda3/bin/python /root/acr-vla-conformal-refinement/src/train_crm.py \
    --benchmark object --precompute \
    --cache_dir /root/autodl-tmp/crm_cache_v5
```

**Step 2: LTO 训练（只用 5 个任务）**
```bash
/root/miniconda3/bin/python /root/acr-vla-conformal-refinement/src/train_crm.py \
    --benchmark object \
    --cache_dir /root/autodl-tmp/crm_cache_v5 \
    --task_names "TASK_A,TASK_B,TASK_C,TASK_D,TASK_E" \
    --epochs 100 --output_dir /root/autodl-tmp/crm_lto_train5
```

**Step 3: 在 held-out 任务上评估**
```bash
/root/miniconda3/bin/python /root/acr-vla-conformal-refinement/src/evaluate.py \
    --benchmark object \
    --crm_checkpoint /root/autodl-tmp/crm_lto_train5/crm_best.pt \
    --mode acr_vla \
    --task_indices "5,6,7,8,9"
```

> 具体 task name 需从 HDF5 文件中获取（LIBERO-Object 有 10 个任务）。拿到数据后 precompute 一次，manifest.json 里的 `task_names` 列表就会显示所有可用任务名。

---
