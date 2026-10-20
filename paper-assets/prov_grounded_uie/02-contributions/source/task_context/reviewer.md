---
loop: 2
reason: max_wall_time
updated: '2026-05-12T22:48:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:0 和 cuda:1（2×RTX PRO 6000 @ westd-37397，`execution.gpu_ids=[0,1]`）
- posthoc_nli / evaluate 的 NLI 模型必须跑在 CPU（`nli_device="cpu"`），不能占 GPU 显存
- report_to 必须设 "none"（AutoDL 离线环境，wandb 不可用）
- SFT checkpoint 路径固定：`/root/autodl-tmp/prov_grounded_uie/outputs/sft/merged`，不要用 HF hub ID
- NLI 模型本地路径：`/root/autodl-tmp/.hf_cache/ms_deberta/cross-encoder/nli-deberta-v3-large`

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397(root)，工作目录 `/root/autodl-tmp/prov_grounded_uie`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 激活方式：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：SFT merged checkpoint @ `./outputs/sft/merged`（Qwen3-8B + LoRA merged）
- 数据：`./data/docred_train.jsonl` (3027 samples), `./data/docred_dev.jsonl` (985 samples)
- HF cache：`/root/autodl-tmp/.hf_cache/`
- W&B：未配置（report_to=none）
- 活跃进程：sft_eval_v4 (PID 40397, GPU 0, `python -u evaluate.py --batch_size 8 --max_prompt_length 4096`)
- GPU 1：完全空闲（0 MiB / 0%）
- TRL 版本：1.1.0；vLLM 版本：0.18.1（TRL 警告不兼容，支持到 0.17.1）

### 3. 📊 当前状态
**我刚完成的核心工作：确认 GRPO 零奖励根因 = Qwen3 thinking mode 未禁用。**

已向 Director 发送 3 条 critical 报告：
1. GPU 1 空闲 — posthoc_nli_v1 失败后未重启（代码已修复可重启）
2. GRPO 零奖励根因 — Qwen3 `<think>` mode 在 sampling (T=0.7) 下被触发，1024 tokens 全是推理文本
3. 精确修复方案 — 修改 tokenizer.chat_template 禁用 thinking，已给出代码

**Registry 状态：**
- `sft_eval_v4` RUNNING — 400/985, RE-F1≈0.29, GPU 0, 预计 ~1.5h 完成
- `sft_baseline_v3` DONE/success — eval_loss=0.356, 570 steps, 1h18m
- `posthoc_nli_v1` DONE/failed — 卡死 6h 被 kill（旧代码 truncated@2048）
- `sft_eval_v3` DONE/failed — 同上，已被 v4 替代
- `sft_baseline_v1` DONE/failed — OOM
- `sft_baseline_v2` DONE/killed — 被 Director 改方案

**等待中：** Director 对 3 条 critical 的响应（GPU 1 重启 posthoc_nli、GRPO thinking mode 修复）

### 4. 📋 待办
- sft_eval_v4 完成 → 核实最终 RE F1 和 Evi F1 数值，这是 kill criteria 的 SFT baseline 锚点
- Director 批准重启 posthoc_nli → 核实 GPU 1 启动、验证用了 `--batch_size 8 --max_prompt_length 4096`、日志路径更新到 registry
- posthoc_nli_v2 完成 → 核实 Evi F1 ceiling，这是 kill criteria 的 post-hoc 锚点
- GRPO thinking mode 修复部署 → 核实：(a) tokenizer.chat_template 已修改 (b) 重新测试 reward>0 (c) completions 不再以 `<think>` 开头
- GRPO 正式训练启动 → 核实 GPU 边界（只用 cuda:0/1）、max_completion_length≥2048、reward 非零
- sft_eval_v4 的 RE-F1 如果显著低于预期 → 考虑 evaluate.py 也受 thinking mode 影响（greedy T=0 下概率低但非零）

### 5. 🎯 战略上下文
**决策链：** D001（立项 DocRED+Qwen3-8B）→ D002（加 post-hoc NLI 对照+三档 kill）→ D003（MR-UIE 阻塞）→ D004（阻塞解除，MR-UIE ≠ ProvUIE）

**Kill Criteria：** GRPO Evi F1 vs post-hoc NLI Evi F1: <2pt kill / 2-4pt inconclusive / ≥5pt pass；RE F1 regression ≤2pt

**最容易判断错的事：**
1. **GRPO 不能直接跑 no-vLLM 模式**：Qwen3-8B + batch=2 × num_gen=4 × 2048 tokens 在 backward 时 OOM（49.47GB + 2.32GB > 94.97GB）。必须用 vLLM colocate 或降 num_generations/max_completion_length
2. **vLLM 0.18.1 与 TRL 1.1.0 不兼容**（TRL 支持 0.11.0-0.17.1）。之前降级到 0.17.1 又升回来了。如果 vLLM colocate 仍有问题，可能需要再降级
3. **不要混淆 EvalArgs.max_prompt_length (4096) 和 GRPOArgs.max_prompt_length (2048)**——两个不同的 dataclass 有同名字段但默认值不同
4. **evaluate.py / rerank_nli.py 在项目根目录**，不在 src/ 下（`ls` 确认过，src/config.py 不存在）
5. **Qwen3 thinking mode 是当前最大阻塞项**——温度 >0 时模型大概率进入 `<think>` 模式。修复方案已明确（修改 chat_template），但尚未部署
