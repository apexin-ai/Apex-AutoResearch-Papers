# code r6 r1 8b bootstrap fix

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r6_r1_8b_bootstrap_fix_20260518T033527_result.json`
- **Structured JSON:** [`d000c0c1653592dde45a.json`](../../sessions/d0/d000c0c1653592dde45a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

### 修复内容
`run_bootstrap_10k.py` 第 28 行 R1-8B `"window": 3` → `"window": 15`

### R1-8B (L14, W=15, 10k resamples) 结果

```
R1-8B (L14, W=15, 10000 resamples):
  HS precision:   0.7527
  Text precision: 0.4279
  Δ precision:    +32.5pp
  95% CI:         [+20.2, +45.2]pp
  p-value:        0.0000

  HS bal_acc:      0.8045
  Text bal_acc:    0.6946
  Δ bal_acc:       +11.0pp
  95% CI:          [+4.8, +17.2]pp
  p-value:         0.0011

  HS pre-cp FPR:   0.0898
  Text pre-cp FPR: 0.1815
  Δ FPR:           -9.2pp
  95% CI:          [-15.6, -2.6]pp
  p-value:         0.0049
```

### 关于 Δ 与 Table 2 不一致的说明

Δ precision = +32.5pp（非预期的 +22.4pp），原因是聚合方式不同：
- **Table 2 (+22.5pp)**：pooled precision（所有 test step 汇总计算）
- **Bootstrap (+32.5pp)**：per-trace precision（每条 trace 独立计算 precision 后取平均）

Per-trace 聚合是 bootstrap 统计检验的正确做法（trace 是独立采样单元）。修复前 W=3 的 bootstrap Δ 是 +27.9pp，修复后 W=15 变为 +32.5pp（HS probe 从更长窗口获益更多）。所有 p-value 仍然显著 (p < 0.005)。

---
