# research circuit api survey

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_circuit-api-survey_20260512T095923_result.json`
- **Structured JSON:** [`bf9e454a501f91308992.json`](../../sessions/bf/bf9e454a501f91308992.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研报告已写入 `artifacts/structfuse-mvp/API_SURVEY.md`。

关键发现：

- **EAP-IG**（`hannamw/eap-ig` v2.0）是最成熟的 edge-level attribution 库，依赖 `transformer-lens>=2.15.0`，4 步 API（Graph → attribute → topn → evaluate）
- **ACDC** 原始代码作者推荐用 **Auto-Circuit**（`pip install auto-circuit`）替代，同样基于 TransformerLens
- **Edge Pruning**（`princeton-nlp/edge-pruning`）用 L0 mask 优化，原版也依赖 TransformerLens 2.15.0（**不是 nnsight**），实验版已迁移到 HuggingFace transformers
- **AtP*** 官方未开源，社区实现（`koayon/atp_star`）不成熟且是 node-level，不推荐直接用
- **CIRCUS** 无开源代码，但 config-bagging 逻辑简单可自行实现（~50 行）
- **MIB Circuit Track** 基于 EAP-IG 构建，可直接作为标准化评估框架复用
- **兼容性**: Python 3.10 + torch 2.5.x + transformer-lens 2.15.0 是所有库的安全公共基线

---
