# agent / loop_1.md

**prism collapse mixing** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`7d0262e6d7907a54cda0.json`](../../sessions/7d/7d0262e6d7907a54cda0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-15T23:05:44+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 rtx6000-diagprobe 的 cuda:0 和 cuda:1（gpu_ids 白名单）
- 服务器无法连 HuggingFace，所有 HF 操作必须 `HF_HUB_OFFLINE=1`（模型已缓存）
- `WANDB_MODE=disabled`（W&B 未配置，不设会 crash）
- 预注册 pass/fail 标准不可修改（D003 决策）：ρ<0.5 at Gen3, >0.7 at Gen0-1, 单调退化≥15%, 双 seed
- compute_signals.py 已修复 OOM（forward hook），但只对 Gen 2+ 生效（Gen 1 用旧代码跑完了，数据有效）
- entropy 是 pass/fail 主信号；spectral_rank per-example ρ 基线低（~0.21）是结构性的，不是 bug，作辅助

### 2. 🖥️ 基础设施快照
- 服务器：rtx6000-diagprobe，工作目录 `/root/prism_collapse_mixing/`
- Python：conda base，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：`EleutherAI/pythia-410m-deduped` 缓存在 HF 默认路径，405M params
- 数据：`/root/prism_collapse_mixing/data/`（real_pool 579K 行，probe_set 5000 行，val_set 14881 行）
- 结果：`/root/prism_collapse_mixing/results/signals_gen{0,1}_seed{42,137}.json` 已完成
- 活跃进程：PID 197985（run_pipeline.py 父进程），子进程动态创建/销毁
- Cron：`mvp_collapse_decoupling_v2` 监控 PID 197985，interval=120s
- GPU：2× RTX PRO 6000 Blackwell，各 94GB

### 3. 📊 当前状态
Pipeline 正在跑 Gen 2（刚完成合成数据，正在混合或训练阶段），GPU 利用率 92-94%。

**Registry:**
- `mvp_collapse_decoupling_v2` — RUNNING，Gen 2 进行中
- `mvp_collapse_decoupling` — DONE/failed（旧条目，OOM 崩溃记录，保留历史）

**已完成的关键结果:**
- Gen 0: ρ(loss,entropy)=0.929, ρ(loss,spectral)=-0.211
- Gen 1: ρ(loss,entropy)=0.912, ρ(loss,spectral)=-0.205（两 seed 几乎一致）
- 文献调研完成→literature_map.yaml 已写入，novelty 成立（无人系统量化过跨代 ρ）

**等待中:**
- Worker `ssh:review-analysis-scripts`（审查 analyze_correlation.py + plot_results.py + 拉 Gen 0 完整指标）——可能已完成但未收到回调
- Cron 回调：pipeline 完成或崩溃时触发

### 4. 📋 待办
- Cron 回调 pipeline 完成 → spawn worker 读 Gen 2+3 信号 JSON → 更新 registry metrics → 汇报 Director
- Gen 2 信号出来后 → 评估 ρ 衰减速度：若加速下降则 pass 有望，若持平则启动 Contingency Plan (a)（扩到 5 代）
- 全部 3 代完成 → 跑 analyze_correlation.py 做 pass/fail 判断 → 跑 plot_results.py 生成图表 → register_artifact
- review-analysis-scripts Worker 回来 → 如果报了 bug，在 Gen 3 完成前派 Worker 修复
- 结果 = negative → 按 red-section skill 产 Framing 调整提案，禁止默默跑下一个实验
- 结果 = success → 更新 report.md，与 experiment-matrix 对标，向 Director 建议 research 阶段方案

### 5. 🎯 战略上下文
- **核心风险：ρ 衰减太慢。** Gen 0→1 仅降 1.8%（0.929→0.912），线性外推 Gen 3≈0.88，远不到 0.5。但 collapse 通常非线性加速，Gen 2-3 是关键。
- **Contingency 优先级**：(a) 扩代数 → (b) 加 tokens/gen → (c) 换大模型。不跳级。
- **DDL 5/25（EMNLP ARR）**，预计 5/16 上午出完整 pass/fail。即使 fail 也有 10 天调整。
- **易错点**：spectral_rank per-example ρ 一直很低（~0.2），不要误判为"已经脱钩"——它从未耦合过，不满足 Gen 0-1 |ρ|>0.7 的前提条件，不能用于 pass/fail 判断。
- **两 seed 极度一致**是好事（可重复），但也意味着如果 fail 就是 robustly fail，不存在"一个 seed 勉强 pass"的弱 pass 情况。
- D001: MVP 方案确定 | D002: 量化 pass/fail 阈值 | D003: 不改预注册标准，entropy 为主信号


---
