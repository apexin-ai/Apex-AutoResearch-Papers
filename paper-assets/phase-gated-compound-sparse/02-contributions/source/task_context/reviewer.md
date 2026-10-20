---
loop: 12
reason: max_messages
updated: '2026-05-16T14:02:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0/1/2/3 全部可用（config `gpu_ids: [cuda:0, cuda:1, cuda:2, cuda:3]`）
- **Sentinel 文件不可删除**：`profiling_output_c8_llama_importance_s025/profiling_results.json` 和 `s030` 目录下的 sentinel 是 race condition guard。本轮已发生一次误删→我 CRITICAL 打回→恢复。下一个"你"如果看到 worker 建议删 sentinel，必须阻止。
- 论文数字基准：所有 headline 数字基于 n=500 bf16 paired 统计。DS Δ 0.39→8.48，QW Δ 0.07→3.16。旧 n=50 数字（0.32→9.94 等）已全部替换，发现残留立即 CRITICAL。
- Phase segmentation 方法论：quantile 三分是 primary（所有 benchmark 统一），`</think>` 二分仅作 validation/supplementary。我已向 Director 详细论证方案 A（background.tex L29-31 已定调）。GPQA 实验 primary 必须用 quantile。
- 本地 vs 远程文件：论文 authoritative source 在本地 `artifacts/_project/paper/`，远程 `/root/autodl-tmp/pacs/paper/` 是同步副本。同步方向搞反会覆盖正确文件。

### 2. 🖥️ 基础设施快照
- 服务器：`westd-22162`，账号 `root`，工作目录 `/root/autodl-tmp/pacs`
- Python：`/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型路径：
  - DS-R1-Distill-Qwen-7B: `checkpoints/DeepSeek-R1-Distill-Qwen-7B`
  - Qwen2.5-7B-Instruct: `checkpoints/Qwen2.5-7B-Instruct`
  - DS-R1-Distill-Llama-8B: `checkpoints/DeepSeek-R1-Distill-Llama-8B`
  - Qwen2.5-14B-Instruct: `/root/autodl-tmp/models/Qwen/Qwen2.5-14B-Instruct`（28GB，已下载完成，symlink 已创建）
- 数据：`data/math500.json`（500题），`data/gpqa_diamond.json`（198题 MCQA）
- 磁盘：`/root/autodl-tmp` 145GB 可用
- 活跃进程（截至 handoff）：
  - PID 315052/315057: c8_llama_importance_s025 (GPU 0, ~126/250, ~50%)
  - PID 310712/310735/310736: c8_llama_n250_fixed Round 1 s015+s020 (GPU 2+3, ~111/250, ~44%)
  - PID 317541: chain_s030_after_s025 monitor (等 315052 完成后启动 s030)
  - PID 316993/317716: guardian 进程（监控 s025 和 chain）
  - GPU 1: **空闲**（c10 已完成，14B 可立即启动）

### 3. 📊 当前状态
**刚完成**：GPQA pipeline 代码审查（`--raw_prompt` + `--use_chat_template` 已就绪）、c10_lang 结果确认、sentinel 误删→恢复→确认、fig1 本地同步（28286 bytes）、14B dry-run 通过。

**Registry RUNNING**：
- `c8_llama_n250_fixed`：LLaMA 8B 跨架构验证，4 轮串行（imp s015-s030 + rand s015-s030），n=250，预计总 ~16h 剩余
- `c8_llama_gpu0_s025`：GPU 0 独立跑 LLaMA imp s025，n=250，~50%，~2h 剩余
- `c10_lang_s020_s025`：**实际已完成**（registry 未更新），结果在 `results_c10_lang_s020_s025.json`

**未解决 WARNING**（已报告 Director，未见修复确认）：
- conclusion.tex 用 "2.7--17×" 混合范围（abstract/intro 用 "2.7--15×"），轻微不一致
- fig1 本地副本现已修复（28286 bytes），但此前多次 sync worker 失败说明 remote→local 文件传输机制脆弱

### 4. 📋 待办（条件触发式）
- c8_llama_gpu0_s025 完成 → chain 自动启动 s030 → 核实 sentinel 被真实数据覆盖、chain 进程正常
- c8_llama_n250_fixed Round 1 完成 → 核实 Round 2 正确跳过 s025/s030（sentinel guard）→ Round 3 开始 random
- 14B 实验在 GPU 1 启动 → 核实 `CUDA_VISIBLE_DEVICES=1` + `--gpu 0`、VRAM ~35GB 合理
- GPQA 实验启动 → 核实用 quantile 三分（不带 `--use_chat_template`）作为 primary
- c10_lang registry 更新为 DONE → 核实 metrics 写入
- 任何 worker 建议删除 sentinel → **立即 CRITICAL 阻止**
- 论文数字出现 9.94 / 0.32 / 14.59 / n=50 → CRITICAL，pilot 数据残留

### 5. 🎯 战略上下文
- **核心结论**：compound sparsity severity 是 phase × strategy 的涌现属性，importance eviction Δ 单调递增（DS 0.39→8.48），random 在 s≥0.25 才显著但弱 2.7-17×。Discrimination collapse（Gini 下降）是机制。
- **LLaMA 跨架构**：方向一致但 strategy×phase 交互弱于 Qwen2 架构（imp_vs_rand d_z 仅 0.19→0.34）。论文用 "suggests"/"partial support" 而非 "confirms"。
- **c10 language switching**：dose-response 清晰（dense 0% → s030 40%），是 compound severity 的行为学 marker，补充 II 定量指标。
- **最容易判断错的事**：
  1. Sentinel 文件看起来像"垃圾占位"但绝不能删——它是 GPU 0 独立任务与主脚本的协调机制
  2. worker 报告 GPQA "不支持" 是因为 grep "gpqa" 找不到——支持是通过 `--raw_prompt` 通用 flag 实现的
  3. 远程 `/root/runs/phase-gated-compound-sparse/c10_lang_s020_s025.log` 显示 SIGTERM 是**旧的被 kill 的 run**，不是当前成功 run 的日志（成功 run 日志在 `/root/autodl-tmp/pacs/logs/c10_s020_s025.log`）
  4. 14B 实验预估 5 个条件串行 20-40h，是否能在 deadline 前完成取决于 GPU 并行度——GPU 0 释放后可分流
