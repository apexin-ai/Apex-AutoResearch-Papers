# agent / loop_22.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_22.md`
- **Structured JSON:** [`d6056fc1ada421168c80.json`](../../sessions/d6/d6056fc1ada421168c80.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 22
reason: idle_timeout
updated: '2026-05-22T22:14:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-23072 (cuda:0, cuda:1), westd-32935 (cuda:0, cuda:1, cuda:2, cuda:3)。westd-29022 已死，不可用
- westd-32935 网络不通，所有实验命令必须加 `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1`
- eval 脚本必须加 `--max_new_tokens 2048`，否则少数 sample 生成卡顿导致超时
- westd-29022 数据盘 100% 满（619GB），不可再部署新实验
- Cron "process dead with no sentinel/W&B" 可能是误报——先 tail 日志确认是否实际完成再判定 failed

### 2. 🖥️ 基础设施快照
- **westd-32935**: 4× RTX PRO 6000, 工作目录 `/root/recovery_aware_struct_prune`, Python `/root/miniconda3/bin/python`, conda base 环境, 数据盘 `/root/autodl-tmp` 用 48% (437G 可用)
- **westb-23072**: 2× RTX PRO 6000, 同上路径布局, 数据盘 51% 用 (6.9T 可用)
- 模型路径: `/root/autodl-tmp/recovery_aware_struct_prune/` 下各子目录 (sft_*, grpo_*, pruned_*)
- HF cache: `/root/.cache/huggingface/`
- 活跃 cron 5 个（reconcile 已确认）:
  - eval_math500_grpo_standard_20_fair_2048_v2 (westd:0, pid=2234)
  - eval_gsm8k_sft_alpha4_20_v5 (westd:2, pid=3586)
  - eval_math500_sft_random_20_v3 (westd:1, pid=5236)
  - eval_math500_sft_standard_20_1p5b (westb:0, pid=147023)
  - eval_math500_sft_rasp_20_1p5b (westb:1, pid=147308)

### 3. 📊 当前状态
刚处理 eval_gsm8k_grpo_alpha4_20_v3 的 cron 失败回调——诊断为 **cron 误判，实际 success**。已修正 registry（conclusion=success, metrics=62.77%），已发飞书卡片，已向 Director 汇报并请求 westd:3 下一个实验分配。收到同一实验的第二次重复 cron 回调，已忽略。

**RUNNING (5)**:
| exp_id | GPU | 说明 |
|--------|-----|------|
| eval_math500_grpo_standard_20_fair_2048_v2 | westd:0 | Standard GRPO MATH-500 |
| eval_math500_sft_random_20_v3 | westd:1 | Random SFT MATH-500 |
| eval_gsm8k_sft_alpha4_20_v5 | westd:2 | α=4.0 SFT GSM8K 全量 |
| eval_math500_sft_standard_20_1p5b | westb:0 | 1.5B cross-scale |
| eval_math500_sft_rasp_20_1p5b | westb:1 | 1.5B cross-scale |

**空闲**: westd:3 — 等 Director 分配

**等待**: Director 回复 westd:3 下一个实验（建议了 eval_math500_sft_standard_25_2048 / eval_mbpp_grpo_standard_20_v2 / eval_mbpp_grpo_rasp_20_v2）

### 4. 📋 待办（条件触发式）
- Director 指定 westd:3 实验 → 立即提交，GPU 不能空着
- eval_math500_grpo_standard_20_fair_2048_v2 完成 → 收割 Standard GRPO MATH-500 数据，patch ROADMAP 表格
- eval_gsm8k_sft_alpha4_20_v5 完成 → 得到 α=4.0 SFT GSM8K 最终值（当前 interim 60.71%*），更新 ROADMAP，计算 Δ(GRPO-SFT) for α=4.0
- eval_math500_sft_random_20_v3 完成 → 补全 MATH-500 Random SFT 数据
- 1.5B cross-scale 两个完成 → 评估是否入 appendix
- 所有 westd eval 完成 → Paper Agent patch 表格 → Round 6 审稿提交

### 5. 🎯 战略上下文
- **投稿目标**: EMNLP 2026 Main (ARR May 25) — **~2 天**
- **核心结论**: Pruning criterion shapes RLVR recovery capacity. CKA-only >> Standard >> Random >> RASP
- **关键决策链**: D099 α=4.0 RASP collapse 是 α-dependent → D100 追加 α=4.0 SFT eval → D101 C1 decoupling 初步确认 universal → D103 CKA-only MATH-500 修正 29.2%→26.6% → D104 三线并行扩展
- **α=4.0 已确认数据**: GRPO GSM8K = 62.77%（本次确认），SFT GSM8K = 60.71%*（running），α=4.0 将 RASP 从 collapse 翻转为超越 Standard（+2.93pp）
- **易错点**: (1) westd-32935 是 westd-29022 的克隆机，但数据盘独立，不要假设 westd-29022 上的 checkpoint 在 westd-32935 上存在 (2) MATH-500 数据之前有 @4096 vs @2048 混淆（D103 已修正），所有 MATH-500 数据以 @2048 为准 (3) Worker 池 = 0，下一个"你"应立即铺 CPU 任务（文献联动 / 论文 patch）满足 ≥2 约束


---
