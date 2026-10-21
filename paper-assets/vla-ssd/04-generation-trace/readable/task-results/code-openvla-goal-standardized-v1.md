# code openvla goal standardized v1

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_openvla_goal_standardized_v1_20260522T002914_result.json`
- **Structured JSON:** [`f0eae8a76f4a2b2e6043.json`](../../sessions/f0/f0eae8a76f4a2b2e6043.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动并正常运行。

**总结：**
- **exp_id**: `openvla_goal_standardized_v1`
- **PID**: 591230
- **GPU**: cuda:1（RTX PRO 6000 Blackwell, 98GB）
- **脚本**: `/root/autodl-tmp/vla-ssd/scripts/libero_goal_full_pipeline.py`（基于 Long pipeline 模板创建）
- **条件**: trained (`openvla-7b-finetuned-libero-goal`) + untrained (`openvla-7b`)
- **UNNORM keys**: trained=`libero_goal`, untrained=`bridge_orig`
- **5 phases**: R² probing → L1 attention → cross-instruction → RSA → counterfactual
- **预计耗时**: ~3-4 小时（参考 Long untrained 用了 ~1.8h，两个条件合计约 3.5h）
- **日志**: `~/runs/vla-ssd/openvla_goal_standardized_v1.log`

当前已进入 Phase 1 trained condition，正在提取表征（~5s/100 samples）。

---
