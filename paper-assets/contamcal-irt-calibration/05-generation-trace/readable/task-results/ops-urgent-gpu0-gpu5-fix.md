# ops urgent gpu0 gpu5 fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_gpu0_gpu5_fix_20260514T010616_result.json`
- **Structured JSON:** [`826866145e0180187b44.json`](../../sessions/82/826866145e0180187b44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都找到了 HumanEval 本地缓存，正在继续执行：
- **GPU 2** (0.5B d000_s123): HumanEval 12/164, ~5s/it → 约 **13 min** 后完成释放
- **GPU 1** (0.5B d000_s42): HumanEval 18/164, ~7s/it → 约 **17 min** 后释放（但 3B eval 仍占 ~9GB）

---

## 产出清单

### 1. ✅ GPU 0 僵尸 kill + 确认
- PID 248703 已 kill，GPU 0 显存 0 MiB → 已释放

### 2. ✅ exp_001_sft_d100_15B → FAILED
- `conclusion=failed`，`notes` 已写入 OOM 详情
- status 从 PREPARING → QUEUED（状态机限制无法直接跳到 DONE）

### 3. ✅ exp_001_sft_d100_15B_v2 已在 GPU 0 训练
- tmux session `exp_001_sft_d100_15B_v2` 运行中
- GPU 0 占用 10053 MiB，batch_size=1, grad_accum=16
- 进度: 4/4159 steps, ~3.3s/it，预计 **~3.8h** 完成
- Registry: hypothesis + parent 已设置

### 4. ❌ exp_001_sft_d005_15B 无法提交到 GPU 5
- **GPU 5 被 eval_15B_d000_s123 占用**（GSM8K 3%，预计还需 ~3h+）
- Registry entry 已创建，hypothesis 已设置
- **需等 GPU 5 释放后再提交**，或改用其他 GPU

### 5. GPU 1/2 eval 状态 + 下一批 eval
- GPU 1: 0.5B d000_s42 HumanEval **~17 min** 后完成；3B d000_s42 eval 仍在跑
- GPU 2: 0.5B d000_s123 HumanEval **~13 min** 后完成 → **GPU 2 将空闲**
- GPU 4: 1.5B d000_s42 eval 运行中
- GPU 5: 1.5B d000_s123 eval 运行中（GSM8K 阶段，~3h 剩余）
- **0.5B d100 和 d005 checkpoint 均已就绪**，GPU 2 释放后可立即提交 contaminated model eval
- 优先：`exp_001_eval_05B_d100` → GPU 2（~13 min 后），`exp_001_eval_05B_d005` → GPU 1 0.5B eval 释放后（~17 min 后，与 3B eval 共用 GPU 1）

---
