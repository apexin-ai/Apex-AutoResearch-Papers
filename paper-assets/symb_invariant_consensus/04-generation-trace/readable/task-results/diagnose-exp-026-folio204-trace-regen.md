# diagnose exp 026 folio204 trace regen

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-026-folio204-trace-regen_20260518T120909_result.json`
- **Structured JSON:** [`577db1886e120085fada.json`](../../sessions/57/577db1886e120085fada.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是完整分析：

## 诊断结论

**4 次运行记录：**

| Run | 时间 | T | 处理题数 | 状态 |
|-----|------|---|---------|------|
| 1 (原始) | 19:39 | 0.30 | 7/204 (6完成) | 静默崩溃 |
| 2 (restart) | 19:46 | 0.70 | 28/204 (27完成) | 静默崩溃 |
| 3 (final) | 20:11 | 0.70 | **11/204 进行中** | PID 27245 存活 |
| 4 (v3) | 20:11 | 0.70 | <1 | 已死 (PID 27310) |

**关键发现：**

1. **所有崩溃无任何错误输出** — 无 Traceback、无 OOM、无 dmesg 记录、无 cgroup kill、无 journalctl
2. **脚本缺 `set -o pipefail`** — `python ... | tee ...` 管道掩盖了 Python 的退出码，bash 继续打印 `FOLIO_204_DONE`，让 cron 监控误判
3. **Run 3 和 Run 4 同时启动** — 两个实例竞争写同一个输出文件 `folio_204_results.json`，Run 4 已死
4. **Temperature 不匹配** — 用户意图 T=0.3，脚本写死 T=0.7（Run 1 的 T=0.3 来自不同命令）
5. z3 版本 4.15.4，`parse_z3_formula()` 用 `eval()` 将 LLM 生成的公式字符串传给 z3 C++ 后端

**根因：z3 C++ 层 SIGSEGV** — LLM 生成的约束公式经 `eval()` 传入 z3 后，特定病态输入触发 z3 native segfault，Python 进程被直接杀死（绕过所有 try/except）。崩溃点随 temperature/随机种子变化（不同输出→不同公式→不同 z3 代码路径）。

```json
{"root_cause":"z3 C++ SIGSEGV on pathological LLM-generated constraint formulas via eval() in parse_z3_formula(); masked by set -e without set -o pipefail in | tee pipeline","error_type":"infrastructure","fix_steps":["kill duplicate wrapper PIDs (27296/27302 already dead, verify no zombies)","add 'set -o pipefail' to run_folio_trace_regen.sh line 5","wrap z3 dedup+MaxSAT in subprocess (multiprocessing.Process with timeout) so SIGSEGV kills child not main process","fix script temperature from 0.7 to 0.3 to match intended experiment config","add flock or PID file guard to prevent concurrent launches","current PID 27245 is alive at 11/204 with T=0.70 — decide whether to let it run or kill and restart with correct T=0.3"],"can_auto_fix":false,"partial_results":"有部分结果: PID 27245 已保存 11/204 (folio_0~folio_10) 到 results/folio_204_14b/, 但 T=0.70 非目标温度 0.3"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "z3 C++ SIGSEGV on pathological LLM-generated constraint formulas via eval() in parse_z3_formula(); masked by set -e without set -o pipefail in | tee pipeline",
    "error_type": "infrastructure",
    "fix_steps": [
      "kill duplicate wrapper PIDs (27296/27302 already dead, verify no zombies)",
      "add 'set -o pipefail' to run_folio_trace_regen.sh line 5",
      "wrap z3 dedup+MaxSAT in subprocess (multiprocessing.Process with timeout) so SIGSEGV kills child not main process",
      "fix script temperature from 0.7 to 0.3 to match intended experiment config",
      "add flock or PID file guard to prevent concurrent launches",
      "current PID 27245 is alive at 11/204 with T=0.70 — decide whether to let it run or kill and restart with correct T=0.3"
    ],
    "can_auto_fix": false,
    "partial_results": "有部分结果: PID 27245 已保存 11/204 (folio_0~folio_10) 到 results/folio_204_14b/, 但 T=0.70 非目标温度 0.3"
  }
}
```

</details>

---
