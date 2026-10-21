# code gradient flow v3 enhance

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gradient_flow_v3_enhance_20260519T150036_result.json`
- **Structured JSON:** [`b326d83c68603e98929b.json`](../../sessions/b3/b326d83c68603e98929b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**gradient_flow_v3 完成。**

结果摘要：
- **3 模型 × 200 样本**，所有随机种子固定 (seed=42)
- **CKA-only 梯度幅度显著高于 Standard (~2.9x) 和 RASP (~2.0-2.3x)**
- Wilcoxon paired test：CKA-only vs Standard **55/56 层显著** (p<0.05)，CKA-only vs RASP **56/56 层显著**
- Bootstrap 95% CI 全部远离 1.0，唯一例外 layer_26_mlp (CKA-only vs Standard, p=0.186)
- 输出目录：`/root/autodl-tmp/recovery_aware_struct_prune/results/gradient_flow_v3/`（含 3 组图表 + 2 个 JSON）
- Registry: `gradient_flow_v3` → DONE (success)

---
