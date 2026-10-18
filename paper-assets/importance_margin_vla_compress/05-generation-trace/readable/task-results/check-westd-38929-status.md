# check westd 38929 status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-38929-status_20260522T015359_result.json`
- **Structured JSON:** [`8a0062e19e2d796ba095.json`](../../sessions/8a/8a0062e19e2d796ba095.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 10047/97887 MiB | 0% |
| 1-3 | ~1/97887 MiB | 0% |

### 实验状态

| exp_id | PID | 状态 | Suite | Prune | Keep | SR(%) | 备注 |
|--------|-----|------|-------|-------|------|-------|------|
| pi05_l2norm_k09_spatial_seed42 | 48423 | ✅ DONE | spatial | l2norm | 0.90 | **95.0%** | 确认，与 ROADMAP 一致 |
| pi05_random_k09_spatial_seed42 | 9126 | ✅ DONE | spatial | random | 0.90 | **54.6%** | 确认，与 ROADMAP 一致 |
| pi05_random_k085_spatial_seed42 | 48588 | ✅ DONE | spatial | random | 0.85 | **58.4%** | 新结果 |
| pi05_random_k0925_object_seed43 | 68029 | ✅ DONE | object | random | 0.925 | **30.0%** | 新结果 |
| pi05_l2norm_k085_spatial_seed42 | 227008 | 🔄 RUNNING | spatial | l2norm | 0.85 | ~96% (T0-T1) | 刚启动 13min，T0=98%, T1=94% |
| openvla_l2norm_k05_object_v4 | 999560 | ❌ CRASH | object | l2norm | 0.50 | — | ImportError: HF hub 版本冲突 |
| oft_baseline_goal_seed42 | 466583 | ❌ KILLED | goal | — | — | 0% | EXIT_CODE=143, 全 FAIL |
| oft_object_std_v3 | 465264 | ❌ KILLED | object | — | — | 0% | EXIT_CODE=143, 全 FAIL |

### 新结果详情

**pi05_random_k0.85_spatial (SR=58.4%)**
| Task | SR |
|------|-----|
| T0: bowl between plate & ramekin | 76% |
| T1: bowl next to ramekin | 62% |
| T2: bowl from table center | 86% |
| T3: bowl on cookie box | 4% |
| T4: bowl in top drawer | 62% |
| T5: bowl on ramekin | 32% |
| T6: bowl next to cookie box | 44% |
| T7: bowl on stove | 76% |
| T8: bowl next to plate | 88% |
| T9: bowl on wooden cabinet | 54% |

**pi05_random_k0.925_object_seed43 (SR=30.0%)**
| Task | SR |
|------|-----|
| T0: alphabet soup | 48% |
| T1: cream cheese | 44% |
| T2: salad dressing | 26% |
| T3: bbq sauce | 16% |
| T4: ketchup | 8% |
| T5: tomato sauce | 54% |
| T6: butter | 46% |
| T7: milk | 14% |
| T8: chocolate pudding | 18% |
| T9: orange juice | 26% |

### 关键观察
- **l2norm vs random 差距巨大**：spatial k=0.9 → l2norm 95.0% vs random 54.6%（差 40.4pp）
- **random pruning 在 spatial 上 k=0.85 (58.4%) 反而优于 k=0.9 (54.6%)**，可能是随机性波动
- **OFT baseline 在 goal/object 上全 0%**，已被杀掉
- **OpenVLA v4 实验因 HF hub 版本冲突崩溃**，需修环境后重跑
- **l2norm_k085_spatial 正在运行**，前两个 task 表现优秀 (98%/94%)，GPU 0 上

---
