# check mvp 003 progress

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_mvp_003_progress_20260514T103512_result.json`
- **Structured JSON:** [`c6abda9f6b9d9fe38e50.json`](../../sessions/c6/c6abda9f6b9d9fe38e50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## mvp_003 实验进度报告

### PID 状态
- **PID 37622**：运行中
- **已运行时间**：44 分 15 秒
- **CPU**：1.0%，**内存**：0.0%

### 进度
- **已完成**：8 / 50 题（16%），当前正在处理 Problem 9 (pw_24132)
- **配置**：50 problems × 8 chains = 400 total chains
- **平均耗时**：~5.4 分钟/题
- **预估剩余**：42 题 × 5.4 min ≈ **3.8 小时**

### 当前准确率（前 8 题）

| 方法 | 正确数 | 准确率 |
|------|--------|--------|
| SVS | 4/8 | 50% |
| SC (baseline) | 4/8 | 50% |

逐题结果：

| # | Problem | SVS | SC |
|---|---------|-----|-----|
| 1 | pw_20952 | True ✓ | True ✓ |
| 2 | pw_3648 | Unknown ✓ | True ✗ |
| 3 | pw_819 | Unknown ✓ | True ✗ |
| 4 | pw_24299 | True ✗ | False ✓ |
| 5 | pw_9012 | False ✗ | True ✗ |
| 6 | pw_8024 | True ✗ | True ✗ |
| 7 | pw_7314 | Unknown ✓ | Unknown ✓ |
| 8 | pw_4572 | Unknown ✗ | True ✓ |

### 异常/报错
- **Z3 sandbox SyntaxError**：大量出现（数百次），autoformalize 生成的 Z3 代码语法无效，会自动重试最多 3 次。非致命，但说明 formalization 质量不高。
- **502 Bad Gateway**：偶发，外部 API（47.94.22.126）返回 502，有自动重试机制。
- **Traceback**：10 次，均与上述错误相关，未导致进程崩溃。

### 日志尾部摘要
进程正在为 Problem 9 (pw_24132) 执行 chain sampling，通过本地 vLLM (DeepSeek-R1-Distill-Qwen-14B) 生成推理链，同时用外部 API (deepseek-v3.2) 做 claim decomposition。运行正常。

---
