# director / loop_2.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`f43e35ee4af40d7aec4b.json`](../../sessions/f4/f43e35ee4af40d7aec4b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-14T13:23:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westb-23072 的 cuda:0 + cuda:1（约束 C001）
- GRASPrune 目录下**绝对不要运行 `pip install -r requirements.txt`**——会降级 torch 从 2.10.0 到 2.7.0，破坏环境
- rescale 补偿阶段（pipeline.py L405）硬编码 WikiText2，无法通过 config 切换——论文中必须说明此差异
- model_utils.py 只处理了 MLP 非均匀加载，attention 非均匀加载未实现——50% sparsity 剪到 attention 时会崩

### 2. 🖥️ 基础设施快照
- 服务器：westb-23072 (connect.westb.seetacloud.com)，2× RTX PRO 6000 96GB
- 工作目录：/root/recovery_aware_struct_prune
- Python：/root/miniconda3/bin/python（conda base，不是 venv）
- 模型：DeepSeek-R1-Distill-Qwen-7B（本地缓存，HF 网络不可达需 `source /etc/network_turbo`）
- GRASPrune：/root/GRASPrune/（已 clone + GSM8K 校准适配完成）
- 论文：本地 `paper/` 目录（introduction.tex, method.tex, related_work.tex, experiments.tex, references.bib 22 条目）
- 活跃进程：mvp_rasp_pipeline_v2 在 tmux 中运行，但 GPU health 数据过期无法确认 PID。**新 session 第一件事确认 GRPO 是否存活**
- Cron：MVP 监控 cron 在 Agent session 重置时可能丢失，需重新注册

### 3. 📊 当前状态
MVP v2 pipeline 从 Step 3.5 resume（第三次提交，修复了 GQA 粒度 + MLP 加载 + OverflowError）。Step 3.5 eval 预计 ~18:50 UTC 完成，之后自动进入 Step 4 GRPO（12-15h 关键路径）。**当前不确定 eval 是否已完成、GRPO 是否已启动——GPU health 数据 stale，必须 SSH 确认。**

Registry：mvp_rasp_pipeline_v2 RUNNING；mvp_rasp_pipeline DONE(failed)。

论文 4 section 初稿齐全，所有 Reviewer WARNING 已修（Algorithm 1 改 parameter-budget-based、citation keys 统一、activation shift 描述对齐代码、RASP 公式去重）。baseline_eval.json 可能缺失，MVP 完成后 5min 补跑。

### 4. 📋 待办
- **立即**：SSH 确认 GRPO 是否在跑 → 活着则 WAIT；死了则查 log + 重启
- Step 4 GRPO 完成 → Step 5+6 post-recovery eval + correlation（~3h）→ 判定 ρ ≥ 0.4 pass / [0.3,0.4) 25% 重试 / < 0.3 contingency
- MVP pass → complete_mvp() → post-mvp-kickoff skill（paper_framing.md → experiment_plan.yaml → dream_simulate → ROADMAP）
- MVP pass → 立即启动 Phase 2 P1 GRASPrune（代码已就绪，一条命令 run_graspune.sh）
- MVP pass + Phase 2 需更多 GPU → director_post_to_manager 申请云 GPU 扩容
- baseline_eval.json 缺失 → MVP 完成后补跑 Step 0（5min）

### 5. 🎯 战略上下文
- 核心假设：CKA functional overlap F(h) 预测结构化剪枝后 RLVR recoverability，Spearman ρ ≥ 0.4 为 pass
- D001：35% sparsity 下 MLP-only pruning 是模型结构特征的正确反映（attention GQA groups 参数量小，全局排序自然不剪），不强制剪 attention
- 目标会议：EMNLP 2026 ARR May 25（~11 天）
- 35% 剪枝后模型质量很差（部分样本生成 inf），post-prune accuracy 会很低——这对我们有利，GRPO 恢复后的 Δ 应该显著
- GRASPrune 同时剪 MLP + attention（与 RASP MLP-only 不同）且有 rescale compensation，论文需讨论公平性
- **易错**：(1) Agent session 重置后 cron 监控丢失，必须重新注册 (2) 不要假设 eval/GRPO 还活着，先 SSH 确认 (3) GRASPrune 的 rescale 阶段始终用 WikiText2 无法配置切换


---
