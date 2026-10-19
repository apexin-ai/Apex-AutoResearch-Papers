# analyze westd pi05 vla only object paired

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_westd-pi05-vla-only-object-paired_20260526T115819_result.json`
- **Structured JSON:** [`7d46dd90cf61989bf251.json`](../../sessions/7d/7d46dd90cf61989bf251.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。Registry 已更新 checkpoint_path 和 log_path。

## π0.5 VLA-only Object Baseline (westd Blackwell, 10 tasks × 20 rollouts)

| Seed | Success Rate | 失败 task |
|------|-------------|-----------|
| 42 | **99.5%** | bbq_sauce 19/20 |
| 43 | **100.0%** | 无 |
| 44 | **99.5%** | bbq_sauce 19/20 |

**Mean ± Std: 99.7% ± 0.3%**

## 与 registry 中其他 π0.5 Object 结果对比

| 实验 | Server | Mode | Success Rate |
|------|--------|------|-------------|
| westd VLA-only (本次) | westd-49937 (Blackwell) | vla_only | **99.7 ± 0.3%** |
| westd Adaptive Conformal s42 | westd-49937 (Blackwell) | adaptive_conformal_crm | 83.5% |
| 4090 Adaptive Conformal s42 | cqa1 (4090) | adaptive_conformal_crm | 85.5% |
| 4090 Adaptive Object s43 | bjb2-24035 (4090) | adaptive_conformal_crm | 83.0% |

π0.5 VLA-only 在 Object suite 上接近完美（仅 bbq_sauce 偶发失败），Adaptive Conformal 在该 suite 上反而降低约 15pp — 对于 near-ceiling baseline，correction 引入的扰动大于收益。

---
