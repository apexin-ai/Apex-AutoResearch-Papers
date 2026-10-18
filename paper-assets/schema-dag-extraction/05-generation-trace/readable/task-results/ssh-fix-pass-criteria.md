# ssh fix pass criteria

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-pass-criteria_20260514T233645_result.json`
- **Structured JSON:** [`8f0f66fb004cd7d50051.json`](../../sessions/8f/8f0f66fb004cd7d50051.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，`--help` 正常运行。改动汇总：

1. **新增 `pass_recall` 判据**（~行 210-212）：`|r(recall, BCS)| >= 0.3 且 p < 0.05`
2. **`recall_vs_bcs`** 加了 `pass_fail: pass_recall, role: "primary"`（行 228）
3. **`f1_vs_bcs`** 加了 `role: "supplementary"`（行 223）
4. **日志输出**：recall 标记为 `[PRIMARY]`，F1 标记为 `[supplementary]`

总计改动约 10 行，未触及其他逻辑。

---
