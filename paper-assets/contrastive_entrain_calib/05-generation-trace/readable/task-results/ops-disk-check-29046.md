# ops disk check 29046

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-check-29046_20260523T161243_result.json`
- **Structured JSON:** [`272b6c56cbe106ba3454.json`](../../sessions/27/272b6c56cbe106ba3454.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 磁盘空间检查结果

### 1. 整体磁盘使用

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| `/`（根分区） | 30G | 25G | **5.5G** | 82% |
| `/dev/sda2`（数据盘，autodl-tmp） | 439G | 16G | **400G** | 4% |

### 2. 大目录 Top 10

| 目录 | 大小 | 位置 |
|------|------|------|
| `/root/autodl-tmp/checkpoints/` (exp003 seed1+seed2) | 23G | 数据盘 |
| `/root/autodl-tmp/contrastive_entrain_calib/outputs/` | 18G | 数据盘 |
| `/root/contrastive_entrain_calib/checkpoints/` | 7.5G | **根分区** |
| `/root/.cache/huggingface/` | 3.1G | **根分区** |
| `/root/contrastive_entrain_calib/output/` | 1.5G | **根分区** |
| `/root/contrastive_entrain_calib/backups/` | 1.5G | **根分区** |
| `/root/contrastive_entrain_calib/outputs/` | 682M | **根分区** |
| `/root/contrastive_entrain_calib/results/` | 415M | **根分区** |
| `/root/autodl-tmp/eval_checkpoints/` | 235M | 数据盘 |

### 3. 空间判断

- **数据盘（autodl-tmp）：400G 可用，远超 35GB 需求，完全充足。**
- **根分区：仅 5.5G 可用，已经很紧张。** 根分区上有 ~14GB 的项目数据（checkpoints/output/backups），如果后续实验误写根分区会立刻满。

### 4. 可安全清理的候选目录

**根分区上（释放空间优先级高）：**

| 目录 | 大小 | 说明 |
|------|------|------|
| `/root/contrastive_entrain_calib/checkpoints/exp002v2_dcgrpo_cosine` | 5.4G | 旧实验 exp002v2 的 checkpoints |
| `/root/contrastive_entrain_calib/checkpoints/exp002_dcgrpo_seed1` | 719M | 旧实验 exp002 |
| `/root/contrastive_entrain_calib/checkpoints/exp008_dryrun` | 682M | dryrun checkpoint |
| `/root/contrastive_entrain_calib/checkpoints/exp008_dryrun_v4` | 682M | dryrun v4 checkpoint |
| `/root/contrastive_entrain_calib/output/activations.pt` | 721M | 旧 activations 文件 |
| `/root/contrastive_entrain_calib/output/phase5/` | 721M | 旧 phase5 输出 |
| `/root/contrastive_entrain_calib/backups/act-s1` | 682M | 旧备份 |
| `/root/contrastive_entrain_calib/backups/reduced-lora` | 748M | 旧备份 |

清理以上可释放约 **10.3GB**，使根分区可用空间达到 ~15.8G。

**数据盘上（非紧急，但可释放空间）：**

| 目录 | 大小 | 说明 |
|------|------|------|
| `/root/autodl-tmp/checkpoints/exp003_r3only_seed1` | 12G | 如果 seed1 实验已完成且结果已记录 |
| `/root/autodl-tmp/checkpoints/exp003_r3only_seed2` | 12G | 同上 |
| `/root/autodl-tmp/contrastive_entrain_calib/outputs/exp-004-act-baseline-s2` | 9.4G | 如果 baseline s2 已完成 |

### 5. 结论

**数据盘空间充足（400G），后续实验只要确保 outputs 写到 `/root/autodl-tmp/` 下即可。根分区偏紧（5.5G），建议清理根分区上的旧 checkpoints 和 backups（可释放 ~10G）。未删除任何文件。**

---
