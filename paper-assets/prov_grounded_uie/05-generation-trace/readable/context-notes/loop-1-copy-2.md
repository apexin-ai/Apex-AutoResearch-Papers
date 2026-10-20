# agent / loop_1.md

**prov grounded uie** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`d1cf3cc83142aae347f0.json`](../../sessions/d1/d1cf3cc83142aae347f0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-12T17:00:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-rtxpro6000 的 cuda:0 和 cuda:1，不可用其他设备
- NLI 模型必须用本地路径 `/root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large`，HF ID 在 AutoDL 离线环境会失败
- Qwen3-8B 本地路径 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`，同理不可用 HF ID
- submit_training_job 命令必须 `bash -c "source ... && conda activate base && ..."` 包裹（tmux 用 sh 不是 bash）
- 术语用 "evidence provenance reward" / "grounding reward"，不用 "faithfulness reward"（避免 MR-UIE 撞词）
- max_seq_length=4096 不可降低（Director 明确指令：截断破坏 evidence co-prediction 训练信号）

### 2. 🖥️ 基础设施快照
- 服务器：autodl-rtxpro6000 (connect.westd.seetacloud.com:37397, root)，2×RTX PRO 6000 96GB
- 工作目录：`/root/autodl-tmp/prov_grounded_uie/`
- Python：`/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 镜像：aml-train（conda 环境，不是 venv）
- tmux：v3.2a 已安装
- 模型：Qwen3-8B → `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`；DeBERTa NLI → `/root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large`
- SFT merged checkpoint：`/root/autodl-tmp/prov_grounded_uie/outputs/sft/merged/`
- 数据：train 3027 条 `./data/docred_train.jsonl`，dev 985 条 `./data/docred_dev.jsonl`
- Token 长度分布：mean=1648, p50=1443, p90=2725, p95=3299, p99=4909, max=10140
- W&B：未配置，MVP 阶段用 `--report_to none`
- 活跃进程：sft_eval (PID 17840, cuda:0)，posthoc_nli (PID 17369, cuda:1)
- Cron：sft_eval_v3 (PID 17835, 300s interval)，posthoc_nli_v1 (PID 17369, 300s interval)

### 3. 📊 当前状态
SFT v3 训练已完成（570/570 steps, eval_loss=0.356, 双卡 DDP, 1h18m）。正在等两个评估完成：
- **sft_eval_v3** (RUNNING, cuda:0)：evaluate.py 跑 985 条 dev set，已运行 ~1.5h，预计还需 30-60min。输出→ `./outputs/sft/eval_results.json`
- **posthoc_nli_v1** (RUNNING, cuda:1)：rerank_nli.py post-hoc NLI reranking，同期启动。输出→ `./outputs/posthoc_nli/eval_results.json`

GRPO 代码已修复并同步到服务器（3 个 warning 全修，NLI 设备隔离/默认路径/report_to）。但有一个 **未决的 Director 决策**：`max_prompt_length` 在 TRL 1.1.0 GRPOConfig 中不存在，需要决定是数据预处理截断还是查 TRL 内置机制。

Registry 状态：sft_baseline_v1 DONE/failed (OOM), sft_baseline_v2 DONE/killed, sft_baseline_v3 DONE/success, sft_eval_v3 RUNNING, posthoc_nli_v1 RUNNING。

### 4. 📋 待办（条件触发式）
- **sft_eval_v3 cron 回调（进程退出）** → spawn worker 读取 `eval_results.json` → update_registry(metrics: RE F1 + Evi F1) → 汇报 Director 锚点数据
- **posthoc_nli_v1 cron 回调（进程退出）** → spawn worker 读取结果 → update_registry → 汇报 Director（NLI reranking oracle upper bound）
- **两个 eval 都完成** → 汇报 Director 完整对比表（RE F1 / Evi F1 baseline vs post-hoc），应用 kill criteria：Evi F1(GRPO) - Evi F1(post-hoc) < 2pt → Kill; ≥ 5pt → Pass
- **Director 回复 max_prompt_length 决策** → 执行相应方案（A: 数据预处理截断 / C: 确认 TRL 内置机制）→ 准备 GRPO 提交命令
- **两个 eval 完成 + GRPO 代码就绪** → 立即提交 GRPO 训练（双卡 DDP 或单卡，取决于 reward 函数 NLI 是否需要独立 GPU）

### 5. 🎯 战略上下文
- **项目核心**：ProvUIE = evidence span co-prediction 作为 GRPO verifiable reward 用于 UIE。与 MR-UIE 正交（已验证，低威胁）。
- **MVP 路径**：Step 0-1 ✅ → Step 2 SFT ✅ → Step 3 eval + NLI rerank (进行中) → Step 4 GRPO → Step 5 对比
- **Kill criteria**：Evi F1(GRPO) - Evi F1(post-hoc NLI) < 2pt → Kill 项目; ≥ 5pt → Pass。这是整个 MVP 的生死线。
- **易错点 1**：TRL 1.1.0 API 变更频繁——`max_seq_length` → `max_length`，`max_prompt_length` 不在 GRPOConfig。不要假设参数名，先 `--help` 验证。
- **易错点 2**：GRPO 的 reward 函数中 NLI 模型默认在 CPU 跑（已改），不要改回 cuda，否则与主模型竞争显存 OOM。
- **易错点 3**：posthoc-nli worker 可能还在运行（上次 check 时仍活跃），不要重复 spawn。先 `get_worker_status` 确认。
- **决策链**：D001 MR-UIE 新颖性→低威胁 → D002 MVP 执行批准 → D003 max_length=4096 不可降（evidence 完整性） → D004 max_prompt_length 待决


---
