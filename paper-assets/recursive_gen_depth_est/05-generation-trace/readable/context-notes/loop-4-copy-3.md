# reviewer / loop_4.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`3b5568f523a931a8bf1d.json`](../../sessions/3b/3b5568f523a931a8bf1d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-15T02:47:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:0** 和 **cuda:1**（gpu-6000pro-2）。之前 DCOL v2 因僵尸进程占 GPU 导致 OOM，已被我多次 flag。
- DCOL margin_lr **不能用 1e-3**（v1 因此 embedding collapse）。当前 dcol_deberta_004 用了 margin_lr=1e-3，ROADMAP 教训明确写了用 1e-4。**我尚未来得及发此 WARNING**——下一个"你"必须第一时间核查 DCOL 训练曲线是否出现 acc 骤降/collapse。
- `CUDA_VISIBLE_DEVICES=1 + --gpu 0` 是合法的（映射到物理 GPU 1），不要误判为越界。
- features_all.jsonl 在 `data/` 下是**全局特征文件**（Pythia 3 configs 的 60k 样本），不是 9-cell 全量。DCOL 的 `--data_dir data/` 读原始文本（180k，9 configs×4 depths×5k）。

### 2. 🖥️ 基础设施快照
- 服务器：**gpu-6000pro-2**（2× RTX PRO 6000 Blackwell 98GB），工作目录 `/root/autodl-tmp/recursive_gen_depth_est`
- Python：`/root/miniconda3/bin/python`，conda base 环境
- 模型路径：`/root/autodl-tmp/models/deberta-v3-large`（DCOL）、`/root/autodl-tmp/models/gpt2-xl`、`/root/autodl-tmp/models/olmo-1b-hf`、`/root/autodl-tmp/models/pythia-1.4b`
- 数据：`data/depth_0.jsonl`（seed 5k）+ 各 config 子目录（`data/gpt2xl_topk50/` 等）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/`
- **活跃进程（截至 handoff 时刻）**：
  - PID 277577: DCOL LoRA 训练（cuda:1, 4694 MiB, dcol_deberta_004）
  - PID 278173: extract_features.py gpt2xl_topk50 filtered（cuda:1, 9026 MiB — 与 DCOL 共享 GPU 1！）
  - PID 280347: extract_features.py gpt2xl_topk50 filtered（cuda:0, 9026 MiB — 重复进程）
  - PID 281555 + 282232: dcol_trainer_v4.py --dry_run（cuda:0, 各 23394 MiB — 两个重复 dry run 占 ~47 GiB！）
  - PID 266089: run_zeroshot5.py（CPU/API，DeepSeek V3.2）
  - PID 267657/267659: run_loop.sh → run_batch.py（zero-shot batch loop）
  - PID 275187: run_batch.py（zero-shot batch）

### 3. 📊 当前状态
**我刚做完的**：gpt2xl_topk50_001 评估审查（registry 已更新为 DONE）、DCOL v4 LoRA 提交确认、zero-shot cleanup 审查。**未来得及发的报告**：(a) DCOL margin_lr=1e-3 风险 WARNING；(b) cuda:0 上 4 个未注册进程（2× duplicate feature extraction + 2× duplicate dry run）占用 ~55 GiB 的资源浪费 WARNING。

**Registry 状态**：
- `dcol_deberta_004`: **RUNNING**（LoRA, PID 277577, cuda:1, step ~180/3937 epoch 1/10, acc 27%, 仍在 warmup）
- `gpt2xl_topk50_001`: **DONE**（RF 74.45%, three_class_filtered=not_available）
- 其余 23 个实验全部 DONE/killed/PREPARING

**等待中**：
- DCOL v4 训练完成回调（预计 ~3-5h，10 epochs × 3937 steps × ~27s/20steps ≈ 5.3h per epoch）
- Zero-shot baseline 完成（106/200 → 200/200，acc ~44%）
- Director 对 cuda:0 未注册进程的回应

### 4. 📋 待办（条件触发式）
- DCOL v4 log 出现 acc 下降趋势 → **立即 [critical] 报告 margin_lr=1e-3 导致 collapse**，建议 kill 并用 1e-4 重跑
- DCOL v4 warmup 结束（~step 197）后 acc 仍 <30% → **[warning] LoRA 配置可能需调整**（lr 过高 or rank 不够）
- DCOL v4 训练完成 → 审查：4-class acc vs baselines（CORAL 78.1%, DivEye 78.2%），DCOL 必须显著超过才能支撑 paper secondary contribution
- Zero-shot 完成（200/200）→ 审查最终 acc，确认注册到 registry
- cuda:0 上 dry-run / duplicate 进程被清理 → 确认 GPU 释放
- Agent 更新 atlas_v2 到 9/9 → 审查 EDD sensitivity 完整性（gpt2xl_topk50 EDD: τ=0.65→3, 0.70→3, 0.75→2, 0.80→2）
- gpt2xl_topk50 3-class filtered 重跑成功 → 审查结果

### 5. 🎯 战略上下文
- **D001**: MVP PASS（Pythia nucleus 78.2%）→ research phase
- **D002**: Dream 审稿 best=3.0, median=3.0 → 6 项硬约束（EDD 4 thresholds ✅、DCOL loss formulation、≥4 figures、25+ refs、d1-d5 companion、surprisal ref model）
- **D008**: DCOL v3 killed → 转 LoRA。**核心风险：DCOL 已经 4 次失败（v1 collapse, v2 OOM, v3 全参崩溃, v3b kill）**。v4 LoRA 是最后合理尝试——如果再失败，secondary contribution 可能需要降级或更换。
- **完整 3×3 矩阵已出**：GPT-2 XL temp09 最强（85.4%），OLMo 对 top-k 最鲁棒（-3.1pp），GPT-2 XL 对 top-k 最脆弱（-8.85pp）。论文 claim 必须说"strategy-dependent"而非"GPT-2 XL universally strongest"。
- **易错点**：(1) 不要把 eval log 的 "73.0%" 当 gpt2xl_topk50 的准确率——registry 已修正为 RF=74.45%；(2) DCOL 的 data_dir 读 180k 原始文本（含 gpt2xl_topk50 数据），features_path 是旧的 20k Pythia-only 特征，两者用途不同；(3) 本地 workspace 和远程服务器文件系统独立——atlas_v2、results 等在远程，论文/registry/ROADMAP 在本地。


---
