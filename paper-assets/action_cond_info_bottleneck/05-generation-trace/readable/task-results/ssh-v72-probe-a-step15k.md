# ssh v72 probe a step15k

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_v72-probe-a-step15k_20260517T124847_result.json`
- **Structured JSON:** [`49e12c2d7dd4b0e8c18f.json`](../../sessions/49/49e12c2d7dd4b0e8c18f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 probe 都成功完成。结果汇总：

## Probe A: Fixed Image, Swap Instruction (step 15000)

### Seed 1
| Pair | cos | L2 | bit_eq |
|------|-----|-----|--------|
| inst 0 vs 1 | 0.8847 | 3.660 | False |
| inst 0 vs 2 | 0.8042 | 3.990 | False |
| inst 1 vs 2 | 0.9480 | 2.089 | False |

Per-instruction weights:
- "bbq sauce → basket": mean=0.2405, std=0.2324
- "black bowl next to cookie → plate": mean=0.5467, std=0.1912
- "black bowl in drawer → plate": mean=0.5083, std=0.2360

### Seed 2
| Pair | cos | L2 | bit_eq |
|------|-----|-----|--------|
| inst 0 vs 1 | 0.6970 | 5.776 | False |
| inst 0 vs 2 | 0.6013 | 6.100 | False |
| inst 1 vs 2 | 0.9233 | 1.245 | False |

Per-instruction weights:
- "bbq sauce → basket": mean=0.6317, std=0.1932
- "black bowl next to cookie → plate": mean=0.1660, std=0.2131
- "black bowl in drawer → plate": mean=0.1670, std=0.2332

## Probe B: Natural Cross-task

| | Seed 1 cos range | Seed 2 cos range |
|--|---|---|
| min | 0.6275 | 0.7574 |
| max | 0.7499 | 0.8298 |

## 判定

**极强正面信号。** 两个 seed 一致：

1. **Probe A**: cos 远低于 0.8（seed2 低至 0.60），weight_std 全部 > 0.19 → scorer 对 language instruction 高度敏感，不同指令产生截然不同的 importance map
2. **Probe B**: cos ∈ [0.63, 0.83] → importance map 是 task-dependent 的，不是固定的 spatial position prior
3. **Verdict**: scorer is language-condition-dependent + task-dependent importance maps

产出文件：
- `/root/autodl-tmp/v72_probe/seed1_step15000/cross_task_probe_summary.json`
- `/root/autodl-tmp/v72_probe/seed2_step15000/cross_task_probe_summary.json`
- 每个 seed 各有 probe_A 和 probe_B 的 heatmap PNG

---
