# code pi05 a1 sdf integration

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pi05_a1_sdf_integration_20260522T222344_result.json`
- **Structured JSON:** [`4a7d684084aa999dfdfb.json`](../../sessions/4a/4a7d684084aa999dfdfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇报结果：

---

## 完成汇报

### 1. 文件变更清单

| 文件 | 操作 | 说明 |
|------|------|------|
| `scripts/train_a1_sdf_aux_pi05.py` | **新建** | Pi0.5 版 A1 SDF 训练脚本 |
| `scripts/eval_safelibero.py` | **修改** | 添加 `--pi05` flag，4 处改动 |

### 2. 与 `train_a1_sdf_aux.py` 的代码差异

| 项目 | Pi0 (原) | Pi0.5 (新) |
|------|----------|-----------|
| model_config | `Pi0Config(paligemma_variant="gemma_2b", action_expert_variant="gemma_300m")` | `Pi0Config(pi05=True, action_horizon=10, discrete_state_input=False)` |
| 权重路径 | `pi0_base` | `pi05_libero` |
| `--lambda_sdf` 默认值 | 0.1 | **0.005** (M030 教训) |
| config/exp_name 前缀 | `a1_sdf_` | `a1_sdf_pi05_` |
| SdfAuxHooks / SDFDecoder / EEExtractor / LoRA | 完全不变 | 完全不变 |

### 3. 训练启动命令模板

```bash
# Dry run 验证
python scripts/train_a1_sdf_aux_pi05.py --scene spatial_bowl --dry_run --gpu 0

# 正式训练
python scripts/train_a1_sdf_aux_pi05.py \
    --scene spatial_bowl \
    --seed 0 \
    --gpu 0 \
    --batch_size 32 \
    --num_train_steps 30000 \
    --lambda_sdf 0.005 \
    --lambda_ee 0.01 \
    --lr 2.5e-5 \
    --save_interval 2000
```

### 4. Eval 使用

```bash
# A1 评估（baseline/a1 模式直接用 config_name）
python scripts/eval_safelibero.py \
    --model_type a1 \
    --checkpoint /root/autodl-tmp/checkpoints/a1_sdf_pi05_spatial_bowl/... \
    --config_name pi05_libero \
    --suite safelibero_spatial --task_id 0 --n_episodes 50

# A3 评估需要 --pi05 flag
python scripts/eval_safelibero.py \
    --model_type a3 --pi05 \
    --checkpoint ... \
    --config_name pi05_libero \
    --suite safelibero_spatial --task_id 0
```

### 5. 技术风险

- **权重未同步**：`/root/autodl-tmp/openpi_weights/pi05_libero/` 在 westd-35807 上不存在，需从 westd-45947 的 `/root/autodl-tmp/openpi_weights/pi05_libero/` rsync（~12GB）
- **action_horizon 影响 mean pooling**：Pi0.5 的 suffix_out 是 `[B, 10, 1024]`（Pi0 是 `[B, 50, 1024]`），mean pooling 粒度变粗，SDFDecoder 收到的特征信息密度不同，可能影响 SDF 预测质量
- **assets/norm_stats 兼容性**：当前 SCENE_CONFIG 指向 `baseline_spatial_bowl` 的 assets，这是 Pi0 的 norm_stats。Pi0.5 可能需要自己的 norm_stats（取决于 pi05_libero checkpoint 是否包含适用于 SafeLIBERO 数据的统计量）

---
