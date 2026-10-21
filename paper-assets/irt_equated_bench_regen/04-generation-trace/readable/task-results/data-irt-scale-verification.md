# data irt scale verification

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_irt_scale_verification_20260520T203626_result.json`
- **Structured JSON:** [`743908e6a0f9daf8b86f.json`](../../sessions/74/743908e6a0f9daf8b86f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已写入。核心发现：

**`mmlu-preproc.rds` 中的 `diff`/`disc` 是 CTT 统计量，不是 IRT 参数。**

- **`diff`** = 0.75 × 正确率（猜测校正），概率尺度 [0, 0.75]，不是 IRT 的 b 参数
- **`disc`** = 点双列相关系数（项目-总分相关），[-1, 1]，不是 IRT 的 a 参数
- 验证：`sd` 与 `sqrt(p*(1-p))` 相关系数 = 1.0，确认为二值响应统计量

**METABENCH 的实际 IRT 拟合**在 `crossvalidate.R` 中用 `mirt::mirt()` 完成，参数存在模型对象文件（如 `mmlu-2PL-1-cv-seed=1.rds`）中，使用 slope-intercept 参数化（a1, d），可转标准形式 `b = -d/a1`。

**CTT → IRT 不可直接转换**，必须从原始响应矩阵重新拟合。对 DIF 分析的影响：如需 IRT equating 必须从 response matrix 重做 IRT 拟合，但 CTT 的 diff 可作为 Mantel-Haenszel DIF 分析的 difficulty 分层变量。

---
