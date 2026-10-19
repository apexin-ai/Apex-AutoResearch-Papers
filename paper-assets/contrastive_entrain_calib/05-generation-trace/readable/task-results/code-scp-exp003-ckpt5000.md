# code scp exp003 ckpt5000

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scp-exp003-ckpt5000_20260520T100842_result.json`
- **Structured JSON:** [`f2f5bb9c88ddd363be0b.json`](../../sessions/f2/f2f5bb9c88ddd363be0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

scp 完成。总结：

- **ckpt-5000 已成功传输到 westd-28034**
- 实际存储路径：`/root/autodl-tmp/checkpoints/exp003/checkpoint-5000/`（数据盘，根分区已满无法存放）
- 软链接：`/root/contrastive_entrain_calib/checkpoints/exp003/checkpoint-5000` → 数据盘路径
- 大小：718M，16 个文件，与 29046 源完全一致
- 之前的 `tmp_scp_key` 仍然有效，无需重新生成

注意：28034 根分区已 100% 满，后续写文件需注意使用数据盘。ckpt-4000 占了根分区 1.1G，如果不再需要可以清理腾出空间。

---
