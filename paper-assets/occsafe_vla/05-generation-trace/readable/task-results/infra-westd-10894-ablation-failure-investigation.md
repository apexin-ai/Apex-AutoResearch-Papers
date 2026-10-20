# infra westd 10894 ablation failure investigation

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd-10894-ablation-failure-investigation_20260521T104137_result.json`
- **Structured JSON:** [`c7c903fe4a995492a0b9.json`](../../sessions/c7/c7c903fe4a995492a0b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

情况和 Cron 报告不同。让我汇总。

## 调查结果

### Cron 报告有误 — 4 个进程中只有 1 个真正失败

| 实验 | PID | GPU | 状态 | 当前 step | 说明 |
|------|-----|-----|------|-----------|------|
| ablation_occ_detach_s0 | 515223 | cuda:0 | **挂死** | 死于 ~12500 | 磁盘满时保存 checkpoint 失败，进程未退出，卡住占 62GB 显存 |
| ablation_random_occ_s0 | 494454 | cuda:1 | **存活** | ~12350 | 刚保存 step 12500 checkpoint，运行正常 |
| ablation_occ_detach_s1 | 517869 | cuda:2 | **存活** | ~822 | 正在训练，~1 it/s（有周期性 I/O 尖峰降到 3-6 s/it） |
| ablation_random_occ_s1 | 519025 | cuda:3 | **存活** | ~821 | 正在训练，~1 it/s（同上） |

### 失败原因

**ablation_occ_detach_s0** — 唯一真正失败的实验：
- 原因：`safetensors_rust.SafetensorError: I/O error: No space left on device (os error 28)`
- 发生在 step 12500 保存 checkpoint 时（merge LoRA → save_pretrained）
- 进程状态 Ssl（sleep），占 62GB GPU 显存但无任何输出，**需要 kill**
- 最后成功保存的 checkpoint：step 10000

**ablation_occ_detach_s1 和 ablation_random_occ_s1** — Cron 误报，实际仍在训练。可能是 Cron 监控的是 wrapper 脚本 PID 而非 python 进程 PID。

### 磁盘状态

```
/dev/md0  250G  111G  140G  45%  /root/autodl-tmp
```

### Checkpoint 空间分布

| 目录 | 大小 | 内容 |
|------|------|------|
| vanilla_s0 | 15G | latest + 50000_chkpt（已完成） |
| vanilla_s1 | 15G | latest + 50000_chkpt（已完成） |
| vanilla_s2 | 15G | latest + 50000_chkpt（已完成） |
| ablation_occ_detach_s0 | 15G | latest + 10000_chkpt |
| ablation_random_occ_s0 | 15G | latest + 12500_chkpt |
| ablation_occ_detach_s1 | 4K | 仅 dataset_statistics（还没到第一个 save_freq=2500）|
| ablation_random_occ_s1 | 4K | 同上 |
| **总计** | **~75G** | |

### I/O 尖峰问题

s1 实验的训练速度周期性从 ~1 it/s 暴跌到 3-8 s/it。时间点与其他实验保存 checkpoint 吻合——4 个实验共享同一块磁盘，checkpoint save（merge 全模型 ~7.5GB）会造成严重 I/O 争抢。

### 建议

1. **立即 kill PID 515223**（ablation_occ_detach_s0 挂死进程），释放 cuda:0 的 62GB 显存
2. **重启 ablation_occ_detach_s0**，从 step 10000 resume
3. **可安全清理的 checkpoint**（如果 vanilla 评估已完成）：
   - `vanilla_s0/s1/s2` 中的 `openvla-7b+...--image_aug/` 目录（非 `--50000_chkpt`）是训练时的中间状态，每个约 7.5G，可删除释放 ~22.5G
4. 当前磁盘 140G 空余足够，但 4 个 ablation 实验全部跑完（各保存 ~20 个 checkpoint × 清理策略）需要注意空间规划

---
