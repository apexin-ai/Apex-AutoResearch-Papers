# ICML 2026 Data Lockdown Audit

**日期**: 2026-05-26 | **锁定日期**: 2026-05-27 | **投稿**: 2026-05-29
**实验总数**: 184 (92 success / 41 negative / 2 running / 3 queued / 46 other)

---

## 1. Claim → 实验覆盖表

| Claim | 状态 | 关键实验 | 环境覆盖 | Seeds | 数据可用 |
|-------|------|----------|----------|-------|----------|
| **C1: Variable-rate degradation** | ✅ Strong | exp_006 (dt=2), exp_007 (dt=4), exp_005 (learned gate), exp_078/091 (Cheetah) | Walker + Cheetah | 多 seed | 全部完成 |
| **C2: Trained dt_emb → CIVO susceptibility** | ✅ Strong | Walker: 008d(s0), 009e(s1), 009b(s2), 059(s5), 008d_s3, 008d_s4 — 5/5 onset; Cheetah: 078(s0), 091(s2) onset, 088(s1) no onset — 2/3; Controls: frozen 0/11, removed 0/8 | Walker + Cheetah | Walker 5/5, Cheetah 2/3, Controls 0/19 | 完成 (Fisher p&lt;0.0001) |
| **C3: Untrained dt_emb protection** | ⚠️ Walker strong, Cheetah partial | Walker: 008a(s0) 778@105K=85% BL, unexposed_s1/s2; Cheetah: unexposed_s0/s1 | Walker ✅ + Cheetah ✅(unexposed) | Walker 3, Cheetah 2 (unexposed) | **exp_100 RUNNING — Walker 2nd proper seed** |
| **C4: Longer dt amplifies** | ✅ Moderate | exp_006 (dt=2), exp_007 (dt=4), baseline (dt=1) | Walker only | 1 seed per dt | 完成 |
| **C5: Horizon/subsample secondary** | ✅ Moderate | 008c vs 008a (H=8 vs H=15), 008e_v3 | Walker | 多 seed | 完成 |
| **C6: dt=1 imag partial falsification** | ✅ Moderate | 008e_v3_s1 (success), 008e_v3_s2 (collapse, non-CIVO pathway); D152 clarified | Walker | 4 seeds (current code) | 完成 |
| **C7: SGS failure / gradient decoupling** | ✅ Strong | 016e, 018/021, 025/026; 17 seeds, 1/17 CIVO-free. Removal 5/5 | Walker + Cheetah | 17 seeds | 完成 |
| **C8: Intervention Hierarchy** | ✅ Moderate | TCN 2/10, RAVE 0/2, SGS 1/17, Dual-critic (factorial). 7 methods × 3 levels × 3 envs | Walker + Cheetah + PickCube | 多 seed | 完成 |

---

## 2. 数据缺口清单（按优先级）

### P0 — 锁定前必须确认

| 缺口 | 影响 | 当前状态 | Action |
|------|------|----------|--------|
| **exp_097 完成确认** (Cheetah 008d s3) | C2 Cheetah onset rate: 3/4 or 维持 2/3 | RUNNING @65K, CIVO onset @45K (NVE=2.3) | 等待完成 → NVE 分析 → 更新 C2 |
| **exp_100 完成确认** (Walker 008a s1) | C3 Walker proper 008a 第2 seed | RUNNING, 无 metrics 更新 | 等待完成 → NVE 分析 → 确认 value suppression |

### P1 — 应完成（有替代）

| 缺口 | 影响 | 替代 | Action |
|------|------|------|--------|
| **RSSM fidelity v3 Cheetah** | 论文 Table 1 Cheetah 行 | Walker v3 独立可用；Cheetah 旧数字可注明版本 | 需 exp_097 checkpoint |
| **RSSM v3 Walker+Cheetah 合并表** | 数字一致性 | Walker v3 单独可用 | CPU 任务 |

### P2 — 有则更好，缺不致命

| 缺口 | 影响 | 替代 |
|------|------|------|
| **exp_102/103** (Cheetah 008a proper) | C3 Cheetah 补充 | **已有 008a_cheetah_unexposed_s0/s1 (success)**，核心机制一致 |
| **C4 finer dt grid** | 强化 monotonic | 2 个 dt 值足够 supporting claim |
| **Distributional value analysis** | 回应 R3 | exp_064 初步分析已有 |

---

## 3. 运行中实验时间线

| 实验 | 提交 | 预计完成 | 进度 |
|------|------|---------|------|
| exp_097 (Cheetah 008d s3, cuda:0) | 05-26 03:18 UTC | **~10:00 UTC** | @65K/105K (62%), CIVO onset confirmed |
| exp_100 (Walker 008a s1, cuda:1) | 05-26 03:38 UTC | **~10:00 UTC** | 进行中 |

### exp_102/103 可行性

- GPU 释放预计 05-26 ~10:00 UTC
- 每实验 3-5h，并行 2 卡可完成
- 锁定窗口 ~14h → **可行但非必须**（已有 unexposed 数据）

---

## 4. 已有但尚未整合进论文的分析

| 分析 | 状态 | 优先级 | 说明 |
|------|------|--------|------|
| **RSSM fidelity v3 (Walker)** | ✅ 完成 | P0 | worker_analysis_rssm_standardized_v3 已完成，需更新论文 Table 1 |
| **NVE V2 组合诊断 (D155)** | ✅ 完成 | P1 | 三维标准(peak+持续性+时序因果)，AUROC=0.989, N=61 |
| **D152/D153 008e_v3 bug clarification** | ✅ 决策完成 | P1 | 旧 CIVO 由 gate_max_dt=8 bug 导致，C6 当前代码 0/4 |
| **D156 stochastic onset** | ✅ 已更新 paper_framing | P0 | trained dt_emb 必要非充分 |
| **Cheetah v3 RSSM fidelity** | 🔄 等待 exp_097 | P1 | 需 checkpoint |
| **exp_101 RSSM prediction quality** | ❌ Killed | 放弃 | 服务器迁移中断 |

---

## 5. 风险评估

### 🟢 低风险 — 核心 claims 数据充分

- **C1, C2, C7** 最强：多环境多 seed + 完备控制实验
- C2 necessity: 0/19 controls vs 7/8 trained onset → Fisher p&lt;0.0001
- C7: 1/17 SGS seeds CIVO-free, removal 5/5
- C8: 7 methods × 3 levels 完整
- NVE AUROC=0.989 已锁定

### 🟡 中风险

| 风险 | 概率 | 影响 | 缓解 |
|------|------|------|------|
| exp_097/100 未在锁定前完成 | 低 | C2 Cheetah 维持 2/3; C3 Walker 维持已有 seeds | 已有数据足够 |
| RSSM v3 Cheetah 缺失 | 中 | Table 1 仅 Walker v3 | 注明版本差异 |
| exp_102/103 不完成 | 高 | C3 Cheetah 用 unexposed 配置 | unexposed 核心机制一致 |

### 🔴 高风险 — 无

8/8 Claims 均有已完成实验数据支撑。

---

## 6. 锁定前 Action Items

### 必须完成

1. **[~4h等待]** exp_097 + exp_100 完成
2. **[30min]** exp_097 → NVE 分析 → 更新 C2 Cheetah onset
3. **[30min]** exp_100 → NVE 分析 → 确认 C3 value suppression
4. **[1h]** exp_097 checkpoint → Cheetah RSSM v3 → 合并表
5. **[30min]** 论文 RSSM 数字用 v3 替换
6. **[30min]** paper_framing 数字交叉验证
7. **[可选]** GPU 释放后提交 exp_102/103

### 锁定确认清单

- [ ] exp_097 final metrics
- [ ] exp_100 final metrics
- [ ] RSSM v3 数字锁定
- [ ] C2 Cheetah onset rate 最终确认
- [ ] 论文数字交叉验证
- [ ] 声明数据锁定

---

## 7. 总结

**覆盖率**: 8/8 claims 有完成实验支撑

**最强证据链**: C2 necessity (0/19 controls vs 7/8 trained, p&lt;0.0001) → C7 SGS failure (1/17) → C8 Hierarchy (TCN 2/10 唯一成功且 fragile)

**最弱环节**: C4 仅 2 dt 值 (supporting claim); C3 Cheetah 用 unexposed 配置

**结论**: 论文核心叙事的实验证据链完整。锁定前主要任务是确认 2 个 RUNNING 实验并更新数字，非填补证据缺口。
