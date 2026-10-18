# ops healthcheck westd41074 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_healthcheck-westd41074-v2_20260524T093538_result.json`
- **Structured JSON:** [`e5cb05dfce9253a7658c.json`](../../sessions/e5/e5cb05dfce9253a7658c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总：westd-41074 全 4 卡空闲，所有实验已完成

| GPU | 实验 ID | Status | SR | Episodes | 结果文件 |
|-----|---------|--------|-----|----------|----------|
| 0 | eval_pi05_random_k0925_object_seed42_postfix | **COMPLETED** (17:04 today) | **27.2%** | 500 (136 succ) | `eval_results/pi05_random_k0.93_libero_object_seed42.json` |
| 1 | eval_pi05_random_k0925_goal_seed42_v3 | **COMPLETED** (16:26 today) | **70.0%** | 500 (350 succ) | `eval_results/pi05_random_k0.93_libero_goal_seed42.json` |
| 2 | eval_pi05_random_k095_spatial_seed42_postfix_v2 | **COMPLETED** (16:28 today) | **76.8%** | 500 (384 succ) | `eval_results/pi05_random_k0.95_libero_spatial_seed42.json` |
| 3 | eval_pi05_l2norm_k085_goal_seed42_postfix | **COMPLETED** | **87.4%** | 500 (437 succ) | `eval_results/pi05_l2norm_k0.85_libero_goal_seed42.json` |

### Per-task breakdown

**GPU 0 — Random k=0.925 Object (SR=27.2%)**
| Task | SR |
|------|-----|
| T0 alphabet soup | 30% |
| T1 cream cheese | 36% |
| T2 salad dressing | 22% |
| T3 bbq sauce | 28% |
| T4 ketchup | 8% |
| T5 tomato sauce | 44% |
| T6 butter | 48% |
| T7 milk | 20% |
| T8 chocolate pudding | 16% |
| T9 orange juice | 20% |

**GPU 1 — Random k=0.925 Goal (SR=70.0%)**
| Task | SR |
|------|-----|
| T0 open middle drawer | 68% |
| T1 bowl on stove | 52% |
| T2 wine bottle on cabinet | 58% |
| T3 open drawer + bowl inside | 64% |
| T4 bowl on top cabinet | 94% |
| T5 push plate | 88% |
| T6 cream cheese in bowl | 88% |
| T7 turn on stove | 96% |
| T8 bowl on plate | 86% |
| T9 wine bottle on rack | 6% |

**GPU 2 — Random k=0.95 Spatial (SR=76.8%)**
| Task | SR |
|------|-----|
| T0 between plate & ramekin | 100% |
| T1 next to ramekin | 86% |
| T2 table center | 88% |
| T3 on cookie box | 64% |
| T4 top drawer wooden cabinet | 50% |
| T5 on ramekin | 80% |
| T6 next to cookie box | 92% |
| T7 on stove | 76% |
| T8 next to plate | 94% |
| T9 on wooden cabinet | 38% |

**GPU 3 — L2norm k=0.85 Goal (SR=87.4%)**
| Task | SR |
|------|-----|
| T0 open middle drawer | 90% |
| T1 bowl on stove | 92% |
| T2 wine bottle on cabinet | 98% |
| T3 open drawer + bowl inside | 84% |
| T4 bowl on top cabinet | 100% |
| T5 push plate | 94% |
| T6 cream cheese in bowl | 88% |
| T7 turn on stove | 100% |
| T8 bowl on plate | 84% |
| T9 wine bottle on rack | 44% |

### 额外发现（tmux session 中完成的旧实验）
- `smolvla_spatial` session: SmolVLA official spatial baseline = **55.0%** (110/200, 20eps/task)
- `xvla_long` session: xVLA l2norm k=0.9 libero_10 = **27.5%** (55/200, 20eps/task)

### 硬件状态
- 4× NVIDIA RTX PRO 6000 Blackwell (96GB each)
- 全部 idle (0% util, 0 MiB VRAM)
- 磁盘: 数据盘 86% (213G/250G) — 偏满，注意空间

---
