# analysis error overlap visualization

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_error-overlap-visualization_20260517T003842_result.json`
- **Structured JSON:** [`5f909d76b5a16a362842.json`](../../sessions/5f/5f909d76b5a16a362842.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。输出文件：

- `/root/trace-verdict-study/docs/paper/figures/error_overlap.pdf` — 主图（error count bar + Jaccard heatmap）
- `/root/trace-verdict-study/docs/paper/figures/error_overlap.png`
- `/root/trace-verdict-study/docs/paper/figures/error_containment.pdf` — 与 no_trace 的包含关系图
- `/root/trace-verdict-study/docs/paper/figures/error_overlap_data.md` — 数据表

**关键发现：**

| Condition | Errors | Rate |
|-----------|--------|------|
| ae_only | 1 | 0.1% |
| exception_only | 2 | 0.2% |
| vota | 7 | 0.6% |
| loop_only | 171 | 14.4% |
| full_trace | 217 | 18.2% |
| no_trace | 296 | 24.9% |

层级包含关系**不成立**。实际模式：
1. exception_only 和 ae_only 的错误与其他条件**几乎无交集**（Jaccard ≈ 0）
2. full_trace 和 no_trace 有最高重叠（J=0.437, 156 shared errors）
3. full_trace 和 loop_only 重叠次高（J=0.416, 114 shared）
4. vota 的错误完全包含于 no_trace（7/7 = 100% coverage）

这暗示不同 trace 类型解决的是不同的失败模式，而非简单的信息量层级关系。exception_only/ae_only 虽然信息少，但可能更精准地定位了 bug 类型。

---
