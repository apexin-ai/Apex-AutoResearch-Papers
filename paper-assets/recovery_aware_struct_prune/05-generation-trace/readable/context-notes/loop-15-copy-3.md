# reviewer / loop_15.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_15.md`
- **Structured JSON:** [`d2e5f0c3d2a99eee349b.json`](../../sessions/d2/d2e5f0c3d2a99eee349b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_wall_time
updated: '2026-05-19T08:59:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 C005：westb-23072 cuda:0/1 + westd-29022 cuda:0/1/2/3。越界即 CRITICAL
- westb-23072 磁盘 250GB，当前 24GB free（已清理 unstructured checkpoint）。seed123 训练完成时需 ~12GB 存 checkpoint，余量够但紧张
- `eval_humaneval.py` 第 51 行已修复为 `sys.executable`（原 `["python", ...]` 导致 SFT CKA-only 假 0%）。所有新 HumanEval eval 必须用修复后的脚本
- Standard GRPO v5 fair checkpoint 路径是 `grpo_stage2_standard_20_fair`（不是 `grpo_standard_20_fair`），RASP 同理 `grpo_stage2_rasp_20_fair`

### 2. 🖥️ 基础设施快照
- **westd-29022**：`/root/autodl-tmp/recovery_aware_struct_prune/`，Python `/root/miniconda3/bin/python`
  - cuda:0 **空闲**（MATH-500 SFT Standard 已完成）
  - cuda:1 PID 78740：HumanEval SFT CKA-only v2 re-run（76/164, 46%）
  - cuda:2 PID 76392：HumanEval GRPO Standard fair v3（~30/164）
  - cuda:3 PID 74303：HumanEval GRPO RASP fair（~100/164）
- **westb-23072**：同路径
  - cuda:0 **空闲**（unstructured GSM8K eval 已完成）
  - cuda:1 PID unknown：grpo_cka_only_20_seed123 训练（~35/100, ~7h remaining）
- W&B entity/project 未配置，不可用。验证指标直接读 log/result JSON
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/`

### 3. 📊 当前状态
刚完成的审查：
- E2 Standard Extended 300步 GSM8K = 59.29%（Worker 错误声称 baseline 52-53%，实际 baseline 58.91%，已 CRITICAL 纠正）
- Unstructured GRPO GSM8K = 87.64%（PASS，完美支持 C1 decoupling + collapse=structural damage）
- GRPO CKA-only HumanEval final = **20.12%** (33/164)（interim 27.5% 过度乐观）
- MATH-500 SFT Standard = 25.8% (129/500)（PASS，完成 MATH-500 全表）
- **SFT CKA-only HumanEval 0% 是 PATH bug 假结果**（CRITICAL 已报 Director）→ v2 re-run 进行中

等待中的 eval（预计 1-3h）：
- `eval_humaneval_sft_cka_only_20_2048_v2`：re-run，确认 0% 是否真实（D070 基石）
- `eval_humaneval_grpo_standard_20_fair_2048_v3`：v5 fair 模型，interim ~5%
- `eval_humaneval_grpo_rasp_20_fair_2048`：v5 fair 模型，interim ~15%

Director 待办请求：
- "unstructured GRPO 结果出来后重新审查叙事一致性" → unstructured 已出，但需等 HumanEval re-run 后做完整 narrative review
- D070 C1 reframing 已审查（WARNING），等 re-run 数据确认后可能需要更新

### 4. 📋 待办（条件触发式）
- SFT CKA-only HumanEval v2 完成 → 如果仍 0%：D070 confirmed，发 PASS 报告；如果 >0%：D070 叙事需重大修改，发 CRITICAL
- GRPO Standard fair HumanEval 完成 → 对比 GRPO CKA-only 20.12%，评估 "CKA-only specific" claim 强度
- GRPO RASP fair HumanEval 完成 → 同上，组合三方法做完整 HumanEval narrative review
- 三个 HumanEval 全完成 → 执行 Director 要求的完整叙事一致性审查（D070 + unstructured + HumanEval 数据整合）
- seed123 训练完成（~7h后）→ 审查多 seed 验证结果，检查 CKA-only reward gradient 可复现性

### 5. 🎯 战略上下文
- **核心贡献**：C2 = Recovery Capacity Gradient（CKA-only >> importance-based），由 representational diversity 驱动。C1 = GRPO-accuracy decoupling（降级为 supporting analysis，D065）
- **D070/D071 reframing**：C1 从 "universal decoupling" 改为 "task-dependent"（SFT-recovered tasks decoupling，SFT-failed tasks GRPO recovery）。我已审查为 WARNING——"SFT 0% = strong task adaptation" 的 spin 不诚实，应改为 "catastrophic forgetting + GRPO partial recovery"
- **最容易判断错的事**：
  1. paper_framing.md 中 58.91%（Standard GRPO 100步 GSM8K）无 backing result file，可能来自 pre-fair 模型。只有 300步 59.29% 是完整可溯源的
  2. GRPO Standard/RASP HumanEval 有新旧模型两套数据——old (v8/v9) 和 fair (v5)。论文引用时必须区分
  3. SFT CKA-only HumanEval 0% 第一次是假结果（PATH bug）。v2 re-run 才是真数据，等它出来才能定论
  4. HumanEval interim 数字容易过度乐观（27.5% → 20.12%），不要在 final 出来前锁定 framing
- **Target venue**：EMNLP 2026 Main (ARR May 25)，~6 天


---
