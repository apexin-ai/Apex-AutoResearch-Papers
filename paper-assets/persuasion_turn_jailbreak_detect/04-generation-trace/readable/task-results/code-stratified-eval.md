# code stratified eval

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_stratified-eval_20260517T080331_result.json`
- **Structured JSON:** [`47a4629ca591f4cd2113.json`](../../sessions/47/47a4629ca591f4cd2113.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| Subset | N | F1 | Accuracy | Precision | Recall | FPR |
|--------|---|----|---------|-----------|---------|----|
| Full test | 76 | 0.9870 | 0.9868 | 1.0000 | 0.9744 | 0.0000 |
| Persuasion-based (jailbreak) | 21 | N/A (单类) | 1.0000 | N/A | **1.0000** | N/A |
| Cipher-based (jailbreak) | 18 | N/A (单类) | 0.9444 | N/A | **0.9444** | N/A |
| Benign only | 37 | N/A (单类) | 1.0000 | N/A | N/A | 0.0000 |
| Persuasion + Benign | 58 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 |

**关键发现**：结果与预期相反。

- Persuasion-based recall = **1.0000** (21/21 全部正确检测)
- Cipher-based recall = **0.9444** (17/18，漏检 1 个)
- Full test 唯一的 1 个 FN 来自 cipher-based 样本，不是 persuasion-based
- FPR = 0.0000（benign 全部正确分类）

Baseline GRU 在 persuasion-based attacks 上表现完美，反而是 cipher-based 有一个漏检。不过测试集较小（76 samples），这个差异不具有统计显著性。

---
