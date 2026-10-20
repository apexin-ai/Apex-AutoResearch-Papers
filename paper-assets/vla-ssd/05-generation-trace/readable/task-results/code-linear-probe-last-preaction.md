# code linear probe last preaction

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_linear_probe_last_preaction_20260518T064617_result.json`
- **Structured JSON:** [`aaa4f0646dcde5d94ab5.json`](../../sessions/aa/aaa4f0646dcde5d94ab5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已在运行，输出正常。trained/L0 R²=-0.32, L1 R²=0.19，符合预期的先升后降趋势。

实验预计 ~28 分钟完成。已提交：
- **脚本**: `/root/vla-ssd/scripts/linear_probe_last_preaction.py`
- **exp_id**: `linear_probe_last_preaction`
- **GPU**: cuda:1 on westd-19183
- **日志**: `/root/autodl-tmp/vla-ssd/logs/linear_probe_last_preaction.log`
- **输出 JSON**: `/root/autodl-tmp/vla-ssd/results/linear_probe_last_preaction.json`

脚本变更要点：
1. readout = `last_preaction`（非 image_mean）
2. probe = `Linear(4096, 7)`（无 hidden layer）
3. 顺序跑 trained → untrained 各 33 层（单 GPU）
4. 自动加载 MLP probe 的 last_preaction 结果做对比
5. 输出包含 inverted-U 检测、bootstrap 对比、以及 MLP vs Linear 比较

---
