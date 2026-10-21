# westb-23072 Qwen-Math SFT 诊断与修复报告

**时间**: 2026-05-20 17:50 UTC

## 诊断发现

### OOM 原因
`sft_qwen_math_standard_20_v2` 在 step 0 OOM 崩溃。原因是 **CUDA_VISIBLE_DEVICES 映射错误**，两个 SFT 进程均加载到 GPU 0：

- CKA-only v2（PID 9957）占用 GPU 0 约 49.85 GiB
- Standard v2 尝试在 GPU 0 分配 optimizer state，剩余仅 44.25 MiB，触发 OOM

错误信息：`torch.OutOfMemoryError: Tried to allocate 130.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 44.25 MiB is free. Process 9957 has 49.85 GiB memory in use.`

**根因**: 首次提交 Standard v2 时 CUDA_VISIBLE_DEVICES 未正确注入为 `1`，导致 `--gpu 0` 映射到物理 GPU 0 而非 GPU 1。

### 单卡 VRAM 需求
Qwen2.5-Math-7B SFT 单卡峰值 ~50 GiB（模型 + optimizer + activations），95 GiB GPU 完全足够，**无需 gradient_checkpointing**。

## 修复措施

1. **确认 CKA-only v2 已完成**: epoch 1.0, train_loss=0.3481, mean_token_accuracy=0.8595, runtime=1013s。模型已保存至 `/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final`

2. **重新提交 Standard v2**: 通过 `submit_training_job` 提交到 `cuda:1`，框架自动注入 `CUDA_VISIBLE_DEVICES=1`
   - PID: 12115
   - tmux session: sft_qwen_math_standard_20_v2

## 两个 SFT 当前状态

| 实验 | GPU | 状态 | PID | 预估完成时间 |
|------|-----|------|-----|-------------|
| sft_qwen_math_cka_only_20_v2 | cuda:0 | **已完成** ✓ | - | 已完成 (17:37 UTC) |
| sft_qwen_math_standard_20_v2 | cuda:1 | **运行中** (重新提交) | 12115 | ~18:07 UTC (~17min runtime) |

预估完成时间基于 CKA-only v2 的实际运行时间 1013 秒（~17 分钟）。