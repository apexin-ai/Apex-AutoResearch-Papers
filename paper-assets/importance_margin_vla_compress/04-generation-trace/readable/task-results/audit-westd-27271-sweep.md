# audit westd 27271 sweep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd-27271-sweep_20260521T150230_result.json`
- **Structured JSON:** [`726b44201c657cc81be5.json`](../../sessions/72/726b44201c657cc81be5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### GPU 状态
| GPU | 型号 | 显存使用 | 利用率 |
|-----|------|---------|--------|
| 0 | RTX PRO 6000 Blackwell | 15.6 / 95.6 GB | 70% |
| 1 | RTX PRO 6000 Blackwell | 41.2 / 95.6 GB | 0% |

### 1. eval_openvla_l2norm_k05_object_seed43 — **仍在运行** (GPU0)
- PID 250599, 已运行约 15 小时
- 当前进度: **Task 5/10**, 约 50% 完成
- 速度: ~1.8 eps/min, 预计还需 ~2.5 小时

已完成 task 的 SR:
| Task | SR |
|------|----|
| 1. butter | 56.0% (28/50) |
| 2. cream cheese | 14.0% (7/50) |
| 3. salad dressing | 38.0% (19/50) |
| 4. bbq sauce | 32.0% (16/50) |
| 5. ketchup | 进行中 (23/30) |

### 2. train_openvla_sc_m32_vtconly_seed42 — **仍在运行** (GPU1)
- PID 921279, 已运行 1 天 4 小时 15 分
- tmux session `train_openvla_sc_m32_seed42` 存活
- GPU1 利用率 0% 可能是当前在做 data loading 或 checkpoint 保存间隙

### Registry 更新
Eval 尚未完成，不更新 registry。等 10 个 task 全部跑完后再收集最终 SR。

---
