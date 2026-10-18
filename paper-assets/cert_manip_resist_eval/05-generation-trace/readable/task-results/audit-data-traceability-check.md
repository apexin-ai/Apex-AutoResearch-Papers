# audit data traceability check

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_data-traceability-check_20260523T191548_result.json`
- **Structured JSON:** [`2fb68ac46fde407a439a.json`](../../sessions/2f/2fb68ac46fde407a439a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计报告已写入 `docs/paper/data/DATA_TRACEABILITY_AUDIT.md`。

核心发现：

**118 个数字被审计**，其中 52 个（44%）仍是 V1 旧值，需要 V2 更新。47 个（40%）已与 V2 一致。5 个存在论文内部自相矛盾。14 个缺少 V2 数据源无法验证。

最严重的 V1 残留问题：

1. **Table 1**：6 个 cell 用的 V1 sig/dominance（V2 应为 keff 12/12 全正，dominance Co:10/K:2/eta:0）
2. **Table 2**：4 行全部是 V1 值（Bayesian dir 应为 5+/1- 而非 1+/6-；Majority keff 应为 12/12 而非 8/12）
3. **GAM 6:6 split 声明**：在 6 个位置仍声称"shared-bias 负方向"，但 V2 数据显示 12/12 全部正方向
4. **Bayesian reversal 声明**：8 个位置仍声称"符号翻转"，但 V2 是 5+/1- 没有翻转
5. **Regime transition 计数**：所有 K 值的 sig count 都是 V1（如 K3 eta 5→3，keff 1→4；K5 keff 7→10）
6. **main.tex abstract 已更新为 V2**，但 abstract.tex 和正文 body 仍是 V1，造成论文内部自相矛盾

---
