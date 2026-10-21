# fix eval unified gpu arg and sync

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval-unified-gpu-arg-and-sync_20260519T101030_result.json`
- **Structured JSON:** [`08ce5c4602da37f0b5b4.json`](../../sessions/08/08ce5c4602da37f0b5b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**修复 1（westd-28034）**：
- 删除了 `--gpu` argparse 参数定义
- 删除了 `os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)`
- 删除了 `logger.info("gpu: %d", args.gpu)`
- docstring 添加了 `GPU selection: use CUDA_VISIBLE_DEVICES=X environment variable prefix.`

**修复 2（westd-29046）**：
- 文件通过 base64 传输同步，md5sum 一致（`c90ec862`）
- `nli_utils.py` 两边已一致（64行），无需同步
- `--help` 验证通过，`--gpu` 参数已不存在

---
