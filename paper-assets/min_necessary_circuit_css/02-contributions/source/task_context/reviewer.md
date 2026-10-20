---
loop: 3
reason: max_wall_time
updated: '2026-05-13T01:44:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目**只能用 cuda:5**（6 卡机器 index 0-5）。D007 记录了一次越界到 cuda:0/1 的事故，被 CRITICAL 打回。每次审查训练实验必须 `nvidia-smi` 核对。
- 服务器上同时跑着另一个项目 **structfuse**（非 min_necessary_circuit_css）的 batch_extract + CodeQL + 模型下载，占大量 CPU/内存。不要把 `/root/autodl-tmp/structfuse/` 的进程误认为本项目的。本项目代码在 `/root/min_necessary_circuit_css/`。
- ARR deadline **2026-05-25**，剩余 12 天。

### 2. 🖥️ 基础设施快照
- 服务器：**cqa1-21977** (root)，6× RTX 4090D (24GB each)
- 工作目录：`/root/min_necessary_circuit_css/`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 模型：GPT-2 Small（HF cache，HF_HUB_OFFLINE=1 模式运行）
- W&B：未配置（不检查 W&B）
- 活跃进程：**无**。所有 GPU 空闲（cuda:5 仅 3MiB 残留）。无 tmux session 存活。
- 其他项目进程占 CPU：starcoder2-3b 下载 (PID 444913/494664/570727) + structfuse batch_extract (PID 577872) + CodeQL queries — 均非本项目。

### 3. 📊 当前状态
**D020 暂停了 MVP pass 判定。** 这是最重要的状态。

实验列表：
- `mvp_pilot_gpt2_ioi_v3` — DONE/success。off-diagonal 13.3%（≥10% 线），但 stable_core CPR=-0.187 **三重 FAIL**：IOI recall 仅 0.17，faithfulness 为负。根因是 D013 CIRCUS 1D percentile 退化为 top-k，未修复。
- `mvp_arithmetic_gpt2_k3` — PREPARING。D018/D019 要求的 Arithmetic 确认实验，尚未部署。
- v1/v2 已 killed/failed，不再相关。

**等待中**：Agent 应先修复 CIRCUS（2D non-nested grid），再重跑 IOI 分析 + 部署 Arithmetic 实验。目前无活跃 Worker 在做这件事（所有进程空闲）。

### 4. 📋 待办（条件触发式）
- Agent 声称修复 CIRCUS 并重算 IOI → **验证远程 `circus.py` 是否真的改了**（D016 教训：Agent 曾声称修复但远程文件零改动，用 `ssh_read_only` 读代码确认 2D grid 实现）
- Arithmetic 实验提交 → 检查 `CUDA_VISIBLE_DEVICES=5` + 确认代码用的是修复后的 CIRCUS
- 重算后 stable_core CPR 仍为负 → CRITICAL，cross-tabulation 附加价值不成立，需触发 framing 讨论（CSS alone 可能就是论文的全部贡献）
- 重算后 stable_core CPR > 0 且 < CSS≥0.67 → WARNING，说明 CIRCUS 加分有限但不为负，论文需诚实讨论
- 重算后 stable_core CPR > CSS≥0.67 → 核心假设成立，MVP 可正式 PASS

### 5. 🎯 战略上下文
**核心发现链**：
- D012 确立 CIRCUS×CSS cross-tabulation（4-cell taxonomy）为论文核心 novelty
- D017 揭示 CIRCUS-CSS 作用域不匹配导致 off-diagonal 结构性膨胀 ~98%（已修复方向：统一 edge universe）
- D020 揭示 CIRCUS 本身退化（1D→top-k）导致 stable_core 系统性选错边 → faithfulness 为负

**最容易判断错的事**：
1. **不要被 off-diagonal 13.3% 迷惑**。D017 修复后这个数字可能来自仅 15 条 CIRCUS-core 边中的 2 条，CI 极宽 [1.7%, 40.5%]，统计功效严重不足。
2. **CSS 单独表现很好**（recall=1.0, CPR=+0.063），cross-tabulation 的附加价值是**未被证实的**。整个论文 story 取决于修复后的 CIRCUS 是否真正给 CSS 增值。如果修复后仍不增值，论文可能需要 pivot 到"CSS alone 就够了"的 framing。
3. **D016 教训**：Agent 声称完成了修复但远程代码未改动。任何 Agent 声称"已修复 CIRCUS"的 claim，**必须 ssh_read_only 读远程 circus.py 源码确认 2D grid / non-nesting 逻辑存在**，不信口头报告。
4. **EP 也是坑**：当前 mask_gradient EP 与 EAP-IG 同属 gradient 族（D008），Phase 2 必须换 L0 EP，但 L0 EP 也有 per-layer 粒度退化问题（D016）。三方法中两个有粒度问题，edge-level CSS 叙事脆弱。
