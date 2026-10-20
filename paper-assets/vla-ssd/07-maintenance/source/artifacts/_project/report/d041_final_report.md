# D041 Final Report: unified_rsa_results.json 权威数据集

## n_demos 确认

所有主条件（with_inst, random_s0, shuffled）+ standalone baselines = **50 demos/task**，直接可比。
no_inst 有 minor 不一致（4-5 个 task 仅 10 demos），不影响主表。

## Paper 主数值表（Method B, 50 demos/task）

| Model | RSA | 条件 |
|-------|-----|------|
| DINO cls | 0.692 | standalone |
| VLA trained last_preaction peak (L12) | 0.6425 | unified |
| Fused 2176d | 0.634 | branch-split |
| DINO patch_mean | 0.631 | standalone |
| VLA trained image_mean peak (L12) | 0.6282 | unified |
| VLA untrained last_preaction peak (L1) | 0.6262 | unified |
| SigLIP branch | 0.621 | branch-split |
| DINOv2 branch | 0.619 | branch-split |
| SigLIP projector | 0.615 | standalone |
| VLA untrained image_mean peak (L0) | 0.6117 | unified |
| CLIP patch_mean | 0.557 | standalone |

## Per-layer Curves

### Trained image_mean (all 33 layers)
L0:0.612 L1:0.612 L2:0.612 L3:0.613 L4:0.614 L5:0.615 L6:0.618 L7:0.620
L8:0.619 L9:0.620 L10:0.620 L11:0.617 L12:0.628 L13:0.627 L14:0.624 L15:0.617
L16:0.613 L17:0.609 L18:0.607 L19:0.607 L20:0.604 L21:0.596 L22:0.572 L23:0.556
L24:0.546 L25:0.535 L26:0.516 L27:0.514 L28:0.513 L29:0.497 L30:0.440 L31:0.433
L32:0.422

### Untrained image_mean (all 33 layers)
L0:0.612 L1:0.571 L2:0.560 L3:0.560 L4:0.558 L5:0.558 L6:0.559 L7:0.557
L8:0.555 L9:0.553 L10:0.551 L11:0.551 L12:0.550 L13:0.550 L14:0.549 L15:0.549
L16:0.550 L17:0.550 L18:0.550 L19:0.550 L20:0.549 L21:0.549 L22:0.550 L23:0.550
L24:0.549 L25:0.548 L26:0.548 L27:0.547 L28:0.546 L29:0.545 L30:0.545 L31:0.545
L32:0.545

### Trained last_preaction (all 33 layers)
L0:NaN L1:0.568 L2:0.582 L3:0.588 L4:0.589 L5:0.584 L6:0.562 L7:0.543
L8:0.547 L9:0.568 L10:0.558 L11:0.599 L12:0.643 L13:0.640 L14:0.637 L15:0.635
L16:0.630 L17:0.626 L18:0.623 L19:0.619 L20:0.616 L21:0.609 L22:0.606 L23:0.600
L24:0.595 L25:0.586 L26:0.581 L27:0.582 L28:0.581 L29:0.579 L30:0.572 L31:0.570
L32:0.584

### Untrained last_preaction (all 33 layers)
L0:NaN L1:0.626 L2:0.621 L3:0.616 L4:0.612 L5:0.608 L6:0.605 L7:0.603
L8:0.601 L9:0.601 L10:0.598 L11:0.597 L12:0.595 L13:0.594 L14:0.593 L15:0.594
L16:0.594 L17:0.595 L18:0.595 L19:0.595 L20:0.594 L21:0.594 L22:0.593 L23:0.592
L24:0.591 L25:0.591 L26:0.590 L27:0.589 L28:0.588 L29:0.589 L30:0.588 L31:0.587
L32:0.587

## Trained vs Untrained Bootstrap CI

### Best-vs-best
- image_mean: Δ=+0.017, CI=[-0.0002, +0.035], p=0.026, NOT significant
- last_preaction: Δ=+0.016, CI=[+0.0001, +0.031], p=0.025, MARGINAL

### Same-layer L12
- image_mean: Δ=+0.079, CI=[+0.060, +0.099], p<0.0001, SIGNIFICANT
- last_preaction: Δ=+0.047, CI=[+0.024, +0.071], p<0.0001, SIGNIFICANT

## Instruction Control (4 conditions, image_mean, trained)

| Condition | Best Layer | Peak RSA |
|-----------|-----------|----------|
| normal | 12 | 0.6282 |
| empty | 13 | 0.6225 |
| random_s0 | 12 | 0.6283 |
| shuffled | 12 | 0.6282 |

## D040 Status
D040 (provisional) superseded by D041. L9-only 10-demo "readout RSA training degradation" was non-peak artifact.
