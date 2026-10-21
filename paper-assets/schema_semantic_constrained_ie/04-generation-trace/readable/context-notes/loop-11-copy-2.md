# reviewer / loop_11.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`7ef8f2aefd097a39b4f2.json`](../../sessions/7e/7ef8f2aefd097a39b4f2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-16T03:19:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：cuda:0 + cuda:1（westd-16980 双卡）。当前分配：Llama→cuda:0, Qwen→cuda:1。W6 Mistral 实验必须等当前卡空出才能跑，不可越界。
- DocRED constrained eval 输出文件路径已锁定：`outputs/w5_llama_docred_lora_constrained_eval.jsonl` 和 `outputs/w5_qwen_docred_lora_constrained_eval.jsonl`。不要删除或覆盖——支持 `--resume`。
- Limitations 节当前仍写 "DocRED fine-tuning is not reported"——constrained eval 完成后必须更新，否则论文自相矛盾。
- W6 Mistral 三实验 registry spec 为空（零字段），已上报 Director。启动前必须要求补全 spec，否则无法追溯审查。

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980 (root)，2× NVIDIA RTX PRO 6000 Blackwell (98GB each)
- 工作目录：`/root/schema_semantic_constrained_ie`
- Python：`/root/miniconda3/bin/python3`（conda base 环境，无 venv）
- 模型路径：
  - Qwen3-8B: `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`
  - Llama-3.1-8B: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`
  - Qwen LoRA DocRED merged: `/root/autodl-tmp/checkpoints/qwen_lora_docred_merged`
  - Llama LoRA DocRED merged: `/root/autodl-tmp/checkpoints/llama_lora_docred_merged`
  - Mistral: **未下载**，脚本在 `/root/schema_semantic_constrained_ie/download_mistral.sh`，目标 `mistralai/Mistral-7B-Instruct-v0.3`
- 数据集：SciERC `data/processed_data/test.json` (551), DocRED `data/docred/dev.json` (998)
- 无 W&B 配置（本项目不检查 W&B）
- 活跃进程（截至 handoff）：
  - Llama constrained eval: PID 317469 (wrapper 317464), cuda:0, tmux session, 621/998
  - Qwen constrained eval: PID 321568 (wrapper 321563), cuda:1, tmux session, 217/998

### 3. 📊 当前状态
刚完成：审查 `worker_paper_composability_update_prep` 产出——论文 section5_composability.tex SciERC 表数字全部与 registry 一致（已逐格核对）。向 Director 上报了 5 条发现（ROADMAP 16h+ 过时、W6 Mistral spec 空、Mistral 模型版本可能过旧、运行中实验正常、registry 状态不一致）。

RUNNING：
- `w5_llama_docred_lora_constrained_eval`: 621/998 (62%), cuda:0, ~3.8 samples/min, ETA ~1.5h
- `w5_qwen_docred_lora_constrained_eval`: 217/998 (22%), cuda:1, ~2.9 samples/min, ETA ~4.5h

PREPARING（活跃）：
- `w6_mistral_scierc_unconstrained`, `w6_mistral_scierc_constrained`, `w6_mistral_docred_unconstrained` — 空壳注册，无 spec

PREPARING（遗留，需清理）：
- `w1_cf_fallback_llama_scierc` (conclusion=killed), `w1_cf_fallback_llama_docred` (conclusion=killed), `w5_llama_docred_sft_data_gen` (conclusion=success) — status 未同步

### 4. 📋 待办（条件触发式）
- **Llama constrained eval on_complete 回调** → 立即审查 metrics：DR 应 ≈0%，R-F1 delta vs unconstrained (43.72) 应 <0.5pp。交叉核对输出文件行数=998。
- **Qwen constrained eval on_complete 回调** → 同上审查。额外关注 parse_fail_rate 是否与 unconstrained (7.11%) 一致或更高（constrained 模式通常更慢，超时风险更大）。
- **两个 constrained eval 均完成** → 审查论文更新：section5_composability.tex 应新增 DocRED 行，Limitations 应删除 "DocRED fine-tuning is not reported"。数字一致性全文审查。
- **W6 Mistral 实验转 RUNNING** → 检查 spec 是否已补全、GPU 分配是否合规、模型是否已下载。Mistral-7B-Instruct-v0.3 版本问题已上报，看 Director 决策。
- **ROADMAP 更新通知** → 核对是否反映了 DocRED 完整 2×2 + Mistral 计划。

### 5. 🎯 战略上下文
- **核心结论 Claim 3**：Fine-tuning 和 constrained decoding 互补——FT 提 F1，constraints 确保 long-tail compliance。SciERC 已双模型确认（Qwen DR 1.95→0.00%, Llama DR 1.11→0.09%, F1 delta <0.1pp）。DocRED 即将补完。
- **决策链**：D020 CF fallback→analytical finding / D023 reframe Claim 3 / D025+D028 SciERC composability 确认 / D029 DocRED 训练重提交
- **最易判断错的事**：
  1. 不要因为 Qwen parse_fail_rate 7.1% 就判定实验失败——Agent 已添加 excl_fail 指标变体，这是已知的 Qwen 长文档超时问题，不是 bug。
  2. Mistral v0.3 版本问题——已上报但 Director 未回复。不要自行决定"版本太旧不跑"，等 Director 决策。版本选择可能有参数量匹配 (7B 级) 的合理理由。
  3. ROADMAP 极度过时（最后更新 15T18:13），不要把 ROADMAP 当 ground truth——以 registry 为准。
  4. `discussion_cf_fallback.tex` 是独立文件但未被 `main.tex` include（主文用 `appendix_discussion.tex` 包含同内容），可能是历史草稿残留，不影响 PDF 输出。


---
