# diagnose exp020 exit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp020_exit_20260516T144006_result.json`
- **Structured JSON:** [`862a0b13e7bb437db889.json`](../../sessions/86/862a0b13e7bb437db889.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**exp-020 全部 4 个 config 成功完成。** Registry 已更新为 DONE/success。

### 关键发现

1. **进程退出原因**: 日志末尾显示 `Terminated`（SIGTERM），但发生在所有数据生成和评估已完成之后。数据完整性验证通过（每个 config 6 depths × 5000 lines = 30000 条）。

2. **结果**:  所有 config **K\*=2**（threshold=0.6），与假设一致——decoding 策略不影响 contamination depth 上限：
   - greedy: 1v2 AUC 最高 (0.88)，因 repetition collapse
   - t12 (高温): 1v2 AUC 最低 (0.62)，刚过阈值
   - t07/nuc09 居中

3. **cuda:2 状态**: 已空闲，无残留进程。

4. **Registry**: status=DONE, conclusion=success, metrics 含全部 4 config 的 K* 和 per-pair AUC。

---
