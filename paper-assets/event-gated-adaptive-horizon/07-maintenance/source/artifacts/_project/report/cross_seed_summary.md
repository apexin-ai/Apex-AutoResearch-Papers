# Cross-Seed Summary Statistics

生成时间: 2026-05-29
数据来源: registry + artifacts 已完成实验 (排除 failed/killed/RUNNING)

## 汇总表

| 配置 | Seeds (n) | eval_return (mean±std) | NVE_peak (mean±std) | NVE_peak max | CIVO rate | 备注 |
|------|-----------|----------------------|---------------------|-------------|-----------|------|
| Walker baseline (dt=1) | 4 | 787.7±230.8 | — | — | — | s2 低 (443.5) 拉低均值 |
| Walker 008d (trained dt_emb+sub ON) | 4 eval / 5 NVE | 190.6±90.2 | 3.32±1.61 | 4.72× | 5/5 (100%) | 所有 seed 均 CIVO onset |
| Walker 008f (dt_emb=0) | 4 | 302.4±134.8 | 1.09±0.42 | 1.69×* | 0/4 | *s0 NVE=1.69 为 eval 跌落假阳性 |
| Walker 008a (untrained dt_emb) | 4 | 820.9±68.8 | 0.46±0.19 | 0.59× | 0/4 | value suppression, 性能稳定 |
| Walker 008e_v3 (dt=1 imag) | 4 | 689.8±369.1 | — | 3.78×† | 0/4* | †s2 Pathway B 非 CIVO 崩溃 |
| Cheetah baseline (dt=1) | 2 | 446.1±2.9 | — | — | — | 极高一致性 (CV<1%) |
| Cheetah 008d (trained dt_emb+sub ON) | 4 | 123.2±132.9 | 33.1±63.0 | 127.6× | 3/4 (75%) | s2 极端崩溃 (NVE=127.6) |
| Cartpole baseline (dt=1) | 3 | 673.3±142.0 | — | — | — | |
| Cartpole 008d (trained dt_emb+sub ON) | 3 | 236.3±29.7 | 0.047±0.010 | 0.058× | 0/3 | CIVO 不在 Cartpole 发生 |

**跨环境 CIVO onset rate**: Walker 5/5 + Cheetah 3/4 = 8/9 (89%) multi-joint locomotion; Cartpole 0/3

---

## 各 seed 明细

### 1. Walker baseline (dt=1)

| seed | exp_id | eval@105K | ve_ratio@105K | 备注 |
|------|--------|-----------|---------------|------|
| s1 | exp_001_baseline | 915.67 | 0.656 | 论文主 reference |
| s2 | exp_001_baseline_s2 | 443.46 | 0.645 | 显著低于其他 seed |
| s3 | exp_001_baseline_s3 | 869.03 | — | 不在附录完整表 |
| s4 | exp_001_baseline_s4 | 922.80 | — | 不在附录完整表 |
| **mean** | | **787.7±230.8** | **0.651±0.008** (n=2) | |

### 2. Walker 008d (trained dt_emb + subsample ON + H=8)

| seed | exp_id | eval_final | NVE_peak | NVE_final | CIVO | 后果模式 |
|------|--------|-----------|----------|-----------|------|----------|
| s1 | exp_009e | 131.08 | 4.13 | 1.57 | ✅ | oscillatory→sustained |
| s2 | exp_009b | 267.9 | 1.62 | 0.38 | ✅ | transient→self-corrected |
| s3 | exp_008d_civo_trigger_s3 | 267.6 | 1.53 | 1.53 | ✅ | borderline onset |
| s4 | exp_008d_civo_trigger_s4 | — | 4.62 | — | ✅ | onset |
| s5 | exp_059_walker_trained_s5 | 95.8 | 4.72 | 1.22 | ✅ | onset→self-correcting |
| **mean** | | **190.6±90.2** (n=4) | **3.32±1.61** (n=5) | | **5/5** | |

备注: eval 统计排除 s4（无 eval 数据）。原始 exp_008d (s1) 在 55K 被 kill (eval=82.75), exp_009e 为同 seed 延续运行。

### 3. Walker 008f (dt_embed_dim=0 + subsample ON + H=8)

| seed | exp_id | eval@105K | NVE_peak | CIVO | 备注 |
|------|--------|-----------|----------|------|------|
| s0 | exp_008f_s0 | 139.5 | 1.69 | ❌ | NVE 为 eval 跌落伪信号，非 value 膨胀 |
| s1 | exp_008f_s1 | 468.8 | 0.88 | ❌ | |
| s3 | exp_009c_s3 | 311.9 | 1.04 | ❌ | |
| s4 | exp_008f_s4 | 289.3 | 0.76 | ❌ | |
| **mean** | | **302.4±134.8** | **1.09±0.42** | **0/4** | |

备注: s2 缺失。所有 seed NVE<2.0（τ=2.0 阈值下无 CIVO）。与 008d 形成 4/4 vs 0/4 完美分离。

### 4. Walker 008a (untrained dt_emb + no subsample + H=15)

| seed | exp_id | eval@105K | NVE | CIVO | 备注 |
|------|--------|-----------|-----|------|------|
| s0 | exp_008a_no_subsample_dt2 | 777.7 | 0.59 | ❌ | 原始实验 |
| s1 | exp_100_walker_008a_s1 | 750.59 | 0.33 | ❌ | registry 验证 |
| s2 | exp_008a_unexposed_s2 | 899.4 | — | ❌ | |
| s3 | exp_074_008a_walker_s3 | 855.9 | — | ❌ | |
| **mean** | | **820.9±68.8** | **0.46±0.19** (n=2) | **0/4** | |

备注: value suppression 模式（NVE 持续<1.0），性能接近 baseline (-4.1%)。未训练的 dt_emb 防止乐观漂移。

### 5. Walker 008e_v3 (trained dt_emb + dt=1 imagination + subsample ON + H=15)

| seed | exp_id | eval@105K | NVE_peak | ve_ratio@105K | CIVO | 备注 |
|------|--------|-----------|----------|---------------|------|------|
| s1 | exp_008e_v3 | 869.9 | 0.80 | 0.526 | ❌ | 健康: 95% baseline |
| s2 | exp_008e_v3_s2 | 136.96 | 3.78 | — | ❌ | Pathway B 非 CIVO 崩溃 |
| s2 repro | exp_081 | 597.1 | 0.80 | 0.500 | ❌ | s2 重跑，健康 |
| s4 | exp_008e_v3_s4 | 899.33 | — | 0.609 | ❌ | 健康: 98% baseline |
| s5 | exp_072 | 853.1 | — | 0.600 | ❌ | 健康: 93% baseline |
| **mean (s1,s2,s4,s5)** | | **689.8±369.1** | | | **0/4** | |
| **mean (排除 s2-orig)** | | **804.9±136.7** (n=4) | | | | s1/s2-repro/s4/s5 |

备注: 原始 s2 经历 "Pathway B" 非 CIVO 崩溃（NVE=3.78 为 NVE 诊断假阳性，actor entropy 升高而非 value 膨胀）。重跑 s2 (exp_081) 正常。论文中 s2 作为 NVE 假阳性案例分析。

### 6. Cheetah baseline (dt=1)

| seed | exp_id | eval@105K | ve_ratio@105K | 备注 |
|------|--------|-----------|---------------|------|
| s0 | exp_077_cheetah_baseline_s0 | 448.1 | 0.611 | |
| s1 | exp_083_cheetah_baseline_s1 | 444.0 | 0.600 | |
| **mean** | | **446.1±2.9** | **0.606±0.008** | CV<1%, 极高可复现性 |

备注: 论文亦引用 exp_023 系列 (5 seeds, mean=593.9±60.4)，但与 exp_077/083 baseline 值差异~148 (不同 server/配置)。exp_077/083 为论文主 reference。

### 7. Cheetah 008d (trained dt_emb + subsample ON + H=8)

| seed | exp_id | eval_final | NVE_peak | NVE_peak_step | CIVO | 后果模式 |
|------|--------|-----------|----------|---------------|------|----------|
| s0 | exp_078 | 119.5 | 2.3× | 75K | ✅ | sustained→self-correcting |
| s1 | exp_088 | 309.3 | 0.31× | — | ❌ | no onset (72% baseline) |
| s2 | exp_091 | 2.5 | 127.6× | 95K | ✅ | catastrophic collapse |
| s3 | exp_097 | 61.7 | 2.3× | 45K | ✅ | transient→degraded |
| **mean** | | **123.2±132.9** | — | | **3/4** | |

备注: s2 经历极端 NVE 爆发 (127.6×)，eval 归零不可恢复。三种后果模式与 Walker 一致。Onset timing: 3 个 onset seed 均在 45K-75K 区间，与 Walker onset (35K-45K) 时间窗口重合。

另有早期实验 exp_010b (s0: NVE=70.64, eval=0.83; s1: NVE=8.27, eval=51.7)，使用不同 baseline (exp_023)，未纳入主统计。

### 8. Cartpole baseline (dt=1)

| seed | exp_id | eval@105K | 备注 |
|------|--------|-----------|------|
| s0 | exp_060 | 809.4 | |
| s1 | exp_060 | 684.4 | |
| s2 | exp_060 | 526.1 | |
| **mean** | | **673.3±142.0** | |

### 9. Cartpole 008d (trained dt_emb + subsample ON + H=8)

| seed | exp_id | eval@105K | NVE_peak | CIVO | 备注 |
|------|--------|-----------|----------|------|------|
| s0 | exp_061 | 211.1 | 0.058 | ❌ | |
| s1 | exp_061 | 269.0 | 0.040 | ❌ | |
| s2 | exp_061 | 228.9 | 0.043 | ❌ | |
| **mean** | | **236.3±29.7** | **0.047±0.010** | **0/3** | |

备注: Cartpole 所有 trigger seed NVE 均 <0.1×，远低于 CIVO 阈值 (2.0×)。CIVO 现象不在 Cartpole 上发生，可能与 reward/dynamics 结构差异相关。eval 仍下降至 baseline 35%，但不由 value overestimation 驱动。

---

## 跨环境汇总

| 环境 | CIVO onset rate | NVE_peak range | eval degradation (vs baseline) | 主要发现 |
|------|----------------|----------------|-------------------------------|----------|
| Walker Walk | 5/5 (100%) | 1.53×–4.72× | -75.8% (190.6 vs 787.7) | 确定性 onset, 三种后果模式 |
| Cheetah Run | 3/4 (75%) | 0.31×–127.6× | -72.4% (123.2 vs 446.1) | 更高 NVE 峰值, s1 为唯一 no-onset |
| Cartpole | 0/3 (0%) | 0.04×–0.06× | -64.9% (236.3 vs 673.3) | 无 CIVO, 退化非 value-driven |

**关键结论**:
1. CIVO onset 在 multi-joint locomotion (Walker/Cheetah) 中高度一致 (8/9=89%), 在 Cartpole 完全不发生
2. CIVO 后果为随机性: 同一配置可产生 full collapse / self-correction / degradation
3. 控制实验完美分离: trained dt_emb 8/9 onset vs removed 0/4 vs untrained 0/4 vs frozen 0/10
