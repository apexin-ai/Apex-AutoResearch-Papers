# reviewer / loop_1.md

**Transformer Model EAP-IG** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`44f9e247103814707e36.json`](../../sessions/44/44f9e247103814707e36.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-12T16:50:19+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目**只能用 cuda:5**@cqa1-21977（resources.yaml 白名单 `gpus: [cuda:5]`）
- 已发生一次 GPU 越界事故：进程跑到 cuda:0/1，被我 CRITICAL 打回。根因是 `run_mvp.py` 未设 `CUDA_VISIBLE_DEVICES=5`，已修复（代码硬编码 + 启动命令双重保险）。下一个"你"每次看到新进程必须独立 `nvidia-smi --query-compute-apps` 核对 UUID→index 映射
- cuda:4 上有 `/root/structfuse` 目录的进程（非本项目），不要误判为越界

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977（host: connect.cqa1.seetacloud.com:21977），账号 root
- 工作目录：`/root/min_necessary_circuit_css/`（MVP 运行代码在此）；`/root/structfuse-mvp/` 是早期上传目录（可忽略）
- Python：`/root/miniconda3/bin/python3`（conda base 环境）
- 已装：transformer-lens, auto-circuit, eap-ig, torch
- 代码文件：`run_mvp.py`, `circuit_discovery.py`, `css.py`, `circus.py`, `cross_tabulate.py`, `evaluation.py`, `config.py`, `edge_pruning_l0.py`, `ifr_discovery.py`
- 缓存：`cache_eap_ig.json`(1.3MB), `cache_edge_pruning.json`(1.3MB) — EAP-IG 和 mask_gradient 结果已缓存
- 活跃进程：PID 98594（`python3 run_mvp.py`，cuda:5，ACDC 阶段 ~48%，~40min 后完成）
- W&B：未配置（不查 W&B）
- 无 tmux/cron

### 3. 📊 当前状态
MVP pilot 正在运行（GPT-2 Small / IOI，K=3）。EAP-IG + Edge Pruning(mask_gradient) 已完成并缓存，ACDC 跑到 ~50%，预计 ~40 分钟后出 `mvp_results.json`。

Registry 空（Agent 尚未注册 MVP 实验）。

**关键待判定**：MVP 的 Edge Pruning 实际用的是 auto-circuit `mask_gradient`（gradient 族），不是 L0 mask optimization。因此当前 MVP = 2 gradient + 1 greedy causal = 2 族。Director 已知晓（D008 解读协议），L0 EP 代码已上传到服务器但未接入 `circuit_discovery.py`。

### 4. 📋 待办
- **ACDC 完成 + mvp_results.json 生成** → 审查 off-diagonal %（用 `core_off_diagonal_pct` 指标，不是代码原始的 `off_diagonal_pct`——后者分母错误，我已 CRITICAL 标记过）。按 D008 解读：≥10% 可信为 gate pass（保守估计）；<10% 需 L0 EP 重测
- **若 ≥10%** → 确认 gate pass，提醒 Director Phase 2 必须换 L0 EP + 部署 IFR
- **若 <10%** → 要求 Agent 将 `circuit_discovery.py` 的 `run_edge_pruning` 改为调用 `run_edge_pruning_l0`，用 L0 EP 重跑 IOI 后再判 gate
- **Agent 注册 MVP 到 registry** → 审查 spec 完整性（训练命令、服务器、数据条数、种子）
- **Phase 2 启动前** → 验证 `circuit_discovery.py` 已切换到 L0 EP；验证 IFR 可从 `/root/min_necessary_circuit_css/` import

### 5. 🎯 战略上下文
- **决策链**：D001(MVP定义) → D002(灰区规则) → D003(kill criteria) → D004(K=3 checkpoint) → D005(AtP*不可用,K改3) → D006(大模型用IFR,triangulation框架)
- **核心假设**：CIRCUS-core 边中 ≥10% 落入 off-diagonal cell（方法内稳定但跨方法不一致）
- **目标**：EMNLP 2026 Main（ARR deadline 2026-05-25）
- **最易判断错的事**：`cross_tabulate.py` 的 `off_diagonal_pct` 属性分母是全部边而非 CIRCUS-core 边——这是 BUG，我已 CRITICAL 标记。正确指标应为 `method_specific / (stable_core + method_specific)`。如果 Agent 没修，结果会被严重稀释导致误判 <2% 触发 kill
- **易踩的坑**：(1) L0 EP 的 per-layer mask 粒度与 IFR 相同（per-head 退化），论文需披露 (2) GPT-2 Small 用 3 因果族（EAP-IG/EP/ACDC），大模型用 2 因果+1 相似度（EAP-IG/EP/IFR），CSS 语义不同，论文需区分 (3) CIRCUS baseline 是 "CIRCUS-style config-bagging on EAP-IG" 非原版 CIRCUS（原版用 CLTs）


---
