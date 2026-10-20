# Factorial Data Summary (2026-05-26)

> 论文 deadline May 29. 本文档整理 2×2 factorial (BN×Gradient) 所有可用数据。
> **核心约束**: v1/v2 代码不等价（D050），只有 v2 数据可跨 cell 比较。

---

## 表 A: V2 代码 — 已完成数据（可用于 ANOVA）

### Per-seed metrics

| Cell | Condition | Seed | Exp ID (registry) | TSR | CAR |
|------|-----------|------|--------------------|-----|-----|
| 1 | Full OCC BN (Grad ON + BN) | 42 | full_occ_retrain_s0_eval_v2 | 0.802 | 0.746 |
| 2 | Full OCC LN (Grad ON + LN) | 42 | full_occ_ln_s0_eval | 0.930 | 0.766 |
| 2 | Full OCC LN (Grad ON + LN) | 43 | full_occ_ln_s1 | 0.894 | 0.718 |
| 2 | Full OCC LN (Grad ON + LN) | 44 | full_occ_ln_s2 | 0.866 | 0.744 |
| 3 | Detach BN (Grad OFF + BN) | 42 | detach_bn_v2_s0_eval | 0.870 | 0.774 |
| 3 | Detach BN (Grad OFF + BN) | 43 | detach_bn_v2_s1_eval | 0.926 | 0.736 |
| 3 | Detach BN (Grad OFF + BN) | 44 | detach_bn_v2_s2_eval | 0.914 | 0.762 |
| 4 | Detach LN (Grad OFF + LN) | 42 | detach_ln_s0_eval | 0.914 | 0.792 |
| 4 | Detach LN (Grad OFF + LN) | 43 | detach_ln_s1_eval | 0.906 | 0.756 |
| 4 | Detach LN (Grad OFF + LN) | 44 | detach_ln_s2_eval | 0.884 | 0.748 |

D051 Cell 3 已完成：3-seed v2 data replaces provisional retrain data. ablation_occ_detach_s0_retrain_eval (CAR=0.754) 与 detach_bn_v2_s0 (CAR=0.774) 差异 2pp，同方向。

### V2 Cell 均值

| Cell | Condition | n | CAR mean±std | TSR mean±std |
|------|-----------|---|-------------|-------------|
| 1 | Full OCC BN | 1 | 0.746 | 0.802 |
| 2 | Full OCC LN | 3 | 0.743 ± 0.024 | 0.897 ± 0.032 |
| 3 | Detach BN | 3 | 0.757 ± 0.019 | 0.903 ± 0.029 |
| 4 | Detach LN | 3 | 0.765 ± 0.023 | 0.901 ± 0.016 |

V2 Vanilla baseline: vanilla_retrain_s0_eval (seed 42) TSR=0.882, CAR=0.768 (n=1)

---

## 表 B: 在跑实验 + 完成后预期覆盖

### RUNNING 实验（registry 查询结果）

| Exp ID | Cell | Seed | Server | GPU | Retry |
|--------|------|------|--------|-----|-------|
| full_occ_bn_v2_s1 | 1 (Full OCC BN) | 43 | **34685** | **cuda:3** | 3 |
| detach_bn_v2_s0 | 3 (Detach BN) | 42 | 34685 | cuda:0 | 0 |
| detach_bn_v2_s1 | 3 (Detach BN) | 43 | 34685 | cuda:1 | 1 |
| detach_bn_v2_s2 | 3 (Detach BN) | 44 | 34685 | cuda:2 | 1 |
| cutoff_45k_s2_v2 | dose-response | 44 | 10894 | cuda:0 | 0 |
| mvp_occ_s3_v2 | 1 (Full OCC BN) | 45 | 10894 | cuda:1 | 0 |
| full_occ_ln_s3_v2 | 2 (Full OCC LN) | 45 | 10894 | cuda:2 | 0 |
| ablation_occ_detach_s3_v2 | 3 (Detach BN) | 45 | 10894 | cuda:3 | 0 |

s3 实验全部从头训练（v2 代码），ETA ~10:40 UTC May 26。

### 全部完成后的 V2 Factorial 覆盖

| Cell | Condition | 当前 n | D051后 n | s3后 n | Seeds |
|------|-----------|--------|---------|--------|-------|
| 1 | Full OCC BN | 1 | **2** | **3** | s0(42)✅, s1(43)🔄D051, s3(45)🔄10894 |
| 2 | Full OCC LN | 3 | 3 | **4** | s0(42)✅, s1(43)✅, s2(44)✅, s3(45)🔄10894 |
| 3 | Detach BN | 0 | **3** | **4** | s0(42)🔄D051, s1(43)🔄D051, s2(44)🔄D051, s3(45)🔄10894 |
| 4 | Detach LN | 3 | 3 | 3 | s0(42)✅, s1(43)✅, s2(44)✅ |

**D051 后 (11 obs)**: Cell 1=2, Cell 2=3, Cell 3=3, Cell 4=3. 不均衡，残差 df=7，功效 <30%。
**s3 后 (14 obs)**: Cell 1=3, Cell 2=4, Cell 3=4, Cell 4=3. 更均衡，功效显著提升 → **确认性 ANOVA**。

---

## 论文 Table 1 草稿

### 当前可填写版本（v2 only）

| Condition | Gradient | Norm | n | CAR | TSR |
|-----------|----------|------|---|-----|-----|
| Full OCC + BN | ON | BN | 1 | 0.746 | 0.802 |
| Full OCC + LN | ON | LN | 3 | 0.743 ± 0.024 | 0.897 ± 0.032 |
| Detach + BN | OFF | BN | 0 | — | — |
| Detach + LN | OFF | LN | 3 | 0.765 ± 0.023 | 0.901 ± 0.016 |
| Vanilla | — | — | 1 | 0.768 | 0.882 |

### 预期完整版（当前 RUNNING 全部完成后）

| Condition | Gradient | Norm | n | CAR | TSR |
|-----------|----------|------|---|-----|-----|
| Full OCC + BN | ON | BN | **2** | TBD | TBD |
| Full OCC + LN | ON | LN | 3 | 0.743 ± 0.024 | 0.897 ± 0.032 |
| Detach + BN | OFF | BN | 3 | TBD | TBD |
| Detach + LN | OFF | LN | 3 | 0.765 ± 0.023 | 0.901 ± 0.016 |
| Vanilla | — | — | 1 | 0.768 | 0.882 |

---

## 缺口分析

| 问题 | 严重性 | 解决方案 |
|------|--------|---------|
| Cell 1 (Full OCC BN) 完成后仅 2 seeds | **高** | 需再跑 1 seed (~14h+3h) |
| Cell 3 (Detach BN) 0 seeds 完成 | **高** | 3 个在跑，预计 ~12h 后完成 |
| Vanilla baseline 仅 1 v2 seed | 中 | v1 3-seed 可辅助 (0.780±0.012) |
| full_occ_ln s1/s2 eval 不在 registry | 低 | 数据在 memory.md，需确认或补录 |

---

## 附录: V1 数据（内部一致性，不可跨版本比较）

### Full OCC BN (v1) — 50r eval

| Seed | Exp ID | TSR | CAR |
|------|--------|-----|-----|
| 42 | mvp_occ_s0 | 0.904 | 0.832 |
| 43 | occ_s1_fresh (50K) | 0.938 | 0.788 |
| **Mean (3-seed, memory)** | | | **0.797** |

v1→v2 代码版本效应 (seed 42): CAR -8.6pp (0.832→0.746), TSR -10.2pp (0.904→0.802)

### Detach BN (v1) — 50r eval

| Seed | Exp ID | TSR | CAR |
|------|--------|-----|-----|
| 42 | ablation_occ_detach_s0 | 0.914 | 0.746 |
| 43 | ablation_occ_detach_s1 | 0.898 | 0.744 |
| 44 | ablation_occ_detach_s2 | 0.624 | 0.748 |

s2 TSR=0.624 异常；v1 detach 实现不可验证（0 行 OCC/AUX 日志）

### Vanilla (v1) — 50r eval

| Seed | Exp ID | TSR | CAR |
|------|--------|-----|-----|
| 42 | mvp_vanilla_s0 | 0.900 | 0.788 |
| 43 | mvp_vanilla_s1 | 0.918 | 0.766 |
| 44 | mvp_vanilla_s2 | 0.904 | 0.786 |
| **Mean** | | **0.907 ± 0.009** | **0.780 ± 0.012** |

### Random OCC (v1) — 50r eval

| Seed | Exp ID | TSR | CAR |
|------|--------|-----|-----|
| 42 | ablation_random_occ_s0 | 0.856 | 0.814 |
| 43 | ablation_random_occ_s1 | 0.902 | 0.798 |
| 44 | ablation_random_occ_s2 | 0.848 | 0.754 |
| **Mean** | | **0.869 ± 0.029** | **0.789 ± 0.031** |

### Dose-response cutoff@35K (v1) — 50r eval

| Seed | Exp ID | TSR | CAR |
|------|--------|-----|-----|
| 42 | cutoff_s0_eval | 0.912 | 0.768 |
| 43 | cutoff_s1_eval | 0.918 | 0.798 |
| 44 | cutoff_s2_v2_eval | 0.970 | 0.770 |
| **Mean** | | **0.933 ± 0.032** | **0.779 ± 0.017** |

### Dose-response 其他条件 (v1, 部分 multi-seed)

| Condition | Seeds | TSR | CAR |
|-----------|-------|-----|-----|
| cutoff@15K s0 | 42 | 0.912 | 0.804 |
| cutoff@15K s1 | 43 | 0.854 | 0.760 |
| cutoff@25K s0 | 42 | 0.844 | 0.688 |
| cutoff@25K s1 | 43 | 0.930 | 0.760 |
| cutoff@45K s0 | 42 | 0.896 | 0.764 |
| reverse (35K-50K) s0 | 42 | 0.788 | 0.700 |
| reverse (35K-50K) s1 | 43 | 0.890 | 0.736 |

### Retrain v2 对照

| Condition | Seed | Exp ID | TSR | CAR | Code |
|-----------|------|--------|-----|-----|------|
| Full OCC BN | 42 | full_occ_retrain_s0_eval_v2 | 0.802 | 0.746 | v2 |
| Detach BN | 42 | ablation_occ_detach_s0_retrain_eval | 0.944 | 0.754 | v2 |
| Vanilla | 42 | vanilla_retrain_s0_eval | 0.882 | 0.768 | v2 |
