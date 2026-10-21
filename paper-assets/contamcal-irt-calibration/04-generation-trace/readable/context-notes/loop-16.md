# director / loop_16.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_16.md`
- **Structured JSON:** [`66d3a882cc7c31a72402.json`](../../sessions/66/66d3a882cc7c31a72402.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_messages
updated: '2026-05-19T08:40:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- **westd-29999 GPU**: gpu_ids=[0,1,2,3]，全部 96GB RTX PRO 6000 Blackwell。当前 4/4 在用（3 训练 + 1 eval）
- **cqa1-21977 GPU**: 只有 **1× RTX 4090D 24GB** (gpu_ids=[0])。Agent 反复误报 4 张，已纠正 3 次。下次 Agent 报 cqa1 多卡直接打回
- Phi-4 14.7B (~30GB bf16) 不能上 cqa1（超 24GB）。Gemma-2 9B (~18GB) 勉强可能，需测试
- evaluate.py 是项目唯一 eval 标准（MMLU 5-shot + ARC 25-shot, logprob MC）。禁止用 lm_eval（M017 教训：42pp 差异）
- westd 无网络，HF 数据集需 SCP + HF_DATASETS_OFFLINE=1
- **Variant A/B 未判定**——论文全文冻结定量 claim，用占位表述。不预判 negligible vs meaningful
- **EMNLP 2026 ARR May 25 DDL**，约 6 天

### 2. 🖥️ 基础设施快照
- **westd-29999**: root@westd-29999, 工作目录 /root/autodl-tmp/exp001/
  - train_sft.py（LoRA SFT 训练，支持 --lora-targets）
  - evaluate.py（MMLU+ARC eval）
  - HF cache: /root/.cache/huggingface/（Qwen2.5 全系列 + Phi-4 + OLMo-2 + Gemma-2 基础模型均已下载）
  - HF datasets cache: 已从 cqa1 SCP 过来，支持 offline eval
- **cqa1-21977**: root@cqa1-21977, 工作目录 /root/autodl-tmp/exp001/
  - evaluate.py 已部署，HF datasets cache 可用
  - OLMo-2-7B 基础模型已下载
  - Gemma-2-9B 模型 SCP 中（上次 66MB/18GB）
- **活跃进程（westd）**:
  - cuda:0: Phi-4 d100 训练 PID 121911
  - cuda:1: Gemma-2 d100 训练 PID 110293
  - cuda:2: OLMo-2 d100 训练 PID 114339
  - cuda:3: Phi-4 eval batch (d025/d050 进行中)
- **LoRA 统一配置**: 全家族 r=16 α=32 lr=5e-5 bf16 AUGMENT mode

### 3. 📊 当前状态
**刚做完**：
- paper_framing.md 更新了 D147（benchmark-specific direction）、三层结论框架、OLMo-2 near-null 分析
- Paper Agent 完成 C1-C3 + W1 + §6 中性化（Abstract/Intro/Conclusion 全部冻结定量 claim）
- Paper Agent 收到 claim 矩阵更新 + cross-family Results section 预写指令

**训练**（最后 3 个 run）：
- Phi-4 d100 (cuda:0) — 刚启动，~5h
- Gemma-2 d100 (cuda:1) — RUNNING，~3h
- OLMo-2 d100 (cuda:2) — RUNNING，~5h

**Eval 完成情况**：
| Family | 完成 | 待 eval |
|--------|------|---------|
| Qwen 7B | 10/10 ✅ | — |
| Qwen 14B | 5/5 ✅ | — |
| Phi-4 | d000-d050 4/5 ✅ (cuda:3 跑着) | d100 |
| OLMo-2 | d000-d025 3/5 ✅ (cqa1) | d050, d100 |
| Gemma-2 | **0/5** ❌ 最大缺口 | 全部 |

**等待中**：Phi-4 eval batch 完成回调、cqa1 Gemma-2 模型 SCP 完成、3 个 d100 训练 cron 回调

### 4. 📋 待办（条件触发式）
- Phi-4 eval batch 完成（d025+d050 结果出）→ 更新 registry，启动 Phi-4 d100 eval（如 d100 训练也完成）或释放 cuda:3
- Gemma-2 SCP 到 cqa1 完成 → 立即串行 eval d000/d005/d025/d050。**Gemma-2 结果决定 cross-family claim 成败**：正向 → 3/4 families positive（strong claim）；null → 2/4 positive，claim 大幅 downgrade
- 任何 d100 训练完成 → 立即 eval（westd 空闲 GPU 或 SCP 到 cqa1）
- 全部 eval 完成 → (1) IRT fitting with per-benchmark γ_k, (2) TOST equivalence test for ARC（bound ±1.5pp）, (3) Variant A/B 最终判定
- OLMo-2 d050/d100 eval 出来 → 如果 MMLU 明确正向(≥1pp) → 三层框架 Layer 2 扩到 4/4；如果仍 null → 维持 3/4 hedge + Layer 3 exploratory
- 14B s123 replication (D145) — d000_s123 + d050_s123 跑 Cohen's d，灰色地带最终判定需要这个
- **M019 pattern**：Agent 训练完成后不自动启动下一任务——已记录 4 次。每次 cron 回调后检查 GPU 是否空闲，空了立即催

### 5. 🎯 战略上下文
**核心发现链**：
- D146: scale × benchmark interaction（MMLU 随 scale 递增，ARC 递减/平坦）
- D147: benchmark-specific contamination direction（MMLU positive, ARC null/negative）— 跨家族 3/3 方向一致
- Phi-4 效应量 (+1.20pp@d050) < Qwen 14B (+2.28pp@d050) 尽管 Phi-4 更大 → 不纯粹 scale-dependent，family-specific 因素存在
- OLMo-2 near-null 效应 → 三层结论框架（Layer 1 all non-negative / Layer 2 baseline≥65% positive / Layer 3 capability floor exploratory）

**决策链**: D141(scope expansion) → D144(family framing) → D145(postpone Variant A/B) → D146(scale×benchmark) → D147(benchmark-specific direction)

**易错点**：
1. 不要 claim "effect scales with model size"——Phi-4 数据反驳了这个（更大但效应更小）。正确：effect varies by family and scale
2. 不要 claim "MMLU always positive"——7B d005 两个家族都负向。必须限定 d025+
3. OLMo-2 选择会被审稿人质疑（为什么选这么弱的模型）——justify: AllenAI 独立 + open source + 训练数据独立
4. cqa1 永远只有 1 张卡，不管 Agent 报什么
5. Gemma-2 eval 是论文能否 claim cross-family 的决定性因素——优先级最高


---
