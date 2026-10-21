# diagnose eval openvla l2norm k05 goal seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_openvla_l2norm_k05_goal_seed42_v2_20260523T190107_result.json`
- **Structured JSON:** [`6bd5a3195fd8c31699ff.json`](../../sessions/6b/6bd5a3195fd8c31699ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**根因**: `--mode l2norm` 不是合法选项。脚本的 argparse 只接受 `baseline`, `random_prune`, `l2norm_prune`, `attention_prune`。

日志明确显示:
```
error: argument --mode: invalid choice: 'l2norm' (choose from 'baseline', 'random_prune', 'l2norm_prune', 'attention_prune')
EXIT_CODE=2
```

**修复**: 将命令中的 `--mode l2norm` 改为 `--mode l2norm_prune`。

环境和文件都没问题——脚本存在、模型权重完整（4个 safetensors 分片）、conda 环境正常（v1 的 python not found 已解决）。纯粹是 CLI 参数名写错了。

---
