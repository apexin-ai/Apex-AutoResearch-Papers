# research literature scan

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan_20260514T194806_result.json`
- **Structured JSON:** [`19d5f35b137f8969e501.json`](../../sessions/19/19d5f35b137f8969e501.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

literature_map.yaml 已更新（24 → 31 篇）。

## 扫描报告

新增 **7 篇**论文：

**Method-component（3 篇，高相关）：**
- **FANG** (2512.23014, Dec 2025) — function-aware neuron grouping，与我们的 CKA functional overlap 思路最接近，但用 activation-based grouping 且无 recovery 组件
- **FuncNet** (2508.05239, Aug 2025) — ICA 分解 LLM 功能网络再剪枝，类似 "digital brain" 动机，无 RLVR recovery
- **RestoreLCC** (2510.21834, NeurIPS 2025) — activation compensation 恢复剪枝损失，plug-and-play，可与我们 RLVR 组合做 staged recovery

**Background（4 篇）：**
- **HAP-E** (ICLR 2026 submitted) — Hessian-aware structured pruning + adaptive budget
- **SlimLLM** (2505.22689, ICML 2025) — PCA-based channel/head importance
- **SPAP** (2505.03373) — optimization-based MLP pruning
- **Wanda++** (2503.04992, ACL 2025) — regional gradient 增强的 unstructured pruning

**直接竞品：未发现。** 无论文同时组合 CKA + structured pruning + RLVR recovery。FANG/FuncNet 做了 function-aware pruning 但无 recovery；Self-Healing 做了 RLVR recovery 但无 CKA-guided selection。我们的 novelty（CKA overlap 指导剪枝 → 预测 RLVR recoverability）仍然独特。

---
