# code data preparation

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_data-preparation_20260513T215917_result.json`
- **Structured JSON:** [`0b9681f18bb57af9b0c7.json`](../../sessions/0b/0b9681f18bb57af9b0c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出汇总：

**数据文件** (6个)：
- `data/phase0_100.jsonl` — 100 条 Phase 0 baseline
- `data/train_500.jsonl` — 500 条训练集 (与 phase0 不重叠)
- `data/test_100.jsonl` — 100 条 held-out 测试集 (与 phase0、train 均不重叠)
- `data/train_500_seed{42,123,456}.jsonl` — 3 种 shuffle

**脚本** (2个)：
- `scripts/prepare_data.py` — 数据拆分 + shuffle 生成
- `scripts/verify_xor.py` — XOR 展开验证 + 重叠检查

**验证结果**：
- 3 集完全不重叠 ✓
- XOR 展开无错误、无残留 ✓
- 126 个括号不匹配来自 FOLIO 上游标注缺陷，非本项目引入

---
