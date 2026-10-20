# 实验失败诊断报告：磁盘满导致 checkpoint 保存失败

**日期**: 2026-05-26  
**服务器**: westd-10894  
**失败时间**: 两个实验均在 05/26 ~04:24 崩溃

---

## 根因：数据盘 `/dev/md0` 100% 满

```
/dev/md0  250G  250G  292K  100%  /root/autodl-tmp
```

两个实验同时在 step 30000 触发 checkpoint 保存，磁盘空间不足导致 safetensors 序列化失败。

---

## 实验 1: full_occ_ln_s3_v2

**训练进度**: 从 step 20000 resume，训练到 step 30000（完成 10K 步）  
**失败点**: 保存 step-30000 checkpoint 时崩溃

**关键 traceback**:
```
finetune.py:1265 → save_training_checkpoint()
finetune.py:694  → vla.module.save_pretrained(adapter_dir)
safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```

**30000 checkpoint 状态**: 仅 2.5MB，严重不完整（只有 tokenizer 和空 lora_adapter 目录，缺少模型权重）→ **不可用，需删除**  
**20000 checkpoint 状态**: 15G，完整可用，可重新 resume

---

## 实验 2: ablation_occ_detach_s3_v2

**训练进度**: 从 step 20000 resume，训练到 step 30000（完成 10K 步）  
**失败点**: 保存 step-30000 checkpoint 时崩溃

**关键 traceback**:
```
finetune.py:1265 → save_training_checkpoint()
finetune.py:734  → merged_vla.save_pretrained(checkpoint_dir)
safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```

**30000 checkpoint 状态**: 5.0GB，部分写入（有 model-00001-of-00004.safetensors 但缺 2-4 分片，有 action_head/occ_head/proprio_projector）→ **不可用，需删除**  
**20000 checkpoint 状态**: 完整可用，可重新 resume

---

## 磁盘占用分析

当前 `/root/autodl-tmp/checkpoints/` 主要占用：

| 目录 | 大小 |
|------|------|
| ablation_occ_detach_s3 | 35G |
| full_occ_ln_s3 | 30G |
| mvp_occ_s3 | 30G |
| cutoff_45k_s2 | 30G |
| full_occ_ln_s0/s1/s2 | 15G × 3 = 45G |
| cutoff_45k_s2_v2 | 15G |
| full_occ_retrain_s0 | 15G |
| vanilla_retrain_s0 | 15G |
| ablation_occ_detach_s0_retrain | 15G |
| **合计 checkpoint** | **~230G** |

每个完整 checkpoint 约 15G。两个实验继续跑到 50K 还需保存 step 30K/40K/50K，共需额外 ~90-180G 空间。

---

## GPU 状态

GPU 2/3（实验用卡）已释放，当前仅 GPU 0 有进程在跑（PID 4294，占用 62G）。

---

## 修复建议

1. **删除损坏的 30K checkpoint**（释放 ~7.5G）：
   - `rm -rf /root/autodl-tmp/checkpoints/full_occ_ln_s3/...-30000_chkpt/`
   - `rm -rf /root/autodl-tmp/checkpoints/ablation_occ_detach_s3/...-30000_chkpt/`

2. **清理不再需要的旧 checkpoint** 以腾出足够空间。候选：
   - 各实验的中间 checkpoint（如保留最新的，删除 10K checkpoint）
   - 已完成评估的旧实验 checkpoint（mvp_occ_s3、cutoff_45k_s2 等）
   - 需要用户确认哪些可以删

3. **确保至少有 60G 可用空间**后再重新 resume（两个实验各需保存 30K/40K/50K 三个 checkpoint）

4. **从 step 20000 重新 resume**（注意：C002 约束要求 cutoff/reverse_cutoff 实验禁止 resume，但这两个实验不受此约束）
