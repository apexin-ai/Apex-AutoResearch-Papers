# reviewer / loop_14.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_14.md`
- **Structured JSON:** [`333e42e0d1a65d1f7e77.json`](../../sessions/33/333e42e0d1a65d1f7e77.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-05-17T23:00:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- westb GPU 白名单未明确限定（项目 config 需确认），但当前 grpo_cka_only_20 和 grpo_random_20 各占一张卡，不可干扰
- westd GPU 白名单：eval 任务使用 cuda:0 和 cuda:2，之前出过 duplicate process 占 cuda:2 的问题（已解决）
- eval_postprune_cka_only_30 的 pruned 模型用的是 "dummy_ones_importance + rasp_alpha1 = pure CKA-only" 方法（不是标准 importance pruning）——审查时注意方法一致性
- D051 confound 未解决：Standard GRPO 用 checkpoint-50（v8, max_steps=100），RASP 用 v9-final（max_steps=30, collapsed）——4-way 对比中只有 CKA-only vs Random 是完全受控的

### 2. 🖥️ 基础设施快照
- **westb-23072** (root): `/root/recovery_aware_struct_prune`（代码）, `/root/autodl-tmp/recovery_aware_struct_prune`（模型/结果）
  - 活跃训练：grpo_cka_only_20 (step 70/100, ~400s/step), grpo_random_20 (step 70/100, ~440s/step)
  - Logs: `/root/runs/recovery_aware_struct_prune/`
- **westd-11672** (root): 同上路径结构
  - 活跃 eval: eval_math500_grpo_rasp_20_v3 (260/500), eval_postprune_cka_only_30 (35/200), eval_postprune_standard_30 (139/200), eval_sft_cka_only_20_n1319 (running)
  - Logs: `/root/runs/recovery_aware_struct_prune/`
- wandb: entity="xiaoyucorynne-", project="recovery_aware_struct_prune"（但 metrics fetch 不稳，直接读 log 更可靠）

### 3. 📊 当前状态
**刚完成**：
- 叙事审查全套：C2 "recovery capacity gradient" 定稿建议已提交 Director，含 step 10-70 完整验证数据
- C1 critical 预警（MATH-500 可能挑战 "universal decoupling"），但 interim 数据下降中（34%→28%），最终可能接近 SFT baseline
- eval_postprune_rasp_30 确认 0% accuracy（cron 误报，EXIT_CODE=129=SIGHUP，实验正常完成）
- eval_postprune_cka_only_30 tokenizer 缺失 bug 已修复，eval 重新提交运行中

**RUNNING 实验**：
- grpo_cka_only_20: step 70/100, frac_zero=0.125（持续新低）
- grpo_random_20: step 70/100, frac_zero=0.300（平台）
- eval_math500_grpo_rasp_20_v3: 260/500, acc=28.0%（下降中）
- eval_postprune_cka_only_30: 35/200（tokenizer 修复后重启）
- eval_postprune_standard_30: ~139/200, acc≈3%
- eval_sft_cka_only_20_n1319: running on westd

**PREPARING**: prune_cka_only_30（registry 注册但未执行，模型已存在且 eval 已提交）

### 4. 📋 待办（条件触发式）
- eval_math500_grpo_rasp_20_v3 完成 500/500 → 对比 SFT RASP MATH-500 (24.2%)：若 Δ<3pp 则 C1 "universal decoupling" 基本成立（benchmark-specific saturation），若 Δ>5pp 则 C1 需重大修正
- grpo_cka_only_20 到 step 80/90/100 → 确认 frac_zero 持续下降趋势是否稳定（当前 0.175→0.35→0.15→0.2→0.125，需看是否继续或反弹）
- eval_postprune_cka_only_30 完成 → 对比 RASP 30% (0%)：若 CKA-only 30% >0% 则 sparsity cliff 是方法相关（强 C2 证据）；若也=0% 则 cliff 是 sparsity-universal
- eval_postprune_standard_30 完成 → interim 3% 确认：Standard 30% 接近崩溃但非完全零（RASP 0% < Standard 3% < CKA-only ?%）
- Director 回复 C1/C2 framing 决策 → 根据决策方向调整后续审查重点

### 5. 🎯 战略上下文
- **核心发现（已验证）**：CKA-only 展示 active super-recovery（step 40 spike 后持续下降到 0.125），Random 只恢复到 baseline 后平台。这比原来的 "collapse gradient" 更有 novelty。
- **C2 已定方向**：D054 决定 "recovery capacity gradient"，我提交了一句话措辞建议，等 Director 确认
- **C1 风险**：MATH-500 interim 曾显示 GRPO 有效（+6pp），但数据在下降中（28% at N=250 vs SFT 24.2%）。最终结果决定 C1 是否需要从 "universal" 修正为 "in-distribution specific"
- **易错点**：
  1. 不要混淆 4-way 和 2-way 对比——只有 CKA-only vs Random 是完全受控实验（同 config/同 steps/同起点），Standard/RASP 来自历史 run
  2. frac_reward_zero_std 是 noisy metric（非单调），KL 和 reward 更稳定——论文核心 evidence 建议锚定 KL
  3. cron on_failed 经常误报（SIGHUP=129, 重复进程 Terminated），先读 log 确认是否真失败
  4. MATH-500 数据在下降趋势中——不要基于 early interim（50 samples）做结论，等 full 500


---
