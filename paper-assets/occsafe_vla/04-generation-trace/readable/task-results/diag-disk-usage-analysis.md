# diag disk usage analysis

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_disk_usage_analysis_20260520T093429_result.json`
- **Structured JSON:** [`590ce395aa9e453b4eb5.json`](../../sessions/59/590ce395aa9e453b4eb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已收集完毕。以下是分析报告。

---

## 磁盘空间分析报告

### 1. 当前状态（与预期不符）

**df 实际读数：数据盘可用 416GB**，与"上次报告"一致，并非 214GB。可能之前看到的 214GB 是临时状态（如大文件下载/编译过程中）。

```
数据盘 /dev/sda2:  879G 总量 | 419G 已用 (51%) | 416G 可用
根分区 overlay:     30G 总量 |  19G 已用 (63%) |  12G 可用
```

### 2. 空间使用分项明细

| 类别 | 路径 | 大小 |
|------|------|------|
| **模型权重** | `/root/autodl-tmp/models/openvla-7b` | **15G** |
| **已保存 checkpoint（含合并模型）** | `/root/autodl-tmp/runs/...--100_chkpt/` | **15G** |
| **Conda 环境 (occsafe)** | `/root/miniconda3/envs/occsafe` | **11G** |
| **Conda base lib** | `/root/miniconda3/lib` | **7.4G** |
| **数据集 (libero_spatial)** | `/root/autodl-tmp/libero_datasets/` | **6.0G** |
| **pip 缓存** | `/root/.cache/pip` | **5.6G** |
| **数据集 (modified_libero_rlds)** | `/root/autodl-tmp/data/` | **2.0G** |
| **/tmp（flash-attn 编译中间文件等）** | `/tmp/` | **1.8G** |
| **Conda pkgs 缓存** | `/root/miniconda3/pkgs` | **626M** |
| **项目代码** | `/root/occsafe_vla/` | **111M** |
| **训练中 checkpoint（尚无权重）** | `/root/autodl-tmp/checkpoints/vanilla_s0-s2` | **176K** |
| **用户层面合计** | | **~63G** |

数据盘显示 419G 已用，但用户目录仅 ~63G — 差额 ~356G 是系统/容器层占用。

### 3. 训练 checkpoint 空间预估

当前训练参数：
- `save_freq = 10000`，总步数 50005 → 每个 seed **5 个 checkpoint**（step 10K/20K/30K/40K/50K）
- `save_latest_checkpoint_only = False`（保留所有 checkpoint）
- 3 个 seed（vanilla_s0/s1/s2）正在训练，当前在 step ~844，尚未保存任何 checkpoint

**每个 checkpoint 大小估算：**

参考现有 `--100_chkpt`（15G），但该 checkpoint 包含了完整基座模型权重（14.25G safetensors）。根据 `save_training_checkpoint()` 代码，自动保存实际只写入：

| 组件 | 大小 |
|------|------|
| LoRA adapter | ~463M |
| action_head | ~289M |
| proprio_projector | ~65M |
| processor configs + tokenizer | ~3M |
| **每个 checkpoint 合计** | **~820M** |

注：`--100_chkpt` 中的 14.25G 完整模型权重更可能来自后续的合并/导出操作，而非自动保存。

**vanilla 训练总空间需求：**
- 5 checkpoint × 820M × 3 seeds = **~12G**
- 若含完整模型合并导出（5 × 15G × 3）= **225G**（但通常只在最终评估时合并最佳 checkpoint）

### 4. occ 实验额外空间

occ 实验额外保存 `occ_head` 权重。相比 vanilla，每个 checkpoint 增加 occ_head 大小（取决于具体架构，预计数十 MB 量级），整体差异不大。

### 5. 结论

**416GB 完全够用。** 即使按最坏情况（每次 checkpoint 都做全模型合并导出）225G 也在可控范围内。实际自动保存仅需 ~12G。

### 6. 可安全清理的空间

| 可清理项 | 大小 | 说明 |
|----------|------|------|
| pip 缓存 `~/.cache/pip` | 5.6G | `pip cache purge` |
| Conda pkgs 缓存 | 626M | `conda clean --all` |
| `/tmp/` flash-attn 编译中间文件 | ~1.8G | `rm -rf /tmp/tmpxft_*` |
| 旧 checkpoint `runs/--100_chkpt` | 15G | 若不再需要该旧实验结果 |
| **可回收合计** | **~23G** | |

---
