# Gradient Analysis: V1 vs V2 Methodology Comparison

## Script Paths

| Version | Analysis Script | Compare Script | Shell Runner |
|---------|----------------|----------------|-------------|
| V1 | `/root/occsafe_vla/scripts/same_seed_gradient_analysis.py` | `/root/occsafe_vla/analysis/compare_gradients.py` | `/root/occsafe_vla/scripts/run_gradient_same_seed.sh` |
| V1 (earliest) | `/root/occsafe_vla/analysis/gradient_analysis.py` | — | — |
| V2 | `/root/occsafe_vla/scripts/run_gradient_analysis_v2.py` | `/root/occsafe_vla/scripts/compare_gradient_conditions.py` | — |

## Methodology Comparison

| 维度 | V1 (`same_seed_gradient_analysis.py`) | V2 (`run_gradient_analysis_v2.py`) | 一致? |
|------|--------------------------------------|-------------------------------------|-------|
| **数据源** | 真实 RLDS DataLoader (`RLDSDataset` + `RLDSBatchTransform`) | 同 v1 | ✅ |
| **样本数** | `--num_batches 200` × bs=4 = **800 samples** | `--num_samples 800` / bs=4 = **200 batches** (修正后) | ✅ (修正前 default=200 → 50 batches) |
| **batch_size** | 4 | 4 | ✅ |
| **seed** | `torch.manual_seed(42)` + `np.random.seed(42)` | 同 v1 | ✅ |
| **梯度获取** | `torch.autograd.grad(loss, all_params)` | 同 v1 | ✅ |
| **参数范围** | `model.vision_backbone.named_parameters()` | 同 v1 | ✅ |
| **层分组** | 按 encoder block: `featurizer.blocks.{0..39}` (DINOv2) + `fused_featurizer.blocks.{0..26}` (SigLIP) + `.stem` | 同 v1 (`get_layer_groups()` 函数一致) | ✅ |
| **Norm 计算** | 逐组 flatten → concat → L2 norm (`vec.norm()`) | 同 v1 (`compute_per_layer_grads()` 函数一致) | ✅ |
| **Action loss** | `L1Loss(gt_actions, pred_actions)` via `action_head.predict_action()` | 同 v1 | ✅ |
| **OCC loss** | `FocalLoss(occ_logits, occ_targets)` via `occ_head(patch_features)` | 同 v1 | ✅ |
| **Detach 处理** | `pf = patch_features.detach() if occ_detach else patch_features` | 同 v1 | ✅ |
| **Cosine similarity** | `F.cosine_similarity(action_vec, occ_vec)` per layer | 同 v1 | ✅ |
| **Conflict rate** | `sum(cos < 0) / len(cos)` per layer | 同 v1 | ✅ |
| **Vanilla 条件** | 总是加载 OCC head (即使 random init)，设 `--occ_detach true` | Auto-detect: vanilla 不加载 occ_head，`occ_loss=0` | ⚠️ 功能等价 |
| **BN drift** | 有 `extract_bn_stats()` 记录 | 无 | ⚠️ 不影响梯度数据 |
| **输出格式** | `per_layer.{group}.action_grad_norm_mean/std/occ_grad_norm_mean/std/cosine_sim_mean/std/conflict_rate` | 同 v1 | ✅ |

## Differences Found & Corrections

### 1. [FIXED] Sample Count Mismatch

**Before**: v2 默认 `--num_samples 200` → 50 batches = 200 samples
**After**: v2 默认 `--num_samples 800` → 200 batches = 800 samples，与 v1 完全一致

Files modified:
- `run_gradient_analysis_v2.py`: line 56, default 200 → 800
- `compare_gradient_conditions.py`: line 45, default 200 → 800

### 2. [No Fix Needed] Vanilla OCC Head Handling

V1 总是加载 OCC head 并用 `--occ_detach true`，V2 跳过 OCC head。
**无需修正**：两种方式对 action gradient norms 结果相同，因为 detached OCC loss 不影响 backbone 梯度。

### 3. [No Fix Needed] BN Drift Tracking

V1 有 `extract_bn_stats()` 记录 OCC head 内 BN 层的 running stats drift。
V2 不记录。**无需修正**：BN drift 不影响梯度分析结论。

## Run Commands (3 conditions)

```bash
# Environment
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export CUDA_VISIBLE_DEVICES=0
cd /root/occsafe_vla/scripts

# Checkpoint path pattern
CKPT_BASE="/root/autodl-tmp/checkpoints"
CKPT_SUFFIX="openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug"
OUTPUT_DIR="/root/occsafe_vla/artifacts/gradient_v2"

# --- Option A: Run each condition separately ---

# 1. Vanilla v2 s0 (seed 42)
VANILLA_CKPT="${CKPT_BASE}/${VANILLA_EXP_ID}/${CKPT_SUFFIX}--${VANILLA_EXP_ID}--50000_chkpt"
python3 run_gradient_analysis_v2.py \
    --checkpoint_dir "${VANILLA_CKPT}" \
    --condition_name "Vanilla_v2" \
    --seed 42 --num_samples 800 --batch_size 4 --gpu 0 \
    --output_dir "${OUTPUT_DIR}"

# 2. Full OCC LN v2 s0 (seed 42)
FULL_OCC_CKPT="${CKPT_BASE}/${FULL_OCC_EXP_ID}/${CKPT_SUFFIX}--${FULL_OCC_EXP_ID}--50000_chkpt"
python3 run_gradient_analysis_v2.py \
    --checkpoint_dir "${FULL_OCC_CKPT}" \
    --condition_name "Full_OCC_LN_v2" \
    --seed 42 --num_samples 800 --batch_size 4 --gpu 0 \
    --output_dir "${OUTPUT_DIR}"

# 3. Detach LN v2 s0 (seed 42)
DETACH_CKPT="${CKPT_BASE}/${DETACH_EXP_ID}/${CKPT_SUFFIX}--${DETACH_EXP_ID}--50000_chkpt"
python3 run_gradient_analysis_v2.py \
    --checkpoint_dir "${DETACH_CKPT}" \
    --condition_name "Detach_LN_v2" \
    --seed 42 --num_samples 800 --batch_size 4 --gpu 0 \
    --output_dir "${OUTPUT_DIR}"

# --- Option B: Use compare wrapper (runs all 3 + generates comparison) ---

python3 compare_gradient_conditions.py \
    --vanilla-ckpt "${VANILLA_CKPT}" \
    --full-occ-ckpt "${FULL_OCC_CKPT}" \
    --detach-ckpt "${DETACH_CKPT}" \
    --num-samples 800 --batch-size 4 --gpu 0 --seed 42 \
    --output-dir "${OUTPUT_DIR}" \
    --output-json "${OUTPUT_DIR}/comparison_results.json"

# --- Option C: Compare from pre-computed JSONs ---

python3 compare_gradient_conditions.py \
    --vanilla-json "${OUTPUT_DIR}/Vanilla_v2_gradient_stats.json" \
    --full-occ-json "${OUTPUT_DIR}/Full_OCC_LN_v2_gradient_stats.json" \
    --detach-json "${OUTPUT_DIR}/Detach_LN_v2_gradient_stats.json" \
    --output-json "${OUTPUT_DIR}/comparison_results.json"
```

**Note**: Replace `${VANILLA_EXP_ID}`, `${FULL_OCC_EXP_ID}`, `${DETACH_EXP_ID}` with actual experiment IDs from the v2 training runs.

## Conclusion

V2 脚本方法论与 V1 **完全一致**（修正样本数后）。唯一的结构差异（Vanilla OCC head handling、BN drift tracking）不影响梯度分析的核心指标（per-layer action gradient L2 norm、cross-condition ratio）。
