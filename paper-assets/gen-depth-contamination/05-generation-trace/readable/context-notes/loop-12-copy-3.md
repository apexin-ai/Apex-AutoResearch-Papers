# reviewer / loop_12.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_12.md`
- **Structured JSON:** [`dfb0c10f5a8bc75a83cd.json`](../../sessions/df/dfb0c10f5a8bc75a83cd.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-16T11:52:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：`gpu_ids=[0,1,2,3]`（4×RTX 3090 24GB），本项目独占整台机器，无越界风险但需注意进程间冲突
- exp-020 Pythia nuc09 曾出现重复进程写同一目录（已修复），审查新实验时注意检查是否有类似重入
- Mistral-7B (exp-019) K*=1 是**真实结论**，不是 bug——bootstrap CI [0.5835, 0.6032] 确认，不要质疑这个结果
- Pythia greedy K*=2 + AUC=0.88 是 repetition collapse 导致的（TTR 0.72→0.19→0.14），不是检测能力强——论文中不能当正面证据用

### 2. 🖥️ 基础设施快照
- 服务器：`cqa1-22115(root)`，工作目录 `/root/autodl-tmp/gen-depth-contamination`
- Python：conda base (`/root/miniconda3/bin/python`)，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型缓存：`/root/autodl-tmp/.hf_cache`，需 `HF_DATASETS_OFFLINE=1` 避免 streaming hang
- 网络：`source /etc/network_turbo` 必须在 pip/git 前执行
- 活跃进程（截至 handoff）：
  - exp-018 LLaMA-8B: PID 10403, cuda:0, tmux `exp_018_llama8b`（运行 >6h，cross-scorer）
  - exp-019b Mistral cross-scorer: PID 36365, cuda:1, tmux `exp_019b_mistral_cross_scorer`
  - exp-020 Pythia nuc09: PID 27042, cuda:2（evaluation 阶段）
  - exp-021 length_512: PID 32175, cuda:3, tmux `exp_021_length_ablation`（depth 3 gen ~18%）

### 3. 📊 当前状态
刚完成：exp-020 nuc09 重复进程修复审查（数据完整，2 个多余 PID 已 kill）。

已完成实验（本轮已审）：
- exp-019 Mistral-7B: K*=1, 1v2=0.5934 (**打破 K*=2 universality**)
- exp-020 Pythia greedy: K*=2, 1v2=0.8838 (repetition collapse artifact)
- exp-021 length_128: K*=2, 1v2=0.6219
- exp-021 length_256: K*=2, 1v2=0.6282

RUNNING：exp-018 (cuda:0), exp-019b (cuda:1), exp-020 nuc09 (cuda:2), exp-021 len512 (cuda:3)
NOT_STARTED：exp-020 t07/t12, exp-022 cross-scorer matrix, exp-023 wiki, exp-024 arxiv

### 4. 📋 待办
- exp-019b 完成 → 核心问题：Mistral cross-scorer K* 是否 >1？若 K*≥2 → Mistral K*=1 是 scorer-dependent（paper 可 claim "cross-scorer 恢复"）；若仍 K*=1 → text-intrinsic，paper framing 必须调整为 "K* model-dependent"
- exp-018 LLaMA-8B 完成 → 若 K*=1 → 两个 7B+ 模型都 K*=1，"K*=2 universal" claim 彻底不成立；若 K*=2 → Mistral 是特例
- exp-021 length_512 完成 → 确认 K*=2 + 对比 128/256 的 AUC 是否有显著上升趋势
- exp-020 nuc09 完成 → 验证 nucleus sampling K* 与 greedy 的差异（greedy 的 0.88 是 collapse，nuc 应回归正常范围）
- 全部子配置完成后 → 做 coverage matrix 全面审查 + claim 强度最终评估

### 5. 🎯 战略上下文
- 核心发现：K* boundary 存在但**不 universal**。Qwen-1.5B 系列 K*=2 稳固（base/instruct/各 decoding/各长度），Mistral-7B K*=1
- paper_framing.md 当前写的 "K*=2 在所有 10 个测试条件下保持不变" **已过时**，需根据 exp-018/019b 结果改写
- 最易判断错的事：**不要把 Pythia greedy 的高 AUC (0.88) 当作 "Pythia 更容易检测" 的正面证据**——那是 repetition collapse 的 artifact，文本质量本身已崩溃（TTR<0.2），检测 trivial。论文应排除或标注为 degenerate case
- DDL：EMNLP 2026 ARR May 25（距今 9 天）。4 GPU 并行 + 弹性扩容足够完成剩余实验
- exp-019b 是当前最关键的诊断实验——它决定 Mistral K*=1 的归因（scorer vs text），直接影响论文 narrative 走向


---
