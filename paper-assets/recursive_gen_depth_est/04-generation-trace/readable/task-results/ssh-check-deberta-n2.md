# ssh check deberta n2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_deberta_n2_20260515T123057_result.json`
- **Structured JSON:** [`73fb7db86f174687971f.json`](../../sessions/73/73fb7db86f174687971f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/n2_deberta_check_result.md`。

**结论**：训练仍在运行，当前完成 Fold 1/5，预估还需 ~2.5 小时。

**核心问题**：Fold 1 val_acc 仅 55.0%（best epoch），远低于 RF baseline 78.2%。train_loss 持续下降而 val_acc 不升，过拟合严重。5-fold 跑完后若结果依然差，需排查输入格式和标签映射是否与 RF pipeline 一致。

---
