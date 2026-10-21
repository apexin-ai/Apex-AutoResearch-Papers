# agent / loop_3.md

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`f2307e9b6642c927268a.json`](../../sessions/f2/f2307e9b6642c927268a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-15T22:00:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: 仅 `westd-32608:cuda:0`，严禁使用其他 GPU
- **模型固定 QwQ-32B**，路径 `/root/autodl-tmp/models/QwQ-32B/Qwen/QwQ-32B/`（ModelScope 嵌套结构），不可替换
- **vLLM 独占**: 实验运行期间禁止其他进程向 vLLM 发请求
- **vLLM max_model_len=16384**，32768 会导致 engine core 初始化失败
- **rescore 必须纯 CPU**: 不重新生成 trace、不做 extraction、零网络请求
- **May 19 UTC 硬 checkpoint**: MVP 未 pass → 放弃 EMNLP May 25，切 AAAI 2027 (Aug 1)
- **P5 "120→80 翻转" 是虚假声明**（D008），禁止引用

### 2. 🖥️ 基础设施快照
- **服务器**: westd-32608, root, 工作目录 `/root/symb_invariant_consensus`
- **Python**: `/root/miniconda3/bin/python`（conda base），激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **关键包**: torch 2.11.0+cu130, vllm 0.20.2, z3-solver 4.15.4, CUDA 12.8
- **GPU**: NVIDIA RTX PRO 6000 Blackwell 98GB, vLLM 占 61 GiB (~91%)
- **模型路径**: `/root/autodl-tmp/models/QwQ-32B/Qwen/QwQ-32B/`
- **数据**: AIME subset `/root/symb_invariant_consensus/data/aime2024_subset.json` (30题), MATH subset `data/math500_subset.json` (50题)
- **活跃进程**: sica_aime30_v3, PID 129992, tmux session, cuda:0, cron 监控中
- **磁盘**: 根分区 16GB free, 数据盘 /root/autodl-tmp 232GB free

### 3. 📊 当前状态
**sica_aime30_v3 正在运行** (22/30, SICA=SC=72.7%, 0pp gap, ETA ~04:45 UTC 05-16)。这是从 v2 (P5卡死被kill) 恢复的 resume run，timeout 已修为 1800s。

**核心发现（结构性）**: QwQ-32B 在所有已测域（AIME 22题 + MATH L4-5 5题 + smoke 5题 = 32题）中产生**零答案分歧**——每题 K=12 条 trace 只出现 1 个候选答案。SICA 机制只能在多候选竞争时产生差异，单候选下 SICA≡SC。这不是 bug，是 reasoning model 的结构性特征（D010/D011）。

**已完成的 v4 代码修复**（在磁盘上但 v3 进程未加载）: max_tokens 16384, fallback extraction, finish_reason 检查, save-intermediates, Int/Real sort 统一, ProofWriter prompt 适配。

**Worker 池**: 0 running（违反 L1 #4，但当前阻塞在 v3 完成 + GPU 独占）。

### 4. 📋 待办（条件触发式）
- **v3 cron 回调到达** → (1) spawn Worker 做 vote diversity 分析（全 30 题候选答案分布）; (2) update_registry + report.md; (3) 向 Director 汇报 0pp 结论
- **vote diversity 确认单候选** → spawn Worker 准备 MATH-10 trace-only 诊断（L4-5 10题子集 `data/math500_L45_10.json`，用 v4 代码 --max-tokens 16384 --save-intermediates，~1h）
- **MATH-10 也确认单候选（≥80%题单候选）** → 立即转逻辑域：spawn Worker 并行准备 ProofWriter-30 + FOLIO-30 数据和评测脚本，向 Director 汇报 pivot 到逻辑域
- **MATH-10 意外出现 ≥20% 多候选率** → 回到 MATH-50 全量实验
- **逻辑域实验完成** → 按 on-experiment-done 流程处理，与 AIME/MATH 数据合并做 domain boundary 分析
- **任何实验 conclusion=negative** → 走 red-section Framing 提案流程，禁止默默跑下一个

### 5. 🎯 战略上下文
- **项目本质**: SICA 的核心假设（跨路径 MAX-SAT 约束验证能检测统计共识遗漏的矛盾）在数学域遭遇结构性挑战——QwQ-32B 答案太一致，无矛盾可检测
- **决策链**: D001(MVP设计) → D002(拒绝CRD回归SICA) → D003(MVP标准v2) → D004-D006(优先AIME) → D007-D009(parser/truncation修复) → D010(0pp结构性确认) → D011(转向逻辑域策略)
- **最易判断错的事**: 不要以为修好 parser/max_tokens 就能打破 0pp——根因是 QwQ-32B 答案一致性，不是工程 bug。v4 修复只是让数据更干净，不改变单候选结构
- **逻辑域是最后机会**: ProofWriter/FOLIO 的 FOL 规范化程度高、answer distribution 天然多候选（True/False/Unknown）、Z3 parser 损耗低。如果逻辑域也 0pp → SICA 在 reasoning model 上 FAIL，需要 Director 决策是否换弱模型或放弃
- **CRD 数据已有**: crd_folio_main (FOLIO 204题, Qwen3-32B-AWQ) 已完成，baseline acc 74%，pipeline acc 81.4%，可作为对比参考但方法不同(CRD≠SICA)
- **时间极紧**: 距 May 19 checkpoint 仅 4 天，距 EMNLP ARR May 25 仅 10 天


---
