# ops vtc eval prep westd38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_vtc-eval-prep-westd38929_20260521T185934_result.json`
- **Structured JSON:** [`709612cd56bc7f939d51.json`](../../sessions/70/709612cd56bc7f939d51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westd-38929 有 4 块 NVIDIA RTX PRO 6000 Blackwell (98GB each)，可以并行跑两个 eval。

## VTC Eval 环境就绪度汇报

### 环境状态 ✅ 就绪

| 项目 | 状态 |
|------|------|
| **Python 环境** | conda base: torch=2.8.0+cu128, transformers=5.9.0, accelerate=1.13.0 |
| **LIBERO 依赖** | libero, robosuite=1.4.1, mujoco=3.8.1, h5py, einops, PIL ✅ |
| **OpenVLA 模型** | `/root/autodl-tmp/openvla-libero-object` (15GB) ✅ |
| **代码同步** | eval_openvla_smart_compress.py + openvla_vtc_adapter.py 从 westd-41074 同步，md5 校验通过 ✅ |
| **Config 文件** | m32/m64/m96 yaml 已同步 ✅ |
| **LIBERO 数据** | libero_object (10 tasks, 7GB) ✅ |
| **Dry-run** | 所有 import + VTC 实例化 + eval --help 通过 ✅ |
| **GPU** | 4x RTX PRO 6000 Blackwell (98GB), 全部空闲 |
| **磁盘** | 47GB 可用（可放 2 个 19GB checkpoint） |

### 训练进度（截至 03:01 UTC）
- **M96** (westd-41074 GPU2): step 69200/100K, ~0.5 sps → 约 17h 后完成
- **M32** (westd-27271 GPU1): step 70400/100K, ~0.5 sps → 约 16.5h 后完成
- M64 也在 westd-41074 GPU3 训练中

### Checkpoint 传输命令（训练完成后在 westd-38929 执行）

```bash
# M96 from westd-41074
scp -o StrictHostKeyChecking=no -P 41074 root@connect.westd.seetacloud.com:/root/autodl-tmp/importance_margin_vla_compress/checkpoints/openvla_sc_m96_seed42/checkpoint.pt /root/autodl-tmp/importance_margin_vla_compress/checkpoints/openvla_sc_m96_seed42/

# M32 from westd-27271
scp -o StrictHostKeyChecking=no -P 27271 root@connect.westd.seetacloud.com:/root/autodl-tmp/importance_margin_vla_compress/checkpoints/openvla_sc_m32_seed42/checkpoint.pt /root/autodl-tmp/importance_margin_vla_compress/checkpoints/openvla_sc_m32_seed42/
```

### Eval 命令
```bash
# M96 on GPU0
CUDA_VISIBLE_DEVICES=0 python eval_openvla_smart_compress.py \
  --n_queries 96 --checkpoint_path checkpoints/openvla_sc_m96_seed42/checkpoint.pt \
  --suite libero_object --num_episodes 50 --gpu 0

# M32 on GPU1 (可并行)
CUDA_VISIBLE_DEVICES=1 python eval_openvla_smart_compress.py \
  --n_queries 32 --checkpoint_path checkpoints/openvla_sc_m32_seed42/checkpoint.pt \
  --suite libero_object --num_episodes 50 --gpu 0
```

### 注意事项
- 磁盘只剩 47GB，传完 2 个 checkpoint (38GB) 后仅剩 ~9GB，建议 eval 完及时清理
- 仅有 libero_object 数据；如需评 libero_spatial 等其他 suite 需额外下载

---
