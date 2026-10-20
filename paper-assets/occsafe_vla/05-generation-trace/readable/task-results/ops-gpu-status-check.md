# ops gpu status check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260526T135104_result.json`
- **Structured JSON:** [`fdf205b2f2058403439e.json`](../../sessions/fd/fdf205b2f2058403439e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已收集完毕。当前时间 UTC 21:52 (May 26)。

```
| 服务器:GPU         | exp_id              | step/50005   | 速度       | GPU利用率 | 显存        | tqdm剩余   | ETA (UTC)         |
|--------------------|---------------------|--------------|------------|-----------|-------------|------------|-------------------|
| 10894:0            | reverse_cutoff_s2_v2| 17147/50005  | ~1.00 it/s | 92%       | 62.2/97.9G  | ~9h09m     | May 27 ~07:01     |
| 10894:1            | full_occ_ln_v2_s0   | 6206/50005   | ~1.05 it/s | 99%       | 63.0/97.9G  | ~11h36m    | May 27 ~09:28     |
| 10894:2            | full_occ_ln_v2_s1   | 6140/50005   | ~1.06 s/it | 96%       | 62.2/97.9G  | ~12h56m    | May 27 ~10:48     |
| 10894:3            | detach_ln_v2_s0     | 6192/50005   | ~1.06 it/s | 91%       | 62.2/97.9G  | ~11h31m    | May 27 ~09:23     |
| 34685:0            | vanilla_v2_s1       | 18187/50005  | ~1.02 it/s | 99%       | 62.2/97.9G  | ~8h38m     | May 27 ~06:30     |
| 34685:1            | vanilla_v2_s2       | 18291/50005  | ~1.05 it/s | 53%       | 62.2/97.9G  | ~8h26m     | May 27 ~06:18     |
| 34685:2            | detach_ln_s3        | 18194/50005  | ~1.03 it/s | 99%       | 62.2/97.9G  | ~8h33m     | May 27 ~06:25     |
| 34685:3            | cutoff_25k_s1_v2    | 16888/50005  | ~1.06 it/s | 45%       | 62.2/97.9G  | ~8h40m     | May 27 ~06:32     |
```

**总结：**
- 8 张 GPU 全部满载训练中，显存占用一致 (~62-63G/98G)
- 34685 上的 4 个实验 (vanilla/detach_ln/cutoff) 启动较早，进度 33-37%，预计 **May 27 06:18-06:32 UTC** 完成
- 10894:0 的 reverse_cutoff_s2_v2 也是早批启动，进度 34%，预计 **May 27 ~07:01 UTC**
- 10894:1-3 的 3 个实验 (full_occ_ln_v2_s0/s1, detach_ln_v2_s0) 启动较晚（~3h前），进度 12%，预计 **May 27 09:23-10:48 UTC** 完成
- 34685:1 (vanilla_v2_s2) 和 34685:3 (cutoff_25k_s1_v2) GPU 利用率偶尔偏低 (53%/45%)，但速度正常，可能是采样时刻的波动

---
