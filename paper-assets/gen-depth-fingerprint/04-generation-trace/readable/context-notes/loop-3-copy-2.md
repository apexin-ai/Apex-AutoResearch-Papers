# agent / loop_3.md

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`ffe70e7f4afb2ade31ae.json`](../../sessions/ff/ffe70e7f4afb2ade31ae.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-15T03:19:28+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 `cuda:0, cuda:1, cuda:2, cuda:3`（autodl-5090），只有这 4 张卡
- plan-014（Qwen3-8B，PID 134817）正在 cuda:0 上跑，**不要 kill 它**，cron 在监控
- 所有训练输出必须写 `/root/autodl-tmp/`，**根分区只有 30GB**（曾因 checkpoint 占满导致集体 OOM）
- `submit_training_job` 注入 `CUDA_VISIBLE_DEVICES` 后脚本只能看到 cuda:0，`--device` 参数必须写 `cuda:0`
- Claim 3 (Downstream Utility) 已被 D009 reframe 为 **diagnostic-not-curative**（负面结果），论文中不能 claim depth filtering 改善下游质量
- EMNLP 2026 ARR deadline **2026-05-25**（10 天后），AAAI 2027 deadline **2026-08-02**

### 2. 🖥️ 基础设施快照
- 服务器：**autodl-5090**（4× RTX 5090），工作目录 `/root/gen-depth-fingerprint`
- Python：`/root/miniconda3/bin/python`（conda base，不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型路径（全在数据盘）：pythia-2.8b `/root/autodl-tmp/.hf_cache/EleutherAI/pythia-2___8b`，pythia-410m(ref) `/root/autodl-tmp/models/pythia-410m/...`，olmo-2-1b `/root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B`，qwen3-1.7b/0.6b `/root/autodl-tmp/models/Qwen/Qwen3-{1___7B,0___6B}-Base`，qwen3-8b `/root/autodl-tmp/models/Qwen/Qwen3-8B-Base/Qwen/Qwen3-8B-Base/`
- HF cache：`HF_HOME=/root/autodl-tmp/.hf_cache`
- 数据盘符号链接：`data/qwen3-8b` → `/root/autodl-tmp/gen-depth-fingerprint/data/qwen3-8b`，`experiments/downstream` → `/root/autodl-tmp/gen-depth-fingerprint/experiments/downstream/`
- 活跃进程：plan-014 PID 134817（tmux，cuda:0，Qwen3-8B 生成链）
- 活跃 cron：plan-014 监控中
- 活跃 Worker：`worker_analysis_plan-014-completion` + `worker_ops_check-014-status`（两个都在 running，可能是前 session 硬限前派出的）

### 3. 📊 当前状态
前 session 刚处理完 plan-004-v2 的负面结果（D009 reframe），正在等 plan-014（Qwen3-8B 生成链）完成。plan-014 是最后一个 P0 实验（RC9 Scale 验证）。已派 2 个 Worker 检查 plan-014 状态，但这些 Worker 是前 session 硬限前派出的，可能已经卡住或完成——**需要先检查这两个 Worker 的状态**。

Registry 概览：
- **RUNNING**: plan-014（Qwen3-8B 生成，cuda:0，383/~996 seeds @上次检查）
- **DONE(success)**: mvp-001, plan-001/001-fix, plan-002/002-eval, plan-003, plan-013, plan-015/015-v2（共 12 个成功实验）
- **DONE(negative)**: plan-004-v2（Claim 3 downstream utility）
- **DONE(failed)**: 8 个历史失败（tmux SIGHUP bug、重复提交、OOM），全部已由后续实验覆盖

### 4. 📋 待办（条件触发式）
- Worker `worker_analysis_plan-014-completion` / `worker_ops_check-014-status` 回调 → 读产出，判断 plan-014 是否已完成
- plan-014 仍 RUNNING → 等 cron 回调，不干预
- plan-014 完成 → 立即派 Worker：(1) 特征提取（用 Pythia-410M ref 对 Qwen3-8B 数据跑 extract_features），(2) LOGO 评估（加入 cross_generator_eval），(3) 更新 registry + report.md，(4) 汇报 Director（Scale claim RC9 结果）
- plan-014 LOGO F1 ≥ 0.75 → RC9 (Scale) 标记 ✅，**全部 P0 完成** → 向 Director 汇报并建议启动 Paper Agent
- plan-014 LOGO F1 < 0.70 → 可能需要分析原因（8B 模型是否 dropout 严重导致样本不足）
- 全部 P0 完成 + Director 批准 → 启动论文写作流程，先 Read `paper-plan` skill

### 5. 🎯 战略上下文
**项目核心结论链**：
- D001: MVP PASS (F1=0.84) → D002: 进入研究阶段 → D004/D005: Claim 2 dual dynamics framing → D006: 重定位为实证/概念贡献 → D007: Re-dream 条件达标 → D008: ensemble 一致性叙事 → D009: Claim 3 negative, reframe diagnostic-not-curative

**Story 三支柱**：Claim 1（Depth Discriminability, ✅）+ Claim 2（Differential Response + Complementarity, ✅）+ Claim 3（Diagnostic-not-Curative, ✅ as negative finding）。plan-014 是 RC9 (Scale) 补充证据，不是新 Claim。

**易错点**：
- plan-014 的数据在 `data/qwen3-8b/generations_shard0.jsonl`（符号链接到数据盘），特征提取时路径要对
- Qwen3-8B 是 **Base** 模型（不是 Instruct），生成用 continuation 模式
- nohup 启动的进程（plan-014）没有 tmux session，cron 用 PID 监控存活，不要用 tmux 命令去查
- AutoDL 网络操作前必须 `source /etc/network_turbo`
- 不要把 plan-004-v2 的负面结果当作"失败"——它是 honest negative finding，论文里要透明报告


---
