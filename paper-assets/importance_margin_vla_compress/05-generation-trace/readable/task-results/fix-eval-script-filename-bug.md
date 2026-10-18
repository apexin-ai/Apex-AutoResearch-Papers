# fix eval script filename bug

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval_script_filename_bug_20260525T143544_result.json`
- **Structured JSON:** [`4d88eea15a0a208e7429.json`](../../sessions/4d/4d88eea15a0a208e7429.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成，三台服务器输出逻辑一致。

**修复总结：**

| 服务器 | 状态 |
|--------|------|
| westd-38929 | ✓ 已修复 |
| westd-27271 | ✓ 已修复 |
| westd-41074 | ✓ 已修复 |
| cqa1-33015 | 无此脚本，跳过 |

**两处修改：**
1. **文件名**：`else` 分支从硬编码 `openvla_l2norm_prune_k...` 改为 `openvla_{args.mode}_k...`，同时包含 `_seed{args.seed}` 防止不同 seed 冲突
2. **k_ratio 字段**：从 `args.mode == "random_prune"` 改为 `args.mode != "baseline"`，所有 pruning 模式都正确记录 k_ratio

已运行的实验不受影响，新启动的实验将使用正确的文件名。

---
