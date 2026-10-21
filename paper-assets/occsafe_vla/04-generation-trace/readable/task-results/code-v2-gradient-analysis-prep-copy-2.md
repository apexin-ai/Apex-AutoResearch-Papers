# code v2 gradient analysis prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v2-gradient-analysis-prep_20260527T021109_result.json`
- **Structured JSON:** [`e540599c28b1ef03f82a.json`](../../sessions/e5/e540599c28b1ef03f82a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。汇报如下：

---

## 梯度分析脚本就绪状态

### 脚本路径和状态

| 脚本 | 10894 | 34685 | 状态 |
|------|-------|-------|------|
| `run_gradient_analysis_v2.py` | `/root/occsafe_vla/scripts/` | 已复制 ✓ | 可用 |
| `compare_gradient_conditions.py` | `/root/occsafe_vla/scripts/` | 已复制 ✓ | 可用 |
| `plot_gradient_analysis_v2.py` | `/root/occsafe_vla/scripts/` | 已复制 ✓ | 可用 |

无需修改，v2 checkpoint 格式完全兼容：
- `AutoModelForVision2Seq.from_pretrained(checkpoint_dir)` 直接加载 ✓
- `occ_head--50000_checkpoint.pt` 匹配脚本 glob 模式 ✓
- 自动检测 `occ_detach`/`occ_norm` 从 condition name ✓

### v2 Checkpoint 分布

**10894** (已完成):
- `full_occ_ln_s3_v2` → Full OCC + LN
- `ablation_occ_detach_s3_v2` → Detach + LN

**34685** (已完成):
- `vanilla_v2_s1` → Vanilla baseline
- `full_occ_bn_v2_s1` → Full OCC + BN
- `detach_bn_v2_s0/s1/s2` → Detach + BN

### 当前状态
两台服务器 8 张 GPU 全部训练占用（~62GB/98GB），无法 dry-run。

### 推荐运行命令

训练结束后，分两阶段执行：

**阶段 1：各服务器本地跑 per-condition 分析**

```bash
# === 10894 (GPU 0 or whichever frees first) ===

# Full OCC LN v2
python3 /root/occsafe_vla/scripts/run_gradient_analysis_v2.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/full_occ_ln_s3_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_s3_v2--50000_chkpt \
  --condition_name "Full OCC LN v2" --seed 42 \
  --output_dir /root/occsafe_vla/artifacts/gradient_v2/ \
  --gpu 0

# Detach LN v2
python3 /root/occsafe_vla/scripts/run_gradient_analysis_v2.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/ablation_occ_detach_s3_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--ablation_occ_detach_s3_v2--50000_chkpt \
  --condition_name "Detach LN v2" --seed 42 \
  --output_dir /root/occsafe_vla/artifacts/gradient_v2/ \
  --gpu 0
```

```bash
# === 34685 (GPU 0 or whichever frees first) ===

# Vanilla v2
python3 /root/occsafe_vla/scripts/run_gradient_analysis_v2.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/vanilla_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s1--50000_chkpt \
  --condition_name "Vanilla v2" --seed 42 \
  --output_dir /root/occsafe_vla/artifacts/gradient_v2/ \
  --gpu 0
```

**阶段 2：汇总比较（SCP JSONs 到 10894 后执行）**

```bash
# 从 34685 scp vanilla JSON 到 10894
scp westd-34685:/root/occsafe_vla/artifacts/gradient_v2/"Vanilla v2_gradient_stats.json" \
    /root/occsafe_vla/artifacts/gradient_v2/

# 三条件对比
python3 /root/occsafe_vla/scripts/compare_gradient_conditions.py \
  --vanilla-json "/root/occsafe_vla/artifacts/gradient_v2/Vanilla v2_gradient_stats.json" \
  --full-occ-json "/root/occsafe_vla/artifacts/gradient_v2/Full OCC LN v2_gradient_stats.json" \
  --detach-json "/root/occsafe_vla/artifacts/gradient_v2/Detach LN v2_gradient_stats.json" \
  --output-json /root/occsafe_vla/artifacts/gradient_v2/comparison_results.json

# 可视化（可选）
python3 /root/occsafe_vla/scripts/plot_gradient_analysis_v2.py \
  --results_dir /root/occsafe_vla/artifacts/gradient_v2/ \
  --output /root/occsafe_vla/artifacts/gradient_v2/gradient_analysis_v2_combined.pdf
```

如果还需 BN 条件的 2×2 分析（Full OCC BN + Detach BN），34685 上可额外运行两个 condition，condition_name 分别传 `"Full OCC BN v2"` 和 `"Detach BN v2"`。

---
