# ops gpu check 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_check_34685_20260524T233637_result.json`
- **Structured JSON:** [`bc6d469c82bc32b68437.json`](../../sessions/bc/bc6d469c82bc32b68437.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

```
cuda:0 - 训练中 - PID 20913  - 99% GPU  - cutoff_45k_s1 (从20K重启), step ~6504/50005 (13%), 还需~11h
cuda:1 - 训练中 - PID 861222 - 99% GPU  - cutoff_15k_s1, step ~40302/50005 (81%), 还需~2.5h
cuda:2 - 训练中 - PID 998208 - 45% GPU  - cutoff_25k_s2, step ~23413/50005 (47%), 还需~7h
cuda:3 - 训练中 - PID 999132 - 93% GPU  - reverse_cutoff_s2, step ~23375/50005 (47%), 还需~7h
```

**备注：**
- cuda:0 的 cutoff_45k_s1 是重启训练（resume_step=20000），但 tqdm 显示 6504/50005，说明进度条从 0 计数，实际已保存 checkpoint 到 20K，当前 absolute step 约 26504
- cuda:1 进度最快，已有 10K/20K/30K/40K 四个 checkpoint，预计 ~2.5h 完成
- cuda:2 GPU 利用率偏低（45%），可能在做 checkpoint 保存或数据加载，但仍在正常推进
- 4 张卡全部正常运行，无崩溃

---
