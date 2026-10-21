# ssh cuda0 task submit

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cuda0_task_submit_20260515T030830_result.json`
- **Structured JSON:** [`6d6b4161c1b2a84d4d4a.json`](../../sessions/6d/6d6b4161c1b2a84d4d4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 已有 GPU 任务在跑。** 汇总：

| GPU | 进程 | 显存 | 利用率 |
|-----|------|------|--------|
| cuda:0 | batch feature extraction (PID 287191) | 18066 MiB | 100% |
| cuda:1 | DCOL v5 training (PID 283196) | 4703 MiB | 99% |

**已提交任务**: `batch_feature_extraction_5cells`
- 在 cuda:0 上依次为 5 个缺 features 的 cell 提取特征：gpt2xl_topk50 → gpt2xl_temp09 → olmo_topk50 → olmo_temp09 → pythia_topk50
- 模型：gpt2-xl, olmo-1b-hf, pythia-1.4b
- 输出：`results/{cell}/features.jsonl`
- 日志：`logs/batch_feature_extraction.log`
- 实验已注册为 RUNNING

提取完成后可以在 CPU 上跑分类（plan_009 cross-cell baseline battery 的前置步骤）。

---
