# infra read smoke results

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_read-smoke-results_20260515T113651_result.json`
- **Structured JSON:** [`e00cac8036a1d29c6bc5.json`](../../sessions/e0/e00cac8036a1d29c6bc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Smoke test 已完成，5 题全部跑完。

## Smoke Test 结果

| # | ID | Level | GT | SICA | SC | 约束提取 | 唯一约束 | 满足 | 排除 | 耗时 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | algebra/2470 | L1 | 137½ | 137½ ✓ | 137½ ✓ | 27 | 9 | 9 | 0 | 318s |
| 2 | prealgebra/65 | L2 | 6 | 6 ✓ | 6 ✓ | 26 | 2 | 2 | 0 | 340s |
| 3 | number_theory/847 | L3 | 4210₅ | 4210 ✓ | 4210 ✓ | 21 | 11 | 11 | 0 | 1693s |
| 4 | precalculus/1199 | L4 | π | (空) ✗ | (空) ✗ | 35 | 6 | 6 | 0 | 482s |
| 5 | algebra/2277 | L5 | 0 | 0 ✓ | 0 ✓ | 60 | 6 | 3 | 3 | 671s |

## 汇总

| 指标 | 值 |
|------|-----|
| **SICA accuracy** | **80% (4/5)** |
| **SC accuracy** | **80% (4/5)** |
| **Extraction rate** | 100% (5/5) |
| **Problems with contradictions** | 1/5 (algebra/2277, 3 excluded) |
| **Total time** | 3505s (~58 min) |

## 关键观察

- **SICA 和 SC 结果完全一致**，4 道简单/中等/困难题全部正确，两种方法没有差异。
- **唯一失败题 precalculus/1199 (L4)**：这是一道需要读图的三角函数题（graph of y = a sin(bx+c)+d），模型无法处理图像信息，SICA 和 SC 均产出空答案，vote dist 为空。
- **number_theory/847 耗时异常长**（1693s，占总时间 48%）：constraint extraction 花了 1504s，且有大量 JSON parse failed（14 次），说明该题的 trace 格式解析有问题，但最终结果正确。
- **algebra/2277 (L5)** 是唯一出现矛盾的题（3 satisfied / 3 excluded），SC 投票 7/12，但 SICA 和 SC 都答对了。

---
