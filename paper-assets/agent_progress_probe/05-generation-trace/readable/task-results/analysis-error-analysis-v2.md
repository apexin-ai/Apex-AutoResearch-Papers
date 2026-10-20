# analysis error analysis v2

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_error_analysis_v2_20260514T095901_result.json`
- **Structured JSON:** [`74093c60e279bc55320d.json`](../../sessions/74/74093c60e279bc55320d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，所有文件已保存到 `artifacts/error_analysis/`。关键发现：

### 1. Outcome × Error Type

| Outcome | probe-001 ErrRate | probe-002 ErrRate | 说明 |
|---|---|---|---|
| `submitted` | 4.65% | 8.70% | 正常提交，错误率最低 |
| `submitted (exit_context)` | 10.39% | 12.52% | 超 context 后提交，两个 probe 都较难 |
| `exit_context` | 7.39% | **30.91%** | 未提交直接超 context，probe-002 错误率暴涨 |
| `early_exit` | 2.56% | 4.66% | 早退出，两者都低 |

**`exit_context` 是 probe-002 最大的错误来源**，187/605 错误，主要是 FP（159个）——probe 把实际在 stagnate 的窗口预测为 progress。

### 2. LF Voting × Error Rate

- **probe-001** 只有 conf≥2 样本。conf=2 错误率 7.08%，conf=3 仅 44 个样本但错误率 11.36%（样本太少）
- **probe-002**: conf=1 错误率 **13.38%**（5895 窗口中 789 错），conf=2 错误率 8.98%，conf=3 错误率 3.51%
- **LF 全不一致（conf=1）的 5895 个窗口贡献了 probe-002 新增错误的 80%**

最高错误率 LF pattern（probe-002）:
- `fdd=-1,cr=-1,ob=0`（两个 LF 都说 stagnation，ob abstain）: **62.39%** 错误率
- `fdd=1,cr=0,ob=0`（只有 fdd 说 progress，其他 abstain）: **51.82%** 错误率
- 这些模式中 LF 信号弱/矛盾，probe 也难以准确预测

### 3. Probe-001 vs Probe-002 对比

- 仅 269 个重叠测试窗口（不同 split），probe-001 在重叠上 acc=94.05%，probe-002=89.96%
- probe-002 额外的 7832 个测试窗口错误率 12.22%，其中 conf=1 贡献最多（5895 窗口）
- `exit_context` 类 trajectory 在 probe-002 额外窗口中错误率 30.15%，是最难的 outcome 类型

---
