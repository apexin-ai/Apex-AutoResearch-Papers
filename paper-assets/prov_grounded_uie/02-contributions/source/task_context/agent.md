---
loop: 2
reason: max_wall_time
updated: '2026-05-12T23:08:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：只能用 `westd-37397:cuda:0` 和 `cuda:1`，其他 GPU 未分配
- **vLLM 不可用**：torch 2.10.0 + vLLM (任何版本) 在 Blackwell SM120 上 `AssertionError: duplicate template name`，已验证 0.17.1 和 0.18.1 都不行。GRPO 必须用 `--use_vllm False` (HF native generation)
- **GRPO 采样参数必须设 top_k=20, top_p=0.95**：TRL 默认 top_k=0 导致 Qwen3 不生成 EOS → completions 全截断 → reward=0。这是反复验证过的根因，不要改回默认值
- **max_completion_length=2048 单卡 OOM**（峰值 85GB），正式训练必须 2 卡 DDP。单卡最大 1024
- eval 脚本的 max_prompt_length 必须 4096（匹配 SFT 训练），2048 会截断 30-50% DocRED 样本

### 2. 🖥️ 基础设施快照
- **服务器**：`westd-37397`，8× RTX PRO 6000 Blackwell (SM120)，每卡 ~98GB
- **工作目录**：`/root/autodl-tmp/prov_grounded_uie`（代码在 `src/`）
- **Python**：`/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型**：SFT merged checkpoint `/root/autodl-tmp/prov_grounded_uie/outputs/sft/merged`（Qwen3-8B bf16）
- **NLI 模型**：`/root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large`（本地路径，必须显式传 --nli_model_name）
- **数据集**：`/root/autodl-tmp/prov_grounded_uie/data/docred_dev.jsonl`（985 条）
- **本地 artifacts**：`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/prov_grounded_uie/artifacts/`
- **活跃进程**：sft_eval_v4 PID=40391 cuda:0（cron 已注册，约 46% 进度 @ handoff 时刻）
- **chat_template.jinja 已修改**：无条件输出 `<think>\n\n</think>\n\n`，禁用 thinking mode
- **环境版本**：torch 2.10.0+cu128, transformers 4.57.6, trl 1.1.0, vllm 0.18.1（装了但不能用）

### 3. 📊 当前状态
**刚完成**：GRPO 端到端验证通过（reward=0.4804, mean_length=743.8, train_loss=-0.1361）。采样参数 + thinking mode + jinja 模板全部修复。代码同步 Worker (sync-all-fixes) 可能还在跑。

**Registry**：
- `sft_eval_v4` RUNNING — 正式 eval（batch=8, max_length=4096），cron 监控中，约 46% 进度
- `sft_baseline_v3` DONE(success) — SFT 训练完成
- `sft_eval_v3` DONE(failed) — 卡死 6h+，已 kill
- `posthoc_nli_v1` DONE(failed) — 同上
- `sft_baseline_v2` DONE(killed), `sft_baseline_v1` DONE(failed)

**等待中**：
- sft_eval_v4 cron 回调 → 触发后续流程
- sync-all-fixes Worker 回调（代码同步）

### 4. 📋 待办（条件触发式）
- **sft_eval_v4 cron 回调（进程退出）** → 读取 `outputs/sft/eval_results_v2.json` → update_registry(DONE, metrics) → 标注 RE F1 / Evi F1 基线
- **sft_eval_v4 DONE 后** → cuda:1 立即启动 `posthoc_nli_v2`：`PYTHONUNBUFFERED=1 CUDA_VISIBLE_DEVICES=1 python -u src/rerank_nli.py --predictions_file ./outputs/sft/eval_results_v2.json --batch_size 8 --max_prompt_length 4096 --nli_model_name /root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large --output_file ./outputs/posthoc_nli/eval_results_v2.json`
- **posthoc_nli_v2 完成** → 汇报完整对比表（RE F1 / Evi F1 / Attribution）+ kill criteria 评估 → 提交 GRPO 2 卡训练审批
- **GRPO 正式训练审批通过** → 2 卡 DDP：`accelerate launch --num_processes 2 src/train_grpo.py --sft_checkpoint ./outputs/sft/merged --max_completion_length 2048 --per_device_train_batch_size 2 --num_generations 2 --top_k 20 --top_p 0.95 --use_vllm False --nli_model_name ... --nli_device cpu`
- **sync-all-fixes Worker 回调** → 确认本地代码同步完成

### 5. 🎯 战略上下文
- **项目目标**：GRPO 训练提升 Qwen3-8B 在 DocRED 关系抽取上的 evidence provenance 质量
- **决策链**：SFT baseline 训练完成 → eval 修复（batch+max_length+PYTHONUNBUFFERED） → GRPO 采样参数修复（top_k/top_p） → thinking mode 禁用 → 等正式 eval 基线 → 提交 GRPO 训练
- **最容易判断错的事**：
  1. Worker 报告的模型名经常错（说"Mistral-Small-3.1-24B"），实际是 Qwen3-8B，以 registry 和 config 为准
  2. 不要尝试用 vLLM——已经验证了 2 个版本都不行，这是 torch 2.10 + Blackwell 的硬限制
  3. TRL GRPOConfig 的默认值很多与 Qwen3 不兼容（top_k=0 是最大坑），不要依赖默认值
  4. sft_eval_v4 的 running RE-F1=0.2828（46% 进度时），最终值可能更高或更低，不要提前下结论
  5. posthoc_nli_v2 必须串行等 sft_eval_v4——它依赖 eval_results_v2.json 作为 --predictions_file 输入
