# agent / loop_1.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`5786f6c68b6312f4d068.json`](../../sessions/57/5786f6c68b6312f4d068.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: idle_timeout
updated: '2026-05-14T20:52:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090 的 cuda:0/1/2/3，不得使用其他设备
- 环境激活必须用 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要假设 .venv 存在
- AutoDL 网络：pip/git 前必须 `source /etc/network_turbo`；HF 下载设 `HF_HUB_DISABLE_XET=1`；大模型优先 ModelScope
- 根分区 ~30GB，模型/数据/HF cache 全部放 `/root/autodl-tmp/`

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090（4× RTX 5090 32GB），工作目录 `/root/gen-depth-fingerprint`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：EleutherAI/pythia-2.8b（生成器）+ EleutherAI/pythia-410m（参考模型）——下载路径未确认，可能是失败原因之一
- 数据：`/root/gen-depth-fingerprint/data/wiki_seed_1000.jsonl`（1000 条 Wikipedia 种子）
- 活跃进程：无（4 个 shard 全部崩溃）
- Cron：mvp-001-gen-s0 有一个 reconcile cron 仍在跑（但实验已死）

### 3. 📊 当前状态
**刚做完**：收到 mvp-001-gen-s3 失败 cron 回调，完成 session-start 初始化，派出诊断 Worker（`worker_diagnose_mvp-001-gen-s3_20260514T172438`）读取 4 个 shard 日志。已向 Director 汇报失败。

**Registry 状态**：
- `mvp-001`：RUNNING（父实验，逻辑容器）
- `mvp-001-gen-s0`：PREPARING（cron 还没捕捉到失败，大概率也挂了）
- `mvp-001-gen-s1/s2/s3`：PREPARING + conclusion=failed（EXIT_CODE=1，~30s 内崩溃）

**等待中**：
- 诊断 Worker 回调 → 拿到根因后修复代码并重跑
- Director 无待回复决策

### 4. 📋 待办
- 诊断 Worker 回调到达 → 读取根因 → update_registry 标记 s0-s3 为 DONE(failed) + 记录 failure_reason → 根据原因分支：
  - 若代码 bug → 派 Worker 修复 generate_chain.py → dry-run 验证 → 重新 submit 4 shard
  - 若环境/依赖缺失 → 派 Worker 装依赖 → 验证 → 重新 submit
  - 若模型未下载 → 派 Worker 下载模型到 `/root/autodl-tmp/` → 修改脚本路径 → 重新 submit
- 重跑成功后 → 等 cron 回调数据生成完成 → 进入特征提取 + XGBoost 分类阶段
- 4 张 GPU 当前全部空闲，修复后立即重跑恢复饱和

### 5. 🎯 战略上下文
- 项目处于 MVP 验证最早期：连第一步数据生成都还没跑通
- 核心假设（D001）：Pythia-410M 参考模型的分布特征能区分 Pythia-2.8B continuation 链的 gen-0/gen-1/gen-2+，3-class macro-F1 ≥ 0.45
- Pass/Fail 判据明确：macro-F1 ≥ 0.45 且 gen-0 vs gen-2+ binary F1 ≥ 0.65 = Pass
- **易踩坑**：4 个 shard 全在 30s 内崩溃，很可能是 generate_chain.py 导入时就报错（模型路径不存在、缺包、或脚本本身有语法错误）。不要盲目重跑——必须先拿到日志确认根因再修
- 诊断 Worker 日志路径：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/workers/worker_diagnose_mvp-001-gen-s3_20260514T172438.log`


---
