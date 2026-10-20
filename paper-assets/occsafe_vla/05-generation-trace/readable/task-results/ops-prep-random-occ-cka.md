# ops prep random occ cka

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep_random_occ_cka_20260524T010124_result.json`
- **Structured JSON:** [`167e75d39298fb5720d2.json`](../../sessions/16/167e75d39298fb5720d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完成。汇总如下：

---

## 检查结果

### 1. Random OCC Checkpoint
- **仅在 westd-34685**: `/root/autodl-tmp/checkpoints/ablation_random_occ_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt`
- **大小**: 15GB（完整合并模型 4×safetensors + LoRA 463MB + head checkpoints）
- **westd-10894 上不存在**

### 2. CKA 脚本
- **已部署到 10894**: `/root/occsafe_vla/analysis/cka_analysis.py`（275 行，已添加 Random OCC 颜色 `#FF9800`）

### 3. 10894 依赖可用性
| 依赖 | 路径 | 状态 |
|------|------|------|
| Pretrained model | `/root/autodl-tmp/models/openvla-7b` | OK |
| HDF5 数据 | `/root/autodl-tmp/libero_datasets/libero_spatial/` (10 files) | OK |
| openvla-oft 代码 | `/root/occsafe_vla/openvla-oft/` | OK |
| GPU | 4× RTX PRO 6000 Blackwell (96GB each) | OK |
| 磁盘 | 154GB free on /root/autodl-tmp | OK |

### 4. 阻塞项：Checkpoint 传输

15GB checkpoint 需从 34685 → 10894。方案选择：
- **方案 A**: 从 34685 scp 到 10894（需两台服务器能互通，可能不行）
- **方案 B**: 通过本地机器中转（34685→本地→10894，慢但一定可行）
- **方案 C**: 通过云存储中转（如 HuggingFace Hub / 对象存储）

### 5. 运行命令（待 checkpoint 就位后）

```bash
cd /root/occsafe_vla && CUDA_VISIBLE_DEVICES=0 python analysis/cka_analysis.py \
    --pretrained_path /root/autodl-tmp/models/openvla-7b \
    --checkpoint_paths /root/autodl-tmp/checkpoints/ablation_random_occ_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \
    --condition_names "Random OCC" \
    --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial \
    --num_samples 200 \
    --batch_size 8 \
    --gpu 0 \
    --output_dir /root/autodl-tmp/analysis/cka_random_occ
```

### 6. 资源预估
- **GPU 显存**: ~2-3GB（只有 vision backbone on GPU，bf16）
- **CPU 内存**: ~14GB 峰值（加载完整 7B 模型时）
- **运行时间**: ~8-12 分钟（两次模型加载 + forward pass + CKA 计算）
- **风险**: 无，远低于单卡 96GB 上限

---

**下一步需要决定 checkpoint 传输方案。** 要我尝试从 34685 scp 到 10894 测试连通性吗？

---
