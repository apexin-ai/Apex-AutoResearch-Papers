# diagnose exp 002 signals 05B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_002_signals_05B_20260514T125916_result.json`
- **Structured JSON:** [`946ebd2b026d6dfe6bd5.json`](../../sessions/94/946ebd2b026d6dfe6bd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。下面汇总结果。

## 诊断结果: exp_002_signals_05B

### 1. 失败原因: **selfcritique 信号计算崩溃 + 外层进程被 SIGTERM 终止**

两层问题叠加:

**内层 (compute_signals.py):** 每个 (dosage, benchmark) task 在跑完 embedding 和 minkpp 后，运行 selfcritique 时崩溃（返回非零 exit code）。证据：
- 所有 task 标记为 FAIL，但 embedding/minkpp 文件确实已写入磁盘
- **零个 selfcritique 信号文件存在**
- batch runner 只捕获了 stderr 的最后 500 字符（transformers model type listing），实际 traceback 被截断不可见

**外层 (batch runner):** 进程在 task 4/9 (d005/mmlu) 执行期间被 SIGTERM 终止。日志仅 24 行，无 BATCH SUMMARY。第二次运行（20:55）同样被杀。

### 2. 信号完成度: **6/27**

| dosage | benchmark | embedding | minkpp | selfcritique |
|--------|-----------|-----------|--------|--------------|
| d000 | mmlu | ✓ | ✓ | ✗ |
| d000 | gsm8k | ✓ | ✓ | ✗ |
| d000 | arc_challenge | ✓ | ✗ | ✗ |
| d005 | mmlu | ✓ | ✗ | ✗ |
| d005 | gsm8k | ✗ | ✗ | ✗ |
| d005 | arc_challenge | ✗ | ✗ | ✗ |
| d100 | * | ✗ | ✗ | ✗ |

### 3. 部分结果可用性

6 个已缓存的 signal 文件可用（compute_signals.py 有 `_load_cached_signal` 机制）。**但** batch runner 的 skip 逻辑检查 `signals_merged_{benchmark}.json`（merge 从未执行），所以每次重启都从头跑所有 9 个 task（内部信号级缓存仍有效）。

### 4. 建议

1. **首先修复 selfcritique 崩溃** — 需要单独运行一次 compute_signals.py 带 `--signals selfcritique` 看完整 traceback（可能是 LoRA adapter 加载失败、OOM、或 benchmark 数据格式不匹配）
2. **修复后可重启** — 已缓存的 embedding/minkpp 信号会被自动跳过
3. **调查 SIGTERM 来源** — 可能是 cron 超时、AutoDL 系统策略、或手动 kill

---
