# monitor progress check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_progress-check_20260520T034847_result.json`
- **Structured JSON:** [`0f6714b535428542d5d2.json`](../../sessions/0f/0f6714b535428542d5d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进度汇总

| 实验 | GPU | 进度 | 预计剩余 |
|------|-----|------|---------|
| eval_llama_rsft_s43_no_evidence | cuda:1 | 189/247 (77%) | ~29 min |
| llama_rsft_s44_pipeline | cuda:3 | 训练完成 → eval 205/247 (83%) | ~21 min |
| plan017_14b_rsft_generate | cuda:0+2 | 1611/3027 (53%) | ~7.5 h |

### 详情

- **s43_no_evidence eval**: 平均 ~30s/it，已运行 ~1h37m，剩 58 batches。
- **s44_pipeline**: 训练 3 epoch 已完成（loss=0.49, token_acc=88.7%），10:02:56 进入 Step 2 eval，当前 205/247，平均 ~30s/it，剩 42 batches。
- **plan017_14b_generate**: 从上次 1540 推进到 1611（+71），平均 ~20s/it，剩 1416 samples。

## GPU 利用率

```
GPU 0:  35%  |  17,359 / 32,607 MiB  (plan017 shard)
GPU 1:  69%  |  18,411 / 32,607 MiB  (s43 eval)
GPU 2:  40%  |  19,557 / 32,607 MiB  (plan017 shard)
GPU 3:  74%  |  18,421 / 32,607 MiB  (s44 eval)
```

4 块 GPU 全在工作。s43 eval 和 s44 eval 预计 ~20-30 分钟内先后完成，plan017 generate 还需较长时间。

---
