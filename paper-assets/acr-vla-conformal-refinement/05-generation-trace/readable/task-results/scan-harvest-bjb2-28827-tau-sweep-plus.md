# scan harvest bjb2 28827 tau sweep plus

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_scan-harvest_bjb2-28827-tau-sweep-plus_20260523T171942_result.json`
- **Structured JSON:** [`6c0cc6b9f4acdbd43794.json`](../../sessions/6c/6c0cc6b9f4acdbd43794.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

---

## τ-sweep 结果 (Goal s42)

| τ | SR | trigger_rate | 结论 |
|---|-----|-------------|------|
| 0.10 | 81.0% | 73.9% | 过度触发，低于 baseline (83.5%) |
| 0.15 | **85.0%** | 33.9% | 最佳平衡点，匹配 always-on |
| 0.25 | 84.0% | 8.3% | 已知 |
| 0.40 | 83.5% | 1.2% | 几乎不触发，≈baseline |
| always-on | 85.5% | 100% | 已知 |

## Long s42 结果 (baseline VLA-only=58.0%)

| method | SR |
|--------|-----|
| Reconvla K=10 | 56.5% (-1.5pp) |
| Adaptive τ=0.25 | **59.0%** (+1.0pp, trigger=3.9%) |
| CRM norm=0.05 | 56.5% (-1.5pp) |

## 新部署 (bjb2-28827)

| GPU | exp_id | PID |
|-----|--------|-----|
| cuda:0 | eval-supp-adapt-tau025-obj-s45 | 849131 |
| cuda:1 | eval-supp-adapt-tau025-obj-s46 | 849395 |
| cuda:2 | eval-supp-obj-vla-only-s45 | 849667 |
| cuda:3 | eval-supp-long-reconvla-s44 | 849677 |
| cuda:4 | eval-supp-long-vla-only-s43 | 849946 |
| cuda:5 | eval-supp-long-k2mean-s44 | 850410 |

**空闲 GPU：无（6/6 已部署）**

---
