# agent / loop_3.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`ecf864ca24d1fdd73809.json`](../../sessions/ec/ecf864ca24d1fdd73809.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-14T22:57:10+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 cuda:0, cuda:1（gpu-6000pro-2）。项目配置 `execution.servers[0].gpu_ids = [0, 1]`，绝对不能用其他卡
- DCOL 训练不能与其他 GPU 密集任务共占同一卡——v2 就是因为与 gpt2xl_temp09 feature extraction 共用 cuda:0 导致 OOM（57GB + 9GB > 98GB）
- 所有 pipeline 必须通过 `submit_training_job` 提交，不能 nohup/raw ssh_execute——否则没有 sentinel 文件，cron 会误标 failed
- kill 实验时必须确认所有子进程都死了（`ps -p PID + nvidia-smi`），父进程 kill ≠ 子进程 kill

### 2. 🖥️ 基础设施快照
- **服务器**: gpu-6000pro-2（2× RTX PRO 6000 Blackwell 98GB）
- **工作目录**: `/root/autodl-tmp/recursive_gen_depth_est`
- **Python**: `/root/miniconda3/bin/python`（conda base，不是 venv）。激活命令: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型路径**: `/root/autodl-tmp/models/` 下有 `pythia-1.4b/`, `gpt2-xl/`, `olmo-1b-hf/`, `deberta-v3-large/`
- **数据**: `data/depth_0.jsonl` (5000 seed), 各模型/策略子目录下生成数据各 20000 条
- **checkpoint**: `checkpoints/` 下按模型+策略组织（`gpt2xl/`, `olmo/`, `pythia_temp09/` 等）
- **结果**: `results/` 下按模型+策略组织
- **活跃进程**:
  - gpt2xl_topk50_001: tmux session, cuda:0, PID 211326
  - olmo_temp09_001: cuda:1, **疑似已死**（reconcile 报 "Process gone, no sentinel, miss 3/5"）
- **活跃 Worker**: `worker_ssh_olmo_temp09_001_check` (running, 正在查 olmo_temp09_001 状态)
- **Cron**: olmo_temp09_001 有活跃 cron 监控

### 3. 📊 当前状态
**刚做完**: gpt2xl_temp09_001 分析完成（success, 85.4% 4-class acc, 当前最高）。dcol_deberta_002 OOM 诊断完成，根因确认是僵尸进程占显存。

**RUNNING**:
- `gpt2xl_topk50_001` (cuda:0) — GPT-2 XL top-k k=50 pipeline，3×3 矩阵第 8 格
- `olmo_temp09_001` (cuda:1) — OLMo-1B temp τ=0.9 pipeline，3×3 矩阵第 5 格。**⚠️ 疑似死亡**: reconcile 报进程消失，无 sentinel，miss 3/5。有 Worker 正在查

**PREPARING**:
- `dcol_deberta_003` — DCOL v3 重试（修复 OOM 后），排在 cuda:0 gpt2xl_topk50 完成后
- `olmo_topk50_001` — OLMo top-k k=50，排在 cuda:1 olmo_temp09 完成后，3×3 矩阵最后一格

**等待中**:
- Worker `worker_ssh_olmo_temp09_001_check` 回调 → 确认 olmo_temp09 是真死还是 false alarm
- gpt2xl_topk50_001 cron 回调 → 分析结果 + 排 DCOL v3
- olmo_temp09_001 cron 回调 → 分析结果 + 排 olmo_topk50

### 4. 📋 待办（条件触发式）
- **olmo_temp09_001 Worker 回调确认死亡** → 查日志诊断根因；若 pipeline 部分完成，从断点续跑；若需重跑，立即 submit_training_job 到 cuda:1
- **olmo_temp09_001 Worker 回调确认存活** → false alarm，等 cron 正常回调
- **gpt2xl_topk50_001 完成(success)** → spawn worker 分析结果 + 与 nucleus/temp09 对比 + update registry → 3×3 矩阵第 8 格完成 → 立即提交 dcol_deberta_003 到 cuda:0
- **gpt2xl_topk50_001 完成(failed)** → 查日志，修复重跑
- **olmo_temp09_001 完成(success)** → 分析 → 立即提交 olmo_topk50_001 到 cuda:1（3×3 最后一格）
- **3×3 矩阵 9/9 全完成** → 汇总跨模型跨策略对比表 → 向 Director 汇报完整矩阵结果 + 建议下一步（DCOL / Atlas 出图 / baseline battery）
- **dcol_deberta_003 完成(success)** → 这是 secondary contribution 的关键数据点，需与 RF baseline 对比 → 触发 Atlas 正式出图 + baseline battery 开发
- **dcol_deberta_003 完成(failed)** → 第三次失败，考虑降低 batch_size 或换 gradient checkpointing

### 5. 🎯 战略上下文
**核心结论链**:
- D001: MVP PASS（Pythia 78.2%）→ 递归深度信号存在
- D002: Dream 审稿 3.0/3.0/2.5 → framing 从 DCOL 转向 Atlas/EDD 作为 primary contribution
- D004: 跨策略 claim 从 "strategy-agnostic" 降级为 "strategy-dependent magnitude"
- D006: 解码策略影响是模型依赖的（Pythia temp 降，GPT-2 XL temp 升）
- D007: Feature importance 用 set stability 而非 ranking stability

**项目核心 story**: 递归生成在文本中留下可检测的统计指纹（surprise + perplexity 特征），且这个指纹跨模型、跨解码策略稳健存在（但强度有差异）。Atlas/EDD 框架量化这个指纹的单调衰减趋势。

**易错点**:
- olmo_temp09 的 "process gone" 可能是 false failure（memory.md 记录了 cron false failure 的历史根因），先查日志再判断
- DCOL 必须独占 GPU，绝对不能与其他任务共卡——这是 v2 OOM 的教训
- GPT-2 XL 信号最强可能与跨模型 surprisal 评估（Pythia 参考模型评估 GPT-2 XL 文本）有关，论文需要讨论这个 potential bias
- 不要把不同模型的绝对 accuracy 直接对比下结论——cross-model surprisal 引入了系统性偏差
- feature importance 论文 claim 只能说 "top feature **set** stable"，不能说 "ranking stable"（D007 修正）


---
