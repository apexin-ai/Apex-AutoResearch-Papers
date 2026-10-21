# ssh westd phase2 sanity check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-phase2-sanity-check_20260519T103336_result.json`
- **Structured JSON:** [`154774c5bb1660ba8901.json`](../../sessions/15/154774c5bb1660ba8901.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成了。

## Phase 2 Sanity Check 结果

**ARC-Challenge accuracy: 77.82% (912/1172)**

| | Accuracy |
|---|---|
| Buggy 版本 | 22.95% |
| 修复版本 | **77.82%** |

**判定：PASS**

修复版 accuracy 从 22.95% 恢复到 77.82%，远超 60% 门槛。ARC logprob bug 修复已验证有效。

注意：输出文件名是 `eval_results.json` 而不是 `results.json`（脚本实际输出路径为 `/root/autodl-tmp/exp001/eval_results_v2/sanity_check_gemma2_d005_arc/eval_results.json`）。另外，所有 GPU 进程（包括其他任务）目前都已消失，可能有服务器级别事件发生。

---
