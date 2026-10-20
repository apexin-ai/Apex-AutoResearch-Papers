# reviewer / loop_1.md

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`46804042c292e2301031.json`](../../sessions/46/46804042c292e2301031.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-21T06:44:40+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目使用 westd-35694 全部 4 GPU（cuda:0-3），但 GRPO 固定在 cuda:2（PID 73689），不可抢占
- Mistral eval 已完成但 eval 残留进程（PID 83304, 84455）可能仍占显存，清理前确认不影响后续任务
- PSN-IRT 的 12-model 训练集不包含 Mistral-7B-Instruct-v0.3（已验证），但包含 Qwen 和 Llama 相关模型——引用 PSN-IRT 参数时注意 circularity 问题
- eval_lz.py 的 GRPO stage 必须走 base→SFT merge→GRPO adapter 链（之前有 bug 直接加载 GRPO 到 base，已修复但需警惕回归）
- **跨家族 lz* baseline 差异极大**（Qwen clean +8.68, Llama -0.14, Mistral +5.42）——绝不能在论文中 claim "lz* < -2 即为污染"，检测依赖 Δlz*/Cohen's d 相对比较

### 2. 🖥️ 基础设施快照
- 服务器：westd-35694（4× RTX PRO 6000 Blackwell ~97GB），SSH 账号 root
- Qwen 实验目录：`/root/autodl-tmp/ctrl_contam_pilot/`（train.py SEED_MAP 含 s1-s5）
- Llama 实验目录：`/root/autodl-tmp/ctrl_contam_llama/`（结果在 results/）
- Mistral 实验目录：`/root/autodl-tmp/ctrl_contam_mistral/`（训练+eval 已完成）
- Post-RL 目录：`/root/autodl-tmp/post_rl_contam/`（eval_lz.py + eval_with_ht.py）
- Baseline 对比：`/root/autodl-tmp/baseline_comparison/results/comparison_results.json`
- HF cache：`/root/autodl-tmp/.hf_cache`
- GRPO 日志：`/tmp/grpo_train.log`（PID 73689, cuda:2）
- Seeds 训练日志：`/tmp/train_clean_s4.log`（cuda:1）, `/tmp/train_clean_s5.log`（cuda:3）
- 本地 artifacts：`projects/irt_personfit_contam/artifacts/`
- 新 bib 文件：`artifacts/references/references.bib`（30 条 verified + 1 UNVERIFIED Yin et al.）

### 3. 📊 当前状态
**刚完成**：
- Mistral 三条件 eval 审查（PASS+WARNING），结果已录入 registry DONE
- 跨家族 lz* baseline 分析发现并报告（Qwen/Llama/Mistral clean lz* 差异 ~9σ）
- Reference expansion 审查（30 条 verified，3 条作者替换，1 条 UNVERIFIED）
- Qwen seeds expansion (s4/s5) 审查（训练正常）

**RUNNING 实验**：
- GRPO (cuda:2): ~3269/7021 (47%), ~2.07s/step, ETA ~2h → 预计 ~08:30 完成
- eval_with_ht.py --stage base (cuda:3): D022 HT post-RL base 阶段评估中
- Qwen clean_s4 (cuda:1, seed=301): ~316/939, ~20min 剩余
- Qwen clean_s5 (cuda:3, seed=302): ~329/939, ~20min 剩余

**等待中**：
- GRPO 完成后的 cron 回调（exp-post-rl）
- Mistral eval results Worker 可能触发 registry 更新通知
- Director 对跨家族 baseline 分析的回应

### 4. 📋 待办（条件触发式）
- clean_s4/s5 训练完成 → 验证 checkpoint 存在 + 确认是否立即启动 s6-s10（还差 5 个 clean seeds 达 n=10 目标）
- GRPO 7021 steps 完成 → 审查 eval_lz.py + eval_with_ht.py 的 GRPO stage 结果（关键：lz* 是否在 RL 后保持检测力 + HT 是否失效 = D022 核心假设）
- eval_with_ht.py base 阶段完成 → 检查 base HT 值作为 D022 baseline
- HT post-RL 4 种结果情景需准备审查框架：(1) lz*保持+HT失效=完美, (2) 两者都保持=需替代论点, (3) 两者都失效=负面结果, (4) lz*失效+HT保持=严重问题
- contam seeds 是否需要多 seed → 需 Director 决策（当前仅 clean 扩展）
- 论文章节提交审查时 → 触发 Mode B 写作对抗审查（先 Read paper-quality-lessons.skill.md）

### 5. 🎯 战略上下文
- **核心论点**：IRT person-fit (lz*) 能在 minimal-information 条件下（仅二元响应）检测 LLM benchmark 污染，且跨模型家族 generalize
- **最强证据**：Cohen's d 2.95-3.42（Qwen/Llama 15%），Mistral Δlz* -6.80/-8.57 待多 seed 标准化
- **最大悬念**：D022 HT post-RL 结果——如果 HT 也在 RL 后保持，ℓz* vs HT 的差异化论点需要转向"distributional calibration / Snijders correction / multi-parameter utilization"而非"RL robustness"
- **易判断错的事**：
  1. Qwen contam_15 lz* = +3.85（正值！），不代表检测失败——是 baseline 极高（+8.68）导致的，Cohen's d = -3.42 仍然极显著
  2. Inverted-U 在 Qwen 上明显（50% Δlz* < 15% Δlz*），但 Llama/Mistral 上不明显——不能 claim 为 universal
  3. Seeds 当前只有 clean 在扩展，contam 仅 seed=42——Cohen's d 用 clean std 做分母是合理的（单样本 t 检验），但如果审稿人要求 contam 也多 seed 则需补实验
  4. ARR DDL 仍未确认（5/25 vs 6/15），已 flag 6+ 次无回应
- **决策链**：D019(模型换Qwen2.5-7B) → D020(C群R0处理) → D021(seeds n=10) → D022(HT post-RL 为关键突破口)


---
