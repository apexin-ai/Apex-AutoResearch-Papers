# code plan 012 prep

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_012_prep_20260516T002907_result.json`
- **Structured JSON:** [`2f6a096f651ef60b2a92.json`](../../sessions/2f/2f6a096f651ef60b2a92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. CLIP 模型可用性：**BLOCKER**
服务器上没有 CLIP ViT-L/14 权重。HF cache 仅有 `dinov2-large` 和 `openvla-7b`。服务器无外网，无法在线下载。

**需要手动下载** `openai/clip-vit-large-patch14` 到 `/root/vla-ssd/checkpoints/clip-vit-large-patch14/`。权重约 1.7GB，需要的文件：
- `config.json`, `preprocessor_config.json`
- `pytorch_model.bin` 或 `model.safetensors`

### 2. 脚本状态
- **路径**: `/root/vla-ssd/scripts/extract_clip_features.py`
- **状态**: 语法通过，`--help` 正常，等模型权重即可运行
- 输出格式与 DINO 完全对齐：`traj_{i}/cls_token` + `traj_{i}/patch_mean`，(T, 1024) float16，gzip 压缩
- 输出路径：`/root/autodl-tmp/vla-ssd/features/clip_libero_goal/`
- RSA 脚本只需把 `load_dino_features` 中路径改为 `clip_libero_goal` 即可复用

### 3. 预计资源需求
- **GPU 内存**: ~1.5GB（CLIP ViT-L 仅 304M 参数，比 DINO ViT-L 略小）
- **运行时间**: 10 task × 50 demo × ~150 frames ≈ 75K frames，batch_size=32 约 10-15 分钟（单 GPU）
- 当前 GPU 被 plan_008 占用，需等其完成

---
