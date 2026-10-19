# code fix data root argparse

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_data_root_argparse_20260515T212741_result.json`
- **Structured JSON:** [`95417545ea30769d8f1e.json`](../../sessions/95/95417545ea30769d8f1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。

### 结果

**问题确认**：`train_acib.py` 的 argparse 确实没有定义 `--data_root`，而 `run_acib_v3_train.sh` 第30行传了 `--data_root=/root/autodl-tmp/libero_dataset`，启动会直接崩溃。

**修复内容**（两处改动）：

1. **第56-57行** — `parse_args()` 中新增参数定义：
   ```python
   parser.add_argument("--data_root", type=str, default=None,
                       help="Root directory for dataset cache/storage")
   ```

2. **第137行** — `build_dataloader()` 中将 `data_root` 传递给 `LeRobotDataset` 的 `root` 参数：
   ```python
   dataset = LeRobotDataset(args.dataset_id, root=args.data_root)
   ```

**`--help` 验证**：`--data_root DATA_ROOT` 正常出现，全部参数解析无错误。阻塞项已消除。

---
