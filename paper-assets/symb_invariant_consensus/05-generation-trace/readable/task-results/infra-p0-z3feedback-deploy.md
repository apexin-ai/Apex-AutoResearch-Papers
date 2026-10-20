# infra p0 z3feedback deploy

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_p0-z3feedback-deploy_20260518T181046_result.json`
- **Structured JSON:** [`853220bbfd3cf1a46af8.json`](../../sessions/85/853220bbfd3cf1a46af8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果汇总：

**exp-036 Z3 Feedback 最终结果：**

| 方法 | 准确率 | 正确数/总数 |
|------|--------|------------|
| **Z3-Feedback SICA** | **0.775** | 158/204 |
| Vanilla SICA | 0.745 | 152/204 |
| Self-Consistency | 0.750 | 153/204 |

- Z3FB vs Vanilla: **+9 -3 (net +6)**
- UNSAT traces: 22/2448 (0.9%)
- UNSAT→SAT resolve rate: 86.4% (19/22)
- 总耗时 ~10 分钟

**产出清单：**
1. exp-028 进程已彻底 kill，GPU 2 已释放并重新使用 ✅
2. Z3 Feedback dry-run 通过（所有依赖可导入，数据完整）✅
3. Z3 Feedback 正式实验完成，日志确认是 UNSAT core refinement（非标准 SICA）✅
4. tmux sessions: `z3fb_vllm`（vLLM server，port 8002，PID 74518），`z3fb_runner`（已完成退出）
5. 结果文件: `results/exp036_z3_feedback/z3_feedback_results.json`

Z3 Feedback 比 Vanilla SICA 提升 **+3.0pp**（74.5%→77.5%），比 Self-Consistency 提升 **+2.5pp**。

---
