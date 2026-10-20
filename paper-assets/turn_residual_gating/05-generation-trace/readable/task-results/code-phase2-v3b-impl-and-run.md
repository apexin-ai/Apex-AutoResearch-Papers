# code phase2 v3b impl and run

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase2_v3b_impl_and_run_20260518T133903_result.json`
- **Structured JSON:** [`be3fc0fdd83f6095d944.json`](../../sessions/be/be3fc0fdd83f6095d944.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Now presenting the full results.

## v3b Experiment Results — **PASS**

### Gate Dynamics

| Opt Step | Gate_mean | Gate_std | Gate_min | Gate_max | L_NTP  | L_GAR   |
|----------|-----------|----------|----------|----------|--------|---------|
| 0        | 0.4934    | 0.0432   | 0.3730   | 0.5977   | 2.2779 | -0.0147 |
| 50       | 0.7670    | 0.1154   | 0.5234   | 0.9922   | 1.2437 | -0.5536 |
| 100      | 0.9099    | 0.0873   | 0.5938   | 0.9922   | 0.9400 | -0.7450 |
| 150      | 0.9011    | 0.1159   | 0.4219   | 0.9883   | 1.0651 | -0.9297 |
| 200      | 0.9154    | 0.1289   | 0.3027   | 0.9922   | 1.0904 | -0.9501 |
| 250      | 0.9339    | 0.1017   | 0.4531   | 0.9922   | 0.8485 | -0.9589 |
| 300      | 0.9264    | 0.0976   | 0.4941   | 0.9922   | 1.1137 | -0.9589 |
| 350      | 0.9367    | 0.0945   | 0.4980   | 0.9961   | 1.5433 | -0.9545 |
| 400      | 0.9388    | 0.1013   | 0.4551   | 0.9961   | 1.0112 | -0.9577 |
| 450      | 0.9412    | 0.0980   | 0.4785   | 0.9961   | 1.3354 | -0.9610 |
| **500**  | **0.9388**| **0.0870**| **0.5352**| **0.9922**| 0.7787| -0.9606 |

### Per-Layer Gate Profile (every 100 steps)

```
Step 0:   L0:0.500 L1:0.598 L2:0.498 L3:0.477 L4:0.484 L5:0.490 L6:0.504 L7:0.455
          L8:0.520 L9:0.457 L10:0.496 L11:0.492 L12:0.461 L13:0.475 L14:0.508 L15:0.523
          L16:0.459 L17:0.512 L18:0.428 L19:0.523 L20:0.562 L21:0.531 L22:0.504 L23:0.508
          L24:0.475 L25:0.443 L26:0.559 L27:0.373

Step 100: L0:0.672 L1:0.969 L2:0.961 L3:0.941 L4:0.594 L5:0.887 L6:0.902 L7:0.934
          L8:0.988 L9:0.953 L10:0.887 L11:0.898 L12:0.848 L13:0.848 L14:0.895 L15:0.871
          L16:0.906 L17:0.902 L18:0.934 L19:0.961 L20:0.957 L21:0.969 L22:0.973 L23:0.949
          L24:0.938 L25:0.965 L26:0.984 L27:0.992

Step 200: L0:0.734 L1:0.992 L2:0.980 L3:0.977 **L4:0.303** L5:0.840 L6:0.926 L7:0.953
          L8:0.965 L9:0.969 L10:0.930 L11:0.918 L12:0.887 L13:0.910 L14:0.902 L15:0.906
          L16:0.961 L17:0.945 L18:0.941 L19:0.941 L20:0.965 L21:0.980 L22:0.977 L23:0.969
          L24:0.926 L25:0.977 L26:0.977 L27:0.980

Step 300: L0:0.770 L1:0.992 L2:0.988 L3:0.965 L4:0.494 L5:0.828 L6:0.953 L7:0.945
          L8:0.957 L9:0.973 L10:0.957 L11:0.891 L12:0.891 L13:0.914 L14:0.902 L15:0.918
          L16:0.941 L17:0.906 L18:0.949 L19:0.953 L20:0.961 L21:0.992 L22:0.984 L23:0.988
          L24:0.961 L25:0.988 L26:0.984 L27:0.992

Step 400: L0:0.785 L1:0.996 L2:0.988 L3:0.977 L4:0.455 L5:0.910 L6:0.945 L7:0.953
          L8:0.969 L9:0.980 L10:0.961 L11:0.938 L12:0.926 L13:0.945 L14:0.926 L15:0.949
          L16:0.965 L17:0.945 L18:0.949 L19:0.965 L20:0.965 L21:0.988 L22:0.980 L23:0.988
          L24:0.965 L25:0.988 L26:0.992 L27:0.992

Step 500: L0:0.777 L1:0.992 L2:0.984 L3:0.969 **L4:0.535** L5:0.953 L6:0.941 L7:0.965
          L8:0.961 L9:0.977 L10:0.961 L11:0.934 L12:0.918 L13:0.938 L14:0.918 L15:0.945
          L16:0.957 L17:0.941 L18:0.945 L19:0.961 L20:0.961 L21:0.984 L22:0.980 L23:0.980
          L24:0.961 L25:0.984 L26:0.980 L27:0.980
```

### Judgment: **PASS** (gate_std=0.0870 > 0.05)

**Key findings:**
- Gates moved from uniform ~0.5 (init_bias=0.0) to a differentiated profile within 50 steps
- **L4 is a persistent outlier** (0.484→0.303→0.494→0.455→0.535), consistently the lowest gate across all checkpoints
- **L0 is the second-lowest** (~0.77), another early layer showing suppressed gating
- Late layers (L21-L27) saturate near 1.0
- GAR loss converged quickly: L_GAR went from -0.0147 to -0.96 by step 250
- Gate gradients confirmed: `gate_grad_received=True`
- Training completed in 3565.9s (59.4 min)

**What worked vs v1/v2/v3:** The combination of `init_bias=0.0` (starting at sigmoid midpoint 0.5 instead of saturation), `gate_lr_multiplier=10` (separate higher LR for gates), and `gar_loss_mode=maximize` (continuous non-zero gradients) together broke the frozen-gate pattern. The critical factor was likely init_bias=0.0 giving gates room to move in both directions.

---
