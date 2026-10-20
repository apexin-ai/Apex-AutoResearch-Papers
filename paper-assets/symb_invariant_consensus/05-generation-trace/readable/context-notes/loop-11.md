# reviewer / loop_11.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`10b50d900c4a43539989.json`](../../sessions/10/10b50d900c4a43539989.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-21T17:59:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- **westd-16639 GPU 白名单**：cuda:0 Mistral(8000), cuda:1 Qwen3(8001), cuda:2 70B-AWQ(8002), cuda:3 新Mistral(gpt-5.5 extraction)。不要动 cuda:2 上的 70B pipeline。
- **westd-25068**：当前无活跃 GPU 进程，72B BF16 模型正在从 ModelScope 重新下载（20GB/100GB）。旧 safetensors 全部损坏已删。
- **R1-Distill 自提取数据不可用**：BPE bug 导致 extraction_rate=1.28%，SC=32.35% 是假数据。只能用 cross-model (Mistral) 提取的数据。metrics.json 的 exp_id/model 字段被污染（写着 Qwen2.5-72B-Instruct-AWQ），不要信元数据。
- **论文数据必须用 Reviewer 核实过的数字**：R1-Distill Δ=+2.45pp（不是 Worker 报的 +1.96pp），gpt-4.1 Δ=-1.47pp。Worker 有过数次误报。

### 2. 🖥️ 基础设施快照
- **westd-16639** `/root/symb_invariant_consensus/`
  - vLLM PID 413036 (Mistral:8000, cuda:0), 413844 (Qwen3-14B:8001, cuda:1, 当前 0% util — Phase 2 只用 Mistral), 435354 (72B-AWQ:8002, cuda:2), 466621 (新Mistral:cuda:3, gpt-5.5 extraction)
  - Cross-model SICA 2×2: PID 414515, run.log 在 results/exp_d126_crossmodel_sica/
  - 70B pipeline: PID 436084, 18/204, ~16min/题
- **westd-25068** `/root/symb_invariant_consensus/`
  - 72B 模型下载中: `/root/autodl-tmp/models/Qwen2.5-72B-Instruct/._____temp/` 20GB/100GB
  - Gemini 2.5 Pro SC: 运行中（API），~20/204
  - 4× RTX PRO 6000 Blackwell 96GB 全空闲
- **本地 workspace**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/`

### 3. 📊 当前状态
**刚完成**：
- R1-Distill 全 204 题 cross-extraction 核实 — SC=152/204=74.51%, SICA=157/204=76.96%, Δ=+2.45pp ✓
- gpt-5.5 SC=172/204=84.31% ✓, o3 SC=162/204=79.41% (8 题 n_valid=0) ✓
- ROADMAP 审查 — PASS，已采纳 Reviewer 修正

**RUNNING/PREPARING**:
- `exp-d135-frontier-scb` PREPARING — gpt-5.5 extraction 刚部署(cuda:3), o3 待清洗, gemini ~20/204
- `exp-d126-crossmodel-sica` PREPARING — Phase 2 活跃，ETA May 22 AM
- `exp-d126-70b-sica` PREPARING — 18/204, ~50h ETA（太慢）
- `exp-d126-r1-distill-sica` PREPARING — 204 题 cross-extraction 已完成，可改 DONE

**等待中**：Worker 回调 gpt-5.5 extraction、o3 清洗、70B westd-25068 部署

### 4. 📋 待办（条件触发式）
- gpt-5.5 extraction worker 回调 → 核实 BR/κ 指标，对比 gpt-4.1 cross pattern (κ 高→Δ 负?)
- o3 数据清洗 worker 回调 → 核实排除 0-trace 题后的 SC，检查 pipeline 对 0-trace 的 fallback 逻辑
- Cross-model SICA 2×2 完成 (PID 414515) → 核实 Mistral↔Qwen3 双向 Δ、检查是否支持 D135 narrative
- 70B westd-25068 vLLM 启动 → 核实 tp=4 配置、GPU 白名单、pipeline 参数
- V16 Paper Agent Patch 启动 → 进入审查模式 B，读 paper-quality-lessons skill，按 §5 维度审

### 5. 🎯 战略上下文
**核心结论**：Self-extracted constraints project model bias (BR>1)。Cross-model escape 仅在 **低 Process-κ + 能力匹配** 时有效（R1-Distill κ=0.25 成功 +2.45pp, gpt-4.1 κ=0.79 失败 -1.47pp）。

**关键决策链**：D126(三线并行) → D131(R1-Distill定位) → D133(BPE修正) → D134(gpt-4.1 SC) → D135(cross-model条件性escape, Process-κ双条件)

**易踩的坑**：
1. **Worker 数字不可信** — 本轮出现 3 次 Worker 误报（R1-Distill Δ差 0.49pp、93题baseline对不上、westd-25068 vs 16639 搞反）。所有 Worker 声称的指标必须 SSH 读原始文件验证。
2. **o3 SC=79.41% 是伪值** — 8 题 n_valid_answers=0，真实 SC 更高。论文中报告 o3 必须注明有效 trace 数或排除 0-trace 题。
3. **70B 数据大概率赶不上 V16** — westd-16639 上 18/204 需 50h，westd-25068 还在下模型。Paper Agent 可能需要在无 70B 数据下写 V16。
4. **br_kappa_metrics.json 是自提取（坏的）**，crossmodel_metrics.json 是 cross-model（好的），不要搞混。


---
