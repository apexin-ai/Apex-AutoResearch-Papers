# fix random init label critical

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_random_init_label_critical_20260523T201244_result.json`
- **Structured JSON:** [`e7a0e21c41531fd7803e.json`](../../sessions/e7/e7a0e21c41531fd7803e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。两张图验证通过：

- **fig_multi_layer_attn.pdf**: legend 显示 "Trained VLA"、"Llama-2 Base"、"Random Init"（红色虚线，0/32 heads，底部平线）
- **fig_32layer_attention.pdf**: legend 显示 "VLA Trained"、"Llama-2 Base"、"Random Init"（红色虚线，全层 0 heads，底部平线）

随机初始化条件的标签已从 "Reference VLA" 正确改为 "Random Init"，其他条件标签未受影响。

---
