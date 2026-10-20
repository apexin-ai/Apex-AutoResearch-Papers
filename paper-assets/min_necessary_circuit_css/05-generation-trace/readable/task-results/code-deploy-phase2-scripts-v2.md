# code deploy phase2 scripts v2

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deploy-phase2-scripts-v2_20260513T054518_result.json`
- **Structured JSON:** [`c074e7fdced7bcba50e7.json`](../../sessions/c0/c074e7fdced7bcba50e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

### 修改清单

**1. 新建 `run_circus.py`** — pipeline 编排模块
- `run_pipeline(config)` 函数：scoring → binarization → CSS cross-tabulation
- 支持 TransformerLens (EAP-IG, IFR) 和 auto_circuit (EP, ACDC) 两种 backend
- 自动加载缓存、缺失时计算并缓存
- HF local path redirect（避免网络依赖）

**2. 修改 `run_phase2_experiment.py`**
- IFR 默认二值化从 `unique_score_rank, n=50` 改为 `topn, n=200`（与 EAP-IG/EP 一致）
- 修复第 246 行损坏的字节 (`\x06a\x60\xcd...` → `aggregation`)

**3. 未改动（已就位）**
- `circuit_discovery.py` — IFR normalizer (`_normalize_ifr_edge`) 和 `run_ifr()`/`run_ifr_hf()` 已注册在 `_NORMALIZERS` 中
- `css.py` — 通用 `binarize_scores()` 支持 `topn`/`unique_score_rank` 等策略，无需方法特化

### 验证结果

Pipeline 端到端通过（14.4s）：
- **EAP-IG**: 32491 edges → top-200 binarized
- **Edge Pruning**: 32491 edges → top-200 binarized  
- **IFR**: 32334 edges → top-200 binarized（新计算 + 已缓存）
- **CSS 分布**: 1/3=393, 2/3=90, 3/3=9
- **CSS core**: 9 edges（三方法共识），off-diagonal 98.2%
- CSS core 全部是 `m0->` 开头的边（MLP 0 作为 source），IFR 的 proximity metric 对 MLP 路径敏感

---
