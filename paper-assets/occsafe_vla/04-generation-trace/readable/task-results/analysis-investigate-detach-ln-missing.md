# analysis investigate detach ln missing

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_investigate_detach_ln_missing_20260524T125128_result.json`
- **Structured JSON:** [`ef7cacaf21d6d25a484b.json`](../../sessions/ef/ef7cacaf21d6d25a484b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

根因已确认，信息足够出报告了。

---

## 调查结论

### 缺失原因

**`BEVOccupancyHead` 的 norm 类型不匹配。**

日志文件 `/root/runs/occsafe_vla/gradient_analysis_mixed_seed.log` 第 209 行的错误：

```
RuntimeError: Error(s) in loading state_dict for BEVOccupancyHead:
    Missing key(s) in state_dict: "decoder.1.running_mean", "decoder.1.running_var", 
    "decoder.4.running_mean", "decoder.4.running_var".
```

- `Detach_LN_s0` 的 checkpoint（`/root/autodl-tmp/checkpoints/detach_ln_s0/.../occ_head--50000_checkpoint.pt`）中 `decoder.1` 和 `decoder.4` 只有 `weight` + `bias`（2 个参数），说明训练时用的是 **GroupNorm(1, C)**（LayerNorm 等价）
- `gradient_analysis.py` 第 220 行始终创建 `BEVOccupancyHead`，而 `occ_head.py` 中该类硬编码使用 **BatchNorm2d**（额外有 `running_mean`, `running_var`）
- 加载 state_dict 时 strict 模式报缺失 key，脚本崩溃退出，其余 4 个条件（均使用 BN 版 OCC head）不受影响

### 修复方案

需要修改两处：

**1. `occ_head.py` — 给 `BEVOccupancyHead` 加 `norm_type` 参数：**

```python
class BEVOccupancyHead(nn.Module):
    def __init__(self, in_dim: int, out_resolution: int = 64, num_classes: int = 1,
                 hidden_dim: int = 256, num_patches_per_image: int = 256, norm_type: str = "bn"):
        super().__init__()
        # ...
        norm1 = nn.GroupNorm(1, 128) if norm_type == "ln" else nn.BatchNorm2d(128)
        norm2 = nn.GroupNorm(1, 64)  if norm_type == "ln" else nn.BatchNorm2d(64)
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(hidden_dim, 128, kernel_size=4, stride=2, padding=1),
            norm1,
            nn.GELU(),
            nn.ConvTranspose2d(128, 64, kernel_size=4, stride=2, padding=1),
            norm2,
            nn.GELU(),
            nn.Conv2d(64, num_classes, kernel_size=1),
        )
```

**2. `gradient_analysis.py` — 加 `--occ_norm` 参数并传给 head：**

```python
# argparse 部分加一行
p.add_argument("--occ_norm", type=str, default="bn", choices=["bn", "ln"])

# 第 220 行创建 head 处
aux_head = BEVOccupancyHead(in_dim=embed_dim, out_resolution=64, num_classes=1,
                            hidden_dim=256, norm_type=args.occ_norm)
```

**3. 重跑 Detach_LN_s0 单条件命令：**

```bash
cd /root/occsafe_vla/openvla-oft && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
CUDA_VISIBLE_DEVICES=0 python /root/occsafe_vla/analysis/gradient_analysis.py \
  --checkpoint_path /root/autodl-tmp/checkpoints/detach_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \
  --condition_name Detach_LN_s0 --condition_type occ --occ_detach true \
  --occ_norm ln \
  --data_root /root/autodl-tmp/data/modified_libero_rlds \
  --occ_data_dir /root/occsafe_vla/occ_data \
  --num_batches 200 --batch_size 4 \
  --output_dir /root/occsafe_vla/artifacts/gradient_analysis_mixed_seed/
```

需要我直接在服务器上执行修复并重跑吗？

---
