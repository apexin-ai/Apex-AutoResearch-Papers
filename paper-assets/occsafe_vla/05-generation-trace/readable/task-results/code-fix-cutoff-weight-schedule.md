# code fix cutoff weight schedule

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-cutoff-weight-schedule_20260521T134802_result.json`
- **Structured JSON:** [`0fd1adba99be1a87ca11.json`](../../sessions/0f/0fd1adba99be1a87ca11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

scripts 目录不在任何 git repo 内，注释已更新但无法 git commit。

### 产出汇总

**1. 代码对比**

修改前 (L1110-1113):
```python
if cfg.occ_loss_cutoff_step > 0:
    occ_weight_now = cfg.occ_loss_weight if batch_idx < cfg.occ_loss_cutoff_step else 0.0
else:
    occ_weight_now = cfg.occ_loss_weight * math.exp(-batch_idx / cfg.occ_loss_decay_steps)
```

修改后 (L1110-1114):
```python
if cfg.occ_loss_cutoff_step > 0:
    base_weight = cfg.occ_loss_weight * math.exp(-batch_idx / cfg.occ_loss_decay_steps)
    occ_weight_now = base_weight if batch_idx < cfg.occ_loss_cutoff_step else 0.0
else:
    occ_weight_now = cfg.occ_loss_weight * math.exp(-batch_idx / cfg.occ_loss_decay_steps)
```

config 注释也从 `"no decay, constant weight before cutoff"` 改为 `"exponential decay before cutoff"`。

**2. 验证输出** (cutoff_step=35000):
```
step=     0 base=0.010000 cutoff_weight=0.010000
step= 10000 base=0.008187 cutoff_weight=0.008187
step= 20000 base=0.006703 cutoff_weight=0.006703
step= 30000 base=0.005488 cutoff_weight=0.005488
step= 34999 base=0.004966 cutoff_weight=0.004966
step= 35000 base=0.004966 cutoff_weight=0.000000
step= 40000 base=0.004493 cutoff_weight=0.000000
step= 50000 base=0.003679 cutoff_weight=0.000000
```

**3. Git commit**: `e36e9bd` — `fix: cutoff mode uses exponential decay before cutoff step (eliminates dosage confound)`

**4. cutoff_experiments.sh**: 注释已更新为 `"weight schedule: exponential decay (same as full-OCC), zeroed after cutoff step"`。该文件不在 git repo 内，无需 commit。

---
