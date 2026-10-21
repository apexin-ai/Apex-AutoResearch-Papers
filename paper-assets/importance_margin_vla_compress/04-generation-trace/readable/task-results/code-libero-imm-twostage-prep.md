# code libero imm twostage prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_libero_imm_twostage_prep_20260516T170818_result.json`
- **Structured JSON:** [`53e16486e9287b9db8c0.json`](../../sessions/53/53e16486e9287b9db8c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 完成。结果汇总：

### 1. 配置文件 ✅

`configs/libero_imm_twostage.yaml` 已创建。继承 `libero_baseline.yaml`，添加 IMM + two-stage 设置。

### 2. 兼容性检查 ✅

| 组件 | 结果 |
|------|------|
| `train_twostage.py` | 完全数据集无关，通过 config 加载数据集 |
| `imm/acis.py` | 无 aloha-specific 代码 |
| `imm/token_selection.py` | 无 aloha-specific 代码 |
| `train.py::load_dataset()` | 通用，直接使用 `config["dataset"]["repo_id"]` |
| Config 继承链 | `libero_imm_twostage.yaml` → `libero_baseline.yaml`（LIBERO 数据集、8-dim state、7-dim action、双摄像头）|

**结论：无需修改任何代码，直接可用。**

### 3. 启动 Checklist

- [ ] LIBERO LoRA baseline 100K checkpoint 就绪（从 cqa1 同步到 westd-27271）
- [ ] 确认 checkpoint 路径：`checkpoints/libero_baseline/step_099999/checkpoint.pt`
- [ ] LIBERO 数据集可访问（`HuggingFaceVLA/libero` 在服务器上缓存或可下载）
- [ ] W&B 可用

**启动命令：**

```bash
cd /root/autodl-tmp/importance_margin_vla_compress
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# Dry-run 验证（CPU，几秒完成）
python train_twostage.py --config configs/libero_imm_twostage.yaml --dry_run --max_steps 3

# 正式训练
nohup python train_twostage.py \
  --config configs/libero_imm_twostage.yaml \
  --wandb_run libero_imm_twostage_v1 \
  > logs/libero_imm_twostage.log 2>&1 &
```

---
