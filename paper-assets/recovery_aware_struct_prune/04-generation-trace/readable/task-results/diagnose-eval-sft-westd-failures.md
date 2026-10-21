# diagnose eval sft westd failures

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_sft_westd_failures_20260515T190528_result.json`
- **Structured JSON:** [`122478bd788b550a21ad.json`](../../sessions/12/122478bd788b550a21ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

---

## 诊断结果

### 1. 失败根因

两个实验的错误完全相同：

```
python: can't open file '/root/autodl-tmp/recovery_aware_struct_prune/src/eval_gsm8k.py': [Errno 2] No such file or directory
```

**根因：实验启动时代码尚未同步到数据盘路径。** 实验在 `01:35` 从 `/root/autodl-tmp/recovery_aware_struct_prune/` 目录启动，但 `src/eval_gsm8k.py` 直到 `03:03` 才出现在该路径下。脚本**从未执行**，日志文件各仅 2 行，瞬间失败。

### 2. 结果文件

不存在。两个 JSON 结果文件均未生成（eval 根本没跑起来）。

### 3. 修复建议

重新提交实验前确认代码已同步到工作目录：
- 确保 `cd /root/autodl-tmp/recovery_aware_struct_prune && ls src/eval_gsm8k.py` 存在后再启动
- 或将实验的工作目录改为根分区的 `/root/recovery_aware_struct_prune/`（代码在那里，时间戳 `May 15 11:53`），同时 `--output_path` 和 `--model_path` 用绝对路径指向数据盘

另外注意：实验 2 的 `--output_path` 写错了，用的是 `eval_sft_rasp_20_westd_n100.json`（和实验 1 相同），应该是 `eval_sft_standard_20_westd_n100.json`，重跑时需修正。

---
