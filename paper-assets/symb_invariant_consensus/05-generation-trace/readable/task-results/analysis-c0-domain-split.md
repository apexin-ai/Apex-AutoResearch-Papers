# analysis c0 domain split

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c0-domain-split_20260517T172311_result.json`
- **Structured JSON:** [`84f5438bf7b9ffca0294.json`](../../sessions/84/84f5438bf7b9ffca0294.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已写入 `analysis/c0_domain_split.json`。

**域内 C0 拆分：**

| Domain | n | C0 | SC Acc | SICA Acc |
|--------|---:|-----:|-------:|---------:|
| FOLIO | 204 | 35.3% | 79.4% | 79.4% |
| ProofWriter | 600 | 39.2% | 75.2% | 75.5% |
| Combined | 804 | 38.2% | 76.2% | 76.5% |

Combined 数字与 registry 完全一致。ProofWriter 的 C0 (39.2%) 高于 FOLIO (35.3%)，说明 PW 的 D5 难度下模型回答分歧更大。FOLIO 上 SC 和 SICA 表现相同（79.4%），SICA 的增益主要来自 ProofWriter（75.2% → 75.5%）。

---
