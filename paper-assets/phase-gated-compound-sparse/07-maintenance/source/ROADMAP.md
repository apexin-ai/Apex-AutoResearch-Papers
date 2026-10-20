# phase-gated-compound-sparse — Research Dashboard

> 最后更新: 2026-05-17 UTC | 更新原因: GPU 全部切换至 GPQA Diamond 实验 + Blocking Checklist 更新

> 核心文档链: paper_framing.md → experiment_plan.yaml → 本 ROADMAP

## 核心方向
**Phase-modulated compound sparsity severity**：importance-based eviction 的 compound interaction severity 随 sparsity 单调递增（n=500 confirmed）。详见 paper_framing.md。

## 目标会议
EMNLP 2025 main conference — **截稿 2026-05-25（距今 9 天）**（没中延 Findings）

## 当前进展
- 阶段：**Round 11 提交冲刺**
- 134 实验完成（70 success / 17 negative / 17 failed），c8_llama + c10_lang + recency 全部完成
- 实验侧：4× GPQA Diamond 实验运行中（importance s020/s025/s030 + random s020），s020 importance 最先完成（~70% done）
- 写作侧：4/4 主要修正完成（bib审计✅ abstract/intro✅ §4-7✅ appendix✅），headline 数字一致性已验证通过✅

## ⚠️ Round 11 提交前 Blocking Checklist
- [x] **Headline 数字一致性**：本地 tex 全部使用 n=500 数据（Reviewer + Worker 双重验证通过）
- [x] c8_llama_n250_fixed 完成 + 结果已写入论文
- [x] 用户确认目标会议：EMNLP 2025 main conference（没中延 Findings）
- [x] Figure 1 PDF 已验证
- [x] 远程 tex 同步完成验证（74 文件 rsync，旧数字已清除）
- [ ] GPQA Diamond 结果（至少 s020 importance + random）
- [ ] Recency section 正式写入论文
- [ ] paper_provenance.yaml 更新
- [ ] Round 11 提交

## Round 10 修订进度

### 实验任务
- [x] **P1-CPU** <think> token position validation — DONE (D093: adaptive κ=0.8804)
- [x] **P1-CPU** Per-phase Gini decomposition — DONE (Reviewer PASS: DS+QW 30/30, low_delta > mid > high)
- [x] **P2-CPU** GSM8K power analysis — DONE (D092)
- [x] **P2-CPU** MATH-500 language switching — DONE (c10_lang_switching success)
- [x] **P1-GPU** LLaMA n=250 — c8_llama_n250_fixed DONE，结果已写入论文
- [x] c10_lang_s020_s025 — DONE

### 写作任务（Paper Agent）
- [x] MUSTAFAR 删除 + bib 全量审计 — Reviewer PASS
- [x] Abstract/Intro rewrite — 完成，**headline 数字需验证**（见 Blocking Checklist）
- [x] §4-7 corrections — Reviewer PASS
- [x] Appendix fixes — 完成

## GPU 状态
- RTX 6000 Pro ×4: westd-22162 cuda:0~3
- GPU0: gpqa_ds_importance_s020 (PID 580927) — ~140/198 done，最先完成
- GPU1: gpqa_ds_importance_s025 (PID 599103) — ~53/198 done
- GPU2: gpqa_ds_importance_s030 (PID 606507) — ~23/198 done
- GPU3: gpqa_ds_random_s020 (PID 606658) — ~23/198 done

## 审稿回溯·系统性问题（Round 10 Holistic Pass）

### SYSTEMIC_ISSUE #1: 写作可信度 → Paper Agent 修正完成
R10-C1 (MUSTAFAR ✅), R10-W1 (overclaiming ✅), R10-W3 (H2O confound ✅), R10-W4 (GPU deanon ✅), R10-W5 (statistical gaps ✅), R10-W6 (clarity ✅)

### SYSTEMIC_ISSUE #2: 实验证据厚度 → 6/6 完成
R10-C3 (LLaMA n=250 ✅), R10-C4 (<think> ✅), R10-C5 (Gini ✅), R10-W5 (pilot CI ✅)

### 非系统性 Critical: 定位调整
R10-C2 → Main conference（用户确认），没中延 Findings

## Scope 扩展（Director 批准）

### 线路 A: GPQA Diamond（非数学推理）— RUNNING
- [x] 数据下载 + pipeline 适配
- [ ] DS importance × 3 sparsities (s020/s025/s030) + 1 random control = 4 runs — **全部 RUNNING**
- GPU0 s020 最先完成（~70%），预计数小时内出结果

### 线路 B: 14B 模型（scale 扩展）
- [ ] Qwen2.5-14B-Instruct 下载（CPU Worker 进行中）
- [ ] MATH-500 × importance × 4 sparsities + 1 random control = 5 runs
- 等模型下载 + GPU 释放后开跑

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D103 | 2026-05-17 | 不在 LLaMA 上跑 recency 实验 — 风险大于收益，作为 Limitation 处理 | recency_s015, c8_llama_n250_fixed |
| D102 | 2026-05-17 | C11 升级为 confirmed — recency 三条件全部支持 attention-scor | recency_s015, recency_s025, recency_s030 |
| D101 | 2026-05-16 | Recency s015 证实 II 方向反转（负值/子加性）— 论文升级为 mechanism d | recency_s015 |
| D100 | 2026-05-16 | D100: 采纳 Reviewer 战略评估——P0 recency-based eviction  | dream_20260516T164305 |
| D099 | 2026-05-16 | Dream full review 分析：6 个结构性问题需立即修复，论文 framing 和 bi | dream_20260516T150210 |
| D098 | 2026-05-16 | GPQA segmentation: quantile 三分为 primary，</think> 二 | gpqa_ds_importance_s015, c4_think_validation_math500 |
| D097 | 2026-05-16 | 撤回 D091 Findings track framing 决策，按 EMNLP main con | — |
| D096 | 2026-05-16 | Session 15 决策：c10 等 c5 释放 GPU、Paper Agent 启动 Findi | c5_per_phase_gini, c8_llama_n250_fixed, c10_lang_switching |
| D095 | 2026-05-16 | c8_llama_n250 数据丢失，GPU 2/3 立即重跑；c10 排队等 c5 释放 GPU | c8_llama_n250, c10_lang_switching, c5_per_phase_gini |
| D094 | 2026-05-16 | c8_llama_n250 数据全丢事故——c10 越权 GPU 使用导致级联失败，c8 需从头重跑 | c8_llama_n250, c10_lang_switching |

