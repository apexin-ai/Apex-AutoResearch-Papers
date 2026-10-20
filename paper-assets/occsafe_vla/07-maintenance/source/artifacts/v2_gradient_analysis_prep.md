# V2 梯度分析准备报告

> 生成时间: 2026-05-27 | DDL: 2026-05-28 12:00 UTC

---

## 一、V2 50K Checkpoint 清单

| 条件 | Checkpoint ID | 服务器 | 50K 状态 | 梯度分析状态 |
|------|--------------|--------|---------|-------------|
| Full OCC BN | `full_occ_bn_v2_s1` | 34685 + 10894 | ✅ 完成 | ✅ 已分析（简化版） |
| Full OCC LN | `full_occ_ln_s3_v2` | 10894 | ✅ 完成 | ❌ 待分析 |
| Detach BN | `detach_bn_v2_s0` | 34685 | ✅ 完成 | ✅ 已分析（简化版） |
| Detach LN | `detach_ln_v2_s0c` | 10894:cuda2 | ❌ 训练中 (10K/50K) | ❌ 待分析 |
| Vanilla | `vanilla_v2_s1` | 34685 + 10894 | ✅ 完成 | ✅ 已分析（简化版） |

### Checkpoint 精确路径

```bash
# westd-10894
FULL_OCC_LN="/root/autodl-tmp/checkpoints/full_occ_ln_s3_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_s3_v2--50000_chkpt"

# westd-34685
FULL_OCC_BN="/root/autodl-tmp/checkpoints/full_occ_bn_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_bn_v2_s1--50000_chkpt"
DETACH_BN="/root/autodl-tmp/checkpoints/detach_bn_v2_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_bn_v2_s0--50000_chkpt"
VANILLA="/root/autodl-tmp/checkpoints/vanilla_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s1--50000_chkpt"

# westd-10894（待 50K 完成，预计 ~4h）
DETACH_LN="/root/autodl-tmp/checkpoints/detach_ln_v2_s0c/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s0c--50000_chkpt"
```

### Detach LN v2 可用性风险

- `detach_ln_v2_s0c` 当前在 10894:cuda2 训练，10K/50K，预计 ~4h 后完成
- 备选：`detach_ln_v2_s1` 在 34685 只有 10K（可能已停止/被其他训练占用）
- 无法在 DDL 前拿到的概率较低（50K 应在 ~4h 后完成），但需监控

---

## 二、现有分析脚本状态

### 服务器端脚本（两台服务器均有）

| 脚本 | 路径 | 行数 | 功能 |
|------|------|------|------|
| `run_gradient_analysis_v2.py` | `/root/occsafe_vla/scripts/` | 425 | 单条件逐层梯度分析（RLDS 真实数据，800 samples） |
| `compare_gradient_conditions.py` | `/root/occsafe_vla/scripts/` | ~200 | 多条件对比 + 生成 JSON |

### 方法论要点（与 v1 完全一致）

- **数据源**: 真实 RLDS DataLoader（`libero_spatial_no_noops`）
- **样本数**: 800 samples（200 batches × bs=4）
- **参数范围**: `model.vision_backbone.named_parameters()`
- **层分组**: DINOv2 blocks.{0..23} + SigLIP blocks.{0..26} + stems
- **指标**: per-layer action grad norm, OCC grad norm, cosine similarity, conflict rate
- **Detach 处理**: auto-detect from condition_name

### 已有结果（简化版分析，`v2_gradient_analysis.json`）

用合成数据、5 batches 跑的快速验证，结果已确认核心 pattern：

| 指标 | Full OCC BN | Detach BN | Vanilla |
|------|------------|-----------|---------|
| Action grad norm | 0.531 | 0.753 | 0.584 |
| OCC grad norm | 0.008 | 0.005 | — |
| Cosine sim (act vs OCC) | **-0.001** | **0.000** | — |
| Conflict rate | **0.500** | **0.500** | — |
| OCC/Action ratio | 0.014 | 0.007 | — |
| DINOv2/SigLIP ratio | 1.04 | 1.04 | 1.02 |

**已确认的 v2 pattern**:
- Cosine similarity ≈ 0（梯度正交）→ 与 v1 一致
- Conflict rate ≈ 0.50（随机方向）→ 与 v1 一致
- OCC 梯度量级远小于 Action（1.4%）→ "existence regularization" 而非 gradient competition

---

## 三、推荐分析方案

### 方案 A：完整 5 条件逐层分析（推荐）

用服务器端 `run_gradient_analysis_v2.py` 对 5 个条件各跑 800 samples 的逐层分析。

**论文需要的核心指标**:
1. **Per-layer action gradient L2 norm** — 跨条件对比 gradient flow 差异
2. **Per-layer cosine similarity (action vs OCC)** — 验证梯度正交性
3. **Per-layer conflict rate** — 方向冲突的层级分布
4. **Cross-condition ratio** (Full OCC/Vanilla, Detach/Vanilla) — 放大效应的量化
5. **DINOv2 vs SigLIP 分离** — 两个 backbone 的差异响应

**执行顺序**（GPU 紧张，需分阶段）:

**阶段 1: 立即可执行（westd-34685 GPU 释放后）**
- Detach BN v2 + Vanilla v2（同在 34685，序贯执行 ~40 min）

**阶段 2: 10894 GPU 释放后**
- Full OCC LN v2（10894，~20 min）
- Full OCC BN v2（10894 上也有副本，或从 34685 跑）

**阶段 3: detach_ln_v2_s0c 训练完成后（~4h）**
- Detach LN v2

### 方案 B：仅补 LN 条件（最小化执行）

已有 BN + Vanilla 的简化版分析结果。只需补 Full OCC LN 和 Detach LN。

- 优点：省时间
- 缺点：BN 条件用的是合成数据简化版，LN 用真实数据完整版，方法论不统一

**结论：推荐方案 A，保证所有 5 个条件使用相同方法论。**

---

## 四、预计执行时间和 GPU 需求

| 步骤 | 条件 | 服务器 | GPU | 时长 |
|------|------|--------|-----|------|
| 1 | Vanilla v2 | 34685 | 1× GPU | ~20 min |
| 2 | Detach BN v2 | 34685 | 1× GPU | ~20 min |
| 3 | Full OCC BN v2 | 34685 | 1× GPU | ~20 min |
| 4 | Full OCC LN v2 | 10894 | 1× GPU | ~20 min |
| 5 | Detach LN v2 | 10894 | 1× GPU | ~20 min |
| **总计** | | | | **~100 min**（序贯），可并行降至 ~40 min |

每条件约需 48GB VRAM（7B 模型 bfloat16 + 梯度）。

---

## 五、执行命令模板

### 环境设置

```bash
source /root/miniconda3/bin/activate occsafe
cd /root/occsafe_vla/scripts
export CUDA_VISIBLE_DEVICES=0  # 替换为可用 GPU
OUTPUT_DIR="/root/occsafe_vla/artifacts/gradient_v2_5cond"
mkdir -p $OUTPUT_DIR
```

### 1. Vanilla v2（westd-34685）

```bash
python3 run_gradient_analysis_v2.py \
  --checkpoint_dir "/root/autodl-tmp/checkpoints/vanilla_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s1--50000_chkpt" \
  --condition_name "Vanilla_v2" \
  --seed 42 --num_samples 800 --batch_size 4 --gpu 0 \
  --output_dir $OUTPUT_DIR
```

### 2. Full OCC BN v2（westd-34685）

```bash
python3 run_gradient_analysis_v2.py \
  --checkpoint_dir "/root/autodl-tmp/checkpoints/full_occ_bn_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_bn_v2_s1--50000_chkpt" \
  --condition_name "Full_OCC_BN_v2" \
  --seed 42 --num_samples 800 --batch_size 4 --gpu 0 \
  --occ_norm bn --occ_detach false \
  --output_dir $OUTPUT_DIR
```

### 3. Detach BN v2（westd-34685）

```bash
python3 run_gradient_analysis_v2.py \
  --checkpoint_dir "/root/autodl-tmp/checkpoints/detach_bn_v2_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_bn_v2_s0--50000_chkpt" \
  --condition_name "Detach_BN_v2" \
  --seed 42 --num_samples 800 --batch_size 4 --gpu 0 \
  --occ_norm bn --occ_detach true \
  --output_dir $OUTPUT_DIR
```

### 4. Full OCC LN v2（westd-10894）

```bash
python3 run_gradient_analysis_v2.py \
  --checkpoint_dir "/root/autodl-tmp/checkpoints/full_occ_ln_s3_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_s3_v2--50000_chkpt" \
  --condition_name "Full_OCC_LN_v2" \
  --seed 42 --num_samples 800 --batch_size 4 --gpu 0 \
  --occ_norm ln --occ_detach false \
  --output_dir $OUTPUT_DIR
```

### 5. Detach LN v2（westd-10894，待 detach_ln_v2_s0c 完成 50K）

```bash
python3 run_gradient_analysis_v2.py \
  --checkpoint_dir "/root/autodl-tmp/checkpoints/detach_ln_v2_s0c/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s0c--50000_chkpt" \
  --condition_name "Detach_LN_v2" \
  --seed 42 --num_samples 800 --batch_size 4 --gpu 0 \
  --occ_norm ln --occ_detach true \
  --output_dir $OUTPUT_DIR
```

### 6. 全条件对比

```bash
python3 compare_gradient_conditions.py \
  --vanilla-json "$OUTPUT_DIR/Vanilla_v2_gradient_stats.json" \
  --full-occ-json "$OUTPUT_DIR/Full_OCC_BN_v2_gradient_stats.json" \
  --detach-json "$OUTPUT_DIR/Detach_BN_v2_gradient_stats.json" \
  --output-json "$OUTPUT_DIR/comparison_bn_results.json"

python3 compare_gradient_conditions.py \
  --vanilla-json "$OUTPUT_DIR/Vanilla_v2_gradient_stats.json" \
  --full-occ-json "$OUTPUT_DIR/Full_OCC_LN_v2_gradient_stats.json" \
  --detach-json "$OUTPUT_DIR/Detach_LN_v2_gradient_stats.json" \
  --output-json "$OUTPUT_DIR/comparison_ln_results.json"
```

---

## 六、注意事项

1. **GPU 争抢**: 10894 全部 4 GPU 被训练占满，分析必须等 GPU 释放。34685 同样 4 GPU 全占。需要监控训练完成或找到空闲 GPU 窗口。

2. **Detach LN v2 阻塞路径**: `detach_ln_v2_s0c` 当前 10K/50K，是唯一的 Detach LN v2 活跃训练。如果此训练失败，没有备选。需要优先监控。

3. **`compare_gradient_conditions.py` 扩展**: 当前脚本设计为 3 条件（Vanilla/Full OCC/Detach）对比。5 条件分析需要分别跑 BN 组和 LN 组的对比，或者修改脚本支持 5 路比较。

4. **论文用途**: 核心论点是 "梯度正交性 + 量级不对称 = existence regularization"。Per-layer 分析可以展示：(a) 正交性是否在所有层均匀分布；(b) BN vs LN 条件下梯度传播模式的差异。

5. **已有简化版结果的价值**: `v2_gradient_analysis.json` 虽然用合成数据，但已确认 cosine≈0、conflict≈0.50 的核心 pattern。完整分析主要补充 per-layer 粒度和方法论统一性。
