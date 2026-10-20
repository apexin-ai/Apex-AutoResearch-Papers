# D140 Progress Check — 2026-05-21 17:12 UTC

## GPU Status
| GPU | Name | Util | Mem Used | Mem Total |
|-----|------|------|----------|-----------|
| 0 | RTX PRO 6000 Blackwell SE | 69% | 6,159 MiB | 97,887 MiB |
| 1 | RTX PRO 6000 Blackwell SE | 88% | 11,463 MiB | 97,887 MiB |
| 2 | RTX PRO 6000 Blackwell SE | 89% | 19,599 MiB | 97,887 MiB |
| 3 | RTX PRO 6000 Blackwell SE | 90% | 11,405 MiB | 97,887 MiB |

## Experiment Progress

### d140_1_7b_sft_s42_no_evi_2048_fix (cuda:0)
- PID 87382: **ALIVE** (uptime 1h44m)
- Progress: **205/247** batches (**83%**)
- Speed: ~31s/it
- ETA: **~22 分钟**

### d140_4b_sft_s42_no_evi_2048_fix (cuda:1)
- PID 88987: **ALIVE** (uptime 1h28m)
- Progress: **177/247** batches (**72%**)
- Speed: ~28-32s/it (波动较大)
- ETA: **~35 分钟**

### d140_8b_sft_s42_no_evi_2048_fix (cuda:2)
- PID 87302: **ALIVE** (uptime 1h44m)
- Progress: **139/247** batches (**56%**)
- Speed: ~45-52s/it
- ETA: **~81 分钟**

### d140_4b_sft_s42_with_evi_2048 (cuda:3)
- PID 93402: **ALIVE** (uptime 7m, 刚启动)
- Progress: **11/247** batches (**4%**)
- Speed: ~38s/it
- ETA: **~150 分钟 (~2.5h)**

## Disk
```
Filesystem      Size  Used Avail Use%
/dev/md0        350G  243G  108G  70%
```

## Summary
全部 4 个实验正常运行中。1.7B 最快，预计 ~22min 完成；4B no-evi ~35min；8B ~81min；4B with-evi 刚启动，~2.5h。磁盘空间充足。
