# code plan003 scalar unc ablation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan003-scalar-unc-ablation_20260513T233144_result.json`
- **Structured JSON:** [`fa8ac199a2cf227ffa11.json`](../../sessions/fa/fa8ac199a2cf227ffa11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

**scalar_unc 实现状态**: 原代码只完成了一半——模型层面注册了 `unc_dim=3`，但训练循环缺少 40D→3D 的特征转换，直接运行会维度不匹配崩溃。

**已完成的修改** (`src/train_crm.py`):
1. 添加 `scalar_unc` 标志（line 342）
2. 添加 `_to_scalar_uf()` 辅助函数（line 364-370）：将 CGS 40D 输出压缩为 3D
   - `norm(per_dof_std[:30])` → 整体 std 幅度（1D）
   - `mean(conformal_radius[30:35])` → 平均 conformal 半径（1D）
   - `mean(log_volume[35:40])` → 平均 log 体积（1D）
3. 训练循环 CGS 后加 scalar 转换（line 388-389）
4. 验证循环 CGS 后加 scalar 转换（line 434-435）

**dry-run 验证**: 通过
- 端到端管道测试: 40D→3D 压缩 + CRM forward 正确
- 实际训练: 跑了 120+ batches，loss ~0.02-0.06，正常

**CRM 架构**: input_dim = 30(action) + 3(scalar_unc) + 960(obs) = 993, 参数量 327,966

**最终训练命令**:
```bash
CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py \
  --benchmark spatial object \
  --epochs 50 --batch_size 512 --lr 0.016 --K 10 --seed 42 \
  --input_mode scalar_unc \
  --output_dir /root/autodl-tmp/checkpoints/crm/scalar_unc/
```

---
