# infra p2b disk cleanup and train fix

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_p2b_disk_cleanup_and_train_fix_20260512T162558_result.json`
- **Structured JSON:** [`0e3788a81f55a02597fb.json`](../../sessions/0e/0e3788a81f55a02597fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### Step 1 清磁盘
- 5 个失败 run 目录已不存在（之前已清理）
- 4 个成功 run 各只有 `final/`，无中间 checkpoint 需清
- 无 smoke/dryrun 残留
- autodl-tmp **76GB 可用**（≥60GB ✓），根分区 19GB 可用

### Step 2 修改 checkpoint 策略（4 处变更）
1. **L19** — 添加 `import shutil`
2. **L343** — 初始化 `best_val_loss = float("inf")`
3. **L390-402** — 每次 eval 后比较 val_loss，新 best 时 rolling 覆盖 `best/` 目录（先 rmtree 旧 best）；删除了原来的 `checkpoint-{step}` 中间保存
4. **L410-416** — final save 前检查磁盘空间 <15GB 则跳过

每个 run 最多 2 个 checkpoint（best + final）。`--save-steps` CLI 参数保留但不再生效，避免破坏已有启动脚本。

---
