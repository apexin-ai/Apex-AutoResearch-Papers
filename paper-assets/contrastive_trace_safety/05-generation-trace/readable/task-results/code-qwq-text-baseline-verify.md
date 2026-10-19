# code qwq text baseline verify

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwq_text_baseline_verify_20260516T231355_result.json`
- **Structured JSON:** [`b05c20505e54ac5177c4.json`](../../sessions/b0/b05c20505e54ac5177c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

## 结果

### Step A: 代码审计
**确认：原 exp_001b_bootstrap.py 的 text baseline 是 midpoint heuristic**（`predict 1 if step >= n//2`），不是 all-MiniLM-L6-v2 embedding probe。p=0.001 无效。

### Step B: 真正 text embedding 重跑

| | HS Probe (Layer 2) | Text Probe (MiniLM) |
|---|---|---|
| Pre-CP FPR | 0.2240 | 0.2144 |
| **Difference** | **+0.0096** | (HS 反而略差) |
| **p-value** | **0.904** | (完全不显著) |
| 95% CI | [-0.100, +0.120] | (跨零) |

### 结论
**Claim 1 在 QwQ-32B 上失效。** Hidden state probe 在 layer 2 上与 text embedding probe 表现无差异。跨模型泛化证据仅来自 r1-8b。

所有产出已保存至 `artifacts/qwq_text_verify/`。

---
