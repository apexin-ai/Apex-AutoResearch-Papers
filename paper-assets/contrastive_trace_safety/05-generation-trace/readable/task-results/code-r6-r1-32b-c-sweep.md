# code r6 r1 32b c sweep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r6_r1_32b_c_sweep_20260518T030834_result.json`
- **Structured JSON:** [`47b5d7b1787833b95a25.json`](../../sessions/47/47b5d7b1787833b95a25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| C     | Precision | Bal_Acc |
|-------|-----------|---------|
| 0.01  | 0.5021    | 0.7669  |
| 0.1   | 0.4876    | 0.7566  |
| 1.0   | 0.4819    | 0.7585  |
| 10    | 0.4873    | 0.7499  |
| 100   | 0.5067    | 0.7552  |

数据概况：Train 2197 samples (34.5% positive), Val 765 samples (21.4% positive)。

**最优 C = 0.01**，bal_acc=0.7669, precision=0.5021。但各 C 值差异很小（bal_acc 范围 0.7499–0.7669, precision 0.4819–0.5067），说明 Layer 63 上 LR 对正则化强度不敏感。

建议：如果要从中选一个，C=0.01 略优。但更值得注意的是 Layer 63 的整体 precision 偏低（~50%），这是最后一层，信号可能不如中间层。结果已保存到 `artifacts/exp_r6_c_sweep/results.json`。

---
