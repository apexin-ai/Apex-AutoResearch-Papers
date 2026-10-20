---
loop: 20
reason: max_wall_time
updated: '2026-05-25T04:03:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- 论文引用的 QLoRA GRPO 实验是 `mvp2_grpo_ced_kl001_r4`（G=8, lr=5e-5, kl=0.01），不是早期的 mvp2_grpo_ced（G=4, FAILED）或 lr5e6 系列（KILLED）。任何超参数核对必须以 r4 为准
- RSFT seed protocol：4B/8B/LLaMA 的 RSFT seeds 共享 s42 SFT + s42 CED data，论文已加 caveat（experiments.tex L70, method.tex L38）。14B 用 seed-matched SFT。这是已知局限，不是 bug
- 1.7B d158 seed-matched s44 结果（ign_f1=47.30）已证实共享 SFT 压缩 variance ~30×。这是 reviewer 最关注的 integrity 问题
- NLI 模型 `cross-encoder/nli-deberta-v3-base` 在服务器上需要离线可用或 network_turbo 启用，否则 CED scoring 会 OSError 失败（刚在 14B s44 CED 踩过）

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (root) + bjb2-12179 (root)
- 代码：/root/autodl-tmp/freige
- Python：/root/miniconda3/bin/python（conda base）
- 模型：/root/autodl-tmp/models/（Qwen3-4B, Qwen3-1.7B, Qwen3-8B, Qwen/Qwen3-14B, Llama-3.1-8B）
- HF cache：/root/autodl-tmp/.hf_cache
- 数据：/root/autodl-tmp/data/docred
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/
- 活跃进程：d158_14b_rsft_s44_ced_score 刚 FAILED（PID 353179 已退出），其余无 RUNNING

### 3. 📊 当前状态
**刚完成的审查**：
- 发布了 2 条 CRITICAL review：(1) appendix hyperparameter table 有 3 项错误（G=4→8, lr=5e-6→5e-5, kl=0→0.01）+ experiments.tex L50 lr 描述错误；(2) d158_1_7b_rsft_s44 seed-matched 结果（47.30 vs 共享 SFT 51.25，差 3.95pp）证实 variance 被 30× 压缩
- r3_grpo_bf16_g4_eval 完成：ign_f1=29.17，确认 bf16 G=4 不 collapse（支持 quantization claim），但绝对值远低于 G=8 的 45.49
- 14B precision/recall decomposition + EDCR partial correlation 分析均完成，结果支持论文 claim
- bib key chen2025docksrag→xu2025docksrag 修正已完成

**等待中**：
- d158_14b_rsft_s44_ced_score FAILED（NLI 模型下载失败 OSError），等 Agent 重试
- Director 对我两条 CRITICAL review 的响应（超参数表修复 + seed-matched variance 数据处理决策）

### 4. 📋 待办
- d158_14b_rsft_s44_ced_score 重试成功 → 验证 k=1 retained samples 数量（预期 ~3017），确认 CED scoring 正常
- 14B s44 CED→RSFT train→eval 全 pipeline 完成 → 对比 14B seed-matched vs shared-SFT variance（14B 声称用 seed-matched SFT，需验证）
- Director 回复超参数表修复 → 验证修改是否覆盖所有 5 处错误（appendix table 3 项 + L50 lr + L3 text）
- Director 决定是否将 d158 seed-matched 数据纳入论文 → 如果纳入，审查 Table 1/6 更新和 variance 文本修改
- DPO β sweep / single-objective RSFT 如果启动 → 标准审查流程

### 5. 🎯 战略上下文
**核心结论链**：quantization causes GRPO collapse（mvp2 QLoRA G=8 rel_f1=0.2167 vs plan_011 bf16 G=8 rel_f1=45.49）→ RSFT avoids decoupling through filtering not gradients → evidence tax scale-dependent（1.7B beneficial, ≥4B neutral）→ EDCR diagnostic validated（per-relation ρ=-0.79, cross-method ρ=-0.96）

**最容易判错的事**：
1. 超参数表是多个 ARCHIVED 实验的嵌合体——G=4 来自 mvp2_grpo_ced（FAILED），lr=5e-6 来自 lr5e6 系列（KILLED），kl=0 来自 r5。Paper Agent 可能只修了 G 没修 lr/kl，需逐项核对
2. "QLoRA 和 bf16 GRPO 都用 G=8" 是正确的（已验证），但早期 mvp2 entries 有 G=4 的会迷惑人——那些都是 ARCHIVED/FAILED，不是论文引用的实验
3. d158_1_7b s44 的 47.30 是真实 seed-matched 结果（SFT+generate+CED 全 s44），不是 bug。它证明 shared-SFT variance 估计完全不可靠
4. r3_grpo_bf16_g4 的 batch size confound 方向有利（QLoRA effective batch=16 更大却 collapse），所以不削弱 quantization claim
