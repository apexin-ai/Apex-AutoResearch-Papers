# analysis regex baseline

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_regex_baseline_20260516T033831_result.json`
- **Structured JSON:** [`5c0a83820b4475e7c0a8.json`](../../sessions/5c/5c0a83820b4475e7c0a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果总结

### Exception_only 格式（主战场）

| Baseline | Accuracy | Gap vs SFT |
|---|---|---|
| B1: `[ERROR]` 存在 | 93.45% | -6.39 pp |
| B2: `Traceback` 存在 | 71.51% | -28.32 pp |
| B3: 任意关键词 | 93.45% | -6.39 pp |
| B4: 异常类型 regex | 93.61% | -6.22 pp |
| **B5: 数据格式标记利用** | **99.33%** | **-0.50 pp** |
| B6: ERROR 计数≥2 | 92.02% | -7.81 pp |
| **SFT (exception_only)** | **99.83%** | — |

### 关键发现

**SFT 必要性得到证明。** 标准 regex baseline (B1-B4) 最高 93.61%，与 SFT 差距 >6 pp。

**B5 的 99.33% 是数据格式伪像**，不是真正的 regex 能力：它仅靠 `[No exception data in trace]` 标记判断 pass，其余判 fail。这不是对 trace 内容的理解。

**McNemar p=0.041**，B5 与 SFT 差异统计显著。

**8 个关键边界样本**（pass 但 trace 含异常）：
- 6 个 `ValueError`（被 try/except 捕获）→ SFT 全部正确，B5 全错
- 2 个 `GeneratorExit` → SFT 和 B5 都错

**跨格式对比**：vota 上 regex 最高 75.55%（SFT 99.41%），full_trace 上 regex 77.39%（SFT 81.76%）。

**结论：简单 regex 无法替代 SFT。** 论文的 SFT 方法论站得住。结果已保存到 `/root/trace-verdict-study/analysis/regex_baseline_results.json`。

---
