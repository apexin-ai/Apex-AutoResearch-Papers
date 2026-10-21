# ops check 14b westd

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_14b_westd_20260517T213624_result.json`
- **Structured JSON:** [`e98828d8c2a87db72343.json`](../../sessions/e9/e98828d8c2a87db72343.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告：qwen25_14b_scale_003

| 项目 | 状态 |
|------|------|
| 进程 | 存活，PID 20700，CPU 103%，运行 ~2.5h |
| GPU | cuda:0 占用 32.3GB/97.9GB，利用率 93% |
| 阶段 | Phase 2: 生成 d0（5000 unconditional samples） |
| 进度 | 2557/5000 samples (~51%)，正在持续写入 |
| Error/Warning | 无 error。有一个非致命 warning：tee 目标路径 `results/qwen25_14b_scale/` 目录不存在，导致 tee 写入失败，但不影响实际生成 |
| 预估 | d0 已跑 2.5h 完成 51%，预计再 ~2.5h 完成 d0。之后还有 d1-d3 三轮生成（每轮需要前一轮输出作为 prompt），总计预估还需 ~10-12h |

**结论**：实验正常运行中，无 stall/error。唯一问题是 `results/qwen25_14b_scale/` 目录不存在导致 tee 日志副本写入失败，但主数据正常产出到 `data/qwen25_14b/depth_0.jsonl`。

---
