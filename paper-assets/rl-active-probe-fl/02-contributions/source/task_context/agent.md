---
loop: 1
reason: max_wall_time
updated: '2026-05-14T11:37:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：rtx6000-diagprobe 的 cuda:0 和 cuda:1，不可用其他卡
- evaluate.py 内部 `os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)` 会覆盖外部环境变量。eval 必须用 `--gpu <物理GPU编号>`，不能依赖外部 CUDA_VISIBLE_DEVICES
- submit_training_job 的 command 必须用 `bash -c "..."` 包裹（tmux 跑 sh 不是 bash，source/conda activate 会 127）
- GRPO output-dir 必须是 `checkpoints/grpo_v2`，不要覆盖 v1（v1 虽然无效但保留）
- sandbox.py 的 `execute_probe` 必须传 `test_code` 参数，否则方法不会被调用，probe 永远不执行

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe，account: root
- 工作目录：/root/autodl-tmp/diagprobe
- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（conda base，不是 venv）
- 模型：/root/autodl-tmp/models/Qwen/Qwen3-8B
- SFT v1 ckpt：/root/autodl-tmp/diagprobe/checkpoints/sft
- SFT v2 ckpt：/root/autodl-tmp/diagprobe/checkpoints/sft_v2
- 数据：data/probes_train.jsonl (294), data/eval.jsonl (202)
- wandb：WANDB_MODE=offline（未登录）
- 2× RTX PRO 6000 Blackwell 94GB，torch=2.10.0+cu128，trl=1.1.0
- **活跃进程**：
  - GRPO v2：PID 30171，tmux=grpo-mvp-v2，cuda:0，step ~1/73，~12.5min/step，预计 ~15h
  - eval-sft-v2-ckpt：PID 32728，tmux=eval-sft-v2-ckpt，cuda:1，5/202，~30min 完成
- **Cron**：grpo-mvp-v2 (300s interval)，eval-sft-v2-ckpt (180s interval)
- Qwen3-30B-A3B 下载状态未知（之前 ~50%，在 rtx6000-diagprobe 上）

### 3. 📊 当前状态
刚完成 sandbox 三重修复（typing preamble + test_code driver + INSERT 解析改进），修复后 eval 结果已出：
- eval-base-v3: debug_accuracy=74.8%, probe_executed=59.9%（从 0.5% → 60%）
- eval-sft-v2: debug_accuracy=76.7%, probe_executed=59.4%（从 0% → 59%）
- SFT vs Base 仅 +1.9pp，CI 重叠不显著

Registry RUNNING：grpo-mvp-v2（GPU 0），eval-sft-v2-ckpt（GPU 1）
等待：grpo-mvp-v2 的 cron 回调（首条 reward 日志在 step 5），eval-sft-v2-ckpt 的完成回调
grpo-v2-dual Worker 可能还在运行（已提交任务但未收到 DONE 回调）

### 4. 📋 待办
- eval-sft-v2-ckpt cron 回调（完成）→ 提取 metrics，更新 registry DONE，对比 sft-v1 ckpt vs sft-v2 ckpt
- grpo-mvp-v2 step 5 日志出现 → 检查 reward 是否非零。reward=0 → 立即诊断（sandbox 修复是否真正生效于 reward 函数）；reward>0 → 反馈回路打通，等训练完成
- grpo-mvp-v2 完成 → 提取 metrics，启动 eval-grpo-v2（用 grpo_v2 checkpoint），这是 MVP pass/fail 的最终判断
- eval-grpo-v2 完成 → debug_accuracy >= 79.7% → MVP PASS，启动全量实验 + 论文；< 79.7% → MVP FAIL，触发 red-section framing 提案
- eval-sft-v2-ckpt 完成后 GPU 1 空闲 → 如果 GRPO 还在跑，可以铺其他 ablation（不同 temperature/kl-coef）的代码准备

### 5. 🎯 战略上下文
- 项目目标：EMNLP 2026 ARR（DDL 2026-05-25，还剩 11 天）
- 核心假设：GRPO fix-based reward > SFT-only >= 3pp on debugging accuracy
- D006：禁用 thinking（已解决）→ D007：probe 执行率 0%（已解决）→ D008：sandbox 修复确认 → D009：sandbox 修复后首次 eval 结果出，启动 GRPO v2
- **最容易判断错的事**：debug_accuracy 74.8% 看起来很高，但这主要是 test_code 驱动方法调用的效果（之前方法没被调过）。真正的 probe 贡献要看 probe_dependent（仅 15%）。MVP 判断看的是 GRPO 相对 SFT 的增量，不是绝对值
- **易踩坑**：GRPO ~12.5min/step × 73 = ~15h，不要因为等不及而 kill 重跑。如果 reward 全 0 才需要干预
- sft-v1 和 sft-v2 本质相同（thinking 模式不影响 SFT teacher forcing），eval-sft-v2-ckpt 大概率和 eval-sft-v2 一样
