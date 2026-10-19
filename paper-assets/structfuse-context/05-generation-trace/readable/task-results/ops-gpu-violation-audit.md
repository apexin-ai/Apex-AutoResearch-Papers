# ops gpu violation audit

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-violation-audit_20260513T021132_result.json`
- **Structured JSON:** [`34bf18e088e8c38c4bc1.json`](../../sessions/34/34bf18e088e8c38c4bc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

```
=== PID 795791 状态 ===
存活，运行时间 16:25，状态 Sl
运行在 GPU 4，显存使用 9260 MiB

=== GPU 全局状态 ===
GPU 0: 0 MiB / 24564 MiB, 0% — 空闲 ✅
GPU 1: 0 MiB / 24564 MiB, 0% — 空闲
GPU 2: 22101 MiB, 100% — 其他项目
GPU 3: 22099 MiB, 100% — 其他项目
GPU 4: 9269 MiB, 99% — 我们的合法训练 ✅
GPU 5: 2609 MiB, 97% — 其他项目

=== GPU 越界原因分析 ===
根因：run_m2_early_pilot.sh 缺少 CUDA_VISIBLE_DEVICES 设置。
脚本内没有任何 GPU 绑定，如果 submit_training_job 注入的环境变量在 conda activate 后被重置，或脚本被手动运行，进程就会默认使用 cuda:0。

=== 脚本修复 ===
已在 shebang 后第一行插入 `export CUDA_VISIBLE_DEVICES=4`，位于 conda activate 和所有 python 命令之前。
train.py 中无 CUDA_VISIBLE_DEVICES 相关代码，无需修改。

=== tmux sessions ===
仅 hgate-dpo003-merged（其他项目），无残留 m2_early_pilot session。

=== 当前 GPU 4 训练状态 ===
正常运行，无需干预。
```

---
