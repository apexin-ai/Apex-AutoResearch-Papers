# agent / loop_11.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_11.md`
- **Structured JSON:** [`2c726b4580950e8f5a6c.json`](../../sessions/2c/2c726b4580950e8f5a6c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: idle_timeout
updated: '2026-05-16T02:03:14+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: 仅 westd-16980 cuda:0 + cuda:1，无例外
- **CUDA_VISIBLE_DEVICES 禁止在 spec.command 内硬编码**——GPU 分配由 submit_training_job 的 gpu 参数统一控制。5/15 发生过级联故障：内层 CUDA_VISIBLE_DEVICES=0 覆盖外层注入导致双实验挤同一卡
- **训练脚本内部也不能 `os.environ["CUDA_VISIBLE_DEVICES"] = ...`**
- **SciERC 数据路径是 `data/processed_data/test.json`**（不是 `data/scierc/test.json`），constraints 在项目根 `ontology_constraints.json`（不在 data/scierc/ 下）
- **大 checkpoint 必须存 `/root/autodl-tmp/checkpoints/`**，根分区只有 30G
- kill_job 后必须 `nvidia-smi | grep python` 确认无孤儿进程残留

### 2. 🖥️ 基础设施快照
- **服务器**: westd-16980, account=root
- **工作目录**: `/root/schema_semantic_constrained_ie`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- **环境激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **GPU**: 2× NVIDIA RTX PRO 6000 Blackwell (94GB each), CUDA 12.8
- **框架**: torch 2.10.0+cu128, transformers 4.57.6
- **模型路径**:
  - Qwen base: `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`
  - Llama base: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`
  - Qwen DocRED merged: `/root/autodl-tmp/checkpoints/qwen_lora_docred_merged`
  - Llama DocRED merged: `/root/autodl-tmp/checkpoints/llama_lora_docred_merged`
  - Qwen SciERC merged: `/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged`
  - Llama SciERC merged: `/root/autodl-tmp/checkpoints/llama_lora_scierc_merged`
- **活跃进程**:
  - cuda:1: w5_qwen_docred_lora_constrained_eval, PID 321568 (GPU subprocess), wrapper tmux session, ~5-6h ETA from 01:56 UTC
  - cuda:0: w5_llama_docred_lora_constrained_eval, PID 317464 (wrapper) / 317469 (GPU subprocess), ~3.8h ETA from 00:31 UTC
- **Cron**: reconcile 返回 0 条活跃 cron（可能需要重新注册监控）
- **WANDB**: disabled（项目未配 wandb key）

### 3. 📊 当前状态
两个 DocRED constrained eval 正在双卡并行跑，这是 composability 4×4 matrix 的最后两格：

| Registry ID | GPU | 状态 | 进度 | ETA (from start) |
|---|---|---|---|---|
| w5_qwen_docred_lora_constrained_eval | cuda:1 | RUNNING | 2/998 at 01:56 UTC | ~5-6h |
| w5_llama_docred_lora_constrained_eval | cuda:0 | RUNNING (retry 1) | 11/998 at 00:31 UTC | ~3.8h |

**已完成的 matrix 进展** (SciERC 两模型已满, DocRED FT unconstrained 已满):
- Qwen SciERC: ✅ 完整 2×2 (DR=0.0%, ΔR-F1=-0.09pp)
- Llama SciERC: ✅ 完整 2×2 (DR=0.09%, ΔR-F1=+0.02pp)
- Qwen DocRED unconstrained eval: ✅ done
- Llama DocRED unconstrained eval: ✅ done (DR=0.5%, R-F1=43.72%)
- Qwen DocRED constrained eval: 🔥 RUNNING (cuda:1)
- Llama DocRED constrained eval: 🔥 RUNNING (cuda:0)

**等待中**: 无活跃 Worker, 无活跃 Cron。Cron 监控可能需要重新注册。
**PREPARING 但实际 killed/done**: w1_cf_fallback_llama_scierc (killed), w1_cf_fallback_llama_docred (killed), w5_llama_docred_sft_data_gen (success)

### 4. 📋 待办（条件触发式）
- **w5_llama_docred_lora_constrained_eval 完成 → spawn Worker 跑 eval metric 计算 → 提取 DR/R-F1/CF → update_registry(conclusion, metrics) → 填 Llama×DocRED composability 2×2**
- **w5_qwen_docred_lora_constrained_eval 完成 → 同上 → 填 Qwen×DocRED composability 2×2**
- **两个 constrained eval 都完成 → 完整 4 model×dataset matrix → spawn Worker 做全文数字一致性审查(paper 中 Table 3/5, §5.4/5.5, Appendix B 全部更新) → 汇报 Director**
- **若 constrained eval DR > 0 且 ΔR-F1 < 0.5pp → composability claim 成立，正常推进**
- **若 constrained eval ΔR-F1 > 1pp negative → 触发 red-section Framing 调整提案，先汇报 Director 再动 paper**
- **Cron 监控为空 → 下一轮 session 需检查进程是否还活着（可能 cron 被 reconcile 清掉了），必要时重新注册 cron 或手动 SSH 检查**
- **全部 matrix 填完 + paper 更新 → May 19 内部稿 → May 25 EMNLP ARR 提交**

### 5. 🎯 战略上下文
- **项目核心**: OntoCoDec = 两层约束解码（grammar + semantic）编译 IE ontology schema 为 token-level constraints。核心 novelty: "compile IE ontology domain/range → decoding-time logits masking" 完整 pipeline，gap 已文献确认。
- **当前阶段**: Round 1 审稿应对，composability (Claim 3) 是关键扩展——证明 OntoCoDec 在 fine-tuned model 上仍有价值（FT 内化大部分约束但 tight-constraint 长尾无法覆盖）。
- **决策链**: D020 CF fallback → analytical finding | D023 reframe Claim 3 composability | D025/D028 SciERC 2×2 两模型确认 | D029 kill+resubmit DocRED 训练
- **最容易判断错的事**:
  1. SIGTERM (exit 143) ≠ 失败——cron 检测 exit code ≠ 0 自动标 failed，但需验证 output 完整性（998/998 行写完就算成功）
  2. Llama constrained eval retry 1——之前 grammar 编译 96 relation types 耗时 ~9min 触发 wrapper 超时，实际非故障。脚本支持 --resume
  3. DocRED grammar_only 模式 DR 反升 (26.17% vs unconstrained 18.46%) 是已知行为——grammar 约束强制解析出更多 triples 导致违规基数增大，不是 bug
  4. **CF↔DR 根本性张力**: CF fallback 能消 CF 但 DR 暴增，budget 净增。这是 analytical finding 不是 negative result。不要试图"修复"CF——当前系统已近最优
  5. **constraint tightness 驱动 DR**: DocRED avg tightness=0.842 vs SciERC=0.333，DocRED zero-shot DR 更高是预期的
- **时间线**: May 19 内部稿, May 25 EMNLP ARR 提交。两个 constrained eval 是最后阻塞项。
- **目标分数路径**: 当前估 4.0/5，DocRED LoRA 全补完 → 4.25/5 (very strong accept)


---
