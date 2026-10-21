# Westd Status Check — Loop 17
**Time**: 2026-05-16 10:44 UTC

## GPU Usage
| GPU | Model | VRAM Used | VRAM Total | Util | Process |
|-----|-------|-----------|------------|------|---------|
| 0 | RTX 5090 | 21131 MiB | 32607 MiB | 87% | shard3 eval (PID 453335) |
| 1 | RTX 5090 | 21133 MiB | 32607 MiB | 88% | shard2 eval (PID 448100) |
| 2 | RTX 5090 | 0 MiB | 32607 MiB | 0% | **IDLE** |
| 3 | RTX 5090 | 21133 MiB | 32607 MiB | 88% | v3 eval (PID 443221) |

## Experiment Status

### cwm8b-ckpt400-test-eval-v3
- **PID 443221**: ALIVE (since 08:46 UTC, ~2h running)
- **GPU**: cuda:3
- **Progress**: 6288/9784 (64.3%)
- **Running accuracy**: 65.3% (new=1001, resumed=5287)
- **Rate**: ~57 sec/batch (8 samples)
- **Remaining**: 3496 samples → ~6.9 hours
- **ETA**: ~17:40 UTC

### cwm8b-ckpt400-test-eval-shard2
- **PID 448100**: ALIVE (since 09:25 UTC, ~1h19m running)
- **GPU**: cuda:1
- **Range**: idx 7680–9784 (2104 samples)
- **Progress**: 680/2104 (32.3%), latest idx 8359
- **Rate**: ~56 sec/batch (8 samples)
- **Remaining**: 1424 samples → ~2.8 hours
- **ETA**: ~13:30 UTC

### cwm8b-ckpt400-test-eval-shard3
- **PID 453335**: ALIVE (since 10:37 UTC, ~7 min running)
- **GPU**: cuda:0
- **Range**: idx 6200–7680 (1480 samples)
- **Progress**: 48/1480 (3.2%), latest idx 6247
- **Rate**: ~60 sec/batch (8 samples)
- **Remaining**: 1432 samples → ~3.0 hours
- **ETA**: ~13:45 UTC

### repo-level-cwm-8b-conda-v5 (training)
- **PID 400279**: DEAD
- **Status**: Training finished or crashed (PID gone)
- **Last checkpoint**: checkpoint-6100 (saved May 16 07:53 UTC)
- **Checkpoint history**: 5800 → 5900 → 6000 → 6100 (~40 min/100 steps)
- **Note**: GPU 2 is now idle — training was on cuda:2

## Shard Coverage Map
```
Index:  0 -------- 6200 ---- 7680 ---- 9784
v3:     [=========================>........]  6288/9784
shard3:               [=>.................]  48/1480
shard2:                        [========>.]  680/2104
```
Shards 2+3 will complete the 6200–9784 range (~13:45 UTC) well before v3 reaches it (~17:40 UTC).

## Idle GPUs
- **GPU 2** (RTX 5090, 32GB) — fully idle, available for new work

## Summary
- 3 eval jobs running healthy on GPUs 0/1/3
- Training on GPU 2 ended (last ckpt: 6100); GPU 2 free
- Full test eval (9784 samples) ETA: shards finish ~13:45 UTC, v3 full sweep ~17:40 UTC
