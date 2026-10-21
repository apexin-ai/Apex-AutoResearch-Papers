# code supplement sampling

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_supplement_sampling_20260521T142644_result.json`
- **Structured JSON:** [`fb442520096d4cd7a7ce.json`](../../sessions/fb/fb442520096d4cd7a7ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

本地和服务器数据一致（相同的 seed=43 产出相同结果）。

完成总结：

**补采样完成**
- 从 ConflictQA popQA-chatgpt 子集（7947 条，7208 unique questions）中排除已有 494 条，新采样 1500 条（seed=43）
- 分割：1200 train + 300 test
- 每条生成 conflict + no_conflict 两行

**文件清单**（本地 + 服务器均已就绪）：

| 文件 | 行数 |
|------|------|
| `en_conflict_train_supplement.jsonl` | 2400 |
| `en_conflict_test_supplement.jsonl` | 600 |
| `raw_sampled_train_supplement.jsonl` | 1200 |
| `raw_sampled_test_supplement.jsonl` | 300 |
| `en_conflict_train_full.jsonl` | 3200 (原800+新2400) |
| `en_conflict_test_full.jsonl` | 800 (原200+新600) |
| `raw_sampled_train_full.jsonl` | 1600 (原400+新1200) |
| `raw_sampled_test_full.jsonl` | 400 (原100+新300) |

原始数据文件未修改。`*_full.jsonl` 已就绪作为后续 verify 的输入。

---
