# diagnose exp 001 eval llama32 3B d025 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_eval_llama32_3B_d025_s42_20260516T203328_result.json`
- **Structured JSON:** [`2c484f8e68dff13fbb4f.json`](../../sessions/2c/2c484f8e68dff13fbb4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**实验实际上已成功完成，EXIT_CODE=129 不影响结果。**

### Root Cause

EXIT_CODE=129 (SIGHUP) 是 tmux session 被销毁时发送给前台进程的信号。从 spec note "awaiting actual process submission after tmux cleanup" 看，进程是在 tmux session 中运行的，当 tmux session 被清理（kill/detach）时，shell 收到 SIGHUP 并以 128+1=129 退出。但此时 Python eval 脚本**已经正常跑完**。

### 证据

1. **日志最后几行**显示所有 4 个 benchmark 都完成了：
   - mmlu accuracy: 0.4150 (5828/14042)
   - gsm8k: 已完成
   - arc_challenge: 已完成
   - humaneval pass@1: 0.0244 (4/164)

2. **`.done` sentinel 已写入**（04:29 UTC），确认代码正常走到了 exit 点

3. **所有结果文件齐全**：`eval_results.json`, `correctness_matrix.json`, `item_responses.json` 及各 benchmark 子结果

4. 日志中有大量 HuggingFace 超时 warning（AutoDL 网络问题），但最终通过 retry 和 cache 跑通了

### 结论

- **不是失败**。eval 全部完成，结果完整写入。EXIT_CODE=129 只是 tmux session 在进程退出后被回收的副作用。
- **无需重试**，数据完整可用。
- GPU 3 当前空闲（0MiB 占用），进程已干净退出。

---
