# Memory — error_diag_dpo_recovery

> 只记录不可从 registry/代码派生的决策原因、约束、经验教训。

## 🔴 D029: P1 作废，P2 是唯一 MVP gate（2026-05-12）

P1 divergence timing KW 是代数恒等式（correction_span = expert_length - div_point），p≈0 不是实证发现。P1 降级为描述性分析（failure mode characterization table），不再是 gate。

**MVP gate 只剩 P2: ETADN > single-γ ≥ 3%（3 seeds 平均）**

原 P1 error type taxonomy（action/verification/planning）也已作废——LLM 判 98% planning, rule-based 判 80% action，同一行为反向标签。Error type 降级为解释层（论文叙事用，不作统计分组变量）。

## γ(d) 连续折扣函数（D028-D029, 更新 2026-05-13）

不再是离散的 γ_action/γ_verification/γ_planning，改为连续函数：
- γ(d) = γ_min + (γ_max - γ_min) × d
- d = div_point / expert_length
- 早偏离 d≈0 → γ≈γ_min（重折扣）
- 晚偏离 d≈1 → γ≈γ_max（轻折扣）
- γ_min=0.85, **γ_max=1.0**（D033 更正，原 0.97 改为 1.0，与 γ_planning 对齐）
- Director 最初指定 (1-d)，后更正为 d（与 ROADMAP "早偏离→重折扣" 语义一致）

## Expert/Failure Overlap — DPO 可行性（2026-05-12）

- Expert 3119 条, 1395 unique templates, 全覆盖 6 种 task type
- Combined 192 unique failures: exact match 83.3%, template match 94.8%
- v6 完成后预估 ~210-240 DPO pairs

## 分类器现状（2026-05-12）

已准备 4 种分类方法，全部降级为辅助分析（不再是 gate）：
- LLM zero-shot: 98% planning
- LLM --no_span_hint: 0 变化
- LLM --few_shot: 待跑
- Rule-based v2: 80% action / 20% verification

## v6 数据全部丢失（2026-05-13）

服务器项目目录被意外删除，v6 ICL 数据和所有服务器端代码全部丢失。灾难恢复改为收集 v7。

## 🔴 v7 temperature 回归 bug（2026-05-13, 诊断确认）

灾难恢复重建 collect_trajectories_icl.py 时，temperature 默认值从 **0.5 被错误改为 0.7**。导致 v7 成功率 5.5%（v6 为 63-70%）。ALFWorld 多步决策对 temperature 极敏感，0.2 的差异导致 >10x 性能下降（compound error across 40 steps）。

## 🔴 D033: TextWorld 1.7.0 put→move API 变更（2026-05-13）

**v7/v8 0% SR 的根因**（非 temperature）：TextWorld 1.7.0 的 `put X in/on Y` 动作被拒绝，必须用 `move X to Y`。v7 的 5.1% SR 全部来自不需要 put 的 task type（look_at_obj 等）。

修复：`translate_action()` 在 env.step 前将 `put X in/on Y`（及 `put X in Y`、`put X on Y`）转为 `move X to Y`。regex: `r"put (.+?) (?:in/on|on|in) (?:the )?(.+)"`。

**教训：环境 API 版本变更不一定有显式报错，只会返回 "Nothing happened"。新环境部署后必须用 admissible_commands 验证动作格式。**

## γ(d) 方向反转 bug（2026-05-12, Reviewer 发现）

原 train_dpo.py 自己计算 γ(d) 方向反了。**修复：直接从 JSONL gamma_e 字段读取（单一真值源）**。

## φ 归一化修复（2026-05-13, pipeline dry-run 确认缺失）

灾难恢复重写的 etadn_discount.py 遗漏了 φ 归一化。`compute_discount_weights` 末尾必须 `w = w / w.sum()` 确保 Σφ=1。已修复并同步服务器。**灾难恢复重写代码时必须验证所有已知 fix 是否包含。**

## 关键教训

- LLM 分类器对 ALFWorld trajectory 有 planning 偏见，prompt 微调无法修复
- correction_span 与 div_point 的代数关系使 KW 检验 tautological
- 88% step-1 divergence 使归一化指标退化
- **服务器代码必须有本地备份或 git 管理**——单点存储导致灾难性丢失
- **模型下载不要多进程并行**——互相阻塞
- **灾难恢复重写代码时，必须对照 fix log 逐项验证**——v7 同时遗漏了 temperature 默认值和 φ 归一化
- **ALFWorld ICL 采样 temperature 必须 ≤0.5**——0.7 导致暴力遍历，40 步 budget 不够
- **TextWorld 1.7.0 API: put→move**——环境 API 变更无显式报错，只返回 "Nothing happened"，必须 admissible_commands 验证
