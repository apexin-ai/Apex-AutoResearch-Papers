# infra readonly check 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_readonly-check-10894_20260521T170754_result.json`
- **Structured JSON:** [`bbf69341ae5b7561d8ea.json`](../../sessions/bb/bbf69341ae5b7561d8ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-10894

**GPU:**
```
0, 99 %, 62203 MiB
1, 86 %, 63037 MiB
2, 99 %, 62203 MiB
3, 79 %, 62203 MiB
```

**finetune.py 进程:** 4 个 ablation 训练在跑
- GPU 0: `ablation_occ_detach_s0` (seed 42)
- GPU 1: `ablation_random_occ_s0` (seed 42)
- GPU 2: `ablation_occ_detach_s1` (seed 43)
- GPU 3: `ablation_random_occ_s1` (seed 43)

**Checkpoints:**
```
=== ablation_occ_detach_s0 ===
20000_chkpt  (May 22 01:01)
10000_chkpt  (May 21 21:57)

=== ablation_random_occ_s0 ===
20000_chkpt  (May 22 00:53)
10000_chkpt  (May 21 21:49)

=== ablation_occ_detach_s1 ===
20000_chkpt  (May 22 01:00)
10000_chkpt  (May 21 21:56)

=== ablation_random_occ_s1 ===
20000_chkpt  (May 22 01:01)
10000_chkpt  (May 21 21:57)
```

**磁盘:**
```
/dev/md0  250G  171G  80G  69%  /root/autodl-tmp
```

---

## westd-34685

**GPU:**
```
0, 99 %, 62203 MiB
1, 0 %, 0 MiB
2, 0 %, 0 MiB
3, 0 %, 0 MiB
```

**finetune.py 进程:** 1 个训练在跑
- GPU 0: `occ_s1_fresh` (seed 43, save_freq=2500)

**Checkpoints:**
```
=== occ_s1_fresh ===
10000_chkpt  (May 22 01:27)
7500_chkpt   (May 22 00:48)
5000_chkpt   (May 22 00:08)
2500_chkpt   (May 21 23:29)

=== occ_s0 ===
50000_chkpt (已完成)
47500_chkpt
```

**磁盘:**
```
/dev/md127  350G  231G  120G  66%  /root/autodl-tmp
```

---
