# director / loop_1.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`a048a8e2f693cbde381b.json`](../../sessions/a0/a048a8e2f693cbde381b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-14T15:59:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westb-52439 的 cuda:0 和 cuda:1（2× RTX PRO 6000 Blackwell 98GB）
- OLMo 重跑优先于 Pythia topk50 占 cuda:0——OLMo 是 cross-model generalization gate（plan_005 要求 ≥45% 跨模型精度），topk50 是策略鲁棒性
- Dream 回调未处理前不得批准新的 P0 实验启动（post-mvp-kickoff 流程硬约束）
- experiment_plan.yaml 中 plan_001b/001c 已拆分，registry_id 分别为 pythia_temp09_001 / pythia_topk50_001，不要混淆
- DCOL contingency：如果 DCOL 提升 < 5pp over RF，Atlas (Claim 2) 升为主贡献，DCOL 降为 framework 内方法

### 2. 🖥️ 基础设施快照
- 服务器：westb-52439，工作目录 `/root/autodl-tmp/recursive_gen_depth_est/`
- Python：conda base 环境，`/root/miniconda3/bin/python`
- 模型路径：`/root/autodl-tmp/models/` 下有 `pythia-1.4b`、`olmo-1b-hf`（olmo-1b 也有副本）、`gpt2-xl`
- 数据输出：`/root/autodl-tmp/recursive_gen_depth_est/data/{pythia,olmo,gpt2xl,pythia_temp09,pythia_topk50}/`
- Checkpoints：`/root/autodl-tmp/recursive_gen_depth_est/checkpoints/{pythia,olmo,gpt2xl}/`
- 日志：`/root/autodl-tmp/recursive_gen_depth_est/logs/`
- HF cache：`/root/autodl-tmp/.hf_cache`
- W&B：未配置
- 活跃进程（截至 14:55 UTC）：
  - cuda:0: Pythia temp09 (PID 125083, lora_finetune.py)
  - cuda:1: GPT-2 XL pipeline (PID 126022, generate_next_depth.py depth-1)

### 3. 📊 当前状态
刚完成：novelty self-check 回复用户（结论：核心新颖性成立，无高度相似竞品）；rogue GPT-2 XL 进程清理；OLMo 脚本修复（model path + target_modules）。

Registry 实验状态：
- `cross_model_gpt2xl_001` — RUNNING cuda:1，~19:00 UTC 完成
- `pythia_temp09_001` — RUNNING cuda:0，~17:00 UTC 完成（注意 registry server 字段误记为 autodl-rtx6000，应为 westb-52439）
- `cross_model_olmo_002` — PREPARING（等 cuda:0 释放）
- `pythia_topk50_001` — PREPARING（等 cuda:1 释放）
- `cross_model_olmo_001` — FAILED（脚本引号 bug，depth-0 完成但 1-3 未跑）
- `mvp_pipeline_pythia_002` — SUCCESS（MVP 基准：78.2% 4-class acc）

等待中：
- Dream `dream_20260514T140607`（reviewing 阶段，即将完成）→ 需 Read dream-report-action skill 处理
- Pythia temp09 完成回调
- GPT-2 XL 完成回调

### 4. 📋 待办
- Dream 回调到达 → Read `skills/global/dream-report-action.skill.md` → 三档对比分析 → 构建行动列表 → 批准/调整 P0 实验
- Pythia temp09 完成 → cuda:0 释放 → **立即启动 OLMo 重跑**（cross_model_olmo_002，脚本已修好，depth-0 checkpoint 可复用跳过 ~5min）
- GPT-2 XL 完成 → cuda:1 释放 → 启动 Pythia topk50（pythia_topk50_001）
- 4 条 pipeline 全部完成（~21:00 UTC）→ plan_004 DCOL 训练 + plan_006 Atlas 分析可启动
- 修复 pythia_temp09_001 registry server 字段（低优先级）

### 5. 🎯 战略上下文
- **D001**: MVP PASS — 递归生成深度可从统计特征高精度区分（78.2% 4-class, chance=25%）
- **核心 story**: 3 claims — ordinal depth estimation feasible (DCOL) / Depth Degradation Atlas (EDD) / depth-graduated curation > binary filtering
- **venue**: EMNLP 2026 ARR May 25 deadline，special theme "New Missions for NLP Research" 精准匹配
- **novelty 已验证**: 无竞品做 ordinal depth estimation from text alone；Drayson (EMNLP 2025) 最接近但假设 depth 已知；需补引 Strong Model Collapse (ICLR 2025)、Surplexity、"The Price of Format"
- **易错点**: (1) OLMo 模型有 olmo-1b 和 olmo-1b-hf 两个目录，脚本已修为 olmo-1b-hf；olmo-1b 缺 configuration.json，如果启动报 config error 先查这个。(2) Qwen2.5 系列已证明不适合本项目（代码生成过多），不要再尝试。(3) 3-class (d1/d2/d3) 实验已做完：70.8% acc，证明深度梯度信号独立于 real-vs-synthetic 区分


---
