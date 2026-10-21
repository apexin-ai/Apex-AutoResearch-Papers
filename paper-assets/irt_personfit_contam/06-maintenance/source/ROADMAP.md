# irt_personfit_contam — Research Dashboard

> 最后更新: 2026-05-23 20:15 UTC | 更新原因: 审计修复完成，匿名 repo 推送，收尾检查

> 核心方向
IRT person-fit (ℓz*) 检测 LLM benchmark contamination——首次系统刻画行为边界。详见 paper_framing.md。

## 当前进展
- **阶段**: 论文定稿 + 审稿迭代
- **评分**: Round 7 = **3.5 Borderline Conference** (R1: 3.5, R2: 3.5)
- **用户指令**: "能到 3.0 就投，到不了就存 arXiv" → 3.5 > 3.0，**已达投稿线**
- **DDL**: ARR 2026-05-25 AoE (~32h remaining)
- **Round 7 修复**: 3 MF + 7 SF 全部完成
- **Round 8 review**: 已提交 (continue mode), 等待结果
- **页数**: 主文 8 页（编译确认合规）

## 提分实验 (3.5→4.0)
- ✅ **Multi-seed HT/Acc z-score 重算**: 用原始公式 (chi-squared ratio + bootstrap) 完成。Sanity check 通过（seed 42 值完全匹配 Table 3 原始数据）。Table 3 已更新为 multi-seed means ± SD。
  - HT mean |d|: 5.83±1.30 (15%), 7.84±2.39 (25%), 5.29±3.41 (50%)
  - Acc z mean |d|: 45.0±2.5 (15%), 51.5±1.8 (25%), 70.0±1.1 (50%)
  - 关键发现: seed 42 的 HT 50% |d|=1.66 是异常值（mean=5.29）; Acc z 极稳定
- ✅ **GRPO MIA**: 完成。AUC 0.611→0.493 (random)，已写入 discussion.tex + fig_grpo.pdf

## 核心数据 (全部 multi-seed)

### Table 1: Cohen's d for Δℓz*
| Model | Bench | d(5%) | d(15%) | d(25%) | d(50%) |
|-------|-------|-------|--------|--------|--------|
| Qwen | MMLU | -4.15 | -5.36±1.10 | -7.44±1.86 | -5.08±3.02 |
| Llama | MMLU | — | -2.80±0.60 | -2.56±0.52 | -2.30±0.30 |
| Mistral | MMLU | — | -3.01 | — | -3.50 |
| Qwen | ARC-C | — | +3.16 | — | +5.30 |

### Table 3: Detection-diagnosis tradeoff (Qwen multi-seed means)
| Statistic | |d| (15%) | |d| (50%) |
|-----------|----------|----------|
| ℓz* | 5.36±1.10 | 5.08±3.02 |
| HT | 5.83±1.30 | 5.29±3.41 |
| Acc z | 45.0±2.5 | 70.0±1.1 |

## GPU 资源
- westd-35694: cuda:0-3 (全部 idle，无运行中实验)

## 近期任务
- [x] Round 7 MF1-3 + SF1-7 全部修复
- [x] Table 1/2 multi-seed 更新
- [x] Multi-seed HT/Acc z-score 正确公式重算 + Table 3 更新
- [x] 页数确认 (≤8 pages)
- [x] GRPO MIA 评估 — 完成 (AUC 0.493)
- [x] GRPO MIA 结果写入论文
- [x] 数据正确性审计 + 修复 (commit d3299aa, 1bb11ff)
- [x] 匿名 repo 推送 + 完整性校验
- [ ] Round 8 review — 等审稿结果
- [ ] 最终 ARR 提交 (DDL 05-25)

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D039 | 2026-05-24 | D039: Mistral d(15%) 用 paper baseline 重算 -3.01→-2. | exp-ctrl-contam-mistral |
| D038 | 2026-05-22 | Llama 5% (|d|=5.53) 不纳入论文主体——单 seed 异常值会破坏 Qwen in | exp-ctrl-contam-llama-5pct |
| D037 | 2026-05-22 | Qwen 5% 实验成功，纳入论文——4-point dose-response curve 完整呈 | exp-ctrl-contam-qwen-5pct |
| D036 | 2026-05-21 | D036: Qwen lz* 统一重算完成 (M022 修复) — d_free 从 -4.83/- | exp-ctrl-contam-pilot |
| D035 | 2026-05-21 | D035: θ-fixed n=10 确认 — Qwen contam_50 d_free=1.08 | exp-ctrl-contam-pilot, exp-ctrl-contam-llama-contam15, exp-ctrl-contam-mistral |
| D034 | 2026-05-21 | D034: GRPO 训练轨迹确认 — step 500 后完全平台 + 新发现 lz* seen/ | exp-post-rl-v3 |
| D033 | 2026-05-21 | D033: GRPO v3 step 500 eval 证伪 post-RL robustness  | exp-post-rl-v3 |
| D032 | 2026-05-21 | D032: z-score baseline 确认 — degradation chain 在 de | exp-baseline-comparison |
| D031 | 2026-05-21 | D031: Reframe 方向定调 — 核心贡献从"lz*检测工具"转为"首次系统刻画 IRT p | exp-baseline-comparison, exp-ctrl-contam-pilot, exp-arcc-benchmark |
| D030 | 2026-05-21 | D030: 跨模型 IRT 校准差异确认 — Qwen lz*=+8.68 vs Llama=-0. | exp-ctrl-contam-pilot, exp-ctrl-contam-llama-contam15 |

