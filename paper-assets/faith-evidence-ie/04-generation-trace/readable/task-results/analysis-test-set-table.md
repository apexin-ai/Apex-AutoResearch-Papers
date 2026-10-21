# analysis test set table

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_test-set-table_20260521T194533_result.json`
- **Structured JSON:** [`349747032de8cd9088f8.json`](../../sessions/34/349747032de8cd9088f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

memory.md 已更新。原 "🔴 Test Set Scaling Table Status" 段落替换为 "🔴 Test Set Results & Dev→Test Generalization"，包含：

**综合结果表**：5 个 scale × (SFT dev, RSFT dev, SFT test, RSFT test, 双向 gap, RSFT gain) 全列。SFT test 列待 4 个运行中实验完成后填充。

**核心发现**：
1. **Dev→Test gap = ~20.7pp constant offset**（range 仅 1.5pp），不随 scale 系统性缩小
2. **Scaling 排序完美保持**：test 上 1.7B < 8B < LLaMA < 14B，Spearman ρ=1.0
3. **跨架构优势保持**：LLaMA vs Qwen-8B 在 test 上 +2.46pp（dev 上 +2.21pp）
4. **Evidence quality 在 test 上降幅比 ign_f1 更大**（相对降幅 47% vs 37%）
5. **RSFT gain on test 待 SFT test 完成后验证**

**待补 6 个数据点**：4 个 SFT test evals 运行中，1.7B SFT test 未提交，4B RSFT test 需重训。

---
