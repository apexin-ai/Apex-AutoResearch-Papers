# ops disk cleanup urgent

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-urgent_20260516T035043_result.json`
- **Structured JSON:** [`75193215b1153c7a0864.json`](../../sessions/75/75193215b1153c7a0864.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| 项目 | 状态 |
|------|------|
| **根分区** | 58%（18G used / 13G free），不是 94% |
| **pip cache** | 仅 20K，无需清理 |
| **三个旧实验目录** | 已迁移完毕（符号链接指向 `/root/autodl-tmp/acib_outputs/`） |
| **conda pkgs cache** | 清理释放 ~107MB |
| **HF cache** | 255M，在根分区，量不大暂不处理 |
| **数据盘** | 23%（57G/250G），充裕 |

**seed1 checkpoint 空间**：根分区 13G 可用，当前 `acib_v5_div_reg` 占 1.3G（含已有 checkpoints）。单个 checkpoint 通常几百 MB，空间完全够用。

如果需要进一步释放空间，可考虑迁移 `acib_s`（1.3G）和 `dryrun_norm_fix`（1.3G）这两个非活跃目录到数据盘，能再腾出约 2.6G。

---
