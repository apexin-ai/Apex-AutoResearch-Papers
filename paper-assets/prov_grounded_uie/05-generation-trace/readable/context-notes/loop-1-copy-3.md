# reviewer / loop_1.md

**prov grounded uie** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`30196ca0530a4069d544.json`](../../sessions/30/30196ca0530a4069d544.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-12T15:35:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（`config/projects/prov_grounded_uie.yaml` line 6-8）
- 服务器：autodl-rtxpro6000，账号 root——不要连其他服务器
- NLI 模型路径必须传本地路径 `--nli_model_name /root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large`，HF ID 在 AutoDL 离线环境会失败
- 术语红线：用 "evidence provenance reward" 不用 "faithfulness reward"（防与 MR-UIE 撞词，D004 决策）

### 2. 🖥️ 基础设施快照
- 服务器：autodl-rtxpro6000(root)，工作目录 `/root/autodl-tmp/prov_grounded_uie`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型 HF cache：`/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`
- NLI 模型：`/root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large`
- SFT merged checkpoint：`/root/autodl-tmp/prov_grounded_uie/outputs/sft/merged`
- 数据：`./data/docred_train.jsonl` (3027条), `./data/docred_dev.jsonl` (985条)
- GPU：2×NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB (~96GB) each
- 活跃进程（截至 handoff 时）：sft_eval_v3 推理中（PID 17587/17840 on GPU0, PID 17369 on GPU1）
- W&B：SFT 训练用 `--report_to none`，未接入 wandb

### 3. 📊 当前状态
**刚完成**：SFT v3 训练成功审查 + cuda1-prep worker 审查 + GRPO max_prompt_length 修复验证。

**Registry 实验状态**：
- `sft_baseline_v1`: DONE/failed (OOM)
- `sft_baseline_v2`: DONE/killed (截断问题，我警告后 Director 终止)
- `sft_baseline_v3`: DONE/success (eval_loss=0.356, 570 steps, 1h18m, 双卡 DDP)
- `sft_eval_v3`: PREPARING → 实际在运行（GPU 100%），等结果
- `posthoc_nli_v1`: PREPARING → 可能等 eval 完后启动

**等待中**：sft_eval_v3 完成回调（RE F1 + Evi F1 锚点）

### 4. 📋 待办
- sft_eval_v3 结果出来 → 核实 RE F1 和 Evi F1 数值，这是 kill criteria 基准。关注 Evi F1 是否合理（DocRED evidence 是 sentence-level，F1 应有可比文献参考值）
- posthoc_nli_v1 结果出来 → 核实 NLI reranking 后 Evi F1 提升幅度，确认 ceiling 值。检查 `--nli_model_name` 是否用了本地路径
- GRPO 训练启动时 → (1) GPU 边界检查 (2) 验证 vLLM 0.18.1 与 TRL 兼容性 (3) evidence span 长度分布监控（退化检查：avg length < 50% sentence → warning）
- GRPO 结果出来 → kill criteria 判定：GRPO Evi F1 vs post-hoc NLI Evi F1 差值，<2pt kill / 2-4pt inconclusive / ≥5pt pass；RE F1 回归 ≤2pt

### 5. 🎯 战略上下文
- **决策链**：D001(MVP launch) → D002(加 post-hoc NLI baseline + 3-tier kill) → D003(MR-UIE 阻塞) → D004(阻塞解除，术语改名)
- **核心假设**：GRPO with evidence provenance reward 能内化 NLI-quality evidence selection，超过 post-hoc reranking ≥5pt Evi F1 且 RE F1 回归 ≤2pt
- **已验证差异化**：ProUIE(SFR 无 evidence 维度)、MR-UIE(faithfulness≠evidence grounding)、R2GRPO(真实但方向不同)
- **易错点**：
  - Worker 报告可能包含错误信息（如 "24B 模型" 实际是 8B）——始终用 registry + SSH 独立验证
  - vLLM 版本不兼容是悬而未决的风险，GRPO 启动时可能突然崩
  - DocRED token p99=4909, max=10140——如果 Agent 再次降 seq_length，要再次警告截断问题
  - W&B 未接入——无法用 fetch_wandb_metrics 交叉验证，只能靠 registry + SSH 日志


---
