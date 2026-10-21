# director / loop_1.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`f6a812f7965ca5b1592e.json`](../../sessions/f6/f6a812f7965ca5b1592e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-15T02:51:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cqa1-38874 cuda:0（唯一分配的 GPU）
- BCS 计算必须用 max pairwise cosine similarity，不是 mean（compute_bcs.py 已修复，但新代码要继续遵守）
- 评估必须用 text-match（text.find() offset correction），不能用 exact match（模型 fabricate 96.5% 的 char offset）
- Few-NERD 必须用 fine_ner_tags（66 types），不是 ner_tags（8 types）
- Post-MVP 禁止批准新实验直到 Dream 回调处理完毕（post-mvp-kickoff skill Step 5）

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874 (connect.cqa1.seetacloud.com)，用户 root
- 工作目录：/root/schema-dag-extraction
- 模型：Qwen3-32B-FP8，通过 vLLM 0.20.2 serving（constrained JSON decoding）
- GPU：1× RTX PRO 6000 Blackwell (98GB)，cuda:0
- 数据：Few-NERD via HuggingFace datasets（66 fine-grained entity types，1000 test samples，64 active types）
- 关键代码：src/ 下 compute_bcs.py, run_experiment.py, run_extraction.py, evaluate.py, analyze_results.py, reeval_text_match.py, select_type_batches.py, few_nerd_utils.py
- 活跃进程：无（GPU 空闲，等 Agent 修复 exp3a）

### 3. 📊 当前状态
刚完成 post-MVP kickoff Steps 1-4：
- paper_framing.md 已写好（3 Core Claims: confusability independence / multi-channel degradation / SDGD effectiveness）
- experiment_plan.yaml 已写好（15 experiments, P0=23h, P1=20h, total ~43h）
- Dream 模拟已启动：dream_20260515T024826, review_mode=full, 等待回调
- ROADMAP 已更新为 research phase dashboard

Registry:
- exp001_count_baseline: ANALYZING（MVP 完成）
- exp002_confusability_controlled: ANALYZING (success)（MVP 完成）
- exp003a_prompt_v2_rerun: DONE (failed, EXIT_CODE=2 syntax error)

已派 Agent 诊断修复 exp3a 并重跑。GPU cuda:0 当前空闲。

### 4. 📋 待办
- Dream 回调 `[DREAM dream_20260515T024826] 完成` → Read dream-report-action skill → 分析三档审稿 → 决定是否调整 framing/plan → 达标则批准 P0 实验
- Agent 回复 exp3a 修复结果 → 确认重新提交成功 → GPU 恢复工作
- exp3a 完成后 → 批准 exp-004 (ACE05) + exp-008 (SDGD-zero) + exp-012 (multi-model) 并行铺开（如只有 1 GPU 则串行排优先级）
- 如 Dream 报告指出需要第二个模型才够 reviewer 信服 → director_post_to_manager 申请第二张 GPU 跑 exp-012

### 5. 🎯 战略上下文
- 决策链：D001(立项) → D002(统计功效修正) → D003(Δ→within-count r) → D004(F1→recall主指标) → D005(MVP PASS, Narrative A)
- MVP 核心发现：confusability 的降级通道是 type confusion（标错类型），不是 entity omission（遗漏实体）。这比原假设更精确，是论文的关键 insight
- F1 curve 反转是 over-prediction confound（低 count 时 pred/gold=6.8x），recall 才是干净的 count degradation 信号。写论文时必须解释清楚
- 易错点1：exp3a 之前因 syntax error 失败，不要以为它已经跑过了——数据还没有
- 易错点2：不要在 Dream 回调之前批准 P0 实验（post-mvp-kickoff skill 硬约束）
- 时间极紧：ARR May 25 只剩 10 天，43h GPU 工作量，必须保持 GPU 零空闲
- 多模型验证（exp-012）是最可能被 reviewer 攻击的短板，但也是 GPU 需求最大的实验（6h + 可能需要第二张卡）


---
