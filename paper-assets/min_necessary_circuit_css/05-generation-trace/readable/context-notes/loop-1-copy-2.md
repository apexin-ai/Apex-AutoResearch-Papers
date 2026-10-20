# agent / loop_1.md

**Transformer Model EAP-IG** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`fabe1ac7e20835b54a96.json`](../../sessions/fa/fabe1ac7e20835b54a96.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-12T16:50:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单仅 cuda:5**@cqa1-21977（RTX 4090D）。之前违规用 cuda:0/1 被 Director CRITICAL，已修复但教训深刻
- **Kill 多个同名进程前必须确认各 PID 进度**——本轮误杀了进度 91.4% 的 PID 98300，导致 ACDC 从头重跑浪费 2h+
- **ACDC 无增量缓存**，进程中断后必须从头跑。不要轻易 kill ACDC 进程
- MVP 阶段 Edge Pruning 用的是 auto-circuit mask_gradient（preliminary），**不是** L0 实现。汇报时必须标注 preliminary

### 2. 🖥️ 基础设施快照
- **服务器**：cqa1-21977，SSH config 已配置
- **MVP 代码目录**：`/root/structfuse-mvp/`（run_mvp.py 实际运行位置）
- **另一目录**：`/root/min_necessary_circuit_css/`（L0 EP + IFR 已上传，import 验证通过）
- **本地 artifacts**：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/structfuse-mvp/`
- **已部署脚本**：`collect_results.py`（Wilson CI）+ `test_l0_ep.sh`（L0 EP 单独测试），均在 `/root/structfuse-mvp/`
- **缓存文件**：`cache_eap_ig.json` (1.3MB) + `cache_edge_pruning.json` (1.3MB) 在 `/root/structfuse-mvp/`
- **活跃进程**：PID 98594 跑 `run_mvp.py`（ACDC 阶段），GPU-5 100% util
- **无 cron / 无 tmux**，用 nohup 后台执行

### 3. 📊 当前状态
**MVP pilot 正在运行**，ACDC 最后阶段（上次检查 49.6%，6.87 it/s，ETA ~16:27 UTC）。EAP-IG + Edge Pruning 已缓存完成。

**Registry 为空**（MVP 未注册为正式实验，直接通过 Worker 手动管理）。

**等待中**：
- ACDC 完成 → `mvp_results.json` 自动生成 → 跑 `collect_results.py` → 汇报 gate 判定（core_off_diagonal_pct + Wilson CI）
- 已向 Director 汇报 ETA ~16:27 UTC，Director 在等最终结果

**Phase 2 代码栈已就绪**：L0 EP (edge_pruning_l0.py) ✅ + IFR (ifr_discovery.py) ✅ + CSS binarize ✅ + LargeModelConfig ✅，均已上传到服务器两个目录并 import 验证通过。Artifact 已注册 (art_20260512_833006)。

### 4. 📋 待办
- **ACDC 完成（mvp_results.json 出现）→** `cd /root/structfuse-mvp && python3 collect_results.py` → 读取 gate_verdict + off_diagonal_pct + Wilson CI → 向 Director 汇报完整结果 → 按 gate 规则决策
- **off-diagonal ≥10% →** PASS_MAIN，立即推进 Phase 2（Qwen-2.5 0.5B / IOI K=3 含 IFR）
- **off-diagonal 5-10% →** PASS_FINDINGS，追加 Arithmetic 任务验证
- **off-diagonal <2% →** KILL，按 red-section skill 产出 Framing 调整提案
- **MVP 结果出来后 →** 跑 `test_l0_ep.sh` 验证 L0 EP 在 GPU 上的实际表现（GPU-5 空闲后）
- **如果 off-diagonal <10% 需要 L0 EP 重测 →** 服务器已就绪，一键 `bash /root/structfuse-mvp/test_l0_ep.sh`

### 5. 🎯 战略上下文
- **目标**：EMNLP 2026 Main（ARR deadline 2026-05-25，剩 13 天）
- **核心假设**：CIRCUS-core 边中 ≥10% 落入 off-diagonal cell（method-specific but not CSS-confirmed）
- **决策链**：D001(MVP定义) → D002(灰区规则) → D003(kill criteria) → D004(K=3 checkpoint) → D005(AtP*不可用→K=3) → D006(IFR为大模型第三方法) → D007(GPU越界修复)
- **MVP 用的 EP 是 mask_gradient（preliminary）**，论文正式结果必须用 L0 实现。Director 已明确要求 Phase 2 前切换
- **易错点**：服务器有两个目录 `/root/structfuse-mvp/` 和 `/root/min_necessary_circuit_css/`，MVP 代码在前者运行，L0/IFR 两个目录都有。部署新代码时确认目标目录
- **ACDC 速度随层深度剧烈波动**（1.5-24 it/s），不要用瞬时速度推算 ETA，用已处理 edge 占比更可靠


---
