# code plan001 metric backport

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan001-metric-backport_20260520T104333_result.json`
- **Structured JSON:** [`2fd6775b9c488e6c2b88.json`](../../sessions/2f/2fd6775b9c488e6c2b88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

- Collider/M-bias 的 violation metrics 已与 mediation/frontdoor 统一：violation/sign_flip/amplification 基于全部 4 个 OLS 系数 vs C=I baseline 计算
- 所有 theory-MC 匹配通过，无回归
- IV 部分未改动（Wald/OLS 结构不同，按原计划排除）
- Registry `plan001_dag_taxonomy` metrics 已更新

---
