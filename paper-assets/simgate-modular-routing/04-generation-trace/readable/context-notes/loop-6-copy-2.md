# agent / loop_6.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`b9ddfed3598d20ec3a2f.json`](../../sessions/b9/b9ddfed3598d20ec3a2f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-14T11:19:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 westb-13313:cuda:0 和 westb-13313:cuda:1，不得用其他卡
- CUDA_VISIBLE_DEVICES=N 对应物理 cuda:N，脚本内 --gpu_id 始终为 0
- class_weights auto 是已确认毒参数（D023）：与 max_grad_norm=1.0 交互导致 internal class 有效学习率≈0，所有 router SFT 实验禁用
- tmux kill-session 会 SIGHUP 波及无关进程——清理 tmux 时只 kill 确认的 session，禁止 pkill -f 宽泛 pattern
- plan-002-formal-v6 正在 cuda:0 运行，绝对不要碰

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313，2× RTX 5090 32GB
- 工作目录：/root/autodl-tmp/simgate-modular-routing
- Python：/root/miniconda3/bin/python（conda base 环境，非 venv）
- 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：/root/autodl-tmp/models/Qwen/Qwen3-1.7B（ModelScope 下载，本地离线）
- 数据：results/plan_c_test_labels/implicit_sft.jsonl（2040 samples, 11 tasks）；results/plan_c/（原始 labeled_steps）
- HF_HOME=/root/autodl-tmp/.hf_cache，WANDB_MODE=offline，HF_HUB_OFFLINE=1
- 活跃进程：plan-002-formal-v6 (PID 240633, cuda:0, explicit classification head SFT)
- Worker 在跑：worker_code_plan-003-eval-script（CPU，写 eval 脚本）；worker_retry_plan-004-v4（SSH 清理 + 重提交 implicit SFT 到 cuda:1）

### 3. 📊 当前状态
刚处理 plan-004-v3 失败回调（EXIT_CODE=129 SIGHUP 误杀）。已更新 registry、发飞书卡片、汇报 Director。

RUNNING：
- plan-002-formal-v6 (cuda:0)：explicit classification head SFT，无 class_weights，验证 D023 修复是否让分类头恢复正常

等待回调：
- worker_retry_plan-004-v4：清理 westb-13313 tmux 残留 + 以 plan-004-v4 重提交 implicit router SFT 到 cuda:1（同 v3 配置）
- worker_code_plan-003-eval-script：写 plan-003 end-to-end eval 脚本（依赖 plan-002 完成）

PENDING 审批：
- research-cf-pilot-gpu1：counterfactual labeling pilot

PREPARING：
- plan-001b-gpu1-rebalance、mvp-p1-signal

### 4. 📋 待办
- worker_retry_plan-004-v4 回调 → 确认 plan-004-v4 已 RUNNING，验证 PID 存活，更新 registry
- plan-002-formal-v6 cron 完成回调 → 按 on-experiment-done 分析：关键看 internal recall 是否 >0（去掉 class_weights 后应恢复），与 plan-004-v4 (implicit) 对比
- plan-004-v4 cron 完成回调 → 同上，explicit vs implicit 对照分析。若两者都 success → 向 Director 汇报双路线结果，推进 plan-003 eval
- 若 plan-002-formal-v6 或 plan-004-v4 再次 negative（internal recall=0）→ 走 red-section framing 提案，考虑放弃 router SFT 路线
- worker_code_plan-003-eval-script 回调 → 审查 eval 脚本，等 plan-002 完成后提交 plan-003

### 5. 🎯 战略上下文
- 核心发现已确认（plan-012 全量）：death avoidance ~90% 主导 routing signal（11 tasks, 245 eps, r=0.9698）
- 论文目标：EMNLP 2026 ARR short paper，DDL 2026-05-25（剩 11 天）
- 当前瓶颈：plan-002（explicit）和 plan-004（implicit）两条 router SFT 路线连续失败（class_weights 是根因，已修复）。v6 和 v4 是去掉 class_weights 后的首次干净运行，结果决定论文是否能写 router 实验章节
- D023 决策链：pad_token_id 假说被 v5 否定 → class_weights + max_grad_norm 交互是真正根因 → v6/v4 去掉 class_weights 做对照
- 易错点：plan-004 implicit SFT 的 class_weights 对 generative loss 影响不同于 classification loss（plan-004-ablation-b 证明 implicit 不退化），所以 plan-004-v4 理论上即使不去 class_weights 也能工作，但为了对照一致性已统一去掉
- Critical path：v6 + v4 完成（~数小时）→ plan-003 eval（~15h）→ plan-005 分析（~2h）→ 论文写作（~3 天）


---
