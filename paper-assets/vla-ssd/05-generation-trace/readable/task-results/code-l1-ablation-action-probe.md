# code l1 ablation action probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_l1_ablation_action_probe_20260517T144437_result.json`
- **Structured JSON:** [`40cd9bff2761cde11573.json`](../../sessions/40/40cd9bff2761cde11573.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交。

- **Job**: `l1_head_ablation` on `westd-19183` cuda:0
- **脚本**: `/root/vla-ssd/scripts/l1_ablation_action_probe.py`
- **配置**: 3 conditions (baseline, ablate_all24, ablate_all32) × 3 layers (L1, L8, L13) × 10 tasks × 5 demos
- **预计时间**: ~50-60 分钟（~6900 forward passes/condition，每帧 ~0.15s）
- **输出**: `/root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_results.json`
- **日志**: `~/runs/vla-ssd/l1_head_ablation.log`

---
