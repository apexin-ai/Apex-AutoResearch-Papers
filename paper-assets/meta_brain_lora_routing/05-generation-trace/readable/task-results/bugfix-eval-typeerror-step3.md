# bugfix eval typeerror step3

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_eval_typeerror_step3_20260516T075012_result.json`
- **Structured JSON:** [`e884258c3cc365e67d86.json`](../../sessions/e8/e884258c3cc365e67d86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 第二次日志检查结果

**日志行数对比：**

| 日志 | 第一次 | 第二次 | 增量 |
|------|--------|--------|------|
| eval_par_v1.log | 4608 | 5944 | **+1336** |
| eval_univ_r16.log | 4695 | 5710 | **+1015** |
| eval_univ_r48.log | 4753 | 6060 | **+1307** |

**结论：3 个进程全部存活，正常运行。**

日志尾部仍有 TypeError traceback 输出，但紧接着就是 `[info] using task orders [0, 1, 2, ...]` — 说明错误被 try/except 捕获后进程继续执行下一个 episode。

关于 traceback 显示的是新代码（带 `if np.issubdtype...`）：这是因为 Python 打印 traceback 时从磁盘读取当前源文件行，但运行中的字节码仍然是旧版本。实际运行的是修复前的代码，错误被上层 catch。

**不需要 kill 和重启。** Bug 已在磁盘上修复，下次重启后生效。当前 3 个 eval 进程在正常推进中，每个都在 3-4 分钟内增长了 1000+ 行日志。

---
