# Server Diagnostic Report — autodl-5090

**Date**: 2026-05-18 09:01 UTC

## 1. Disk Space

| Mount | Size | Used | Avail | Use% |
|-------|------|------|-------|------|
| / (overlay) | 30G | 12G | 19G | 40% |
| /root/autodl-tmp | 250G | 102G | 149G | 41% |
| /autodl-pub | 14T | 9.1T | 5.0T | 65% |

Project total: 57G (`/root/autodl-tmp/struct_self_consist_ie/`)

**结论: 磁盘空间充足，149G 可用。非空间不足导致的 I/O 错误。**

## 2. GPU 状态

| GPU | Memory | Util | Process |
|-----|--------|------|---------|
| 0 (5090) | 26804/32607 MiB | 86% | PID 436761 — 3-epoch train (active) |
| 1 (5090) | 26804/32607 MiB | 100% | PID 436916 — 10-epoch train (active) |
| 2 (5090) | 2/32607 MiB | 0% | idle |
| 3 (5090) | 2/32607 MiB | 0% | idle |

- 旧 vLLM 进程 PID 416808 **已不存在**（自行退出或被杀）
- 当前无残留进程

## 3. 训练进度（当前运行中）

**exp_029a (3-epoch, GPU 0)**:
- Step 180/351 (51.28%), elapsed 8:37
- Loss: 0.7057 → 0.0744, eval_loss@100: 0.1054
- checkpoint-100 已成功保存（1015M，文件完整）

**exp_029b (10-epoch, GPU 1)**:
- Step 170/1170 (14.53%), elapsed 8:13
- Loss: 0.8284 → 0.0887, eval_loss@100: 0.1162
- checkpoint-100 已成功保存（1015M，文件完整）

## 4. Checkpoint 完整性

两个 checkpoint-100 目录均完整，包含：
- adapter_model.safetensors (349M)
- optimizer.pt (699M)
- tokenizer files, trainer_state, rng_state 等

**无需清理损坏文件——当前 checkpoint 完好。**

## 5. 根因分析

原始失败（已自行恢复）：
1. **exp_029a I/O 错误**: 磁盘空间充足(149G free)，推测为瞬时 RAID I/O 抖动（/dev/md0）。配置 `overwrite_output_dir: true` 使得重启后覆盖了之前损坏的状态。
2. **exp_029b OOM**: 残留 vLLM PID 416808 占用 30.2GB 显存。该进程已不存在，重启后 GPU 1 可正常使用。

## 6. 训练配置审查

两个 config 共同设置：
- `save_steps: 100`, `save_total_limit: 3`
- 每个 checkpoint 约 1015M（含 optimizer.pt 699M）
- 3-epoch 最多产生 3 个 ckpt × 1015M = ~3G
- 10-epoch 最多产生 3 个 ckpt × 1015M = ~3G

**优化建议**（非紧急，空间充足）：
- 可添加 `save_only_model: true` 将 checkpoint 从 1015M 降至 ~350M（不保存 optimizer state）
- 当前空间充裕(149G)，不加也无碍

## 7. 结论

**无需任何操作。** 两个实验已成功重启并正常运行，checkpoint-100 保存成功。预计完成时间：
- exp_029a: ~8 分钟后完成
- exp_029b: ~40 分钟后完成
