# agent / loop_12.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_12.md`
- **Structured JSON:** [`bbecfbf01cc6543ab2b7.json`](../../sessions/bb/bbecfbf01cc6543ab2b7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: idle_timeout
updated: '2026-05-16T03:21:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：`gpu_ids=[0,1,2,3]`（rtx5090-4x），另有 bjb2-12179 备用服务器但未分配 GPU
- Eval 统一协议（D076）：`batch_size=4 + max_new_tokens=1024 + --no-quantize + --sft_adapter + 正确 seed + CUDA_VISIBLE_DEVICES 显式`。**任何 eval 提交必须严格遵守**，旧协议数据不可用于 paired t-test
- Checkpoint 路径陷阱：`rsft_output_r2b/` 是废弃实验（lora_alpha=32/160步），**不是** CED s42。`rsft_output_s44/`（无 `_ced`）才是 CED s44。详见 memory.md 路径映射表
- 所有命令 cwd 必须 `cd /root/autodl-tmp`，不是 `cd /root/autodl-tmp/freige`
- C3 已降级（D056）——CED vs flat-NLI 统计不可区分，不作为独立贡献

### 2. 🖥️ 基础设施快照
- **服务器**: rtx5090-4x（4× RTX 5090 32GB），工作目录 `/root/autodl-tmp`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **模型**: `/root/autodl-tmp/models/Qwen3-4B`（底座），`/root/autodl-tmp/sft_output`（SFT adapter）
- **数据**: `/root/autodl-tmp/data/docred`（985 docs dev）
- **HF cache**: `/root/autodl-tmp/.hf_cache`（离线模式 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`）
- **RSFT checkpoints**: 8 个（4 CED × 4 flat-NLI，路径见 memory.md 映射表）
- **活跃进程**:
  - eval_rsft_ced_s45: PID 283838, tmux session, cuda:2, ~28% done, ETA ~04:18 UTC
  - eval_rsft_ced_s43: PID 286587, tmux session, cuda:1, ~2% done, ETA ~05:19 UTC
  - eval_plan_014_no_evidence_r2: PID 288109, tmux session, cuda:0
  - reeval_flat_nli_s43_r2: PID 291003, tmux session, cuda:3
- **Cron**: 4 个活跃，分别监控上述 4 个 RUNNING 实验
- **Workers**: 1 个 running（`worker_infra_audit_seed_comparison_script`，审计 seed comparison 脚本）
- **脚本**: `/root/autodl-tmp/scripts/seed_comparison.py`（自动发现 seeds + paired t-test + bootstrap）

### 3. 📊 当前状态
4 张 GPU 全部在跑 eval，均为 paired t-test 关键路径数据点：
| GPU | exp_id | 内容 | 进度 |
|-----|--------|------|------|
| cuda:0 | eval_plan_014_no_evidence_r2 | no-evidence SFT baseline eval (C1 ablation) | 运行中 |
| cuda:1 | eval_rsft_ced_s43 | CED RSFT s43 eval（第 4 个 CED seed） | ~2%, ETA 05:19 |
| cuda:2 | eval_rsft_ced_s45 | CED RSFT s45 eval（第 3 个 CED seed） | ~28%, ETA 04:18 |
| cuda:3 | reeval_flat_nli_s43_r2 | flat-NLI s43 统一协议重跑 | 运行中 |

**PREPARING 队列**（等 GPU 释放）:
- reeval_ced_s44（已指定 cuda:3）
- reeval_ced_s42
- reeval_flat_nli_s42
- seed_comparison_prep（分析任务，非 GPU）

**等待中**:
- 1 个 Worker 回调（audit seed comparison script）
- 4 个 Cron 回调（上述 RUNNING 实验完成时触发）
- 无待处理 Director 决策

### 4. 📋 待办（条件触发式）
- eval_rsft_ced_s45 完成（cuda:2 释放）→ 提交 reeval_ced_s42 或 reeval_flat_nli_s42（先到先用）
- eval_plan_014_no_evidence_r2 完成（cuda:0 释放）→ 提交 reeval_flat_nli_s42 或 reeval_ced_s42
- reeval_flat_nli_s43_r2 完成（cuda:3 释放）→ 提交 reeval_ced_s44（已预分配 cuda:3）
- eval_rsft_ced_s43 完成（cuda:1 释放）→ 提交剩余 PREPARING 实验
- 所有 8 个统一协议 eval 完成 → 运行 seed_comparison.py 生成最终 paired t-test → 汇报 Director
- seed comparison 结果出齐 → plan_002 test set eval（最终论文数据）+ plan_003 EDCR diagnostic + paper retitle
- Worker audit 回调 → 检查 seed_comparison.py 是否有问题，有则修复

### 5. 🎯 战略上下文
**项目核心**: FREIGE — evidence-grounded DocRE 系统性研究。三个 claims：
1. **C1 Evidence Tax**: evidence 生成代价 ~8pp rel_f1，no-evidence SFT=0.4893 vs evidence-SFT=0.4106（已确认）
2. **C2 Decoupling**: QLoRA GRPO 导致 catastrophic task decoupling（QLoRA-specific，bf16 不复现）。Spectrum: GRPO QLoRA > GRPO bf16 > DPO bf16 > RSFT none
3. **C3 降级**: CED vs flat-NLI 统计不可区分，不再作为独立贡献。CED reranker 恢复 97% evidence tax 仍有价值

**当前关键路径**: D076 协议审计发现旧 eval 混用 batch_size/max_new_tokens，4/8 个 seed eval 需重跑。重跑后才能做有效 paired t-test。这是论文 C3 统计基础和主表数据的前置条件。

**易错点**:
- 不要用旧 eval 结果（metrics.json）做统计对比，必须用统一协议重跑的结果
- flat-NLI checkpoint 是 507 步，CED 是 510 步——两者训练数据量略有不同（flat-NLI 2028 vs CED 2040 samples），这是正常的
- `rsft_output/` = CED s42（没有 `_ced` 后缀），`rsft_output_s44/` = CED s44（没有 `_ced` 后缀）——命名不一致是历史遗留
- EMNLP ARR July ~7月15-25，还有约 2 个月，时间充裕但 eval 重跑 + test eval + paper 写作是串行依赖链


---
