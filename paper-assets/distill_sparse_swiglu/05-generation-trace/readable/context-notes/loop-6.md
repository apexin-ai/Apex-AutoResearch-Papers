# director / loop_6.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`6d01dd6f0072e75c0f5f.json`](../../sessions/6d/6d01dd6f0072e75c0f5f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-17T20:39:14+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单（C004）：westd-34887 cuda:0/1 + westd-41718 cuda:0/1，共 4 张卡，禁止用其他
- 训练 log 中 `sparsity=X` 是 predictor 内部诊断值，**不是推理 sparsity**（M008）。判断 sparsity 是否达标必须看 eval 结果
- 论文 allocation claim 已 pivot（D050）：禁止写 "+15.3pp uniform gain"，只能写 variance reduction（7.5× stability）
- evaluate.py 中 `teal_global_ppl` 字段使用 predictor scores 排序（M010），**不是** vanilla TEAL。只有 `baseline_mode=teal_vanilla` 的独立 eval 才是 vanilla TEAL
- 跨服务器提交实验前必须确认 checkpoint/数据存在于目标服务器（M009）
- 50% global 3-seed MMLU = 28.1±0.2（用 s42=27.89, s123=28.34, s456=27.94），旧的 38.07% 来自错误 checkpoint（D051）

### 2. 🖥️ 基础设施快照
- **westd-34887**：SSH -p 34887 root@connect.westd.seetacloud.com，2×RTX PRO 6000 Blackwell (95GB)
  - 工作目录：`/root/distill_sparse_swiglu/`
  - Python：`/root/miniconda3/bin/python`
  - 模型：LLaMA-8B `/root/autodl-tmp/models/llama-3.1-8b/`，Qwen-14B `/root/autodl-tmp/models/qwen2.5-14b/`
  - C4 数据：`/root/autodl-tmp/data/c4_val/`（785MB，本地缓存可用）
  - Checkpoints：`/root/distill_sparse_swiglu/checkpoints/`
- **westd-41718**：SSH -p 41718 root@connect.westd.seetacloud.com，2×RTX PRO 6000 (97GB)，密码 key_id=`westd-41718_ssh_password`
  - 同上工作目录和模型路径（已 rsync）
  - C4 数据**不在**此机器（HF 下载失败过），需从 34887 scp 或用 HF_ENDPOINT=hf-mirror.com
  - `mvp_kl_norm_v2_s123` checkpoint 已 scp 到此机器

### 3. 📊 当前状态
本 session 完成了：Paper Agent 修复 variance→std 术语(ddbb07c)、50% 3-seed 升级(17a0fb5)、14B TEAL PPL 误标注修复(c15c79a)、paper_framing.md D050 合规更新、D051 决策记录。

**应已完成但未收到结果的实验**（上 session 全在跑，预计 ~23:00 UTC 完成，现在应该都 done 了）：
- `qwen14b_bce30_s42_eval`：Qwen-14B BCE 30% downstream（westd-34887 cuda:0）
- `qwen14b_teal30_eval`：Qwen-14B vanilla TEAL 30% baseline（westd-41718 cuda:1）— **论文急等这个数据**
- `qwen14b_dense_baseline`：Qwen-14B dense 5-task eval（westd-41718 cuda:0）
- `bce_isocompute_v3_s456`：LLaMA-8B BCE s456 训练 + eval（westd-34887 cuda:1）

**已确认完成**：
- `qwen14b_kl30_s42_eval`：PPL=7.62, ARC=57.2%, WG=72.1%, MMLU=63.7%, GSM8K=48.8%
- `downstream_teal30_baseline`：KL 平均优于 TEAL +5.6pp（HellaSwag/PIQA/BoolQ）
- `kl50_global_s123_reeval`：Registry 已修正，MMLU=28.34%

### 4. 📋 待办（条件触发式）
- 上述 4 个 eval 结果确认完成 → 构建 Qwen-14B cross-scale 对比表 → 派 Paper Agent 写 cross-scale section + vanilla TEAL 数据填入
- qwen14b_bce30_s42_eval 完成 + westd-34887 cuda:0 空出 → 启动 `bce_isocompute_v3_s123`（Table 2 multi-seed 最后一个 gap）
- bce_v3_s456 eval 完成 → 确认 BCE 50% 3-seed 数据完整
- 全部 14B 数据到齐 → 更新 paper_framing.md Concern #4 + limitations.tex "7-8B"→"7-14B" → 派 Paper Agent 综合 patch
- Paper Agent 完成 14B 综合 patch → C4 OOD 30% eval（在 westd-34887 用本地数据跑，避免 HF 下载问题）
- 所有论文更新完成 → submit_paper_to_review（Round 2 审稿）
- GPU 有余力 → 考虑 KL+compensation 控制实验（R6-N1）、35%/45% sparsity 点（R3-S5）

### 5. 🎯 战略上下文
- **核心 claim 稳固**：KL >> baselines（PPL + downstream + iso-compute + gradient SNR 5.76× + cross-arch + cross-scale 1.47× ratio 一致）
- **决策链**：D047(reframe)→D048(+Qwen14B)→D049(pivot planned)→D050(variance reduction only)→D051(50% s123 data fix)
- **DDL**：EMNLP 2026 ARR May，2026-05-25（剩 ~7 天）
- **最关键的待收数据**：qwen14b_teal30_eval 的 vanilla TEAL PPL — 论文 14B 段落等这个数字才能写 KL vs TEAL 对比
- **易踩的坑**：
  1. BCE 实验的 teal_global_ppl ≠ vanilla TEAL（M010，已被 critical 打回一次）
  2. C4 在 westd-41718 没本地缓存，HF 下载会失败 → 用 34887 跑 C4 eval
  3. 50% uniform MMLU 27.77% 是 s42 单 seed，不是 s456 global（之前搞混过）
  4. bce_isocompute_v3 训练后 train.py 不自带 eval，需要额外提交 eval job
- **Round 6 审稿遗留 open items**：R3-S1(弱化 novelty claim)、R4-W2(弱化 Contribution 1)、R3-S2(coupling→相关性)、R1-W3(multi-seed 在补)、R4-W3(C4 OOD 待做)、R6-W3(SNR extended)


---
