# diagnose w3 gpu check

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w3-gpu-check_20260521T092723_result.json`
- **Structured JSON:** [`e4844e799a541d678fcf.json`](../../sessions/e4/e4844e799a541d678fcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**进程已死，但任务已全部完成。**

### GPU 状态
- GPU 空闲：0MiB 显存，0% 利用率，无任何进程占用

### 进程状态
- 无任何 python/lm_eval 进程存活
- 服务器上仅有系统进程（sshd、supervisord、jupyter-lab）

### Eval 完成情况
**30/30 任务全部完成。** 日志最后一行：

```
17:20:55 ALL DONE
```

最后完成的模型是 `1.3B-100B-HGRN2-hybrid-3-1`，winogrande 于 17:19 完成，piqa 于 17:20 完成。

结果目录确认——winogrande 和 piqa 各 15 个模型全部有结果：
- `winogrande/`: 15 个模型目录（GatedDeltaNet×5 + RetNet×5 + HGRN2×5）
- `piqa/`: 15 个模型目录（同上）

### 结论
W3 eval 脚本已于今天 **17:20:55** 正常跑完全部 30 个任务并退出，所以 GPU 利用率为 0% 是正常的。不需要修复，可以直接进行下一步分析。

---
