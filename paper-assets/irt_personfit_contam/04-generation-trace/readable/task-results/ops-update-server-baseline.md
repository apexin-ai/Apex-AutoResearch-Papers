# ops update server baseline

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_update-server-baseline_20260523T161235_result.json`
- **Structured JSON:** [`988a34bcc8b011c42b5a.json`](../../sessions/98/988a34bcc8b011c42b5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

替换完成，旧值已不存在。验证汇总：

**File 1** (`compute_cohens_d.py`):
- 第10-11行数组已更新为 `[0.8446, -1.8765, 0.3452, 0.0206, 1.7323, 2.8466, -0.4007, 1.1656, 0.1897, -2.2497]`
- 旧值 `-0.4891` 已不存在

**File 2** (`bca_bootstrap.py`):
- 第78行 `llama_free` 已更新为新值数组
- 旧值已不存在

两个文件的数组值来自服务器上 10 个 clean seed V2 re-eval 结果文件（`clean_results.json` ~ `clean_s10_results.json`），mean=0.2618, std(ddof=1)=1.5416。

---
