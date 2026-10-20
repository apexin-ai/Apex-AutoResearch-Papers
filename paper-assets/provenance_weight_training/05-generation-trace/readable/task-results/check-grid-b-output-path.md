# check grid b output path

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_grid-b-output-path_20260514T011449_result.json`
- **Structured JSON:** [`fac08617ac505cc436b6.json`](../../sessions/fa/fac08617ac505cc436b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认完毕，结论如下：

---

**`--output_dir` 路径**：`output/models/grid_b{B}_seed42`（相对路径，展开为 `/root/provenance_weight_training/output/models/grid_b0_5_seed42` 等）

**Symlink 状态**：`/root/provenance_weight_training/output` → `/root/autodl-tmp/provenance_weight_training/output`（symlink 已正确配置）

**checkpoint 物理位置验证**：
- `stat` 显示 Device: `900h`（即 `/dev/md0`，数据盘），确认 checkpoint 实际写在数据盘上
- `du -sh` = 2.3G（b=0.5 已完成的 checkpoint）

**磁盘使用情况**：

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| 根分区 `/` | 30G | 22G | 8.1G | 74% |
| 数据盘 `/root/autodl-tmp` | 250G | 25G | 226G | 10% |

**结论：无溢出风险。** Symlink 生效，checkpoint 全部写入数据盘。6 个 b 值每个约 2.3G，总计约 14G，数据盘剩余 226G 完全充足。根分区不会被 checkpoint 占用。

---
