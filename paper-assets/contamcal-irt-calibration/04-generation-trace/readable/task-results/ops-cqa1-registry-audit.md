# ops cqa1 registry audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-registry-audit_20260519T185056_result.json`
- **Structured JSON:** [`1de1a2160bbb02b36ef5.json`](../../sessions/1d/1de1a2160bbb02b36ef5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cqa1 审计结果

### GPU 进程
- **cuda:0**: PID 269332 (python), 16644 MiB / 24564 MiB, GPU 利用率 95%, 功率 424W/425W
- 确认是 eval_qwen7b_s123_v2 的 evaluate.py 进程

### eval 进度
| dosage | 状态 |
|--------|------|
| d000_s123 | ✅ done |
| d005_s123 | ✅ done (arc_challenge acc=0.8251) |
| d025_s123 | 🔄 运行中 — mmlu 评估 4572/14042 (32.6%), ~20 it/s |
| d050_s123 | 待运行 |
| d100_s123 | 待运行 |

d025 的 mmlu 还剩约 9470 items，按 ~21 it/s 估算还需 ~7.5 分钟完成 mmlu，之后还有 arc_challenge (~1172 items)。d050、d100 各需类似时长。**整体完成预计还需 ~40-50 分钟。**

### Registry 状态
`eval_qwen7b_s123_cqa1_v2` — **RUNNING** ✅ 正确，无需更新。

### 注意
- bitsandbytes 报了 `libnvJitLink.so.13` 加载错误，但不影响评估（非必需库）
- 旧版 eval 结果 (old_20260520) 5 个 dosage 都已完成并保留

---
