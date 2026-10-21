# code re repair data filter

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_re-repair-data-filter_20260517T040909_result.json`
- **Structured JSON:** [`79f6ff1d277996e6b05c.json`](../../sessions/79/79f6ff1d277996e6b05c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

筛选完成。结果汇报：

## 筛选结果

| 阶段 | 数量 |
|------|------|
| 有 per-test oracle 的 problems | 25 |
| Mutation instances (非 gold) | 25 |
| ≥2 f2p tests 实际失败 | 11 |
| CLS 非全对 | **9** |

### 复杂度分布
- simple (2-3 f2p): 7
- medium (4-6 f2p): 0
- complex (7+): 2

### 瓶颈

**per-test 执行 oracle 只覆盖 25 个 problem**（`swebench_test.jsonl` 中的 repo-level test set）。`swebench_verified_meta.jsonl` 有 500 个 instance，mutation patches 覆盖约 415 个，但绝大部分没有逐 test 的执行结果。

### 达到 50-80 的路径

需要两步：
1. **扩展 per-test execution**：对更多 mutation instances 跑 SWE-bench 测试执行，获得 oracle per-test labels（可从 415 个 mutation patches 中选取 FAIL_TO_PASS ≥ 2 的 ~200 个候选）
2. **跑 CLS inference**：对新的 per-test 数据跑 cls8b ckpt3600 推理

这两步都是 CPU/单 GPU 操作，不会影响训练任务。需要我先统计哪些 instances 有 ≥2 f2p tests（从 metadata）并准备执行脚本吗？

当前已输出 9 个实例到：`/root/autodl-tmp/eval_results/re_repair_v2/re_repair_instances.jsonl`

---
