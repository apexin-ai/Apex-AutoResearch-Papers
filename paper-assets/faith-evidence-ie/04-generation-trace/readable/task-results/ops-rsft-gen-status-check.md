# ops rsft gen status check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rsft_gen_status_check_20260515T043509_result.json`
- **Structured JSON:** [`fc707f87e40ee048a549.json`](../../sessions/fc/fc707f87e40ee048a549.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 各 Shard 状态

| Shard | Lines | 进度 | 状态 | 备注 |
|-------|-------|------|------|------|
| **0** | 5,256 | 644/682 (94%) | 🔄 运行中 | PID 135867, 已运行 2h55m |
| **1** | 5,552 | 681/681 (100%) | ✅ 已完成 | 12:32 完成，5448 outputs + 104 行旧续传数据 |
| **2** | 5,568 | 681/681 (100%) | ✅ 已完成 | 12:34 完成，PID 136649 已退出 |
| **3** | 5,008 | 622/657 (95%) | 🔄 运行中 | PID 137985, 已运行 2h46m |

### Shard 1 SIGTERM 调查结论

**Shard 1 实际已正常完成。** 日志末尾明确记录：
```
Generation complete. 681 documents, 5448 total outputs
Format compliance: 5529/5552 (99.6%)
```

SIGTERM (EXIT_CODE=143) 是进程完成后收到的终止信号（可能是 nohup 父进程清理或监控脚本）。**不是 OOM，不是异常中断。**

- 数据完整：最后一行是完整的 JSON 对象（doc "A Free Soul"）
- 5552 行中有 104 行来自之前的 302-doc 续传，5448 行是本次新生成
- format_ok_rate: 99.6%, truncation_rate: 6.9%, diversity: 7.6/8

### Shard 2 也已完成

日志确认：681 docs, 5448 outputs, format compliance 100.0%。

### 剩余 Shard 预估

- **Shard 0**: 剩 38 docs, ~17s/doc → **约 11 分钟**
- **Shard 3**: 剩 35 docs, ~14s/doc → **约 8 分钟**

⚠️ Shard 0 有 truncation_rate 10.1% 警告（建议 max_new_tokens=3072），但不影响当前运行。

---
