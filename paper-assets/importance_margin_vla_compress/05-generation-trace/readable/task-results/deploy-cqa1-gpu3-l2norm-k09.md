# deploy cqa1 gpu3 l2norm k09

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_gpu3_l2norm_k09_20260527T102109_result.json`
- **Structured JSON:** [`aaa848881081d21ede5a.json`](../../sessions/aa/aaa848881081d21ede5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型正在加载中（π0.5 加载需要几分钟）。部署完成，汇总：

**部署结果**：
- **实验**: `eval_pi05_l2norm_k09_long_seed42_strict_cqa1`
- **服务器**: cqa1-33015 GPU3
- **Registry**: RUNNING
- **tmux session**: `pi05_l2n_k09`
- **脚本版本**: 464 行 ✓
- **日志**: 正常启动，模型加载中（suite=libero_10, prune=l2norm, keep=0.9, eps=50）
- **修复**: tmux 内需先 `source conda.sh && conda activate base`，否则 `python` 不在 PATH

---
