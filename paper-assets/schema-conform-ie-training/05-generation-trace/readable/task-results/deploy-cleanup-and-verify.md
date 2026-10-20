# deploy cleanup and verify

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cleanup-and-verify_20260512T105912_result.json`
- **Structured JSON:** [`7770c9777c122d1c1b07.json`](../../sessions/77/7770c9777c122d1c1b07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### 1. 残留进程清理 + GPU 状态
- PID 14819 已 kill，`/tmp/dryrun_conformance` 已删除
- **GPU 0**: 52390 MiB / 97887 MiB — 有两个进程在跑（PID 16149: 30036 MiB, PID 16571: 22340 MiB）
- **GPU 1**: 0 MiB — 完全空闲 ✓

### 2. dry_run_B 状态
- 输出目录存在，有 2 个 completions parquet 文件（`completions_00001.parquet`, `completions_00002.parquet`）
- 没有 `training.log` 或 checkpoint 文件 — 只有 completions，**看起来 dry_run_B 只完成了 generation 阶段（2 steps），没有完整训练**

### 3. 模型路径
- baseline 和 conformance 两个 config 都指向：`/root/autodl-tmp/models/Qwen/Qwen3___5-9B`
- 该路径实际存在（有 `config.json`）✓

### 4. 数据路径
- `/root/autodl-tmp/data/scierc/train.json` — **350 行** ✓

### 5. Ready for 正式训练？
- **GPU 1**: 空闲，可用 ✓
- **GPU 0**: 被占用（两个进程），需要确认这些进程是什么。如果是之前的 dry_run，需要先 kill 掉
- 模型和数据路径均确认有效 ✓
- dry_run_B 看起来未完整完成（仅有 completions，无 checkpoint）

**建议**: 确认 GPU 0 上 PID 16149/16571 是什么进程，决定是否需要清理后再启动正式训练。

---
