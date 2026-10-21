# λ=0.1 实验失败诊断报告

**日期**: 2026-05-27 18:00 UTC
**服务器**: westd-35807

## 结论：两个实验均已正常完成，监控系统误判

---

## 实验 1: train_pi05_a1_obj_s1_l01_high（训练）

**状态**: ✅ 已完成 30000/30000 steps

**日志证据**:
- 最后日志行: `Training: 100%|██████████| 30000/30000 [33:58:06<00:00, 4.08s/it]`
- 最终 checkpoint 保存: `Saved checkpoint at step 30000 -> .../a1_sdf_pi05_object_pudding_seed1_l1/30000` (17:50:19 UTC)
- 总训练时长: ~34h

**Checkpoint 目录** (`/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed1_l1/`):
- `best/` (保存于 May 27 02:20)
- `29999/` (保存于 May 27 17:50)
- `30000/` (保存于 May 27 17:50) ← 最终 checkpoint
- `best_loss.txt`
- `wandb_id.txt`

**最终训练指标** (step 30000): loss=0.0171, action=0.0136, sdf=0.0345, ee=0.0058

**失败原因**: 进程正常退出后 PID 不存在，监控系统检测 5 次均发现进程已死且无 sentinel 文件，误判为失败。训练实际已完成。

**是否需要重启/resume**: ❌ 不需要，训练已完成。

---

## 实验 2: eval_pi05_a1_30k_s0_l01_high（评估）

**状态**: ✅ 已完成全部 4 个 tasks

**评估结果**:

| Task | 内容 | TSR | CAR | Smoothness | Max Disp |
|------|------|-----|-----|------------|----------|
| 0 | orange juice → basket | 30.0% | 60.0% | 0.000776 | 0.0677m |
| 1 | chocolate pudding → basket | 70.0% | 74.0% | 0.000764 | 0.0555m |
| 2 | milk → basket | 24.0% | 68.0% | 0.000645 | 0.0313m |
| 3 | bbq sauce → basket | 64.0% | 30.0% | 0.000627 | 0.0918m |
| **Avg** | | **47.0%** | **58.0%** | | |

**结果文件**: `/root/autodl-tmp/eval_results/eval_safelibero_object_all_levelII_30000_lora_baseline_seed7.json`

**失败原因**: 同上，进程正常退出后被监控系统误判。评估实际已完成。

**是否需要重启**: ❌ 不需要，结果已保存。

---

## GPU 当前状态

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| 0 | 9014MiB / 97887MiB | 51% | PID 751737: eval a1_sdf seed0_l01 (新任务) |
| 1 | 9010MiB / 97887MiB | 27% | PID 747037: eval lora_baseline seed0 (新任务) |
| 2 | 1MiB / 97887MiB | 0% | **空闲** |
| 3 | 27037MiB / 97887MiB | 100% | PID 341425: train lora_baseline spatial_bowl s0 |

- GPU 2 完全空闲，可立即使用
- 无残留进程
- dmesg 无权限访问（容器限制），但无关紧要——两个实验均正常完成，不存在 OOM 或硬件错误

---

## 根因分析

监控系统的 "process dead 5× with no sentinel/W&B" 判定逻辑在进程**正常完成退出**后也会触发，因为：
1. 训练脚本完成后进程退出，PID 不再存在
2. 监控系统检测到 PID 死亡，但找不到 sentinel 文件或 W&B 完成信号
3. 连续 5 次检测均如此，auto-resolved 为 failed

**建议**: 检查 sentinel 写入逻辑是否在脚本正常退出时被正确触发。
