# exp-004-s2 训练失败诊断报告

**时间**: 2026-05-22 18:39 (运行约 6.4 小时后崩溃)

## 失败原因

**根分区磁盘满 (os error 28)**。在 step 2500 保存 checkpoint 时，`safetensors` 序列化写入失败：

```
safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```

Traceback 位于 `run_exp004s2_act.py:303` → `model.save_pretrained(ckpt_dir)` → `safe_save_file()`

## 磁盘状态

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| `/` (root) | 30G | 30G | 200K | **100%** |
| `/root/autodl-tmp` | 250G | 57G | 194G | 23% |

根分区主要占用：
- `/root/contrastive_entrain_calib`: 13GB（含 outputs 3.1GB）
- `/root/miniconda3`: 7.9GB
- `/root/tbab_multi_turn`: 2GB
- 其他项目残留: ~2GB

## 训练进度

- **已完成**: 2500/8000 steps (31.25%)
- **总耗时**: 22850 秒 (~6.35 小时)
- **每 step 耗时**: ~9.1 秒
- **Loss 趋势**: sft loss 已降至 ~0.0000，l2 loss 从 0.005 降至 0.0015，训练正常收敛

## Checkpoint 列表

| Checkpoint | 大小 | 状态 |
|-----------|------|------|
| checkpoint-500 | 682M | 完整 |
| checkpoint-1000 | 682M | 完整 |
| checkpoint-1500 | 682M | 完整 |
| checkpoint-2000 | 682M | 完整（含 adapter_config.json + tokenizer） |
| checkpoint-2500 | 402M | 不完整（adapter_model.safetensors 截断，缺 adapter_config.json 等） |

每 500 步保存一次，每个 checkpoint 约 682MB。5 个 checkpoint 共 3.1GB。

## GPU 状态

- GPU 0: RTX PRO 6000 Black, 38GB/98GB 显存, 95% 利用率 (PID 237437)
- GPU 1: RTX PRO 6000 Black, 空闲（exp-004-s2 已退出）

## 恢复建议

### 立即操作

1. **删除不完整 checkpoint**: `rm -rf /root/contrastive_entrain_calib/outputs/exp-004-act-baseline-s2/checkpoint-2500/`（释放 402MB）
2. **将 outputs 迁移到数据盘**:
   ```bash
   mv /root/contrastive_entrain_calib/outputs /root/autodl-tmp/exp-outputs
   ln -s /root/autodl-tmp/exp-outputs /root/contrastive_entrain_calib/outputs
   ```
   释放根分区 ~3GB，后续 checkpoint 写入数据盘（194GB 可用）
3. **可选清理**: 删除旧 checkpoint（仅保留 checkpoint-2000），再释放 ~2GB

### 恢复训练

- 从 **checkpoint-2000** 恢复（最后一个完整 checkpoint）
- 需要修改训练脚本增加 `--resume_from_checkpoint` 或等效参数
- 剩余 5500 步预计耗时 ~14 小时
- GPU 1 当前空闲，可以立即重启
