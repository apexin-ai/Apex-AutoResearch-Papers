# 诊断报告：ablation_occ_detach_s3_v2 & full_occ_ln_s3_v2 失败

**日期**: 2026-05-26
**服务器**: westd-10894
**失败时间**: 两个实验均于 2026-05-26 04:24 同时失败

## 1. 根因：磁盘满（同一根因）

```
Filesystem      Size  Used Avail Use% Mounted on
/dev/md0        250G  250G  292K 100% /root/autodl-tmp
```

checkpoints 目录占 229GB（91.6%）。两个实验在 step 30000 保存 checkpoint 时磁盘写满，`safetensors` 序列化报错 `os error 28: No space left on device`。

## 2. 各实验错误详情

### ablation_occ_detach_s3_v2

- **训练进度**: step 20000 → 30000（10k 步完成，保存时失败）
- **失败调用栈**:
  ```
  finetune.py:1265 → save_training_checkpoint()
  finetune.py:734  → merged_vla.save_pretrained(checkpoint_dir)
  safetensors/torch.py:307 → serialize_file()
  SafetensorError: I/O error: No space left on device (os error 28)
  ```
- **30000 checkpoint 状态（损坏，需删除）**:
  - ✅ lora_adapter (484MB), action_head (302MB), occ_head (2.4MB), proprio_projector (67MB)
  - ✅ model-00001-of-00004.safetensors (4.48GB)
  - ❌ model-00002~00004 缺失
- **保存路径**: `ablation_occ_detach_s3/`（非 _s3_v2）

### full_occ_ln_s3_v2

- **训练进度**: step 20000 → 30000（10k 步完成，保存时失败）
- **失败调用栈**:
  ```
  finetune.py:1265 → save_training_checkpoint()
  finetune.py:694  → vla.module.save_pretrained(adapter_dir)
  safetensors/torch.py:307 → serialize_file()
  SafetensorError: I/O error: No space left on device (os error 28)
  ```
- **30000 checkpoint 状态（损坏，需删除）**:
  - ❌ adapter_model.safetensors 仅 135KB（正常应 ~484MB）
  - ❌ 缺 adapter_config.json, action_head, occ_head, proprio_projector
- **保存路径**: `full_occ_ln_s3/`（非 _s3_v2）

## 3. 磁盘占用明细

| 目录 | 大小 |
|------|------|
| ablation_occ_detach_s3/ | 35G |
| full_occ_ln_s3/ | 30G |
| mvp_occ_s3/ | 30G |
| cutoff_45k_s2/ | 30G |
| cutoff_45k_s2_v2/ | 15G |
| ablation_occ_detach_s0_retrain/ | 15G |
| full_occ_ln_s0/ | 15G |
| full_occ_ln_s1/ | 15G |
| full_occ_ln_s2/ | 15G |
| full_occ_retrain_s0/ | 15G |
| vanilla_retrain_s0/ | 15G |
| 其他 (cutoff_15k_s1 等) | <1G |
| **checkpoints 合计** | **229G** |
| data + models + libero_datasets | ~23G |

## 4. 服务器状态

- GPU 0: 在用（62200MiB, PID 4294），GPU 1-3: 空闲
- 失败实验进程已退出，无残留

## 5. 重试方案

**可以重试。** 20000 step checkpoint 完好。

### 必做步骤

1. **删除损坏的 30000 checkpoint**（释放 ~5GB）:
   ```bash
   rm -rf /root/autodl-tmp/checkpoints/ablation_occ_detach_s3/*--30000_chkpt
   rm -rf /root/autodl-tmp/checkpoints/full_occ_ln_s3/*--30000_chkpt
   ```

2. **清理旧 checkpoint 释放空间**（需用户确认，建议至少释放 30-50GB）:
   - 各实验的 10k 中间 checkpoint（如果只需 20k+ 结果）
   - 已完成/不再需要的实验目录

3. **从 step-020000 重新 resume**（命令同原始命令）

### 注意事项
- 两个实验同时保存 checkpoint 瞬间需 ~30GB 额外空间（merged model ~15GB × 2）
- 考虑错开启动时间避免同时触发 checkpoint save
