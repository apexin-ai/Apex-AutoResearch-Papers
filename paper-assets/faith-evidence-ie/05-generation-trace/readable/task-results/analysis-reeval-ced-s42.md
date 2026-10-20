# analysis reeval ced s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_reeval_ced_s42_20260516T072635_result.json`
- **Structured JSON:** [`bd6635be665a437aeb6a.json`](../../sessions/bd/bd6635be665a437aeb6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## reeval_ced_s42 结果

### 关键指标

| 指标 | 值 |
|------|-----|
| **F1** | **0.4517** |
| **Ign-F1** | **0.4423** |
| **Evi-F1** | **0.8174** |
| **EDCR** | **0.6569** |
| Evi-F1-Joint | 0.3518 |
| Format OK | 985/985 (100%) |
| Truncated | 214/985 (21.7%) |

### 与旧 eval (rsft_r2b_maxtok1536) 对比

旧 eval 用了不同 checkpoint (`rsft_output_r2b`) + batch_size=8 + max_new_tokens=1536。

| 指标 | 新 reeval | 旧 eval | 差异 |
|------|-----------|---------|------|
| F1 | 0.4517 | 0.4504 | +0.13pp |
| Evi-F1 | 0.8174 | 0.8102 | +0.72pp |
| EDCR | 0.6569 | 0.6740 | -1.71pp (更优) |
| Evi-F1-Joint | 0.3518 | 0.3488 | +0.30pp |

旧 eval 的 Ign-F1 = F1（0.4504），疑似 Ign 计算有 bug，不可比。Truncation 从 146→214 增加（因 max_new_tokens 从 1536 降到 1024），但 F1 和 Evi-F1 反而略好。

### CED 跨 seed 对比（统一协议）

| 指标 | s42 | s43 | s45 | Mean±Std |
|------|-----|-----|-----|----------|
| F1 | 0.4517 | 0.4601 | 0.4514 | 0.454±0.005 |
| Ign-F1 | 0.4423 | 0.4512 | 0.4416 | 0.445±0.005 |
| Evi-F1 | 0.8174 | 0.8063 | 0.8174 | 0.814±0.006 |
| EDCR | 0.6569 | 0.6542 | 0.6550 | 0.655±0.001 |

s42 与 s45 指标几乎一致，s43 的 F1 略高但 Evi-F1 略低。三个 seed 标准差很小，CED RSFT 训练稳定。

### 日志状态
无 error/traceback，EXIT_CODE=0，正常完成。

### 结论
**Success.** reeval_ced_s42 在统一协议下指标正常，与旧 eval 基本持平（略优），与其他 seed 一致性好。已注册 artifact `art_20260516_748dc4`。

---
