# Failure Diagnosis: phase_diagram_t20_a060_s43_fp32

**日期**: 2026-05-21
**服务器**: westd-17855, GPU cuda:4
**运行时长**: ~1.37 GPU hours (4922s)
**EXIT_CODE**: 1

## 1. 失败原因

**磁盘满 (os error 28)**

```
safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```

- 发生在 gen_3 训练完成后保存 checkpoint 时 (`model.save_pretrained()`)
- 磁盘状态: `/dev/md0` 350G/350G 已用 (100%), 仅剩 1.2M
- phase_diagram 目录总占用: 36G

## 2. 实验进度

| Generation | 状态 | metrics.json |
|-----------|------|-------------|
| gen_0 | ✅ 完成 | ✅ |
| gen_1 | ✅ 完成 | ✅ |
| gen_2 | ✅ 完成 | ✅ |
| gen_3 | ❌ 训练完成但保存失败 | ❌ |
| gen_4–gen_19 | 未开始 | — |

gen_3 训练实际跑完了 5000/5000 steps (loss=1.264, train_runtime=650.9s)，但 checkpoint 写入中断，model.safetensors 仅 36KB（应约 800MB），**不可用**。

## 3. 可用的 Partial Results

gen_0, gen_1, gen_2 完整可用（均有 checkpoint + metrics.json）。gen_3 的 synthetic_data 子目录可能完整（训练数据已生成），但 checkpoint 损坏需删除。

## 4. 修复与重试

1. **释放磁盘空间**: westd-17855 数据盘已 100% 满，必须先清理。可考虑:
   - 删除其他已完成实验的中间 checkpoint
   - 或将此实验迁移到磁盘充裕的服务器
2. **删除损坏的 gen_3**: `rm -rf results/phase_diagram/t20_a060_s43_fp32/gen_3/`
3. **从 gen_3 重启**: 如果 iterative_train.py 支持 `--resume_from_gen 3`，则从 gen_2 checkpoint 续跑；否则需确认脚本的断点续跑机制
4. **预估剩余空间需求**: 剩余 17 generations × ~2GB/gen ≈ 34GB 额外空间
