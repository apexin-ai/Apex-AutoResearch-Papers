# analysis silent error analysis n3

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_silent_error_analysis_n3_20260519T053932_result.json`
- **Structured JSON:** [`92a9ce02d8e7a9b2c6c2.json`](../../sessions/92/92a9ce02d8e7a9b2c6c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**数据集中 55.5% (188/339) 的 fail 是 silent logic error**（代码无异常，输出错误，测试 assert 失败）。

各 condition 在 silent error 上的 fail recall：

| Condition | Silent (n=188) | Crash (n=81) | Gap |
|-----------|---------------|-------------|-----|
| no_trace | 62.8% | 98.8% | +36pp |
| exception_only | 100% | 100% | 0pp |
| loop_only | 67.6% | 100% | +32pp |
| full_trace | **50.0%** | 88.9% | +39pp |
| vota | 100% | 100% | 0pp |

关键发现：
- **full_trace 在 silent error 上最弱 (50%)**，仅提供变量快照无 error 标记时模型难以判断
- exception_only 对 silent error 也 100% 有效，因为 trace 系统捕获了测试框架的 AssertionError
- 无 trace 信息的 condition 对 crash 类错误 recall ~99%，但对 silent error 仅 ~63%，差距 32-39pp

报告已注册到 `artifacts/silent_error_analysis.md`。

---
