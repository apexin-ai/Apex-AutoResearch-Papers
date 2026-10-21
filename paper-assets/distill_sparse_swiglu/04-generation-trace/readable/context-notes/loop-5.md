# director / loop_5.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`b268361d35a334a33f06.json`](../../sessions/b2/b268361d35a334a33f06.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-17T17:10:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单（C004）：westd-34887 cuda:0/1 + westd-41718 cuda:0/1，共 4 张卡，禁止用其他
- 训练 log 中 `sparsity=X` 是 predictor 内部诊断值，**不是推理 sparsity**（M008 教训）。判断 sparsity 是否达标必须看 eval 结果
- 论文 allocation claim 已 pivot（D050）：禁止写 "+15.3pp uniform gain"，只能写 variance reduction（7.5x stability）。Paper Agent 已收到此禁令
- qwen14b_bce30_s42 的 hard_mask_ppl=1.075x 不可用于论文对比（6.4% sparsity vs KL 的 28.1%，不公平）。公平对比：TEAL PPL（BCE 8.76 vs KL 7.62，both at 30%）
- 用户提到 "gen-depth-contamination" 还没解释清楚是什么，我问了但没收到回复，不要自行猜测执行

### 2. 🖥️ 基础设施快照
- **westd-34887**：SSH -p 34887 root@connect.westd.seetacloud.com，2×RTX PRO 6000 Blackwell (95GB)
  - 工作目录：`/root/distill_sparse_swiglu/`
  - 模型：LLaMA-8B（`/root/autodl-tmp/models/`），Qwen-14B（`/root/autodl-tmp/models/qwen2.5-14b/`）
  - Checkpoints：`/root/distill_sparse_swiglu/checkpoints/`
  - Results：`/root/distill_sparse_swiglu/results/`
- **westd-41718**：SSH -p 41718 root@connect.westd.seetacloud.com，2×RTX PRO 6000 (97GB)，密码存储 key_id=`westd-41718_ssh_password`
  - 代码/模型已从 34887 rsync 同步，环境就绪（PyTorch 2.8.0+cu128, lm-eval 0.4.12）
  - Qwen-14B 模型已同步到此机器
- **活跃进程**：4 张卡都在跑 eval（见§3），均有 cron 注册自动回调

### 3. 📊 当前状态
刚完成本 session 的核心工作：3-seed allocation 矩阵 + narrative pivot + Qwen-14B 训练。

**RUNNING 实验**（均为 eval，cron 回调已注册）：
- `qwen14b_kl30_s42_eval`：westd-34887 cuda:1，Qwen-14B KL 30% benchmark eval（MMLU/ARC/WG/GSM8K），跑了 ~2h+
- `qwen14b_bce30_s42_eval`：westd-34887 cuda:0，Qwen-14B BCE 30% benchmark eval（同上 5 tasks）
- `qwen14b_teal30_eval`：westd-41718 cuda:1，Qwen-14B TEAL magnitude baseline eval
- `downstream_teal30_baseline`：westd-41718 cuda:0，LLaMA-8B TEAL 30% 扩展 downstream（HellaSwag/PIQA/BoolQ）

**已完成待消化的结果**：
- 30% 3-seed × 2-allocation MMLU 矩阵完整（uniform std=1.27pp vs global std=9.46pp）
- 50% 3-seed 矩阵完整（无显著 allocation 差异）
- Qwen-14B KL 训练成功：PPL 7.62（1.47x ratio，与 8B 完全一致）
- Qwen-14B BCE：Lagrangian 失败（native sparsity 6.4%），TEAL forced PPL 8.76（KL wins 15%）
- BCE v2（λ=50000）同样 6.4%，确认 gradient insufficiency
- Wall-clock speedup：negative（no sparse kernel），FLOPs reduction 1.36x/2.45x 有效
- Extended downstream（KL-30%）：HellaSwag 0.727, PIQA 0.760, BoolQ 0.769；dense baseline 已有
- Per-layer allocation profile：s42/s123 starvation pattern 相似，MMLU 差异非 layer-level 原因

### 4. 📋 待办（条件触发式）
- Qwen-14B KL eval 完成 → 汇总 KL/BCE/TEAL 三方对比表 → 派 Paper Agent 写 cross-scale section（新 Table）
- Qwen-14B TEAL eval 完成 → 补齐 14B baseline 数据 → 与 KL/BCE 合并
- downstream_teal30_baseline 完成 → 构建 Dense/TEAL/KL extended comparison table → 决定是否写入论文
- 所有 14B eval 完成 → 派 Paper Agent patch：新增 Qwen-14B cross-scale table + FLOPs reduction 数据 + Limitations 中 wall-clock 说明
- 用户回复 "gen-depth-contamination" 含义 → 评估并安排
- 用户确认是否需要加更多卡（当前 4 卡够用）
- Paper Agent 完成 Qwen-14B patch 后 → submit_paper_to_review（Round 2 审稿）

### 5. 🎯 战略上下文
- **论文核心 claim 稳固**：KL >> baselines（PPL + 跨架构 + 跨规模 1.47x ratio 完全一致）。这不受 allocation 争议影响
- **Allocation 叙事已 pivot（D050）**：从 "+15pp gain" 转为 "variance reduction 7.5x"。Paper Agent 已完成 rewrite（commits ec25e49 + 2aa4924）。Table 2 和 Table 5 已统一为 mean±std
- **Qwen-14B 是本 session 最大增量**：1.47x ratio 跨规模一致 + BCE gradient insufficiency 双重验证。数据很强，但 eval 还在跑
- **易踩的坑**：
  1. 训练 log 的 `sparsity` 字段是诊断值不是推理 sparsity（M008），不要再误读
  2. BCE hard_mask_ppl (1.075x at 6.4%) vs KL hard_mask_ppl (1.31x at 28.1%) 不能直接比——sparsity 不同
  3. Allocation 在 50% 时两种策略无差异，只有 30% 有 variance reduction 效应，且仅限 MMLU
  4. s42 global MMLU=25.27% 是 outlier，不能单独引用来支撑任何 claim
- **DDL**：EMNLP 2026 ARR May，2026-05-25（剩 ~7 天），时间充裕但需要尽快完成 Qwen-14B 数据整合 + Round 2 审稿
- **决策链**：D047(reframe)→D048(+Qwen14B)→D049(pivot planned)→D050(pivot final: variance reduction only)


---
