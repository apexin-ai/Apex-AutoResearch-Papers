# ssh plan012 clip prep

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan012-clip-prep_20260516T002934_result.json`
- **Structured JSON:** [`be26a69a1e2e92fa9ed9.json`](../../sessions/be/be26a69a1e2e92fa9ed9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

---

## 产出汇总

### 1. 模型可用性
- **本地无 CLIP ViT-L/14 权重**。HF cache 只有 `dinov2-large` 和 LIBERO 数据集，checkpoints 目录只有 `dinov2-large`/`openvla`/`openvla-7b`/`openvla-7b-untrained`
- **需下载**：`openai/clip-vit-large-patch14`（~890MB）。建议用 ModelScope CDN 或 `source /etc/network_turbo` 后 HF 下载
- **需安装的包**：无额外包——`transformers 4.57.6` 已有 `CLIPModel`/`CLIPProcessor`

### 2. 脚本已部署
- **`/root/vla-ssd/scripts/extract_features_clip.py`** — CLIP 特征提取
  - 输入：LIBERO-Goal 10 tasks × 50 demos
  - 输出：`/root/autodl-tmp/vla-ssd/features/clip_libero_goal/{task}.h5`
  - 格式：`traj_{i}/{cls_token, patch_mean}`，shape (T, 1024)，float16，gzip 压缩——与 DINO 完全一致
  - 支持 `--gpu`、`--model_path`（本地路径）、skip 已完成 task
- **`/root/vla-ssd/scripts/rsa_clip.py`** — CLIP RSA 分析
  - 对 `cls_token` 和 `patch_mean` 都跑 RSA，取最佳
  - 输出对比表（vs SigLIP 0.615 / DINO 0.388 等）

### 3. dry-run
`python scripts/extract_features_clip.py --help` ✅

### 4. RSA 兼容性
- CLIP 输出 hidden_size=1024，与 DINO ViT-L 一致
- 输出格式 `traj_*/cls_token` 与 DINO 完全一致，现有 `rsa_analysis.py` 的 `load_dino_features` 也可直接复用（只需改 feature 目录路径）
- 独立 `rsa_clip.py` 已就绪，方法论与 `rsa_siglip_only.py` 完全匹配

### 5. 下一步（GPU 释放后）
```bash
# 1. 下载模型（需网络）
source /etc/network_turbo
python -c "from transformers import CLIPModel, CLIPProcessor; m=CLIPModel.from_pretrained('openai/clip-vit-large-patch14'); m.save_pretrained('/root/vla-ssd/checkpoints/clip-vit-large-patch14'); p=CLIPProcessor.from_pretrained('openai/clip-vit-large-patch14'); p.save_pretrained('/root/vla-ssd/checkpoints/clip-vit-large-patch14')"

# 2. 提取特征
python scripts/extract_features_clip.py --model_path /root/vla-ssd/checkpoints/clip-vit-large-patch14 --gpu 0

# 3. 跑 RSA
python scripts/rsa_clip.py
```

---
