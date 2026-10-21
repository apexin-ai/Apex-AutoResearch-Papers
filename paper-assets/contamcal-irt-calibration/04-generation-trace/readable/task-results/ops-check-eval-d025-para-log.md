# ops check eval d025 para log

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-eval-d025-para-log_20260516T043351_result.json`
- **Structured JSON:** [`10d0725634f369375e05.json`](../../sessions/10/10d0725634f369375e05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无活跃 cron，无需删除。

---

**结果汇总：**

| 项目 | 结果 |
|------|------|
| **判断** | **SUCCESS** |
| **依据** | `.done` sentinel 已写入，3 个 benchmark 全部完成，结果文件已保存 |
| **mmlu (para)** | 0.6468 (4266/6596) |
| **arc_challenge (para)** | 0.8106 (565/697) |
| **humaneval (para)** | 0.0000 (0/26) |
| **输出目录** | `/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned/` |
| **Registry** | DONE / success，metrics 已录入 |
| **cuda:0 状态** | PID 691887 占用 3886MiB（1.5B s123 signals 进程），eval 进程已退出 |

注：bitsandbytes 加载报 `libnvJitLink.so.13` 缺失，但未影响 eval 执行（非必需依赖）。humaneval pass@1=0 值得关注——可能是 paraphrase 后 code generation 格式不匹配导致。

---
