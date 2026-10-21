# westd-10894 三实验同时失败诊断

**时间**: 2026-05-27 ~02:00 UTC
**根因**: **磁盘空间不足 (ENOSPC errno 28)**

## 故障机制

三个实验几乎同时到达 step 20000，触发 checkpoint 保存（每个 ~15GB）。数据盘 `/root/autodl-tmp` 总容量 250GB，当时已存储 ~154GB 旧 checkpoints，三个实验同时写入 ~45GB 导致磁盘满。

reverse_cutoff_s2_v2 (cuda:0) 未受影响——它的 checkpoint 保存时间与其他三个错开。

## 各实验错误

| 实验 | 失败时间 | 失败点 | 具体错误 |
|------|---------|--------|---------|
| full_occ_ln_v2_s0 | 02:00:57 | `merged_vla.save_pretrained()` → `safetensors serialize` | `safetensors_rust.SafetensorError: I/O error: No space left on device (os error 28)` |
| detach_ln_v2_s0 | 02:01:05 | `processor.save_pretrained()` → `backend_tokenizer.save()` | `Exception: No space left on device (os error 28)` |
| full_occ_ln_v2_s1 | 02:03:10 | `processor.save_pretrained()` → `shutil.copyfile(tokenizer.model)` | `OSError: [Errno 28] No space left on device` |

三个都在 `save_training_checkpoint()` (finetune.py:1265) 中失败，只是各自写到了不同的子步骤时磁盘才真正满。

## 当前磁盘状态

```
/dev/md0  250G  176G  75G  71%  /root/autodl-tmp
```

checkpoints 目录共 154GB，主要占用：
- reverse_cutoff_s2_v2: 30GB (2 个完整 checkpoint, 仍在运行)
- full_occ_ln_v2_s0: 20GB (10k 完整 15GB + 20k 残缺 5GB)
- full_occ_ln_v2_s1: 15GB (10k 完整 + 20k 残缺)
- detach_ln_v2_s0: 15GB (10k 完整 + 20k 残缺)
- 其余旧实验各 ~15GB (full_occ_ln_s0, full_occ_ln_s3_v2, ablation_occ_detach_s3_v2, cutoff_45k_s2_v2, mvp_occ_s3_v2)

## 是否可以直接重试

**不能直接重试。** 磁盘空间仍然紧张（75GB 剩余），重启后到 step 20000 三个实验再次同时保存仍会失败。且后续 30k/40k/50k checkpoint 也需要空间。

## 修复步骤

1. **删除三个残缺的 20000_chkpt**（释放 ~5-10GB）：
   ```bash
   rm -rf /root/autodl-tmp/checkpoints/full_occ_ln_v2_s0/*--20000_chkpt
   rm -rf /root/autodl-tmp/checkpoints/full_occ_ln_v2_s1/*--20000_chkpt
   rm -rf /root/autodl-tmp/checkpoints/detach_ln_v2_s0/*--20000_chkpt
   ```

2. **清理已完成/不再需要的旧 checkpoints**（需确认哪些可删）：
   - `cutoff_15k_s1` (463MB)
   - `cutoff_25k_s2` (空目录)
   - `full_occ_ln_s0` (15GB) — 旧版实验，是否已有最终结果？
   - `full_occ_bn_v2_s1` (4K, 几乎空)
   - `reverse_cutoff_s2` (空目录)
   - 目标: 释放至少 60GB，确保三个实验的 20k~50k checkpoints 都有空间

3. **重启三个实验**，使用 `--resume` 从 10000_chkpt 恢复（这三个不是 cutoff 类型，不受 C002 约束）
