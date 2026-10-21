# ssh exp015 status urgent

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp015-status-urgent_20260522T045916_result.json`
- **Structured JSON:** [`32a8062144e51ecd6371.json`](../../sessions/32/32a8062144e51ecd6371.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整输出汇总：

---

**1. exp_015 进程**
```
PID     ETIME
516824  18:57:47
exp_015 ALIVE
```

**2. exp_015 checkpoints (gen_0 ~ gen_9，已全部完成)**
```
/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed44/gen_0
/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed44/gen_1
/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed44/gen_2
/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed44/gen_3
/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed44/gen_4
/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed44/gen_5
/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed44/gen_6
/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed44/gen_7
/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed44/gen_8
/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed44/gen_9
```

**3. exp_015 results (r=0.25, seed44) — 10 gen 全部有数据**
```
gen_0: eff_rank=417.55, SLV=2366.68, ppl=9.55,  d4=0.7305, train_loss=?
gen_1: eff_rank=475.92, SLV=2366.13, ppl=10.22, d4=0.6379, train_loss=1.800
gen_2: eff_rank=484.39, SLV=2364.59, ppl=10.64, d4=0.5156, train_loss=1.689
gen_3: eff_rank=488.62, SLV=2378.05, ppl=11.00, d4=0.4518, train_loss=1.473
gen_4: eff_rank=493.01, SLV=2402.71, ppl=11.33, d4=0.4156, train_loss=1.388
gen_5: eff_rank=494.32, SLV=2415.91, ppl=11.64, d4=0.4008, train_loss=1.319
gen_6: eff_rank=498.74, SLV=2437.92, ppl=11.97, d4=0.3994, train_loss=1.294
gen_7: eff_rank=502.71, SLV=2456.77, ppl=12.30, d4=0.3865, train_loss=1.265
gen_8: eff_rank=504.20, SLV=2463.28, ppl=12.61, d4=0.3703, train_loss=1.239
gen_9: eff_rank=510.29, SLV=2482.46, ppl=13.01, d4=0.3621, train_loss=1.212
```

**4. exp_016 进程**
```
PID     ETIME
614614  05:43:38
exp_016 ALIVE
```

**exp_016 checkpoints (gen_0 ~ gen_2，正在跑)**
```
/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r03_seed44/gen_0
/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r03_seed44/gen_1
/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r03_seed44/gen_2
```

**exp_016 results (r=0.30, seed44) — 3 gen 已完成**
```
gen_0: eff_rank=417.55, SLV=2366.68, ppl=9.55,  d4=0.7305, train_loss=?
gen_1: eff_rank=476.91, SLV=2365.49, ppl=10.19, d4=0.6714, train_loss=1.836
gen_2: eff_rank=484.43, SLV=2371.06, ppl=10.57, d4=0.5271, train_loss=1.748
```

**5. GPU 状态**
```
0, 100 %, 25017 MiB
1, 94 %, 25017 MiB
```

**6. 磁盘**
```
Filesystem      Size  Used Avail Use%  Mounted on
/dev/md0        250G  172G   79G  69%  /root/autodl-tmp
```

**7. tmux**
```
exp_015: 1 windows (created Thu May 21 18:01:59 2026)
exp_016: 1 windows (created Fri May 22 07:16:07 2026)
```

---

**状态摘要**: exp_015 已跑完 10 gen（运行 ~19h），进程仍存活（可能在收尾）；exp_016 正在跑，完成 3/10 gen（运行 ~5.7h）；双卡满载，磁盘 69% 剩余 79G。

---
