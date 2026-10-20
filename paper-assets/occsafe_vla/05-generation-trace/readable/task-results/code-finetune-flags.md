# code finetune flags

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_finetune_flags_20260529T092815_result.json`
- **Structured JSON:** [`c6781d716c99837fc988.json`](../../sessions/c6/c6781d716c99837fc988.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`--help` 验证通过。

### 汇报

**(a) 代码现状——两个 flag 均已实现，无需新增代码**

| Flag | Config 定义 | 使用位置 |
|------|------------|---------|
| `--occ_bn_eval` | line 101: `occ_bn_eval: bool = False` | line 1197-1199: forward 前对 `occ_head` 所有 `BatchNorm2d` 调 `.eval()` |
| `--occ_loss_weight` | line 92: `occ_loss_weight: float = 0.01` | line 1176, 1182: `cfg.occ_loss_weight * math.exp(...)` → 传入 `run_forward_pass` 的 `occ_weight_now` |

**(b) `--help` 验证**

修复前：`--help` 崩溃，因 line 116 注释 `(from 10% to 100%)` 中 `%` 被 argparse 当格式字符（`ValueError: unsupported format character 't'`）。已将 `%` 转义为 `%%`。修复后两个 flag 正常出现在 help 输出中。

**(c) 意外发现**

- `occ_loss_weight` 的 hardcoded `0.01` **无残留**：只出现在 config 默认值处（line 92 occ, line 106 depth），loss 计算全部通过 `cfg.occ_loss_weight` 引用
- `--help` 的 `%` 崩溃是预存 bug，与本次任务无关但顺手修了

---
