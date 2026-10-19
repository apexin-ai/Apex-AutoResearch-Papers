# investigate pi05 regression root cause

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_pi05-regression-root-cause_20260528T063031_result.json`
- **Structured JSON:** [`a915bdac978bd00e8f63.json`](../../sessions/a9/a915bdac978bd00e8f63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。以下是完整汇报。

---

## 汇报

### Part A: bjb1-18228 + cqa1-32758 GPU 状态

**bjb1-18228（4× RTX 4090）：**
| GPU | 占用 | 进程 |
|-----|------|------|
| 0 | 12757MiB | PID 982389 → `pi05-crm-always-on-long-s43` |
| 1 | 1MiB | 空闲 |
| 2 | 12757MiB | PID 983106 → `pi05-crm-always-on-long-s44` |
| 3 | 1MiB | 空闲 |

两个 session 日志均显示 **obs_dim=2048** ✓，SR 正常（85-95%/task），无 regression。**不需要 kill。**

**cqa1-32758（6× RTX 4090D）：**
- 6 张 GPU 全部被占（4017MiB ×3, 3807MiB ×2, 5849MiB ×1）
- tmux sessions: `eval-supp-*`、`smolvla-adapt-*` — **无 Pi05 进程**

---

### Part B: Regression 来源分析

**结论：obs_dim=960 在 VLA-only 模式下是红鲱鱼，不是导致 SR=0% 的原因。**

- **来源**：`src/utils.py:20` 硬编码 `OBS_DIM = 960`（SmolVLA hidden_size），`evaluate.py:93` 用它做 argparse default
- CRM 模式的启动脚本显式传 `--obs_dim 2048 --unified_obs_dim 2088`，所以 CRM 不受影响
- VLA-only 模式不传 `--obs_dim`，所以 args 里显示 960——**但 obs_dim 只在 CRM 构造时使用，VLA-only 不加载 CRM，所以对推理无影响**
- 证据：多个 VLA-only 实验 obs_dim=960 但 SR=94-100%
- **376 missing keys** 是 PaliGemma vision tower 的 lm_head/projector/language_model keys，在所有 Pi05 实验中都出现（包括 CRM obs_dim=2048 的），是正常行为

**Pi05 VLA-only 首次运行 SR=0% 的真实原因：**
- `pi05-vla-only-object-s42-4090`：OOM（GPU 碰撞，另一个进程占了 12.43GB）
- `pi05-vla-only-goal-s42-4090`：SR=0% (0/200) 完整跑完但全部失败——原因是当时的代码 bug（r2 同样 obs_dim=960 但 SR=98%）

---

### Part C: Table 2 旧 Pi05 s42 数据验证

**CRM always-on s42（cqa1-32758）— 全部安全 ✅**

| 实验 | obs_dim | SR | EXIT_CODE |
|------|---------|-----|-----------|
| pi05-crm-always-on-object-s42 | 2048 | **90.5%** | 0 |
| pi05-crm-always-on-spatial-s42 | 2048 | **96.0%** | 0 |
| pi05-crm-always-on-goal-s42 | 2048 | **81.5%** | 0 |
| pi05-crm-always-on-long-s42 | 2048 | **77.0%** | 0 |

所有 4 个 CRM always-on 实验 obs_dim=2048，无异常 missing keys（376 vision tower keys 是正常的），SR 合理非零，Table 2 数据安全。

**VLA-only baselines（bjb1-18228）— r2/r3 版本安全 ✅**

| 实验 | obs_dim (args) | SR | 状态 |
|------|---------------|-----|------|
| pi05-vla-only-object-s42-4090 | 960 | OOM | ❌ GPU碰撞 |
| pi05-vla-only-object-s42-4090-**r2** | 960 | **100.0%** | ✅ 可用 |
| pi05-vla-only-spatial-s42-4090-**r2** | 960 | **98.0%** | ✅ 可用 |
| pi05-vla-only-goal-s42-4090 | 960 | 0.0% | ❌ 代码bug |
| pi05-vla-only-goal-s42-4090-**r2** | 960 | **98.0%** | ✅ 可用 |
| pi05-vla-only-long-s42-4090-**r3** | 960 | **94.0%** | ✅ 可用 |
| pi05-vla-only-long-s43-4090 | 960 | **95.5%** | ✅ |
| pi05-vla-only-long-s44-4090 | 960 | **95.5%** | ✅ |
| eval-pi05-vla-only-goal-seed42-r4 | 960 | **98.0%** | ✅ |
| eval-pi05-vla-only-long-seed43-r4 | 960 | **95.5%** | ✅ |
| eval-pi05-vla-only-long-seed44-r4 | 960 | **95.5%** | ✅ |

**总结**：Table 2 所有 Pi05 数据安全。obs_dim=960 是 argparse default 显示问题，不影响 VLA-only 推理。使用 r2+ 版本的 VLA-only 结果即可。建议在 `evaluate.py` 中当 `--model pi05` 时自动将 obs_dim override 为 2048 以消除日志中的混淆。

---
