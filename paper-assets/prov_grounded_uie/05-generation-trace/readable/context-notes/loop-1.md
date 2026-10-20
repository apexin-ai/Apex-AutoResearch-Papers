# director / loop_1.md

**prov grounded uie** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`4386e4f911cf975f6f1d.json`](../../sessions/43/4386e4f911cf975f6f1d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-12T15:34:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-rtxpro6000 的 cuda:0 和 cuda:1，严禁使用其他设备
- 术语：论文中统一用 "evidence provenance reward"，禁止用 "faithfulness reward"（与 MR-UIE 撞词）
- MVP kill criteria 对照组是 post-hoc NLI reranking（不是 SFT-only），差值 <2pt = kill
- RTX PRO 6000 Blackwell 单卡 96GB（不是 48GB），之前有过多次混淆
- aml-train 镜像用 conda 环境，不要创建 venv；pip install 前必须 `source /etc/network_turbo`

### 2. 🖥️ 基础设施快照
- **服务器**: autodl-rtxpro6000, connect.westd.seetacloud.com:37397, root, SSH key `~/.ssh/id_ed25519`
- **密码**: 存在 secret store `autodl_ssh_password`
- **工作目录**: `/root/autodl-tmp/prov_grounded_uie/`
- **Python**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` → Python 3.12, PyTorch 2.10+cu128
- **模型**: Qwen3-8B at `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`; DeBERTa NLI at `/root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large`
- **SFT merged model**: `/root/autodl-tmp/prov_grounded_uie/outputs/sft/merged/`
- **数据**: `./data/docred_train.jsonl` (3027), `./data/docred_dev.jsonl` (985)
- **本地代码**: `projects/prov_grounded_uie/artifacts/` (config.py, data_utils.py, evaluate.py, rerank_nli.py, rewards.py, train_grpo.py, train_sft.py)
- **W&B**: 未配置，MVP 用 `--report_to none`
- **活跃进程**: sft-eval worker 和 posthoc-nli worker 正在跑（具体 PID 需 SSH 确认，SFT 训练 PID 13271 已结束）
- **残留进程**: PID 12569 占 28GB GPU，是 v2 残留，我已指示 Agent kill 但未确认

### 3. 📊 当前状态
SFT v3 训练已完成（570/570, 1h18m, eval_loss=0.356, token_acc=92%）。双卡 DDP, max_seq_length=4096。

**正在并行执行**:
- cuda:0: sft-eval worker — 跑 evaluate.py 获取 RE F1 + Evi F1 锚点（Reviewer 报告 15:32 完成，但我尚未读到结果）
- cuda:1: posthoc-nli worker — 跑 rerank_nli.py（Step 3）
- GRPO 代码修复已完成（移除 max_prompt_length, vLLM 0.18.1 有警告但不阻塞）

**Registry**: sft_baseline_v1 DONE/failed(OOM), sft_baseline_v2 DONE/killed, sft_baseline_v3 DONE/success

### 4. 📋 待办
- sft-eval 结果到手 → **立即读 RE F1 + Evi F1**，这是 MVP 第一个关键锚点。如果 Evi F1 < 30 → gate 阈值需下调；如果 > 45 → +5pt pass 标准合理
- posthoc-nli 结果到手 → 对比 SFT baseline Evi F1 和 post-hoc NLI Evi F1，确认 post-hoc NLI 的提升幅度
- 两组结果都到 → 启动 Step 4 GRPO（train_grpo.py 已修复，双卡或单卡跑，命令需传 `--nli_model_name /root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large`）
- GRPO 完成 → Step 5 三组对比 + degeneration sanity checks → 判定 kill/inconclusive/pass
- pass → complete_mvp() 进入 research 阶段

### 5. 🎯 战略上下文
- **决策链**: D001(立项MVP) → D002(加post-hoc NLI对照+三档kill) → D003(MR-UIE阻塞) → D004(MR-UIE解除,novelty成立)
- **审稿评估 21% KILL_triage**，项目在边缘线上。MVP 必须证明 GRPO provenance reward > post-hoc NLI reranking，否则 kill
- **ProUIE 差异化已确认成立**：ProUIE SFR 不含 evidence 维度，ProvUIE 的 evidence provenance reward 是真正新增
- **MR-UIE 正交**：MR-UIE faithfulness = CoT 质量检查，不是 span-level grounding
- **幻影引用**: Ground-GRPO 和 LAT 不存在，需从论文中删除
- **易错点**: train_sft.py 远程版本有 3 处 hotfix（max_length, dataset_kwargs, flash_attn），本地 artifacts/ 版本已同步但要注意一致性；evaluate.py 和 rerank_nli.py 的 NLI 模型路径默认值是 HF ID 不是本地路径，AutoDL 离线环境必须传 `--nli_model_name` 本地路径
- **token 长度分布**: mean=1648, p95=3299, max=10140 — max_seq_length 必须 ≥ 4096，低于此截断严重影响 evidence 训练


---
