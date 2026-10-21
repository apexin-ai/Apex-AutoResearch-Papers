# agent / loop_18.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_18.md`
- **Structured JSON:** [`2443f97565199cdc045c.json`](../../sessions/24/2443f97565199cdc045c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: idle_timeout
updated: '2026-05-16T15:06:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单只有 westd-39279:cuda:0 和 cuda:1，不可用其他卡
- Round 2 实验全部用 `--no_wandb`（服务器无 wandb key），metrics 从 reward_log.csv / eval 输出提取
- submit_training_job command 必须 `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && ..."`——裸 source 在 tmux sh 下会 127
- 磁盘空间紧张（之前清理过 54GB），提交前应检查 `df -h /root/autodl-tmp/`，中间 checkpoint 及时清理
- 训练脚本路径：`python3 scripts/train_grpo.py --config configs/...`（不是根目录下的 train_grpo.py）
- 不要说 "H7 is ISR-specific"——只有 H7b 是，H7a 是 GRPO 通用的
- conclusion=success 判断标准：高 hacking + ISR collapse = 验证 Goodhart 假设 = success（不是 negative）

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279，工作目录 `/root/solver-trace-ablation`
- Python：`/root/miniconda3/bin/python3`（conda base env）
- 4B 模型：`/root/autodl-tmp/models/Qwen3-4B`
- 1.7B 模型：正在由 setup Worker 下载/准备中（路径待确认）
- 数据：`data/train_500_seed42.jsonl`（训练），`data/proofwriter_fol_100.jsonl`（eval）
- 输出目录：`/root/autodl-tmp/outputs/`
- 活跃进程：**无**（双卡空闲）
- 无 wandb，无 HF 下载需求（1.7B 下载由 setup Worker 处理）

### 3. 📊 当前状态
**刚做完**：Session-start 初始化，确认 registry 状态，向 Director 汇报 Loop #18 状态。

**关键发现**：
- sweep-isr-b02-s44 已 DONE/success（h7a=100%, genuine=0%）→ β=0.2 三 seed 全部完成
- plan018-random-b01-s45-r2 已 DONE/failed（无 metrics）
- 8B 全部 OOM（4 次尝试）→ D108 决定转 1.7B

**活跃 Worker**（2 个）：
1. `worker_setup_qwen3-1_7b-dual-pilot_20260516T105518`（running，26+ 轮，正在处理 model download + config + timeout 问题）——**关键路径**
2. `worker_analysis_4b-dose-response-table_20260516T110236`（running，聚合全部 4B 实验数据到 CSV/summary）

**Registry**：0 RUNNING / 0 ANALYZING / 9 PREPARING（5-seed 扩展实验）/ 2 QUEUED(killed)

### 4. 📋 待办
- 1.7B setup Worker 回调 → 确认 model path + config paths → 注册两个实验（w2-qwen3-1.7b-exec-only-s42 + w2-qwen3-1.7b-isr-b01-s42）→ 立即双卡提交（cuda:0 exec-only, cuda:1 ISR β=0.1）
- 4B dose-response Worker 回调 → 检查 artifacts/4b_dose_response_table.csv 和 summary.md → 确认数据完整性
- 1.7B 训练完成回调 → eval_sta.py + classify_h7.py → 对比 4B hacking patterns → 如确认 hacking 则 W2 gap 填补完成
- 1.7B exec-only + ISR 都 success → 汇报 Director "跨 scale 验证完成" → 如时间允许铺 1.7B ISR β=0.3
- Director 回复 → 根据指示调整优先级

### 5. 🎯 战略上下文
- **核心方向**：ISR 作为 Goodhart's Law 案例研究，DDL 2026-05-25（剩 9 天）
- **D106 叙事已锁定**：dominant hacking across all β, β=0.2 maximum exploitation, H7a 是 GRPO-general seed-dependent
- **D108 转向**：8B 全参 GRPO 在 96GB 单卡不可行，改用 Qwen3-1.7B（K=4 与 4B 匹配，无训练方法 confound）
- **D109 约束**：1.7B 结果必须框架为"小模型也 hack"而非"scale 验证"
- **4B 证据链完整**：Claim 1（STA 诊断）✅ Claim 2（Goodhart dose-response）✅ Claim 3（跨逻辑泛化）✅
- **1.7B 是最后关键实验**：填补 W2 单模型 gap，成功后可全力写作
- **易错点**：
  - 1.7B 可能需要调整 per_device_batch_size（96GB 卡跑 1.7B 应该绑绑有余，但 K=4 生成阶段仍需注意显存）
  - 双实验并行时 RAM OOM（s45 曾被 kill，exit 137）——cuda:0+cuda:1 同时跑要小心
  - PREPARING 池里的 5-seed 扩展实验优先级低于 1.7B，不要先提交它们
  - report.md 显示"运行中（无）"是正确的——目前确实没有训练在跑，都在等 1.7B setup


---
