# 诊断报告: smollm3_3b_wiki_a100_s43_fp32

**日期**: 2026-05-19  
**服务器**: westd-19828  
**EXIT_CODE**: 1

## 失败阶段

**训练完成后保存 checkpoint 时失败**。gen_2 的 5000/5000 训练步已全部完成（loss=0.04911, train_loss=0.1923），但在 `model.save_pretrained()` 写入 safetensors 文件时磁盘空间不足。

## 具体错误

```
File "/root/autodl-tmp/distrib_canary_collapse/iterative_train.py", line 318, in main
    model.save_pretrained(ckpt_path)
safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```

## Generation 完成情况

| Generation | 状态 | 说明 |
|-----------|------|------|
| gen_0 | 完成 | baseline，有 synthetic_data |
| gen_1 | 完成 | checkpoint (12.3GB) + metrics.json 齐全 |
| gen_2 | **不完整** | 训练完成但 checkpoint 截断（5.36GB vs 期望 12.3GB），无 metrics.json |
| gen_3~gen_9 | 未开始 | 配置要求 10 generations |

## 磁盘状态

```
/dev/md0  250G  250G  3.5M  100%  /root/autodl-tmp
```

主要占用:
- `results/generalize/` 总计 137GB
  - pythia14b_wiki_a100_s43: 53GB
  - smollm3_3b_wiki_a100_s42_fp32_v3: 24GB
  - smollm3_3b_wiki_a100_s43 (本实验): 17GB
- `models/`: 17GB

## Partial Checkpoint

gen_2/checkpoint/ 存在 model.safetensors（5.36GB），但相比 gen_1 的完整文件（12.3GB）**被截断，不可用**。

## GPU 状态

- GPU 0: 29783/97887 MiB, 91% utilization（有其他任务占用）
- GPU 1: 空闲

## 建议修复方案

1. **清理磁盘空间**：本实验每个 generation 的 checkpoint 约 12GB，剩余 7 个 generation 需要 ~84GB 空间。需清理已完成/不再需要的实验结果：
   - `pythia14b_wiki_a100_s43` (53GB) — 如已完成分析可清理
   - `smollm3_3b_wiki_a100_s42_fp32_v3` (24GB) — 如已完成可清理
2. **删除 gen_2 的损坏 checkpoint**：`rm -rf results/generalize/smollm3_3b_wiki_a100_s43/gen_2/`
3. **从 gen_2 重跑**：设置 `start_gen=2`，复用 gen_1 的 checkpoint 继续
4. **代码层面优化（可选）**：训练完成后先删除上一代 checkpoint 再保存当前代，节省一个 checkpoint 的空间（~12GB）
