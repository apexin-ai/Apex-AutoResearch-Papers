# ops gpu check submit 05B s123

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-check-submit-05B-s123_20260516T024005_result.json`
- **Structured JSON:** [`1230b3d3a20a925c6c9e.json`](../../sessions/12/1230b3d3a20a925c6c9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本存在且内容正确（0.5B 模型，s123 种子，4 个 dosage × 3 个 benchmark = 12 个信号计算任务）。

## GPU 状态总结

| GPU | 进程 | PID | 显存 | 利用率 | 运行时间 | 任务 |
|-----|------|-----|------|--------|----------|------|
| cuda:0 | eval d100_a32_s123 (para+aligned) | 642757 | 9008/24564 MiB | 64% | **5h04m** | 4 benchmarks + paraphrase |
| cuda:1 | eval d000_s42 (aligned) | 676497 | 8976/24564 MiB | 69% | 37m | 4 benchmarks |
| cuda:2 | eval d005_s42 (aligned) | 679190 | 8976/24564 MiB | 67% | 24m | 4 benchmarks |
| cuda:3 | eval d025_v3_s42 (para+aligned) | 682166 | 9008/24564 MiB | 0% | 7m | 3 benchmarks + paraphrase |
| cuda:4 | signals 3B d025_s123 (s4) | 668217 | 6562/24564 MiB | 63% | 1h49m | mmlu signal |
| cuda:5 | signals 3B d025_v3_s42 (s4) | 663067 | 7796/24564 MiB | 62% | 2h22m | mmlu signal |

**所有 GPU 都在忙，无法立即提交。**

### 预估最先空闲

**cuda:0 最可能先空闲** — eval d100_a32_s123 已跑 5h+，带 paraphrase 的 4-benchmark eval 通常 5-6h 完成，应该接近尾声。

其次是 cuda:1（eval 37m，无 paraphrase 的 4-benchmark eval 通常约 1.5-2h）和 cuda:2（24m，同类任务）。

cuda:3 刚启动 7 分钟（GPU util 0% 说明可能在加载模型），还需较长时间。cuda:4/5 的 3B signal 计算通常需要 3-5h。

**建议**：等 cuda:0 的 eval 完成后立即提交 0.5B s123 信号计算，预计 30 分钟内空闲。

---
