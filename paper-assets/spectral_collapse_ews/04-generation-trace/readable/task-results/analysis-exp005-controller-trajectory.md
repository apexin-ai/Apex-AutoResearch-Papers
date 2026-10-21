# analysis exp005 controller trajectory

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp005-controller-trajectory_20260517T190910_result.json`
- **Structured JSON:** [`1f381598c1fbb4b44351.json`](../../sessions/1f/1f381598c1fbb4b44351.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全。现在根据源码手动重建 controller 轨迹。

## 完整 Controller 数据轨迹 (exp_005, Gen 0-3)

### 配置参数

| 参数 | 值 |
|------|-----|
| signal | log_det |
| signal_mode | per_gen |
| tau | 0.002 |
| k | 20.0 |
| r_base | 0.50 |
| r_min | 0.20 |
| r_max | 0.80 |
| alpha_ema | 0.5 |
| total_budget | 5.0 (= 10 gens × 0.50) |
| T (total_generations) | 10 |

### 评估指标表

| Gen | log_det | eff_rank | ppl | distinct4 | train_loss |
|-----|---------|----------|-----|-----------|------------|
| 0 | 2366.682861328125 | 417.5472106933594 | 9.553585720044504 | 0.7414389763779528 | — |
| 1 | 2366.46484375 | 476.93048095703125 | 10.094571790418478 | 0.660757874015748 | 1.9863090271759034 |
| 2 | 2395.23291015625 | 486.8538513183594 | 10.423844428836501 | 0.6148799212598425 | 1.8810884401130676 |
| 3 | 2425.44921875 | 496.11138916015625 | 10.759529530959501 | 0.43998622047244096 | 1.7803794955730439 |

### Controller 决策轨迹

| Gen | 决策方式 | S_t (log_det) | S_tilde (EMA) | S_tilde_prev | delta | triggered | r (mix_ratio) | B_rem |
|-----|---------|---------------|---------------|--------------|-------|-----------|---------------|-------|
| 0 | set_baseline | 2366.6829 | — | — | — | — | — | 5.0 |
| 1 | get_first_gen_ratio | — | — | 2366.6829 | — | False | 0.5 | 4.5 |
| 2 | update(Gen1) | 2366.4648 | 2366.5739 | 2366.6829 | +0.00004605 | False | 0.5 | 4.0 |
| 3 | update(Gen2) | 2395.2329 | 2380.9034 | 2366.5739 | -0.006054 | False | 0.5 | 3.5 |

### Delta 计算详解

**per_gen 模式公式：** `delta = (S_tilde_prev - S_tilde_new) / |S_tilde_0|`

**S_tilde_0 (baseline) = 2366.682861328125** (Gen 0 设定，不再变化)

**Gen 1:** `get_first_gen_ratio()` 直接返回 `r_base=0.5`，不使用 spectral 信号。

**Gen 2 (输入 Gen 1 的 log_det=2366.4648):**
```
S_tilde = 0.5 × 2366.4648 + 0.5 × 2366.6829 = 2366.5739
delta   = (2366.6829 - 2366.5739) / 2366.6829 = 0.1090 / 2366.6829 = +0.00004605
triggered = 0.00004605 > 0.002 → False
r_raw   = 4.5/9 + 20 × max(0, 0.00004605 - 0.002) = 0.5 + 0 = 0.5
```

**Gen 3 (输入 Gen 2 的 log_det=2395.2329):**
```
S_tilde = 0.5 × 2395.2329 + 0.5 × 2366.5739 = 2380.9034
delta   = (2366.5739 - 2380.9034) / 2366.6829 = -14.3295 / 2366.6829 = -0.006054
triggered = -0.006054 > 0.002 → False
r_raw   = 4.0/8 + 20 × max(0, -0.006054 - 0.002) = 0.5 + 0 = 0.5
```

### 为什么 Controller 从未触发

**根本原因：log_det 在上升，不在下降。**

- Gen 0 → 1: log_det 几乎不变 (2366.68 → 2366.46, 变化 -0.22)
- Gen 1 → 2: log_det 上升 (+28.77)
- Gen 2 → 3: log_det 继续上升 (+30.22)

per_gen 模式下 `delta = (S_tilde_prev - S_tilde_new) / |S_tilde_0|`：
- 正 delta = spectral 信号恶化（谱坍缩）
- 负 delta = spectral 信号改善（谱扩展）

Gen 2 的 delta 仅 +0.000046（远小于 tau=0.002），Gen 3 的 delta 为负值 (-0.006)，意味着 log_det 在增长，谱空间在扩张而非坍缩。Controller 的触发条件 `delta > tau` 从未满足。

**但值得注意的是**：distinct-4 从 0.741 暴跌到 0.440（-40.6%），输出多样性在显著退化，而 log_det 不但没有检测到这一退化，反而显示谱在"改善"。这说明 log_det 作为 spectral collapse 的早期预警信号，在这种设置下未能捕捉到实际的 diversity collapse。

---
