# analysis qwen truncation audit

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen-truncation-audit_20260521T033603_result.json`
- **Structured JSON:** [`e596d21641fd8c2ca1e7.json`](../../sessions/e5/e596d21641fd8c2ca1e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是 Qwen 全尺度截断审计结果。

---

## Qwen 截断审计汇总（全部 @1024 max_new_tokens，985 docs）

### 1.7B — Qwen3-1.7B

| Model | Condition | truncated | total | trunc_rate | ign_f1 | n_preds |
|-------|-----------|-----------|-------|------------|--------|---------|
| SFT s42 | with-evi | 314 | 985 | **31.9%** | 0.4786 | 17184 |
| SFT s42 v3 | no-evi | 501 | 985 | **50.9%** | 0.3982 | 26157 |
| RSFT s42 r2 | with-evi | 258 | 985 | 26.2% | 0.5050 | 16420 |
| RSFT s43 | with-evi | 262 | 985 | 26.6% | 0.5024 | 16455 |
| RSFT | no-evi | — | — | — | — | 数据缺失 |

**SFT 不对称: +19.0pp** → **CRITICAL**
- no-evi 生成了 52% 更多预测 (26157 vs 17184)，半数文档被截断
- 1.7B 模型 length calibration 差，no-evi 没有 evidence 前缀后疯狂输出更多 relation

### 4B — Qwen3-4B

| Model | Condition | truncated | total | trunc_rate | ign_f1 | n_preds |
|-------|-----------|-----------|-------|------------|--------|---------|
| SFT s42 | with-evi | 288 | 985 | **29.2%** | 0.3974 | 16880 |
| SFT s43 | with-evi | 318 | 985 | 32.3% | 0.4365 | 17055 |
| SFT s44 | with-evi | 249 | 985 | 25.3% | 0.4734 | 16143 |
| SFT s42 noquant | no-evi | 307 | 985 | **31.2%** | 0.4721 | 21181 |
| RSFT s42 | with-evi | 214 | 985 | 21.7% | 0.4423 | 15436 |
| RSFT | no-evi | — | — | — | — | 数据缺失 |

**SFT 不对称 (s42): +2.0pp** → **OK**（对称截断，evidence tax 对比可信）

### 8B — Qwen3-8B

| Model | Condition | truncated | total | trunc_rate | ign_f1 | n_preds |
|-------|-----------|-----------|-------|------------|--------|---------|
| SFT s42 | with-evi | 313 | 985 | **31.8%** | 0.5051 | 17401 |
| SFT s42 v2 | no-evi | 225 | 985 | **22.8%** | 0.5079 | 19948 |
| RSFT s42 | with-evi | 267 | 985 | 27.1% | 0.5433 | 16831 |
| RSFT | no-evi | — | — | — | — | 数据缺失 |

**SFT 不对称: -9.0pp（反转！with-evi 截断更多）** → **REVERSED**
- 8B 模型够强，evidence 字段的 token 开销反而让 with-evi 截断更多
- no-evi 虽然多出了 15% 预测 (19948 vs 17401)，但每条预测更短，总体更紧凑

---

## 结论

| Scale | 不对称性 | 方向 | evidence tax @1024 可信？ | 需要 @2048？ |
|-------|---------|------|------------------------|------------|
| **1.7B** | **+19.0pp** | no-evi 截断严重 | **不可信** — no-evi 性能被人为压低 | **必须重跑** |
| **4B** | +2.0pp | 近对称 | **可信** | 不需要 |
| **8B** | -9.0pp | 反转（with-evi 截断更多） | **可信但保守** — 如果有 bias，是 with-evi 被压低 | 可选（重跑只会让 evidence tax 更小/负） |

**根因**：模型越小 → length calibration 越差 → no-evi 模式下没有 evidence 字段约束，小模型倾向于无限制输出 relation → 1.7B 的 no-evi 平均每文档 26.6 条预测 vs with-evi 17.4 条，超量 52%。

**优先级**：
1. Qwen 1.7B SFT no-evi @2048 — **必须**
2. Qwen 1.7B RSFT no-evi — **完全缺失**，需要先训练 no-evi 版 RSFT 再 eval
3. Qwen 4B/8B RSFT no-evi — **缺失**，无法做 RSFT 层面的 evidence tax 对比

---
