---
loop: 1
reason: max_wall_time
updated: '2026-05-14T08:24:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 C001：仅允许 cuda:0 和 cuda:1（gpu-6000pro-1）
- rtx6000-diagprobe 和 gpu-6000pro-1 是**同一台物理服务器**，不要当两台机器分别提交任务
- Qwen3-8B 必须 `enable_thinking=False`（已修复），否则 `<think>` 消耗全部 token，所有 reward/eval 归零（已踩坑两次，浪费 ~2.5 GPU-hours）
- SFT 训练数据用 `data/probes_train.jsonl`（294 条，含 good_probe/bad_probe），不是 `data/train.jsonl`
- TRL 1.1.0 API 变更：SFT 用 `max_length`（非 max_seq_length），GRPOConfig 无 `max_prompt_length` 参数，reward function 的 completions 是 `list[list[dict]]` 不是 `list[str]`

### 2. 🖥️ 基础设施快照
- 服务器：gpu-6000pro-1 (root)，2× RTX PRO 6000 Blackwell 94GB，CUDA 12.8
- 工作目录：`/root/autodl-tmp/diagprobe`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 模型：`/root/autodl-tmp/models/Qwen/Qwen3-8B`（16GB）
- Qwen3-30B-A3B：下载中（D005，全量阶段用），~60GB，速度慢（~500KB/s）
- 数据：`data/probes_train.jsonl`（294 train），`data/eval.jsonl`（202 eval）
- Checkpoints：SFT → `/root/autodl-tmp/diagprobe/checkpoints/sft/`（LoRA 174MB），GRPO → `checkpoints/grpo/`（无效，reward=0）
- W&B：offline 模式，本地 `/root/autodl-tmp/diagprobe/wandb/`，未配置在线同步
- torch=2.10.0+cu128, trl=1.1.0, peft=0.19.0

### 3. 📊 当前状态
刚完成 no-think 修复审查。Agent 做了 5-sample dry-run 确认 `enable_thinking=False` 生效后，启动了两个并行评估：
- **eval-sft-v1**：GPU 0，17.2GB，tmux=eval-sft-v1，评估 SFT checkpoint（202 samples）
- **eval-base-v2**：GPU 1，16.5GB，tmux=eval-base-v2，重跑 base 评估（202 samples）
- 每 sample ~10s，预计 ~35 分钟完成

Registry 3 个实验全 DONE：sft-mvp-v1（success），grpo-mvp-v1（negative/应为 invalid），eval-base-v1（success/应为 invalid）。eval-sft-v1 和 eval-base-v2 尚未注册或状态未更新。

**GRPO 尚未用 no-think 修复重跑**——当前只修了 eval，GRPO 训练代码是否也加了 `enable_thinking=False` 需要确认。

### 4. 📋 待办
- eval-sft-v1 + eval-base-v2 完成 → 独立核实指标（probe_generation_rate 必须 >>0.5%，否则 no-think 修复未生效）
- eval 结果出来 → 审查 SFT vs base 差异是否合理（SFT 应显著优于 base）
- GRPO no-think 修复重跑通知 → 核实 train_grpo.py 是否也加了 enable_thinking=False + reward function completion 格式适配
- GRPO 重跑完成 → 核实 reward 曲线不再全零，completions_clipped_ratio < 1.0
- eval-grpo 完成 → 与 eval-sft 对比，判断 MVP pass/fail（≥3pp 或 CI 下界 ≥0pp）
- Qwen3-30B-A3B 下载完成 → 不影响 MVP，info 级确认即可

### 5. 🎯 战略上下文
- 核心假设：GRPO fix-based reward > SFT-only ≥3pp debugging accuracy
- 决策链：D001（n=200+CI）→ D002（API 生成测试）→ D003（fix-based reward 必须）→ D004（496 样本够用）→ D005（30B-A3B 全量阶段用）
- **最易误判**：grpo-mvp-v1 registry 标 "negative" 和 eval-base-v1 标 "success"——这两个结论都无效，是 thinking 模式 bug 导致的，不是真实实验结果。不要基于这些数据做任何 pass/fail 判断
- **SFT 可能也有问题**：SFT target 是纯 probe 代码，但如果推理时模型仍倾向 thinking，SFT 的 token_accuracy=0.662 不代表推理时能正确输出。eval-sft-v1 的结果将是第一个真实信号
- **时间线实际状态**：ROADMAP 说 Day 1 完成 SFT+GRPO，实际 GRPO 无效需重跑。真正的 MVP 判断最早 Day 2 中期（GRPO 重跑 ~1h + eval ~30min）
