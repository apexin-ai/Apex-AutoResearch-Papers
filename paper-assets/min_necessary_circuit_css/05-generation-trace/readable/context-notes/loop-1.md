# director / loop_1.md

**Transformer Model EAP-IG** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`60b1961cd97785223059.json`](../../sessions/60/60b1961cd97785223059.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-12T16:50:14+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 仅限 cuda:5**@cqa1-21977。之前发生过越界事故（进程跑到 cuda:0/cuda:1，D007），已被 Reviewer critical。所有启动命令必须 `CUDA_VISIBLE_DEVICES=5`，代码开头必须有 assert 验证。
- 服务器上有其他项目进程（cuda:3 cost-verify-agent-rl，cuda:4 其他项目），绝不能 kill 非本项目进程。
- MVP 当前用 auto-circuit mask_gradient 作为 Edge Pruning proxy（实质是 gradient 方法）。Phase 2 **必须**换 L0 Edge Pruning（已实现 `edge_pruning_l0.py`，已上传服务器）。不可用 proxy 结果作为论文正式数据。

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，SSH `root@connect.cqa1.seetacloud.com:21977`，密码存 secret `ssh_password_cqa1_21977`
- 工作目录：`/root/min_necessary_circuit_css/`（MVP 代码 + 缓存）；另有 `/root/structfuse-mvp/`（旧目录，勿用）
- GPU：1× RTX 4090D 24GB，cuda:5
- 活跃进程：PID 98594 `run_mvp.py`（ACDC greedy search，~16:27 UTC ETA，可能已完成）
- 缓存：`cache_eap_ig.json` + `cache_edge_pruning.json` 已存在，ACDC 无缓存
- Phase 2 代码已上传：`edge_pruning_l0.py`（L0 mask optimization）+ `ifr_discovery.py`（IFR activation decomposition）+ `collect_results.py`（Wilson CI）+ `test_l0_ep.sh`

### 3. 📊 当前状态
ACDC 在服务器上自动跑（nohup），上次报 49.6%@6.87 it/s，ETA ~16:27 UTC。可能已完成。完成后 `run_mvp.py` 自动写 `mvp_results.json`，然后跑 `collect_results.py` 获取 gate 判定。

Registry 空——MVP 未注册为正式实验。无 Worker / 无 Cron。

**第一件事**：SSH 检查 ACDC 是否完成 + 收集结果 + 汇报 gate 判定。

### 4. 📋 待办
- ACDC 完成 → 跑 `collect_results.py` → 汇报 gate 判定（core_off_diagonal_pct + Wilson CI）
- off-diagonal ≥10% → gate pass（保守估计，D008），进入 Phase 2。注意当前是 2 族 proxy（EAP-IG gradient + mask_gradient gradient + ACDC causal），≥10% 仍可信
- off-diagonal <10% → 不直接判 fail，部署 L0 EP 到 `circuit_discovery.py`（替换 mask_gradient），重测 IOI 后再判
- off-diagonal <2%（两组 task）+ ΔF 无差异 → kill project（D003）
- gate pass 后 → Phase 2：先 Qwen-2.5 0.5B/IOI K=3 checkpoint（EAP-IG + L0 EP + IFR），验证 family constraint 有效性（D004）
- Phase 2 前必须向 Manager 申请更多 GPU（全量需 4-6 卡，当前仅 1 卡）

### 5. 🎯 战略上下文
- 项目核心：跨电路发现方法的二值共识（CSS）+ family-agreement constraint 优于 score averaging，用于 OOD 鲁棒电路编辑
- 目标 EMNLP 2026 Main（ARR deadline 5月25日，剩 13 天）
- 决策链：D001 MVP 定义 → D002 灰区规则 → D003 kill criteria → D004 K=3 checkpoint → D005 AtP*不可用改 K=3 → D006 大模型用 IFR → D007 GPU 越界修复 → D008 mask_gradient proxy 解读协议
- **易错点**：(1) 服务器有两个目录 `/root/min_necessary_circuit_css/`（正确）和 `/root/structfuse-mvp/`（旧，勿用）(2) kill 进程前必须确认 PID 对应的是哪个进程，上次误杀了进度更快的 PID 导致 ACDC 从头跑 (3) Reviewer 指出 IFR 和 L0 EP 都有 per-layer 粒度退化（非 per-head），分析 off-diagonal 时需考虑粒度效应
- Reviewer 已交付两场景叙事框架（场景 A ≥10% Main / 场景 B <10% Findings），可直接对着结果套用


---
