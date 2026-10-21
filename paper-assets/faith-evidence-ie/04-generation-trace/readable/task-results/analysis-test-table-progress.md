# analysis test table progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_test-table-progress_20260521T225644_result.json`
- **Structured JSON:** [`72f60fb18306f22cbe02.json`](../../sessions/72/72f60fb18306f22cbe02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已注册为 artifact `test_table_compilation_d147`。核心发现：

**完成度**: 5/10 test eval 已完成（全部 RSFT），4 个 SFT 正在跑，4B RSFT 永久缺失。

**Dev→Test gap**: RSFT 一致 20.4–21.9pp（spread 仅 1.5pp），排名完全保持（ρ=1.0）。Gap 来自 test 标注密度 2.82× dev。

**缺口清单（按优先级）**:
1. 等 4 个 running SFT test eval 完成（无需操作）
2. 14B no-evidence test — D147 spot-check，最高价值
3. 1.7B no-evidence test — 验证 "evidence beneficial at small scale" 是否 test 上成立
4. 4B RSFT — 永久不可恢复，论文用 footnote + dev 数据处理

**4B 处理建议**: 保留在 test table 中（带 Trunc.% 列），RSFT 缺失用 footnote 指向 dev table（4-seed mean 0.4466±0.53pp）。不排除比隐瞒好。

---
