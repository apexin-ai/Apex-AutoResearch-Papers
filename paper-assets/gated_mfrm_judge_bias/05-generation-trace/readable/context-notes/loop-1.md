# director / loop_1.md

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`e9a3ebdce7cb36cc7659.json`](../../sessions/e9/e9a3ebdce7cb36cc7659.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-22T18:19:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：rtx6000-4x cuda:0-3 + autodl-8gpu cuda:0-3，共 8 张。严禁使用白名单外 GPU
- autodl-8gpu 是云租卡，用完后由 cron + Manager 看门狗自动释放，不要手动释放
- exp-003 horseshoe prior 已确认失败（D017），不要再尝试 horseshoe，只用 HalfNormal hierarchical prior
- API 代理地址 http://47.94.22.126/v1（OpenRouter 兼容），402=余额不足
- 6 judge families（9→6 优化，D-series decisions），API 预算 ~$300

### 2. 🖥️ 基础设施快照
- **rtx6000-4x**: connect.westd.seetacloud.com, /root/gated_mfrm_judge_bias, conda base (/root/miniconda3/bin/python)
  - cuda:0 exp-009 OVB validation（RUNNING）
  - cuda:1-3 exp-001/002 judge collection（已基本完成，26000+ judgments）
- **autodl-8gpu**: connect.westd.seetacloud.com, /root/gated_mfrm_judge_bias, conda base
  - cuda:0 exp-003b joint_gmfrm MCMC（HalfNormal prior, RUNNING, ~40-60min ETA from ~17:38 UTC）
  - cuda:1 Mistral-7B response generation（刚分配）
  - cuda:2 Qwen2.5-7B download fix + response generation（下载卡住待修复）
  - cuda:3 空闲，预留给 exp-003b 后续
- HF cache: /root/autodl-tmp/.hf_cache (autodl), /root/.cache/huggingface (rtx6000)
- 论文: /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex (10 pages, 8+2 appendix)

### 3. 📊 当前状态
**刚完成**：
- exp-004 baseline comparison：7 个 baseline 全部 τ=0.786，只有 joint G-MFRM τ=0.857（强 positive）
- Paper Agent prior patch：method.tex horseshoe → HalfNormal 已更新，编译通过
- Reviewer contingency analysis：worst case τ=0.786 仍可投 Findings (3.0)，需 diagnostic framing 调整
- D017 logged：horseshoe → HalfNormal 切换决策

**RUNNING**：
- exp-003b：autodl cuda:0，HalfNormal prior joint_gmfrm MCMC，预计 40-60min
- exp-009：rtx6000 cuda:0，OVB validation（~77.5% complete）
- exp-001/002：rtx6000 cuda:1-3，judge collection（接近尾声）

**等待中**：
- exp-003b worker done 回调（关键路径）
- Reviewer session 已 RESET（刚批准 RESET_BOTH）
- Agent 正在处理我最新的 GPU 分配指令

### 4. 📋 待办
- exp-003b 完成 + R-hat<1.05 + τ≥0.82 → 提取完整结果，进入 Paper Phase 2 写 experiments section，然后重新 submit_paper_to_review
- exp-003b 完成 + R-hat>1.1 或 ESS<50 → 执行 Plan B（SVI init + MCMC 或 fixed-θ conditional estimation），同时按 Reviewer 建议准备 diagnostic framing 调整
- exp-003b 完成 + τ=0.786（收敛但无优势）→ 执行 Plan A diagnostic framing：claim 改为 "calibrated null detection + contamination profiling"，引用 mvp_001 ρ=0 理论预测支撑。Paper Agent patch intro/experiments/abstract
- exp-009 完成 → 提取 OVB 单调性 + bias_corr 结果，补充 experiments section
- 小模型 response 生成完成 → 扩展 exp-003 target models（更多 c_n 数据点）
- 全部实验就绪 → Paper Phase 2（experiments + conclusion + limitations）→ submit_paper_to_review → 用户要求"迅速修复写作再重新审稿"

### 5. 🎯 战略上下文
- **DDL: 2026-05-26 EMNLP ARR**，仅剩 3 天
- **核心 story**: G-MFRM joint calibration of judge bias + benchmark contamination。OVB 理论证明 sequential estimation 有偏，joint model 纠正
- **exp-004 是关键发现**：7 个 baseline 排名完全一致 = 只有 joint modeling 能改变排名。无论 exp-003b τ 结果如何，这都是强论点
- **Reviewer 评估**：worst case (τ=0.786) = Findings 级别 (3.0)；best case (τ=0.857 confirmed) = Borderline Conference (3.5)。用户目标"保3.5冲4"
- **易错点**：(1) exp-003b 即使 R-hat 好，也要检查是否 hit max tree depth——HalfNormal 也可能有采样困难（c_n·e_i 乘法项几何结构）；(2) mvp_001 ρ=0 结果是 contingency narrative 的伏笔，不要忽略；(3) review_issues.yaml 有 16 个 issue 跟踪中（W1-W13 + MR + REPRO + MT），Phase 2 写作要逐条 close
- **决策链**: D001-D017，关键：D014 6-judge-family 优化、D016 exp-003 启动、D017 horseshoe→HalfNormal
- **mistakes.yaml**: M001-M011，关键：M009 缺 sigma_c、M010 JAX io_callback、M011 JAX_PLATFORMS 太晚


---
