# ssh post restart check

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_post-restart-check_20260522T020922_result.json`
- **Structured JSON:** [`6bad733f1e5af3fa33cf.json`](../../sessions/6b/6bad733f1e5af3fa33cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整输出汇总：

**1. 进程存活检查：**
```
516824
exp_015 ALIVE
614614
exp_016 ALIVE
```

**2. GPU 状态：**
```
0, 60 %, 25017 MiB
1, 69 %, 25017 MiB
```

**3. Checkpoint 目录：**
```
/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed44/gen_8
/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed44/gen_7
/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed44/gen_6
/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed44/gen_5
/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed44/gen_4
---
(fixed_mix_r030_seed44: 无 checkpoint 目录)
```

**4. 磁盘状态：**
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/md0        250G  169G   82G  68% /root/autodl-tmp
```

**5. Results JSON：**
```
exp_015: list format, len=8, last_entry gen=7, total_entries=8
exp_016: FILE_NOT_FOUND, candidates=[]
```

**6. tmux sessions：**
```
exp_015: 1 windows (created Thu May 21 18:01:59 2026)
exp_016: 1 windows (created Fri May 22 07:16:07 2026)
```

---
