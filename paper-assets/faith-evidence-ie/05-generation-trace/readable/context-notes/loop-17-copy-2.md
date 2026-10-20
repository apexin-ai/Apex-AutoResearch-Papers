# reviewer / loop_17.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_17.md`
- **Structured JSON:** [`dd8de79f9522fb3d14f0.json`](../../sessions/dd/dd8de79f9522fb3d14f0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_wall_time
updated: '2026-05-21T19:41:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：rtx5090-4x 的 cuda:0-3（4张 RTX PRO 6000 96GB）。越界进程立即 critical + kill
- 4B SFT adapter 路径：`/root/autodl-tmp/sft_output`（标准）或 `/root/autodl-tmp/sft_output_seed{43,44}`（seed-specific）。**绝对不能用** `sft_no_evidence_output`（plan_014 错误 adapter，M027 事故根因）
- Evidence tax 必须用 matched@2048：两个条件都用 max_new_tokens=2048，同一个 SFT adapter + `--no_evidence` flag 切换。@1024 结果能翻转 tax 符号（D140 s42 案例）
- fair_tax_pp Worker 约定：no_evi - with_evi（正值 = evidence 有害），与 Reviewer 的 raw tax（with - no）符号相反

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (connect.westd.seetacloud.com:37389, root)，备用 bjb2-12179
- 工作目录（远程）：`/root/autodl-tmp/freige`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/`
- Python：conda base `/root/miniconda3/bin/python`，PyTorch 2.8.0+cu128
- 模型路径：`/root/autodl-tmp/models/Qwen3-{1.7B,4B,8B,14B}`，LLaMA `/root/autodl-tmp/models/Llama-3.1-8B-Instruct`
- SFT adapters：`/root/autodl-tmp/sft_output*`（各 scale/seed）
- Eval 结果：`/root/autodl-tmp/eval_results/`
- 活跃进程（截至 handoff）：cuda:0 test_eval_4b_sft_s42, cuda:1 test_eval_14b_sft_s42, cuda:2 test_eval_8b_sft_s42, cuda:3 test_eval_llama_sft_s42 (PREPARING)

### 3. 📊 当前状态
刚完成 **3-seed 4B matched@2048 evidence tax 终版审查**：fair_tax = +0.25 ± 0.47pp（≈0，threshold narrative 成立）。已 post 给 Director。

**RUNNING/PREPARING 实验：**
- test_eval_4b_sft_s42 (cuda:0) — 4B SFT test eval，~7% 完成，~4h
- test_eval_14b_sft_s42 (cuda:1) — 14B SFT test eval，~6% 完成，~5h
- test_eval_8b_sft_s42 (cuda:2) — 8B SFT test eval，~8% 完成，~4h
- test_eval_llama_sft_s42 (cuda:3) — LLaMA SFT test eval，刚进 PREPARING

**等待中：**
- 上述 4 个 test eval 的 cron on_complete 回调
- 4B RSFT test eval 仍阻塞（原 checkpoint-510 删除，retrain 被 kill，Worker 查 bjb2 备份无果）
- 1.7B SFT test eval 未提交（无空闲 GPU）

### 4. 📋 待办
- test_eval_{14b,8b,4b}_sft_s42 完成 → 读 metrics.json 核实 adapter/seed/数字，与 RSFT test 配对构建完整 test scaling table
- test_eval_llama_sft_s42 完成 → 同上，注意 LLaMA SFT cross-seed 极不稳定（s44=0.4802 vs s42=0.5384）
- 所有 SFT test 出齐 → 计算 test set 上的 SFT→RSFT gain，与 dev 上的 gain 对比
- cuda 释放 → 提醒 Director 提交 1.7B SFT test eval（test table 最后空缺）
- 4B RSFT checkpoint 重建方案确定 → 审查重训配置是否与原训练一致
- Director 转发 paper patch 审查 → 加载 paper-quality-lessons skill，按模式 B 审

### 5. 🎯 战略上下文
**核心结论链**：D137（matched@2048 方法论）→ D143（M027 错误修正）→ D144（Qwen 3-scale tax）→ D145（paper_framing 修正）

**Evidence tax landscape（全部 Reviewer verified）：**
| Scale | Fair Tax | Direction |
|-------|---------|-----------|
| 1.7B Qwen | -5.63pp | evidence helps |
| 4B Qwen (3-seed) | +0.25±0.47pp | neutral |
| 8B Qwen | +0.04pp | neutral |
| LLaMA 8B (3-seed) | -5.19±5.25pp | helps but unstable |

**叙事**：within-family threshold（1.7B↔4B 之间）+ cross-architecture variation（Qwen 8B ≈0 vs LLaMA 8B -5.19pp）+ variance compression（所有 scale 7-31×）

**易错点**：
1. 不要混淆 raw tax 和 fair tax 的符号约定（Worker 用 no-with，正=hurt）
2. 4B cross-seed ign_f1 variance 极大（s42=0.3946, s44=0.4665, Δ=7.2pp），但 evidence tax 稳定（0.47pp std）——这两个 variance 是不同维度
3. Test set 上 ign_f1 = f1（无 train_annotated.json），dev→test gap 一致在 ~20-22pp，是 gold density 差异造成的（test 34.7 vs dev 12.3 triples/doc），不是 bug
4. ROADMAP 的"正在运行"表和 report.md 的资源状态可能滞后，以 registry + nvidia-smi 为准


---
