# reviewer / loop_19.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_19.md`
- **Structured JSON:** [`907df534a3b953d663df.json`](../../sessions/90/907df534a3b953d663df.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_wall_time
updated: '2026-05-17T21:07:37+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 cuda:0（服务器 westd-39279 实际只有 1 张 RTX PRO 6000 96GB，cuda:1 不存在）
- 早期实验 `w2-qwen3-1.7b-isr-pilot` 曾用 CUDA_VISIBLE_DEVICES=1 — 那是旧配置/双卡时期，现在只有 1 张卡
- nvidia-smi 常显示 utilization=100% + memory=0MiB — 这是 driver 状态缓存，不是真实负载，不要误判为资源被占
- 论文 claim 级别：CMH p-values 已全部移至 appendix（因违反 within-stratum independence），正文只用 descriptive comparison + permutation test。如果有人试图把 CMH 放回正文 → 立即 critical

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279(root)，工作目录 /root/solver-trace-ablation
- GPU：1 × RTX PRO 6000 96GB，当前空闲
- 模型路径：/root/autodl-tmp/models/Qwen3-1.7B, /root/autodl-tmp/models/Qwen3-4B
- 输出目录：/root/autodl-tmp/outputs/
- 训练数据：/root/solver-trace-ablation/data/train_500_seed42.jsonl (500 examples)
- 无 W&B（所有实验 --no_wandb）
- 活跃进程：无（0 RUNNING）
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/

### 3. 📊 当前状态
- 刚完成：最终提交前检查（全 PASS）+ ROADMAP 审查 + 1.7B 追加实验竞争力评估
- Registry：140 experiments，全部 DONE，0 RUNNING
- 等待中：Director 决策——是否追加 1.7B +2 seeds (s43/s44) × 3 conditions = 6 runs。我已评估为"正 EV，15 hrs GPU，低风险，建议执行"
- 论文状态：9 轮内审完成，Reviewer 最终检查 PASS，submission-ready

### 4. 📋 待办
- Director 批准 1.7B 追加 → Worker 开跑后审查：验证 CUDA_VISIBLE_DEVICES=0、seed 正确、config 一致
- 1.7B 新 seed 实验完成 → 核实 metrics 是否与 s42 一致（0% genuine 预期）；如果出现 >0% genuine 在 β=0.1 或 Random → severity warning，可能需调整 §4.5 措辞
- 如果 β=0.3 新 seed PR > 30% 且 genuine > 0 → 需重新评估 "reward collapse" claim
- 论文提交后如收到外审/Round 10 请求 → 按 §5.1-5.2 维度审查

### 5. 🎯 战略上下文
- 核心结论：ISR reliable as diagnostic, unreliable as optimizer。Goodhart collapse at all 4 doses，genuine window transient + closes under extended training
- 决策链关键节点：D120 (Goodhart 叙事恢复) → D124 (5-seed OR=3.48 逆转 3-seed 结论) → D128 (s45-1000 confirms inevitable collapse)
- **最容易判断错的事**：
  1. 不要把 CMH OR=3.37 当成论文核心证据——它已降级为 appendix directional indicator（effective N=5 seeds, not 350 samples）
  2. 不要把 "23% vs 8% genuine" 解读为 ISR 显著优于 random——permutation p=0.26 underpowered，stricter classification OR=0.61 n.s. 甚至反转
  3. 1.7B 的 w2-qwen3-1.7b-isr-pilot 和 w2-qwen3-1.7b-isr-b01 是两个不同实验（pilot 用 100 examples 出 H9，full 用 500 examples 出 H1）——不要混淆
  4. 审稿 concern v3-R12-NI-1（1.7B single seed）是 9 轮持续 critical，如果 Director 决定不追加实验，§4.5 的 "Preliminary" + "exploratory" 限定必须保留


---
