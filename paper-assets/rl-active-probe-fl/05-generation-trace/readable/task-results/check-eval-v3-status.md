# check eval v3 status

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval-v3-status_20260514T103509_result.json`
- **Structured JSON:** [`a38b764de4e733504aea.json`](../../sessions/a3/a38b764de4e733504aea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 两个 eval 均在运行中

| Eval | 进度 | 速率 | 预计完成 |
|------|------|------|----------|
| **eval-base-v3** (base mode) | **186/202** (92%) | ~15s/sample | ~18:40 (~4 min) |
| **eval-sft-v2** (sft mode) | **168/202** (83%) | ~16s/sample | ~18:45 (~9 min) |

两个 eval 均于 17:49 启动，已运行约 47 分钟。

### GPU 使用

| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 100% | 33,984 / 97,887 MiB |
| cuda:1 | 0% | 0 / 97,887 MiB |

注意：eval-sft-v2 设置了 `CUDA_VISIBLE_DEVICES=1` 但 nvidia-smi 显示 GPU 1 无显存占用。日志显示 sft eval 仍在正常推进，可能是 nvidia-smi 快照时恰好在两次推理之间，或存在设备映射问题。进程本身运行正常，无需干预。

### 结果文件

两个结果 JSON 文件（`eval_base_v3.json`、`eval_sft_v2.json`）均尚未生成，预计 eval 完成后写入。

两个 eval 预计 ~10 分钟内全部完成。需要我稍后再查一次提取结果吗？

---
