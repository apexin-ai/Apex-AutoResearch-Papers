---
loop: 10
reason: max_messages
updated: '2026-05-16T14:02:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-22162 的 cuda:0/1/2/3，严禁使用其他服务器或 GPU
- **Sentinel 文件不能删**：c8_llama_n250_fixed 的 s025/s030 output 目录中有 sentinel race guard 文件（`profiling_results.json` 内含 `_sentinel: true`）。GPU 0 独立跑 s025，主脚本 Round 2 通过 sentinel 跳过 s025/s030。本 session 已发生一次误删事故并紧急恢复。
- GPQA segmentation 决策 D098：quantile 三分为 primary（不带 `--use_chat_template`），`</think>` 二分仅为 supplementary validation。论文叙事 = "quantile = primary, `<think>` = validation"，GPQA 必须遵循。
- EMNLP 按正会标准写，不主动降级 Findings framing（用户明确指示）
- Figure 1 同步方向：remote → local（不能反向，否则会用 0 bytes 空文件覆盖远程正确文件）

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162 (connect.westd.seetacloud.com)，账号 root
- 工作目录：`/root/autodl-tmp/pacs`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- 模型路径：
  - DS-R1-7B: `checkpoints/DeepSeek-R1-Distill-Qwen-7B`
  - QW-7B: `checkpoints/Qwen2.5-7B-Instruct`
  - LLaMA-8B: `checkpoints/DeepSeek-R1-Distill-Llama-8B`
  - **14B（新）**: `checkpoints/Qwen2.5-14B-Instruct`（28G, 8 shards, symlink 已建, dry-run 通过）
- 数据：`data/gpqa_diamond.json`（198 题）, MATH-500/GSM8K 已有
- 活跃进程（需重新确认，session idle 6h+ 可能有变化）：
  - c8_gpu0_s025: PID 315052 (GPU 0)，之前 126/250
  - c8_llama_n250_fixed: PID 310712 (GPU 2+3)，Round 1/4
  - gpqa_ds_importance_s015: PID 555739 (GPU 1)，刚提交时 198 题 ~5h
  - s030 chain: PID 317541, guardians: 316993, 317716

### 3. 📊 当前状态
刚执行 RESET_BOTH（Agent + Director），Agent idle 6h+ 因 session 未自动重建。我最后一条消息已发给 Agent 要求一次性检查全 GPU 状态，**尚未收到回复**。

Registry RUNNING（3 个）：
- `c8_llama_n250_fixed`：LLaMA n=250 跨架构验证，8 条件 4 轮串行（GPU 2+3）
- `c8_llama_gpu0_s025`：预加速 s025（GPU 0），可能已完成但未确认
- `gpqa_ds_importance_s015`：GPQA Diamond DS importance s015，quantile primary（GPU 1）

已完成关键实验：c10_lang_s020_s025（switch rate 0→4→14→32→40% 单调递增 ✅），c4_think_validation（κ=0.887 ✅），Figure 1 修复（7B 标题 ✅，28286 bytes 已同步到本地 ✅）

Paper Agent 状态：R10 全部文本修复完成，GPQA/14B 占位结构已建，Limitations 已更新，编译通过 25 页 0 errors。

### 4. 📋 待办（条件触发式）
- Agent 回复 GPU 状态 → 确认 c8_s025 是否完成，完成则确认 s030 chain 启动；GPQA 进度
- c8_gpu0_s025 完成 + s030 chain 完成 → GPU 0 释放，分配给 GPQA QW importance s015 或 14B MATH-500（优先 GPQA QW，打 task diversity）
- GPQA DS s015 完成 → 分析结果，如果 phase gradient 成立则继续 s020/s025/s030 系列
- c8_llama_n250_fixed 全部完成（~10-16h）→ 分析 LLaMA n=250 结果写入论文，这是 R10-C3 cross-architecture 的关键修复
- 所有 scope 扩展实验完成 → 更新 ROADMAP + 派 Paper Agent 填入占位数据 → 提交 Round 11 审稿
- GPU 释放后排队：GPQA DS s020/s025/s030 → GPQA QW 系列 → 14B MATH-500 系列

### 5. 🎯 战略上下文
- 项目核心：compound sparsity（head pruning + KV eviction 同时施加）在推理模型的不同 phase（thinking vs answering）产生差异化退化，II metric 量化 phase gradient
- EMNLP 2026 DDL 5/25（9 天），时间充裕
- R10 审稿 Weak Reject，关键短板：(1) scope 窄（仅 7B + 数学）→ 正在补 GPQA + 14B (2) cross-arch 弱（LLaMA n=49）→ c8 n=250 正在跑 (3) novelty → 用户说按正会写
- 决策链：D098 GPQA quantile primary；用户确认两个方向都做（GPQA + 14B）
- **易错点**：
  - `run_profiling.py` 已支持 GPQA（通过 `--raw_prompt` flag），不要写新脚本
  - Sentinel 文件是有意设计的 race guard，不是残留垃圾——本 session 已踩过这个坑
  - Figure 1 本地文件之前多次出现 0 bytes 空文件，同步后务必验证文件大小
  - Agent 重启后容易丢失上下文，对并行架构（sentinel/chain/guardian）的理解会断裂，需要在指令中显式说明
