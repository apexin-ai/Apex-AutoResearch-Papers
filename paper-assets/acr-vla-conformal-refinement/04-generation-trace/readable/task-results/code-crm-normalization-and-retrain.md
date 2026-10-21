# code crm normalization and retrain

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_crm-normalization-and-retrain_20260514T175717_result.json`
- **Structured JSON:** [`5db2faf7268e82352394.json`](../../sessions/5d/5db2faf7268e82352394.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。简报：

### 执行结果

**1. norm_stats.pt 已计算并保存**  
路径：`/root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt`  
数据来源：2402 spatial 样本（object cache 在 bjb2-40593 上不存在）

关键数值：
| 组件 | 维度 | mean abs | std 范围 |
|------|------|---------|---------|
| base_action | 30 | 0.808 | [0.285, 1.313] |
| per_dof_std | 30 | 0.887 | [0.189, 0.722] |
| conf_radius | 5 | 1.865 | [0.197, 0.278] |
| log_volume | 5 | 1.612 | [1.633, 2.137] |
| obs_features | 960 | 0.361 | [0.033, 0.741] |

obs_features 的 std 平均仅 0.10，远小于 ba(0.66) 和 uf(0.48)，normalization 有意义。

**2. crm.py 已修改** — `norm_mean`/`norm_std` 注册为 buffer，默认 identity（mean=0, std=1），forward 中统一做 `(x - mean) / std`

**3. train_crm.py 已修改** — 新增 `--norm_stats` 参数，按 `input_mode` 组装对应维度的 norm 向量

**4. evaluate.py 已修改** — `load_state_dict` 改为 `strict=False`，v2/v3 checkpoint 均兼容

**5. 3 组 CRM v3 训练已启动** — 共享 cuda:0（eval 仅占 2.4GB），epoch 3 loss 稳定下降：
- `crm-train-v3-perdof` (full): val_loss=1.260
- `crm-train-v3-scalar-unc`: val_loss=1.266
- `crm-train-v3-obs-only`: val_loss=1.267

**注意**：`--benchmark` 仅用 `spatial`（此服务器无 object cache）。如需 object 数据需先 precompute。

---
