# director / loop_1.md

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`b669558fd862637f9fdb.json`](../../sessions/b6/b669558fd862637f9fdb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-13T19:24:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-11235 的 cuda:0 和 cuda:1（项目配置白名单）
- 服务器工作目录已从 `/root/phase-gated-compound-sparse` 重命名为 `/root/div_cal_verify`（今天刚做，registry 路径已全部修正）
- 数据目录 `/root/autodl-tmp/div_cal_verify/`（同步重命名）
- 脚本内部用 `GPU_ID=${1:-0}` 覆盖 CUDA_VISIBLE_DEVICES，必须传参数指定 GPU（`bash run_xxx.sh 0` 或 `bash run_xxx.sh 1`），不能靠外部环境变量
- env.sh 已添加 `export TRANSFORMERS_OFFLINE=1`，所有脚本 source env.sh 即可
- GPU 0 有 ~49GB 驱动级僵尸显存（容器限制无法 reset），但剩余空间够用。GPT2-medium 后续方法并行时可能需关注

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235 (connect.westd.seetacloud.com)，RTX PRO 6000 98GB × 2
- 工作目录：`/root/div_cal_verify/`
- 数据盘：`/root/autodl-tmp/div_cal_verify/`
- HF cache：`/root/.cache/huggingface/hub/`（gpt2、gpt2-medium、contriever 均已缓存）
- 活跃进程：
  - cuda:0: GPT2-medium uncurated seed=42 (PID 283798, tmux=medium_uncurated, ~6h total, 刚启动)
  - cuda:1: seed=456 三方法串行 (tmux=seed456_methods: uncurated Gen 6/7 → ext → rgds, ~4h remaining)
- random_50 seed=123/456 已完成，进程已退出
- Paper Agent session 活跃，正在处理 Methodology critical 修正 + Introduction 修正

### 3. 📊 当前状态
**刚完成的关键决策链 D013-D016：**
- D013: random_50 baseline 发现（RGDS 比随机差 +74% PPL）
- D014: Framing 修正为 "internal embeddings 是问题"（非 "external 是方案"）
- D015: Claim 层级确认（C1/C3 强，C2 定性强，S3 暂缓→部分恢复）
- D016: random < external 在两 seed 中成立（非 noise），趋向 Scenario 2

**Registry RUNNING：**
- medium_uncurated_seed42: GPT2-medium 355M uncurated, cuda:0, ~6h
- uncurated_seed456 / ext_seed456 / rgds_seed456: 在 cuda:1 串行, ~4h remaining

**已完成但 Paper Agent 还在处理：**
- Methodology.tex 有 3 个 critical（算法描述错=facility location vs 实际 DiSF eigenvalue-variance；缺 PCA 降维；rare n-gram 定义错）
- Introduction.tex 有配套问题（Gen 0 定义不一致、citation placeholders、Laurent 引用不当）
- Related Work 尚未写

**Artifacts 已就绪：**
- `artifacts/related_work_references.md` — 36 篇验证引用
- `artifacts/diversity_metrics_seed42.csv` — Self-BLEU/distinct-n
- 4 个趋势 CSV（ppl/ratio/rare/all_metrics）

### 4. 📋 待办（条件触发式）
- seed=456 三方法全部完成（~4h）→ 做完整 4 方法 × 3 seed 统计矩阵（t 检验）→ 确认 random > external 是否显著 → 最终定论 C2/S3 claims → 更新 paper_framing.md
- GPT2-medium uncurated 完成（~6h）→ cuda:0 接着跑 medium_rgds → medium_random50 → medium_external（4 方法串行，D016 决定必须含 external）
- GPT2-medium 全部完成 → 检查 alignment gap 是否在 355M 上复现 → 如果复现则 R1 回应成立
- Paper Agent 完成 Methodology/Introduction 修正 → Reviewer 再审 → Related Work 章节写作
- 3-seed 统计 + GPT2-medium 数据齐全 → 写 Experiments + Results 章节 → 启动完整论文 Iterative Refinement

### 5. 🎯 战略上下文
- **核心发现**：迭代自训练中内部嵌入 diversity selection 灾难性加速 collapse（+74% PPL vs random），机制是 Embedding Alignment Gap（selection ratio 1.04→0.52）。所有不依赖内部嵌入的方法（random/external/uncurated）表现相近但 random 最优。
- **最新趋势（D016）**：random 在两 seed 中都优于 external（-5.1% 和 -15.9%），趋向 Scenario 2（Goodhart's Law：Contriever ratio >1.0 过度选择 rare-rich 反而次优）。如果 3-seed 确认 → 论文 claim 可升级。如果不确认 → 回退到 "normal cluster" 叙事（{random, external, uncurated} 等价）。
- **易错点**：external vs uncurated 跨 seed 方向反转（seed42 ext 赢，seed123 uncurated 赢），不能 claim "external > uncurated"。只有 RGDS 的 negative result 是跨 seed 稳定的。
- **Paper Agent 已知 bug**：Methodology 写了 "facility location" 但代码是 DiSF eigenvalue-variance minimization，已派修正指令。Introduction 的 Gen 0 定义需要 SSH 读代码确认后统一。
- **DDL**：EMNLP 2026 ARR 5/25，还有 12 天。GPU 预算极其充裕（~560h 可用，P0+P1 合计 ~77h）。
- **GPT2-medium 重要决定**：D016 将方法数从 3 改为 4（必须含 external），因为需要验证 "random > external" 是否跨模型规模成立。run_medium_external.sh 尚未创建，需要 Agent 补。


---
