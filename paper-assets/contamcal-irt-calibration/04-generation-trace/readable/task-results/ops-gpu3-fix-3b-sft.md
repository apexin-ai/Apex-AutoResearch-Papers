# ops gpu3 fix 3b sft

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu3-fix-3b-sft_20260514T065129_result.json`
- **Structured JSON:** [`956169974ba5714e9cbe.json`](../../sessions/95/956169974ba5714e9cbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 319555 在 **GPU-c30258a6（GPU 3）** 上，13316 MiB。GPU 0 只剩 1.5B 的 251924（10046 MiB）。

迁移成功。

**汇报：**
- 旧进程 291380（GPU 0）→ 已终止
- 根因：train_sft.py:114 `os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu` 将 submit_training_job 设置的 `CUDA_VISIBLE_DEVICES=3` 覆盖为 `"0"`
- 修复：去掉 `--gpu` 参数，由 submit_training_job 的 CUDA_VISIBLE_DEVICES=3 直接控制
- 新进程 319555 已在 GPU 3 上运行，step 5/4159，13316 MiB
- GPU 0 显存从 95.2% 降至仅 1.5B SFT 的 10046 MiB

---
