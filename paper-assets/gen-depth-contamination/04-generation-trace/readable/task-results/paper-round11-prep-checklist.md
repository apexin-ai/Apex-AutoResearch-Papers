# paper round11 prep checklist

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_round11-prep-checklist_20260519T054933_result.json`
- **Structured JSON:** [`9c7ddbc8f9227446fad0.json`](../../sessions/9c/9c7ddbc8f9227446fad0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Round 11 内审前置准备

### 1. paper_checklist.yaml
不存在。

### 2. 论文现状摘要

| 维度 | 状态 |
|------|------|
| DDL | **May 25** (剩余 ~6 天) |
| 篇幅 | 28 页 |
| Framing | Plan C "domain ceiling + model competence" (D076) |
| 核心 claim | K* ∈ {1,2,3}, domain ceiling 阶梯: Wiki=1, C4/Code=2, arXiv=3 |
| Retrain chain | K*=7 已确认入稿 (D077/D078) |
| Code cross-model | 2/5 done, **3 RUNNING** (LLaMA, Mistral, Qwen-7B) |

---

### 3. Round 11 提交前置项 Checklist

#### 必须完成 (Blocker)

| # | 项目 | 依赖 | 预计完成 | 备注 |
|---|------|------|---------|------|
| B1 | Code cross-model 3 实验完成 | 无 (GPU running) | May 19 12:00–18:00 UTC | LLaMA ~12:00, Mistral ~16:00, Qwen-7B ~18:00 |
| B2 | Code cross-model 结果入稿 (code_crossmodel_table.tex + 正文) | B1 | B1 完成后 ~2h | Paper Agent patch |
| B3 | Dream simulation | B2 | B2 完成后 ~1-2h | Director 决策点：验证 Plan C framing 是否被 code 结果支持 |
| B4 | 最终 framing 定稿 | B3 | Dream 后 ~1h | Plan C vs 调整。如 code 结果出现意外 (如 7B 模型全 K*=1)，可能需调整 ceiling claim |
| B5 | exp_pythia_retrain_depth7 完成并入稿 | cuda:0 启动 | 启动后 ~3h | Pythia retrain ceiling 验证，补齐 retrain 跨模型证据 |

#### 应该完成 (Important)

| # | 项目 | 依赖 | 预计完成 | 备注 |
|---|------|------|---------|------|
| I1 | 论文全文一致性检查 | B4 | framing 定稿后 ~3h | Abstract/Intro/Method/Results/Discussion 主线统一 |
| I2 | AI 写作痕迹清除 | I1 | I1 同步 | grep "—", grep " – ", grep "ing," 全文扫描 |
| I3 | 专有名词/缩写定义检查 | I1 | I1 同步 | 首次出现必须有定义 |
| I4 | 图表视觉审查 (PDF 渲染) | I1 | I1 后 ~1h | 字体 ≥7pt, 标签无遮挡, 小数精度统一 |
| I5 | Reference 覆盖度检查 | I1 | I1 同步 | 直接相关方法/baseline/benchmark/理论基础 |
| I6 | exp_32b_c4 结果入稿 | exp 完成 (~May 20-21) | May 21-22 | 如 DDL 前完成则入稿，否则标注 ongoing |

#### 可选 (Nice-to-have)

| # | 项目 | 依赖 | 备注 |
|---|------|------|------|
| N1 | booktitle 格式统一化 | 无 | bib 条目一致性 |
| N2 | 附录数据完善 | B2, B5 | 补齐 code/retrain 详细数据表 |
| N3 | θ-sensitivity 讨论完善 | B4 | θ=0.60 vs 0.70 的 K* 变化 |

---

### 关键路径

```
B1 (code 实验, ~May 19 18:00)
  → B2 (结果入稿, ~May 19 20:00)
    → B3 (dream, ~May 19 22:00)
      → B4 (framing 定稿, ~May 19 23:00)
        → I1-I5 (全文审查, ~May 20 下午)
          → Round 11 内审 (~May 20 晚 or May 21)

B5 (pythia retrain) 与 B1 并行，完成后直接入稿

I6 (32b_c4) 独立路径，May 21-22 视情况入稿
```

**最早可启动 Round 11 内审时间: ~May 20 晚 (UTC)**，前提是 B1-B4 按时完成且无意外。

---
