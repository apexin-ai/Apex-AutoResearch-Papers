# director / loop_17.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_17.md`
- **Structured JSON:** [`683cbe1d6d71d564bab7.json`](../../sessions/68/683cbe1d6d71d564bab7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_messages
updated: '2026-05-19T12:20:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- **westd-29999 GPU**: gpu_ids=[0,1,2,3]，全部 96GB RTX PRO 6000 Blackwell
- **cqa1-21977 GPU**: 只有 **1× RTX 4090D 24GB** (gpu_ids=[0])。Agent 反复误报 4 张，已纠正多次。下次 Agent 报 cqa1 多卡直接打回
- Phi-4 14.7B (~30GB bf16) 不能上 cqa1（超 24GB）
- **evaluate.py 是项目唯一 eval 标准**（MMLU 5-shot + ARC 25-shot, logprob MC）。禁止用 lm_eval（M017 教训：42pp 差异）
- **evaluate.py 版本**：当前 westd 上是 v3（37,591B, May 19 18:22），含 chat_template logprob 位置修复。cqa1 仍是旧版——**所有 eval 必须用 westd v3**，cqa1 旧版数据全部作废
- **Gemma-2 ARC 数据标记不可靠**（15pp 震荡 = 评估伪影），论文中 Gemma-2 只用 MMLU
- westd 无网络，HF 数据集需 SCP + HF_DATASETS_OFFLINE=1
- westd 上 python 不在 PATH，必须用 `/root/miniconda3/bin/python`
- **EMNLP 2026 ARR May 25 DDL**，约 6 天

### 2. 🖥️ 基础设施快照
- **westd-29999**: root@westd-29999, 工作目录 /root/autodl-tmp/exp001/
  - Python: `/root/miniconda3/bin/python`（不要用 `python`）
  - train_sft.py（LoRA SFT）、evaluate.py（MMLU+ARC eval, v3 修复版）
  - HF cache: /root/.cache/huggingface/（Qwen2.5 全系列 + Phi-4 + OLMo-2 + Gemma-2 基础模型均已下载）
  - Phase 2 输出: `eval_results_v2/{family}_{dosage}/`（统一版本，论文用这个）
  - Phase 2 日志: `phase2_logs/gpu{0,1,2,3}.log`
  - LoRA 统一配置: r=16 α=32 lr=5e-5 bf16 AUGMENT mode
- **cqa1-21977**: root@cqa1-21977, 1×4090D 24GB。evaluate.py 是旧版，数据不可用。暂不分配任务
- **活跃进程（handoff 时刻）**:
  - cuda:0: OLMo-2 d000+d005 eval（olmo2_eval_gpu0.sh）
  - cuda:1: Qwen-14B d100 完成后应切到 OLMo d025+d050
  - cuda:2: OLMo-2 d100 eval（tmux olmo2_gpu2）
  - cuda:3: OLMo-2 d025+d050 eval（手动启动）

### 3. 📊 当前状态
**Phase 2 全量重跑（D148）进行中：22/25 完成，OLMo-2 是最后缺口。**

4 个 family 已完成全部 v2 eval：
| Family | d000 | d005 | d025 | d050 | d100 | 模式 |
|--------|------|------|------|------|------|------|
| Phi-4 14.7B | 76.44/92.06 | 76.36/91.81 | 76.98/92.32 | 76.75/92.41 | 76.27/92.66 | 免疫 ±0.5pp |
| Gemma-2 9B | 61.86/— | 63.42/— | 64.56/— | 64.01/— | 65.62/— | MMLU +3.76pp（ARC 不可靠） |
| Qwen-7B | 66.11/87.88 | 64.74/86.09 | 62.98/84.04 | 63.07/84.56 | 64.33/84.98 | V型 -3.13pp→恢复 |
| Qwen-14B | 69.44/91.04 | 69.01/90.36 | 62.04/88.91 | 59.41/87.63 | 60.07/88.48 | U型 -10.03pp→微恢复 |

OLMo-2 仅 d100 完成（MMLU 57.00%），d000-d050 在 3 GPU 上跑，~40min 全部出齐。

**25/25 训练全部 DONE/success。** Registry 已更新。

Paper Agent 已完成 claim 矩阵更新 + 跨家族 Results section 预写（§5.5 + 附录），编译通过，8 页正文。数据占位表待 eval 填入。

### 4. 📋 待办（条件触发式）
- OLMo-2 d000-d050 eval 全部完成 → **Phase 2 25/25 达成** → 立即收集完整 5×5 表格，进入分析阶段
- 全部 v2 数据到齐 → (1) IRT fitting with per-benchmark γ_k (2) TOST equivalence test for ARC (bound ±1.5pp) (3) 完整 dose-response 图
- OLMo-2 数据出来 → 判断第五种模式（免疫/正向/V型/U型/其他），更新 paper framing
- 全部分析完成 → paper_framing.md 大改：从"contamination effect is small"转为"architecture-dependent contamination sensitivity"（四种模式）
- Framing 更新后 → director_post_to_paper_agent 派 Reframe 任务，重写 Abstract/Intro/Results/Conclusion
- Gemma-2 ARC 伪影 → 如时间允许，专项排查 evaluate.py 对 Gemma-2 ARC 的兼容性；否则论文中注明 limitation
- **M019 pattern**（第 5+ 次）：eval/训练完成后 GPU 空转等人工接管。每次 cron/Worker 回调后立即 nvidia-smi 检查空闲 GPU

### 5. 🎯 战略上下文
**核心发现（比预期更有趣）**：contamination dose-response 不是统一的，而是高度 architecture-dependent：
- Phi-4: 完全免疫（天花板效应，已掌握 MMLU 知识）
- Gemma-2: 低基线获益（记忆→性能提升）
- Qwen-7B: V型（先损后恢复）
- Qwen-14B: U型（灾难性遗忘，-10pp，14B 比 7B 更脆弱）

**决策链**: D141→D144→D145→D146→D147→D148(全量重跑)

**易错点**：
1. 不要 claim "larger models are more resilient"——Qwen-14B 比 7B 脆弱 3 倍
2. 不要 claim "contamination always helps on contaminated benchmark"——Qwen 两个规模都受损
3. Gemma-2 ARC 数据不能用（15pp 震荡），只用 MMLU
4. Phase 1 / cross_family 目录的旧数据全部作废，论文只用 eval_results_v2/
5. cqa1 永远只有 1 张卡；evaluate.py 是旧版，数据不可比
6. Variant A/B 判定需等全部数据——现在看来不是二选一，而是 family-dependent


---
