---
loop: 2
reason: max_messages
updated: '2026-05-12T22:48:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0 / cuda:1（westd-37397 的 2×RTX PRO 6000 96GB）
- AutoDL 根分区 ~30GB，模型/数据/HF cache 必须放 `/root/autodl-tmp/`
- HF 下载必须设 `HF_HUB_DISABLE_XET=1`，pip/git 前必须 `source /etc/network_turbo`
- vLLM 在 Blackwell + torch 2.10.0 上完全不可用（0.17.1 和 0.18.1 都报 `duplicate template name`），不要再尝试
- Qwen3-8B 有 thinking mode：temperature>0 采样时会生成 `<think>...</think>` 消耗全部 tokens。GRPO 训练必须禁用 thinking mode

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397，工作目录 `/root/autodl-tmp/prov_grounded_uie/`（推测，需确认）
- Python：系统 Python 或 conda base（需确认），torch 2.10.0 + transformers 4.57.6 + TRL 1.1.0
- SFT 模型：`./outputs/sft/merged`（Qwen3-8B SFT checkpoint，训练完成 570/570 steps）
- NLI 模型：`/root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large`
- 数据集：`./data/docred_dev.jsonl`（985 条 dev set）
- 代码：`src/` 下有 train_grpo.py, evaluate.py, rerank_nli.py, rewards.py, config.py, data_utils.py
- 活跃进程：sft_eval_v4 PID 40391 (cuda:0, batch=8, max_length=4096)，约 60min 运行中
- vLLM 版本：0.18.1（不可用，仅 HF native generation）

### 3. 📊 当前状态
**sft_eval_v4 (RUNNING, cuda:0)**：修复后的 SFT baseline 评估（batch=8, max_prompt_length=4096），已跑 ~60min，约 400/985 完成（RE-F1≈0.29 中间值）。cron 监控中。

**已完成/失败**：
- sft_baseline_v3: DONE(success)，训练 570 steps / 1h18m / eval_loss=0.356
- sft_eval_v3: DONE(failed)，进程卡死 6h+ 零产出（旧代码 max_length=2048 + 逐条推理）
- posthoc_nli_v1: DONE(failed)，同上

**GRPO 阻塞项（已发指令给 Agent 修复）**：
- Qwen3 thinking mode 导致 reward 全零——已指令 Agent 修改 tokenizer.chat_template 禁用 thinking
- HF native generation + max_completion_length=2048 单卡 OOM——计划 eval 完成后用 2 卡训练
- Agent 应正在执行 thinking mode 修复，可能还未汇报

### 4. 📋 待办（条件触发式）
- sft_eval_v4 完成（cron 回调）→ 读取 eval_results_v2.json，提取 RE F1 / Evi F1，更新 registry DONE
- sft_eval_v4 DONE → 串行跑 rerank_nli_v2（cuda:1, `--predictions_file ./outputs/sft/eval_results_v2.json --batch_size 8 --max_prompt_length 4096`）
- rerank_nli_v2 完成 → 完整对比表（SFT baseline Evi F1 vs post-hoc NLI Evi F1），评估 kill criteria
- Agent 汇报 thinking mode 修复完成 → 验证 GRPO 单样本生成无 `<think>` + reward > 0
- thinking mode 修复验证通过 + eval 对比表就绪 → 提交 GRPO 2 卡训练审批（bf16 + gradient_checkpointing + use_vllm=False + max_completion_length=2048）

### 5. 🎯 战略上下文
- **核心假设**：将 evidence provenance 作为 GRPO 可验证奖励，训练 LLM 在 UIE 时同步输出证据跨度
- **Kill Criteria**：Evi F1(GRPO) - Evi F1(post-hoc NLI) ≥ 5pt 为 Pass，< 2pt 为 Kill
- **决策链**：D001(立项) → D002(加 post-hoc NLI baseline) → D003(MR-UIE 精读) → D004(阻塞解除，MR-UIE ≠ ProvUIE)
- **易错点**：
  - 不要再尝试 vLLM，Blackwell + torch 2.10 彻底不兼容
  - GRPO 必须 2 卡才能跑 max_completion_length=2048（单卡 OOM at backward）
  - evaluate.py 用 greedy (T=0) 不触发 thinking mode，但 GRPO 用 sampling (T=0.7) 会触发——两者行为不同
  - 之前 sft_eval_v3/posthoc_nli_v1 卡死 6h 的根因不明确（可能是旧代码逐条推理 + 某种死锁），修复后代码已正常工作
  - 代码修复已同步到服务器（旧文件备份在 `_backup_v1/`），但注意 thinking mode 修复可能还未同步
