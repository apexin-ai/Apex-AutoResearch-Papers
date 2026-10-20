# Phase Diagram 实验失败诊断 (westd-17855)

**诊断时间**: 2026-05-21
**服务器**: westd-17855

## 根因

**磁盘满 (os error 28)**。`/dev/md0` (挂载 `/root/autodl-tmp/`) 350G 已用 350G，剩余仅 1.2M。

两个实验均在 `model.save_pretrained()` 写 safetensors checkpoint 时失败，traceback 完全相同：

```
File "/root/autodl-tmp/distrib_canary_collapse/iterative_train.py", line 316, in main
    model.save_pretrained(ckpt_path)
  → safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```

## 实验 1: phase_diagram_t25_a050_s42_fp32

| 项目 | 值 |
|------|-----|
| 目标 generations | 25 |
| 已完成 generations | 14 (gen_0 ~ gen_13) |
| 失败位置 | gen_14 checkpoint 写入 |
| GPU 时间浪费 | 训练 gen_14 的 ~10.8 min（训练已完成 5000/5000 steps，仅 checkpoint 写入失败） |
| 总运行时长 | 5.76 GPU hours |
| 最后 train_loss | 1.069 |

gen_14 目录已创建但 checkpoint 不完整。

## 实验 2: phase_diagram_t20_a060_s43_fp32

| 项目 | 值 |
|------|-----|
| 目标 generations | 20 |
| 已完成 generations | 3 (gen_0 ~ gen_2) |
| 失败位置 | gen_3 checkpoint 写入 |
| GPU 时间浪费 | 训练 gen_3 的 ~10.8 min |
| 总运行时长 | 1.37 GPU hours |
| 最后 train_loss | 1.264 |

gen_3 目录已创建但 checkpoint 不完整。

## 磁盘状态

```
Filesystem      Size  Used Avail Use% Mounted on
/dev/md0        350G  350G  1.2M 100% /root/autodl-tmp
```

## 重试建议

1. **必须先清理磁盘**。Pythia-410m 每个 generation checkpoint ~800MB (safetensors)，25 gen 实验需要 ~20GB 增量空间。当前 0 可用空间，无法重试。
2. **清理候选**：
   - 已完成实验的中间 checkpoint（只保留 all_metrics.json 和最终 gen）
   - HF cache 中重复的模型文件
   - `du -h --max-depth=1 /root/autodl-tmp/` 定位大目录
3. **如果 17855 空间无法释放到 50GB+**，考虑转移到其他服务器运行。
4. **重试时可从断点续跑**（如果脚本支持 `--resume_from_gen`），否则需要从头重跑。
5. **不需要修改命令参数**，错误与训练配置无关。
