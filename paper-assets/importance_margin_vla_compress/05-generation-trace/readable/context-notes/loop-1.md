# director / loop_1.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_1.md`
- **Structured JSON:** [`196f7a52b866fb1599e1.json`](../../sessions/19/196f7a52b866fb1599e1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_messages
updated: '2026-05-15T17:45:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-27271 的 cuda:0 和 cuda:1，不可使用其他服务器/GPU
- 当前训练 batch_size=4 + FP32 不可修改（baseline v5 已在此配置下完成 30K 步，IMM v7 必须保持一致以确保公平对比）。GPU 利用率优化（bs=64+BF16）留 post-MVP
- eval_every=999999 是 D008 workaround（lerobot eval 路径有 RoPE bug），IMM 训练不跑 in-training eval，全量评估用独立 evaluate.py
- 不要让 Agent kill 健康运行的训练进程（之前有过误杀 v4 事故）

### 2. 🖥️ 基础设施快照
- 服务器：westd-27271 (2× RTX PRO 6000 96GB)，工作目录 `/root/autodl-tmp/importance_margin_vla_compress`
- Python：conda base (`/root/miniconda3/bin/python`)，需 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 网络：AutoDL 需 `source /etc/network_turbo` + SSL 证书设置（`REQUESTS_CA_BUNDLE` + `SSL_CERT_FILE`）+ `HF_HUB_DISABLE_XET=1`
- HF cache：`/root/autodl-tmp/.hf_cache`，SmolVLM2 权重通过 ModelScope CDN 下载后 symlink
- 数据集：`lerobot/aloha_sim_insertion_scripted_image`（50 eps, 14D action, 1 cam → 64 tokens）
- 活跃进程：mvp_imm_anchor_v7 (PID 41292, cuda:1, step ~1050/30000 at handoff time)
- mvp_baseline_v5 已完成 30K steps，checkpoints 在 `checkpoints/mvp_baseline_v5/`（step 5K/10K/15K/20K/25K/29999）

### 3. 📊 当前状态
- **mvp_baseline_v5**: DONE (ANALYZING)，30K steps 完成。Agent 已收到指令跑全量评估 `evaluate.py --checkpoint checkpoints/mvp_baseline_v5/step_029999 --output results/eval_baseline_v5.json --max_batches 100`，应该正在执行或即将执行
- **mvp_imm_anchor_v7**: RUNNING cuda:1, step ~1050/30K, sps=3.2, 预计 ~04:12 UTC 完成。eval_every=999999, save_every=2000
- **Bug 修复全部就位**：token_selection.py (方案 C binary mask), evaluate.py (3 bugs: noise/time, baseline_forward, preprocess_batch), smolvla_wrapper.py (noise/time params)。Reviewer 已验证服务器部署 ✅
- Agent 还收到指令：IMM v7 到 step 5000 时用 step_002000 checkpoint 做 evaluate.py IMM 路径 dry-run (max_batches=5)

### 4. 📋 待办
- Agent 汇报 baseline 评估结果 → 记录 action_loss 各 condition 数据，作为 Gate Criteria 基准
- IMM v7 step 2000 checkpoint 生成 → Agent 做 evaluate.py IMM dry-run (max_batches=5)，确认 _hard_forward fix + evaluate.py IMM 路径不报错
- IMM v7 训练完成 (~04:12 UTC) → 跑全量 IMM 评估 `evaluate.py --checkpoint checkpoints/mvp_imm_anchor_v7/step_029999 --output results/eval_imm_v7.json --max_batches 100`
- 两组评估结果都出来 → 对比 Gate Criteria：(1) Δ_k 中位数 ≥2x (2) top-k preservation ≥10pp (3) IMM/baseline action_loss ratio ≤1.10 (4) L·ε·k/Δ_k ratio 下降 ≥30%
- 全部 PASS → `complete_mvp()` → post-mvp-kickoff skill → paper_framing + experiment_plan + dream_simulate
- 任何 FAIL → Kill Path: 搜索 δ∈{0.1,0.3,0.5}, λ∈{0.1,0.5,1.0}

### 5. 🎯 战略上下文
- **决策链**：D001(MVP方案) → D002(Reviewer warnings) → D003(L·ε·k/Δ_k量化) → D004(k=96条件+implicit soft topk) → D005(数据集换aloha) → D006(dry-run必须覆盖eval模式) → D007(gate#3放宽到10%) → D008(跳过训练内eval) → D009(_hard_forward改binary mask)
- **最容易判断错的事**：Agent 之前把 _hard_forward prefix 长度不匹配误诊为 "lerobot 内部 RoPE bug"，实际是我们的代码（_hard_forward 物理删除 tokens 导致 tokens_per_cam 不匹配）。如果出现新的 eval crash，先检查是不是序列长度相关的问题，不要轻信 Agent 的根因分析
- **容易踩的坑**：(1) SmolVLAPolicy.forward() 有 action_is_pad masking bug 稀释 loss → 必须用 baseline_forward() (2) AutoDL 网络不稳，tmux 启动命令必须包含 network_turbo + SSL 证书 (3) _merge_borderline_tokens 是死代码（方案 C 去掉了），post-MVP 需要重新设计保持序列长度的 merge
- **目标**：CoRL 2026 (abstract DDL May 26, 11 天)，时间极紧。MVP 通过后立即进入 research 阶段


---
