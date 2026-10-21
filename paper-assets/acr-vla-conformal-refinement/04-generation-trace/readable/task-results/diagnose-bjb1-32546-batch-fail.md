# diagnose bjb1 32546 batch fail

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb1-32546-batch-fail_20260521T003100_result.json`
- **Structured JSON:** [`6d4ecd80b80bfae0d932.json`](../../sessions/6d/6d4ecd80b80bfae0d932.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。结果如下：

---

**根因：系统性失败——`nohup python` 找不到 `python` 命令**

这台服务器用 conda 环境，`python` 只存在于 `/root/miniconda3/bin/python`，不在默认 PATH 中。nohup 启动时没有激活 conda 环境，导致 `python` 命令不可用。**全部 4 个实验都没有真正启动过**，不是 cron false positive。

---

```
exp_id: eval-obs-only-object-norm003-seed62
status: real_failure
evidence: 日志仅一行 "nohup: failed to run command 'python': No such file or directory"，无 output JSON，进程 720053 已不存在
success_rate: N/A（未执行）

exp_id: eval-obs-only-object-norm003-seed63
status: real_failure
evidence: 同上，日志同一错误，无 output JSON，进程 720054 已不存在
success_rate: N/A（未执行）

exp_id: eval-obs-only-object-norm01-seed51-r2
status: real_failure
evidence: 同上，日志同一错误，无 output JSON，进程 720055 已不存在
success_rate: N/A（未执行）

exp_id: eval-obs-only-object-norm01-seed52-r2
status: real_failure
evidence: 同上，日志同一错误，无 output JSON，进程 720056 已不存在
success_rate: N/A（未执行）
```

**附：eval-obs-only-object-norm005-seed49-r2 (PID 720058)** 也是同一问题——日志同样只有 `nohup: failed to run command 'python': No such file or directory`，进程已不存在。

---

**总结**：系统性问题，不是 cron false positive。启动脚本用 `nohup python ...` 调用，但服务器的 `python` 只在 `/root/miniconda3/bin/` 下，nohup 的环境中没有 conda PATH。修复方式：启动命令改为 `nohup /root/miniconda3/bin/python ...` 或在 nohup 前 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。5 个实验都需要重跑。

---
