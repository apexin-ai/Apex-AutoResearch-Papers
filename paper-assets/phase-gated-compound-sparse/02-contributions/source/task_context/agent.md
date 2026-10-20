---
loop: 15
reason: max_wall_time
updated: '2026-05-16T14:41:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- **Sentinel 文件绝对不能删除**：`profiling_output_c8_llama_importance_s025/profiling_results.json` 和 `s030/profiling_results.json` 中含 `_sentinel: true` 的是 race condition guard，GPU 0 独立跑 s025→s030 chain，主脚本靠 sentinel 跳过这两个条件。本 session 已因误删 sentinel 出过事故。
- **GPU 白名单**：cuda:0,1,2,3 on westd-22162。不可用白名单外 GPU。
- **submit_on_allocated 命令必须 `bash -c "..."`** 包裹（tmux 用 /bin/sh，不支持 source/conda activate）
- **submit_on_allocated 前必须设置 top-level 字段**：`server`、`gpu`（字符串非列表）、`account` 三个字段都要在 registry 顶层设置，仅在 spec 中不够
- **c10_lang_s020_s025 已 DONE/success**，不要重跑

### 2. 🖥️ 基础设施快照
- **服务器**: westd-22162, root, RTX 6000 Pro ×4 (各 98GB)
- **工作目录**: `/root/autodl-tmp/pacs/`
- **Python**: `/root/miniconda3/bin/python3`（conda base）
- **激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型路径**:
  - DeepSeek-R1-Distill-Qwen-7B: `checkpoints/DeepSeek-R1-Distill-Qwen-7B` (相对 pacs/)
  - DeepSeek-R1-Distill-Llama-8B: 同上 llama 版
  - Qwen2.5-14B-Instruct: `/root/autodl-tmp/models/Qwen/Qwen2.5-14B-Instruct/` (28G, ready)
- **数据**: `data/gpqa_diamond.json` (~198题), `data/math500.json` (500题)
- **活跃进程**:
  - GPU 0: PID 562663, c8_llama_importance_s030 (chain from s025)
  - GPU 1: PID 555744, gpqa_ds_importance_s015 (tmux=gpqa_ds_importance_s015, cron registered)
  - GPU 2: PID 560643, c8_llama_random_s015 (主脚本子进程)
  - GPU 3: PID 560642, c8_llama_random_s020 (主脚本子进程)
  - 主脚本: PID 310712, c8_llama_n250_fixed (tmux=c8_llama_n250_fixed, cron registered)

### 3. 📊 当前状态
**刚做完**: GPU 状态检查 + c8_gpu0_s025 更新为 DONE/success + GPQA DS s015 提交成功 + c10_lang_s020_s025 更新为 DONE/success

**正在等待**: Worker `worker_analysis_c8_s025_extract_20260516T144010` 正在提取 LLaMA importance s025 (n=250) 的 II 指标，供 Director 判断是否写入论文。

**Registry RUNNING**:
- `c8_llama_n250_fixed`: GPU 2+3 主脚本, Round 3 (random s015+s020), 还剩 Round 4 (random s025+s030)
- `gpqa_ds_importance_s015`: GPU 1, 103/198 (52%), ~8h 剩余

**Cron 监控**: c8_llama_n250_fixed + gpqa_ds_importance_s015 (reconcile 确认)

### 4. 📋 待办
- `worker_analysis_c8_s025_extract` 回调 → 将 LLaMA s025 指标写入 registry metrics + 汇报 Director（对比 DS baseline，判断 cross-arch claim 强度）
- `gpqa_ds_importance_s015` cron 完成回调 → 分析结果 + 更新 registry + 汇报 Director + 如果 GPU 1 释放，Director 决定下一个 GPQA 条件
- `c8_llama_n250_fixed` cron 完成回调 → 全 8 条件统一分析 + 计算 cross-arch effect sizes + 写入论文
- GPU 0 s030 chain 完成 → 确认 sentinel 被覆盖为真实数据 + 更新 registry
- Director 决定 GPU 0 释放后用途 → GPQA QW 或 14B（14B dry-run 已通过，`--model` 切换即可）

### 5. 🎯 战略上下文
- **目标**: EMNLP 2025 main, 截稿 2026-05-25（距今 9 天）
- **核心 claim**: Phase-modulated compound sparsity severity — importance-based eviction 的 compound interaction 随 sparsity 单调递增
- **C8 (cross-arch) 是关键 blocking item**: n=50 时 LLaMA 仅 s030 Bonferroni 显著，n=250 预期提升 power。如果 n=250 让 s025 也显著，claim 大幅加强；如果仍不显著，需要 soften wording
- **GPQA (线路 A)** = 非数学推理 generalization，D098 决策用 quantile 三分 + `--raw_prompt`（不用 `--use_chat_template`）
- **14B (线路 B)** = scale 扩展，模型已 ready，等 GPU
- **run_profiling.py 已支持 GPQA**：通过 `--raw_prompt` flag（L256-263, L673）跳过 math prompt 包装。不需要写新脚本
- **易错点**: ① 不要删 sentinel 文件 ② submit 命令必须 bash -c 包裹 ③ gpu registry 字段要 string 不是 list ④ c8_main 的 importance s025/s030 由 GPU 0 独立完成，主脚本 Round 2 被 sentinel skip 是正确行为
