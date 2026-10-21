# experiment exp wiki multi source

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_exp_wiki_multi_source_20260520T102709_result.json`
- **Structured JSON:** [`6db9b9b4c3bb0b827e29.json`](../../sessions/6d/6db9b9b4c3bb0b827e29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进展良好。with_label 已到 2v3。继续等剩余结果出来，之后进入 unified scorer 阶段（GPU 会开始占用）。

实验正在稳定运行中。当前进度汇总：

**Vocab-only (6D text features)**:
- no_label: 0v1=0.7616, 1v2=0.5434, 2v3=0.5170, 3v4=0.5017, 4v5=0.5084 → **K*=1**
- with_label: 0v1=0.7779, 1v2=0.5520, 2v3=0.5248 → K*=1（进行中）

接下来还需等 with_label 剩余 2 对 + 整个 unified scorer 阶段（模型加载 + rescoring 2个 generator × 6 depths × 5000 texts + 10 个 pairwise bootstrap）。

PID=308488，在 cqa1-22115 cuda:0 上运行。log 路径：`/root/autodl-tmp/gen-depth-contamination/results/exp_wiki_multi_source.log`。registry 状态已更新为 RUNNING。

实验已成功提交并稳定运行，预计总运行时间约 15-20 分钟。

---
