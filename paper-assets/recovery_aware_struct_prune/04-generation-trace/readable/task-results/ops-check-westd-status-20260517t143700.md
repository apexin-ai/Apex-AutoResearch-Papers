# ops check westd status 20260517T143700

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_westd_status_20260517T143700_20260517T143828_result.json`
- **Structured JSON:** [`393f6d723ecc31e94051.json`](../../sessions/39/393f6d723ecc31e94051.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态报告已写入 `artifacts/westd_status_check_143700.md`。摘要：

**GPU 状态:**
| GPU | 任务 | 状态 |
|-----|------|------|
| cuda:0 | humaneval_grpo_rasp_20_2048 | 52/164 (32%), Pass@1=0.20 |
| cuda:1 | math500_grpo_standard_20 | 运行 5h12m, 无日志, 超时风险高 |
| cuda:2 | humaneval_grpo_standard_20_2048 | 39/164 (24%), Pass@1=0.15 |
| **cuda:3** | **空闲** | **可立即使用** |

**MATH-500 RASP 超时诊断:**
- EXIT_CODE=124, 6h timeout 时仅完成 193/500 (38.6%)
- 最后记录 Acc=0.3067 (150/500 时)
- 根因: max_new_tokens 导致部分题目生成极慢 (单题最高 247s)
- 无部分结果 JSON, 需重跑
- cuda:1 的 standard 版同样用 max_new_tokens=4096, 大概率也会超时

---
