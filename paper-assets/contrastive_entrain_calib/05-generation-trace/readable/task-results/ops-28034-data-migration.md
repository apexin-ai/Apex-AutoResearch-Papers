# ops 28034 data migration

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_28034-data-migration_20260523T095506_result.json`
- **Structured JSON:** [`9dcd4248b26639a52bb8.json`](../../sessions/9d/9dcd4248b26639a52bb8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

迁移完成，验证通过。汇报如下：

---

## 已迁移到 29046 (`/root/contrastive_entrain_calib/backups/`)

### 1. Reduced-lora checkpoints（共 750MB）
| Checkpoint | 大小 |
|---|---|
| checkpoint-7000（peak） | 250M |
| checkpoint-7500 | 250M |
| checkpoint-8000 | 250M |

### 2. Eval results（共 8.1MB）
全部 20 个 eval 目录 + 散落的 json/txt 文件已完整迁移，包括 exp-002v3、exp-003、exp-004 各系列及 heldout 评估结果。

---

## 28034 上尚存的潜在重要数据

### `/root/autodl-tmp/outputs/`
| 路径 | 大小 | 说明 |
|---|---|---|
| `exp-004-act-baseline/` | **12G** | ACT s1 全部 checkpoints |
| `exp-004-reduced-lora/` | 4.2G | 已迁移 best 3 个 ckpt，还有其他中间 ckpt |

### `/root/autodl-tmp/checkpoints/`
| 路径 | 大小 | 说明 |
|---|---|---|
| `exp003/` | **8.0G** | R3-only s1 checkpoints |
| `exp003_s2/` | 8.5G | R3-only s2 checkpoints |
| `exp002v3_dcgrpo_scaled_cosine/` | 4.7G | exp002v3 checkpoints |
| `exp004_s2/` | 3.8G | exp004 s2 checkpoints |
| `exp004s2_act_baseline_s2/` | 1.4G | ACT s2 checkpoints |
| `exp004s2_act_seed2/` | 1.4G | ACT seed2 checkpoints |
| `exp003s2_r3only_seed2/` | 719M | R3-only seed2 |
| `exp009_continuous_probe_grpo/` | 2.8G | exp009 probe GRPO |

### `/root/contrastive_entrain_calib/outputs/`
包含 `exp-004-act-baseline`、`exp-004-act-baseline-s2`、`exp-004-heldout-ckpt500`、`exp003_gs8_r3only`、`exp004_heldout` 等子目录（未检查大小）。

### `/root/autodl-tmp/models/` 和 `modelscope_cache/`
各 16G，是基础模型缓存，可重新下载，不需要迁移。

---

**总结**：28034 上 checkpoints 目录合计约 **31G**，outputs 约 **16G**（去掉 models cache）。29046 根分区仅剩 ~11G 可用空间，**无法全部迁移**。请 Director 决定哪些需要额外迁移——特别是 ACT s1（12G）和 R3-only s1（8G）是否值得保留。

---
