# director / loop_1.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`f278ea4b980aa859ff9a.json`](../../sessions/f2/f278ea4b980aa859ff9a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-13T22:36:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 分配：westd-22162 cuda:0~3（4 张 RTX PRO 6000 Blackwell 96GB）
- GPU 实际是 Blackwell sm_100+，**不是** Ada sm_89 或 Hopper sm_90——kernel 开发阶段必须验证 Triton/TileLang 兼容性
- 代码路径：远程 `/root/autodl-tmp/pacs/`，本地 `artifacts/pacs/`。训练代码真源在远程，论文/docs 真源在本地
- AutoDL 下载必须 `source /etc/network_turbo` + 用 ModelScope 替代 HuggingFace（HF ~500KB/s）
- MVP 阶段禁止启动完整研究规划（paper_framing / experiment_plan / dream_simulate）

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162 (connect.westd.seetacloud.com)，root 用户
- 工作目录：`/root/autodl-tmp/pacs/`
- Python/conda：aml-train 镜像，`/root/miniconda3/bin/python`，conda base 环境
- 模型：`/root/autodl-tmp/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B/`（已下载）
- Qwen2.5-7B：可能正在下载到 `/root/autodl-tmp/models/`（未确认完成）
- W&B / Git：未配置
- 活跃进程：**未确认**——Agent 卡死 47 分钟，GPU health 无数据。M1v3 应该已完成但无法确认

### 3. 📊 当前状态
Director session 刚从 RESET_BOTH 重启。**Agent session 疑似卡死**——idle 47 分钟，queue 显示 processing=true 但无活动。已发 `replace_agent_queue` 综合状态检查指令，排在 pending（depth=1），等 Agent 恢复后处理。

Registry:
- `mvp_ii_profiling_v3` — RUNNING（应已完成，~30-40min 实验，启动超过 1h）：random masking + 10%/20% sparsity + quantile segmentation + NaN guard
- `mvp_ii_profiling_v2` — ANALYZING (negative)：已出分析报告，所有 phase 均 super-additive，无 direction reversal
- `mvp_interaction_index_profiling` — DONE (failed)：P0 KV bug + P1 KDE failure

Worker `worker_infra_importance-vs-random_20260513T222105` 已完成（queue 通知被我清掉了，结果未读取）。

### 4. 📋 待办
- Agent 恢复 → 读取 M1v3 结果 JSON + importance-vs-random worker 输出 + GPU 状态
- M1v3 结果出：quantile segments 的 II magnitude CI 不重叠 → **MVP magnitude-PASS**；CI 重叠 → 看 importance-based 结果
- Importance-based II 显示 sub-additive（≥1 sparsity level）→ **MVP PASS**，narrative = "strategy-dependent direction reversal: naive compound destructive, intelligent compound synergistic, gap is phase-dependent"
- 两个都 FAIL → **MVP FAIL**，评估 pivot 选项：A) phase-agnostic compound vs single-axis, B) empirical characterization paper, C) reasoning model uniqueness（需 Qwen2.5-7B 对照）
- MVP PASS 后 → 立即启动 post-mvp-kickoff skill（paper_framing → experiment_plan → dream_simulate → update_roadmap）

### 5. 🎯 战略上下文
- **决策链**：D001(MVP方案) → D007(M1无效,P0+P1) → D008(M1v2否定direction reversal,M1v3最后诊断)
- **核心发现演化**：原始 "phase-dependent direction reversal" 已被 M1v2 否定。两个活路：(1) magnitude variation across segments, (2) strategy-dependent reversal（importance-based 初步 -0.91 vs random +9.38）。后者是更强 novelty 锚点
- **易错点**：M1v2 的 MVP PASS 是假阳性（execution phase NaN CI → 与任何 finite CI 不重叠 = artifact）。不要引用 M1v2 的 PASS 作为 MVP 通过依据
- **时间压力**：EMNLP 2026 ARR 截稿 5/25，距今 12 天。以 AI 团队速度基线，M1-M8 约 240h GPU 时间 + 3-5 天日历时间，但 MVP 还没过
- **GPU 架构坑**：Manager 说 "RTX 6000 Pro"，实际是 Blackwell（D006）。M4 kernel 和 M5+ throughput 仍需 Hopper (H20) 短租


---
