# diag eval humaneval sft cka only 20 2048 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval_humaneval_sft_cka_only_20_2048_v2_20260519T111536_result.json`
- **Structured JSON:** [`9e9db4f0684bbc1b02ef.json`](../../sessions/9e/9e9db4f0684bbc1b02ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**实验已成功完成，非真正失败。** Cron 误报。

### 事实

| 项目 | 状态 |
|---|---|
| 输出文件 | 存在，70KB，完整 JSON |
| 完成度 | **164/164 题全部完成** |
| pass@1 | **20.12%** (33/164 通过，stderr=0.031) |
| 进程 PID 78740 | 已正常退出 |
| cuda:1 | **空闲可用**（0MiB / 0%） |

### 误报原因

Cron 监控检测到进程不存在后报告 "process dead"，但实际上进程是**正常结束**而非崩溃。没有 tmux 日志文件（`~/runs/` 中无对应 `eval_humaneval_sft_cka_only_20_2048_v2.log`）且无 W&B 集成，导致 Cron 无法区分"完成退出"和"异常退出"。

### 模型行为观察

从尾部几题的 error 信息看，模型在很多题上生成的是自然语言推理（chain-of-thought）而非 Python 代码，导致 SyntaxError。这是 SFT CKA-only 模型的行为特征，不是评估脚本 bug。

### 结论

**无需重跑。** 结果文件完整，pass@1 = 20.12%，可直接用于论文表格。cuda:1 当前空闲。

---
