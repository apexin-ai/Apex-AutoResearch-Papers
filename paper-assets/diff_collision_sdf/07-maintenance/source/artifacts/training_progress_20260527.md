# Training Progress Report — 2026-05-27 ~01:45 UTC

## Summary

All 6 experiments **alive**, all GPUs at **100% utilization**, ~27GB VRAM each. No OOM, NaN, or loss spikes.

---

## westd-35807 (conda: libero)

### 1. train_pi05_a1_spatial_bowl_s0_l005 (cuda:0, PID 3708)
| Metric | Value |
|--------|-------|
| Step | **26374 / 30000 (88%)** |
| Speed | 4.64 s/it |
| Uptime | 23h46m |
| Loss | 0.016 (action=0.016, sdf=0.032, ee=0.007) |
| ETA | **~06:30 UTC May 27 (~5h)** |

**No resume needed.** Speed improved from estimated 9s/it to 4.64s/it. Will complete in ~5h.

### 2. train_pi05_a1_obj_s0_l01_high (cuda:1, PID 271266)
| Metric | Value |
|--------|-------|
| Step | **18100 / 30000 (60%)** |
| Speed | 4.62 s/it |
| Uptime | 18h35m |
| Loss | 0.019 (action=0.015, sdf=0.035, ee=0.006) |
| ETA | **~17:00 UTC May 27 (~15h)** |

### 3. train_pi05_a1_obj_s1_l01_high (cuda:2, PID 274407)
| Metric | Value |
|--------|-------|
| Step | **17573 / 30000 (59%)** |
| Speed | 4.63 s/it |
| Uptime | 17h56m |
| Loss | 0.017 (action=0.014, sdf=0.037, ee=0.007) |
| ETA | **~17:45 UTC May 27 (~16h)** |

### 4. train_spatial_bowl_lora_control_s0 (cuda:3, PID 341425, tmux: plan015)
| Metric | Value |
|--------|-------|
| Step | **7825 / 30000 (26%)** |
| Speed | 4.62 s/it |
| Uptime | 5h20m |
| Loss | 0.024 (action only, no SDF head) |
| ETA | **~06:15 UTC May 28 (~28.5h)** |

---

## westd-45947 (conda: base)

### 5. train_pi05_lora_baseline_s2 (cuda:0, PID 78558)
| Metric | Value |
|--------|-------|
| Step | **15497 / 30000 (52%)** |
| Speed | 4.60 s/it |
| Uptime | 15h11m |
| Loss | 0.015 (action only, no SDF head) |
| ETA | **~20:15 UTC May 27 (~18.5h)** |

### 6. train_pi05_a1_obj_s2_l01_high (cuda:1, PID 425058)
| Metric | Value |
|--------|-------|
| Step | **5847 / 30000 (19%)** |
| Speed | 4.60 s/it |
| Uptime | 2h48m |
| Loss | 0.035 (action=0.031, sdf=0.034, ee=0.012) |
| ETA | **~08:40 UTC May 28 (~31h)** |

Phase 1 ran at ~1.2 s/it (steps ~3400), transitioned to ~4.6 s/it (Phase 2 LoRA unfreeze).

---

## λ=0.1 Seed Comparison

| Seed | Step | Progress | Loss (action) | Loss (sdf) | ETA |
|------|------|----------|---------------|------------|-----|
| s0 | 18100 | 60% | 0.015 | 0.035 | May 27 17:00 |
| s1 | 17573 | 59% | 0.014 | 0.037 | May 27 17:45 |
| s2 | 5847 | 19% | 0.031 | 0.034 | May 28 08:40 |

s0 and s1 tracking closely (~1% apart). s2 started much later — loss will converge.

---

## Alerts

- **spatial_bowl SDF**: Finishing in ~5h. No resume needed.
- **No anomalies**: All GPUs 100%, no OOM/NaN/loss spikes.
- **Completion order**: spatial_bowl SDF → obj_s0 ≈ obj_s1 → lora_baseline_s2 → spatial_bowl_lora → obj_s2
