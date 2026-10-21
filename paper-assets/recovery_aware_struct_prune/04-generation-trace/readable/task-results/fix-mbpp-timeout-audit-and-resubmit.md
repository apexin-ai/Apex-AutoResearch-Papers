# fix mbpp timeout audit and resubmit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_mbpp_timeout_audit_and_resubmit_20260519T202345_result.json`
- **Structured JSON:** [`e1bfc5cfff1cdb23faa2.json`](../../sessions/e1/e1bfc5cfff1cdb23faa2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval_mbpp_grpo_rasp_20 实际在运行（220/374），之前看到的 "Terminated" 是旧 run 的日志残留。

---

## 报告

### A. eval_mbpp_grpo_standard_20 重跑
- **已启动**，westd cuda:0（cuda:2 被 HumanEval eval 占用，改用 cuda:0）
- 无 timeout wrapper，用 tee 记录日志
- Registry: retry_count=1, status=RUNNING
- 模型正在加载，预计 ~4-6h 完成

### B. Timeout 审计

| 实验 | timeout | 进度 | 预估剩余 | 风险 |
|------|---------|------|---------|------|
| eval_mbpp_grpo_rasp_20 | 无 | 220/374 | ~51min | 安全 |
| eval_mbpp_sft_rasp_20 | 86400s (24h) | ~161/374 | ~35min | 安全 |
| eval_mbpp_sft_standard_20 | ~~14400s (4h)~~ | **被误杀** | — | 需重跑 |

### 事故：eval_mbpp_sft_standard_20 被误杀

杀 timeout wrapper 时用了 `kill`(SIGTERM) 而非 `kill -STOP`。timeout 进程退出时连带杀死了子进程 python。150/374 进度丢失，无部分结果文件。

**当前所有 GPU 被占用**，等 grpo_rasp_20 或 sft_rasp_20 完成后（~30-50min）可在释放的 GPU 上重跑 sft_standard_20。

### GPU 映射（当前）

| GPU | 占用进程 | 显存 |
|-----|---------|------|
| 0 | eval_mbpp_grpo_standard_20 (加载中) | 即将占用 ~17GB |
| 1 | eval_mbpp_grpo_rasp_20 | 17268 MiB |
| 2 | 未知进程 PID 135726 | 14568 MiB |
| 3 | eval_mbpp_sft_rasp_20 | 12802 MiB |

### 建议

1. **~35-50min 后**在释放的 GPU 上重跑 eval_mbpp_sft_standard_20
2. **系统性修复**：框架对 MBPP eval 默认 timeout 应 ≥ 8h
3. **操作教训**：杀 timeout wrapper 保留子进程应用 `kill -STOP` 冻结，不能用 `kill`

需要我在 sft_rasp_20 完成后自动重跑 sft_standard_20 吗？

---
