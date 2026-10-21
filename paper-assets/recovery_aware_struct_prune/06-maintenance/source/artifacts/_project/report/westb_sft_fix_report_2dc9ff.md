# westb-23072 Qwen-Math SFT 诊断与修复报告

**时间**: 2026-05-20 17:52 UTC

## 诊断发现

### OOM 原因
`sft_qwen_math_standard_20_v2` 在 step 0 OOM 崩溃。

**直接原因**: 两个 SFT 进程均加载到 GPU 0。CKA-only v2（PID 9957）占用 49.85 GiB，Standard v2 在 optimizer init 时仅剩 44.25 MiB，触发 OOM。

**根因**: `sft_recovery.py` 第 19-22 行的 early parsing 逻辑：
```python
# Parse --gpu early to set CUDA_VISIBLE_DEVICES before torch import
    if _arg == "--gpu" and _i + 1 < len(sys.argv):
        os.environ["CUDA_VISIBLE_DEVICES"] = sys.argv[_i + 1]
```

`--gpu 0` 将 `CUDA_VISIBLE_DEVICES` 覆写为 `"0"`，覆盖了 submit_training_job 框架注入的 `CUDA_VISIBLE_DEVICES=1`。两个任务的 `--gpu 0` 都将 CUDA 映射到物理 GPU 0。

### 验证
通过 `/proc/12120/environ` 确认：submit_training_job 确实注入了 `CUDA_VISIBLE_DEVICES=1`，但脚本在 import torch 之前就覆写了它。nvidia-smi 确认进程在物理 GPU 0 上。

### 单卡 VRAM 需求
~50 GiB，95 GiB GPU 完全足够，无需 gradient_checkpointing。

## 修复措施

1. **CKA-only v2 已完成**: train_loss=0.3481, mean_token_accuracy=0.8595, runtime=1013s。模型已保存至 `/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final`

2. **Standard v2 已重新提交**: PID 12115 → python PID 12120，通过 submit_training_job 到 cuda:1。虽然 --gpu 0 仍覆写了 CUDA_VISIBLE_DEVICES，但因 CKA-only 已释放 GPU 0，Standard v2 在 GPU 0 上正常运行，step 14/935 @1.08s/it。

3. **后续建议**: 修改命令不传 `--gpu 0`（让框架 CUDA_VISIBLE_DEVICES 生效），或修改 sft_recovery.py 在 CUDA_VISIBLE_DEVICES 已存在时跳过覆写。

## 当前状态

| 实验 | 物理 GPU | 状态 | PID | 预估完成时间 |
|------|----------|------|-----|-------------|
| sft_qwen_math_cka_only_20_v2 | GPU 0 | **已完成** ✓ | - | 17:37 UTC |
| sft_qwen_math_standard_20_v2 | GPU 0* | **训练中** | 12120 | ~18:08 UTC |

*注: 目标 GPU 1，实际落在 GPU 0（--gpu flag 覆写问题），因 CKA-only 已完成不影响本次运行。
