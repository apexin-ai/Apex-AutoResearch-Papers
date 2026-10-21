# ops 28034 disk cleanup phase2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_28034-disk-cleanup-phase2_20260520T103058_result.json`
- **Structured JSON:** [`0b4099e0f58a22bb6bb8.json`](../../sessions/0b/0b4099e0f58a22bb6bb8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

## 清理报告

| 指标 | 清理前 | 清理后 | 变化 |
|------|--------|--------|------|
| 根分区使用 | 29G/30G (97%) | **6.6G/30G (22%)** | **释放 22.4G** |
| 数据盘使用 | 69G/350G (20%) | 80G/350G (23%) | +11G (迁入 exp-004) |

### 执行明细
- **已删除**: `checkpoints/exp008v3_binary_probe_grpo/` (5.6G) + `checkpoints/exp014_probe_baseline/` (5.6G)
- **已迁移**: `outputs/exp-004-act-baseline/` (12G) → 数据盘，原路径已创建软链接
- **验证通过**: 文件数 172=172，大小 12G=12G，软链接指向正确，exp008v3/exp014 checkpoint 已不存在

---
