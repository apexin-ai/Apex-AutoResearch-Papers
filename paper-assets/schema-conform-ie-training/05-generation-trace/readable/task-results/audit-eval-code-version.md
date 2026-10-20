# audit eval code version

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_eval_code_version_20260514T014250_result.json`
- **Structured JSON:** [`f3769ee7bb2278e18a7f.json`](../../sessions/f3/f3769ee7bb2278e18a7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是审计报告。

---

## Eval 代码版本审计报告

### 1. 修复内容与部署时间

**修复 A — Thinking-mode fix (evaluate.py)**

分两阶段部署：
- **Phase 1** (UTC May 12 ~22:00–23:59): 在 `apply_chat_template` 中加 `enable_thinking=False` (line 71)
  - 触发原因：`base_zero_shot` (v1) 所有指标 ≈ 0，thinking tokens 破坏模型输出
  - 部署后 eval_A_v2 (UTC 00:06) 即恢复正常 entity_f1
- **Phase 2** (UTC May 13 09:52): 追加 chat_template 注入 `{%- set enable_thinking = false -%}` (lines 204-206)
  - 额外加固，实际对输出无影响（v2 与 v3 的 entity_f1 完全一致）

**修复 B — Relation type fix (data_utils.py + rewards.py)**

部署时间：**UTC May 13 04:54** (两文件同时 sync)
- `data_utils.py:79` — 新增 `DYGIEPP_TO_SCHEMA_REL_TYPE` 映射，gold relation 从 DyGIEPP 格式 (`PART-OF`) 转为 schema 格式 (`Part-of`)
- `rewards.py:106` — 新增 `_normalize_relation()` + `_arg_similarity()`，改进 relation matching
- 关联决策：D007 (UTC 04:48) "relation type 大小写不匹配，导致 relation F1 始终为 0"

### 2. 各 Eval 使用的代码版本

| eval_id | 启动 (UTC) | Thinking fix | Relation fix | scierc relation_f1 | 验证 |
|---------|-----------|:----------:|:----------:|:------------------:|------|
| base_zero_shot (v1) | May 12 ~21:00 | **NO** | **NO** | 0.0 (all metrics=0) | entity_f1=0 证实 thinking 未修复 |
| **eval_A_v2** | May 13 00:06 | Phase 1 | **NO** | **0.0** | entity_f1=0.4404 = v3, relation=0 |
| **eval_B_v2** | May 13 00:06 | Phase 1 | **NO** | **0.0** | entity_f1=0.4209 = v3, relation=0 |
| **eval_C_v2** | May 13 03:12 | Phase 1 | **NO** | **0.0** | entity_f1=0.3949 (正常), relation=0 |
| **eval_D1_v4** | May 13 10:50 | Phase 1+2 | **YES** | 0.2913 | 非零，修复后代码 |
| **eval_D2_ckpt400** | May 13 10:08 | Phase 1+2 | **YES** | 0.2379 | 非零，修复后代码 |
| **eval_D2_final** | May 13 10:08 | Phase 1+2 | **YES** | 0.2363 | 非零，修复后代码 |
| **eval_A_v3** | May 13 17:43 | Phase 1+2 | **YES** | 0.181 | 已知用修复后代码 |
| **eval_B_v3** | May 13 17:43 | Phase 1+2 | **YES** | 0.2348 | 已知用修复后代码 |
| **eval_A_cont_ckpt400** | May 13 20:57 | Phase 1+2 | **YES** | 0.2951 | 非零，修复后代码 |
| **eval_A_cont_final** | May 13 20:57 | Phase 1+2 | **YES** | 0.3004 | 非零，修复后代码 |

### 3. 交叉验证

**Thinking fix 验证（通过 entity_f1 一致性）：**
- eval_A_v2 entity_f1 = 0.4404 = eval_A_v3 entity_f1 → 同一模型、同样输出，thinking fix 已生效
- eval_B_v2 entity_f1 = 0.4209 = eval_B_v3 entity_f1 → 同上
- 结论：Phase 1 thinking fix 在 v2 evals 中已完全生效，Phase 2 是冗余加固

**Relation fix 验证（通过 relation_f1 分水岭）：**
- relation_f1 = 0.0：eval_A_v2, eval_B_v2, eval_C_v2 (全部在 UTC 04:54 关键 sync 之前启动)
- relation_f1 > 0：所有 UTC 10:08 之后启动的 eval（全部在关键 sync 之后）
- 分水岭完全吻合 rewards.py + data_utils.py 的 sync 时间

### 4. 结论：需要重跑的 Eval

**不需要重跑：**
- **eval_A_v2 / eval_B_v2**：已有 v3 重跑版本（eval_A_v3 / eval_B_v3），使用完全修复的代码。v2 的 entity_f1 和 conformance 指标与 v3 完全一致，唯一差异是 relation_f1 (0→non-zero) 和由此带来的 f1_correctness 差异。
- **eval_D1_v4, eval_D2_ckpt400, eval_D2_final, eval_A_cont_ckpt400, eval_A_cont_final**：均使用修复后代码，无需重跑。

**可能需要重跑：**
- **eval_C_v2** (base model zero-shot)：使用了旧的 rewards.py，relation_f1 = 0.0。如果需要 base model 的 relation_f1 基线数据，需用修复后代码重跑。但鉴于 D012/D013 已判定 MVP FAIL 且建议 kill+pivot，此项优先级低。

---
