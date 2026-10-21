# agent / loop_13.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_13.md`
- **Structured JSON:** [`3a31c23ad54b9daa4db9.json`](../../sessions/3a/3a31c23ad54b9daa4db9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-05-16T13:41:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：gpu-6000pro-2 cuda:0, cuda:1（仅此两卡）
- 论文 tex 文件有两份：本地 workspace（真源，Worker 用 Edit 改）+ 服务器 `/root/autodl-tmp/recursive_gen_depth_est/paper/`（编译用，需手动 sync）。改完本地必须 sync 到服务器再编译
- EMNLP ARR 正文 ≤8 页硬限。当前 R4 修改导致 11 页，正在压缩中
- Llama-3.1-8B 实验用 BASE 模型（`meta-llama/Llama-3.1-8B`），不是 Instruct。这是隔离 instruction-tuning confound 的核心实验
- submit_training_job command 必须 `bash -c "source ... && python ..."`（tmux 用 sh 不是 bash）

### 2. 🖥️ 基础设施快照
- 服务器：gpu-6000pro-2，工作目录 `/root/autodl-tmp/recursive_gen_depth_est/`
- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- HF cache：`/root/autodl-tmp/.hf_cache`
- 模型下载目标路径：`/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3.1-8B`
- 本地 tex 路径：用 Glob 找 `abstract.tex`（之前 Worker 找到过，可能在 `projects/recursive_gen_depth_est/paper/`）
- Cron 注册：`cross_scale_llama3_base_001`（PID 557455——已废弃，旧下载进程已 kill）
- 活跃 Worker：`worker_writing_r4_compress_20260516T134012`（压缩 tex）+ `worker_ops_fix_model_download_20260516T134026`（修复下载）

### 3. 📊 当前状态
正在并行处理两件事：
1. **R4 正文压缩** — Worker 正在精简 15 条 R4 修改中膨胀的部分（目标：11 页 → ≤8 页）
2. **Llama-3 base 模型下载修复** — Worker 正在 kill 重复进程并用 ModelScope 单进程重下（ignore .pth）

Registry：
- `cross_scale_llama3_base_001` = ALLOCATED（等模型下载完提交）
- `cross_scale_qwen7b_001` = DONE (success, 60.1% acc, EDD>5, U-shape AUC)
- 其他均 DONE

之前的 `worker_ops_llama3_base_download_fix_20260516T133452` 可能还在跑但已被新 Worker 取代（它产生了重复进程问题）。

### 4. 📋 待办
- R4 compress Worker 完成 → sync 到服务器 → 编译验证 → 确认 ≤8 页 → 报告 Director
- 模型下载完成 → dry-run 4-bit 加载验证 → `submit_training_job(server="gpu-6000pro-2", gpu_ids=["cuda:0","cuda:1"], command="bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recursive_gen_depth_est && bash scripts/run_llama3_base_pipeline.sh\"", exp_id="cross_scale_llama3_base_001")` → register_cron 监控
- 训练完成(~8h) → 分析 AUC pattern（monotonic vs U-shape）→ 决定 N3 confound 结论 → 更新论文 §4.4
- 如果 ModelScope 仍慢 → 换 `huggingface-cli download meta-llama/Llama-3.1-8B --exclude "original/*"`

### 5. 🎯 战略上下文
- 项目在 EMNLP ARR May 25 冲刺（剩 9 天）。所有实验完成，论文写完，Round 4 审稿修改中
- cross_scale_llama3_base_001 是**决定性实验**：如果 base model AUC monotonic decay → 可以 claim instruction-tuning 是 U-shape 原因 → 论文从 borderline Findings 升 main conference
- Qwen7B 结果是 U-shape（非 monotonic），Llama-3 Instruct 是 monotonic (EDD=4)。base vs instruct 对比能解释分歧
- 易踩坑：(1) 模型路径——ModelScope 下载的实际路径可能与脚本中 hardcode 的不一致，提交前必须 grep 脚本确认 MODEL_PATH 匹配实际路径 (2) 页数——每次改 tex 后必须编译检查，R4 已经证明文字修改很容易超页 (3) cron PID——旧的 557455 已无效，下载成功后用新 PID 注册 cron


---
