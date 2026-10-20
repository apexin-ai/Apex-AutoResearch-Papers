# diagnose ced s42 s44 eval protocol

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_ced_s42_s44_eval_protocol_20260516T023234_result.json`
- **Structured JSON:** [`34d6175e330690b635e6.json`](../../sessions/34/34d6175e330690b635e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收齐。以下是核实结果：

---

## CED s42 — 来源: `rsft_r2b_maxtok1536` (F1=0.4504)

| 参数 | 标准协议 | 实际值 | 一致？ |
|------|----------|--------|--------|
| batch_size | 4 | **8** | **✗** |
| max_new_tokens | 1024 | **1536** | **✗** |
| seed | 42 | 42 | ✓ |
| --no-quantize | true | true | ✓ |
| --sft_adapter | /root/autodl-tmp/sft_output | /root/autodl-tmp/sft_output | ✓ |
| --base_model | Qwen3-4B | Qwen3-4B | ✓ |

**备选**: `rsft_r2b` (F1=0.4493) 修正了 max_new_tokens=1024，但 batch_size 仍为 8，也不合标准。

---

## CED s44 — 来源: `rsft_s44` (F1=0.4655)

| 参数 | 标准协议 | 实际值 | 一致？ |
|------|----------|--------|--------|
| batch_size | 4 | config 记录 8，但 inference 仅 62 batches (985/62≈16)，**实际可能是 16** | **✗** |
| max_new_tokens | 1024 | 1024 | ✓ |
| seed | 44 | **42** | **✗** |
| --no-quantize | true | true | ✓ |
| --sft_adapter | /root/autodl-tmp/sft_output | /root/autodl-tmp/sft_output | ✓ |
| --base_model | Qwen3-4B | Qwen3-4B | ✓ |

日志 `mvp2_eval_rsft_s44.log` 仅 12 行，严重截断，无法从日志端确认完整参数。

---

## 验证依据

当前正在运行的 s43/s45 标准 eval 确认 batch_size=4：进度条均显示 `0/247` batches（985/4=246.25→247），与标准协议一致。

---

## 结论

**两个都需要用标准协议重跑：**

1. **CED s42**: batch_size=8→4, max_new_tokens=1536→1024，两项偏差。adapter 路径 `rsft_output_r2b`。
2. **CED s44**: batch_size≠4, seed=42→44，两项偏差。adapter 路径 `rsft_output_s44`。

---
