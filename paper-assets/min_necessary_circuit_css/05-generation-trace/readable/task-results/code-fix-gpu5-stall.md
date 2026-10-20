# code fix gpu5 stall

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-gpu5-stall_20260513T015434_result.json`
- **Structured JSON:** [`23efa659d6896379a478.json`](../../sessions/23/23efa659d6896379a478.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 5 使用 3571 MiB，利用率 2%。Arithmetic 脚本正在跑 edge_pruning/ACDC 阶段（比较耗时的计算步骤）。

## 总结

| 项目 | 状态 |
|------|------|
| 模型下载 | 完成（548MB via ModelScope → `/root/autodl-tmp/gpt2-small/model.safetensors`） |
| PID 655404 (circus_fix) | 已 kill |
| PID 646875 (arithmetic) | 已不存在 |
| 补丁添加 | `run_circus_fix.py` 已加 `_patch_hf_from_pretrained()`；`run_arithmetic.py` 本身已有 |
| CIRCUS fix 重跑 | 已完成，结果保存到 `circus_fix_results.json`（FAIL: CPR=-0.0229 < 0.0337, recall=0/12） |
| Arithmetic 重跑 | PID 900199 运行中，GPU 5 占用 3571 MiB，正在执行 |

---
