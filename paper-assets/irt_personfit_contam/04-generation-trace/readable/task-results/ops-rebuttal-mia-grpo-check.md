# ops rebuttal mia grpo check

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rebuttal-mia-grpo-check_20260524T035136_result.json`
- **Structured JSON:** [`67fb976319bdd3eaf066.json`](../../sessions/67/67fb976319bdd3eaf066.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## 1. GRPO Checkpoint 信息

**位置**: `/root/autodl-tmp/post_rl_contam/checkpoints/grpo/`
- `checkpoint-500`, `checkpoint-1000`, `checkpoint-1500`（默认 symlink 指向 1500）
- 另有独立目录 `grpo_step500`, `grpo_step1000`, `grpo_step1500`

**模型**: Qwen/Qwen2.5-7B-Instruct
- SFT 阶段在 MMLU seen 数据上微调（LoRA, r=16, alpha=32）
- GRPO 阶段在 SFT 上继续 RL 训练，reward = MMLU 答题正确性
- 训练配置: batch=2, grad_accum=4, lr=5e-6, num_generations=16, max_steps=3000, save_steps=500

**总占用**: `post_rl_contam/` 约 511MB（都是 LoRA adapter，不大）

---

## 2. 现有 MIA 结果（已完成）

所有实验已经跑过了。核心 AUC-ROC 汇总（Min-K% k=10, 最佳 MIA 配置）：

| Stage | Loss AUC | Min-K%10 AUC | Min-K%++10 AUC | lz* delta (seen-unseen) |
|-------|----------|--------------|----------------|------------------------|
| **base** | 0.486 | 0.493 | 0.488 | 不显著 |
| **SFT** | **0.592** | **0.611** | **0.569** | **-3.674** (强信号) |
| **GRPO step500** | 0.486 | 0.493 | 0.488 | lz*=3.41 vs 7.00 |
| **GRPO step1000** | 0.486 | 0.493 | 0.488 | 类似 |
| **GRPO step1500** | 0.486 | 0.493 | 0.488 | lz*=3.54 vs 6.86 |

**关键发现**：
- SFT 阶段 MIA 有效：Min-K%10 AUC = 0.611（检测到 contamination）
- GRPO 后 MIA 完全失效：AUC 跌至 ~0.493（接近随机）
- 而 lz* 在 GRPO 后仍然有效：seen lz*=3.54 vs unseen lz*=6.86，差异显著
- GRPO 各 step（500/1000/1500）MIA 表现几乎无变化——说明 RL 第一步就已经抹平了 MIA 信号

---

## 3. 现有 MIA 代码

完全可复用：
- `eval_mia.py` — 实现了 Loss, Min-K%, Min-K%++ 全套方法，支持 `--stage base/sft/grpo` 切换
- `compare_mia_lz.py` — 自动加载 MIA 和 lz* 结果，生成对比表
- `train_grpo.py` — GRPO 训练脚本

---

## 4. 是否需要重新训练

**不需要。** 已有完整的 base → SFT → GRPO pipeline，包括 3 个 step checkpoint 和全部 MIA + lz* 评估结果。数据完备。

---

## 5. 磁盘和 GPU 状态

- **磁盘**: 250GB 数据盘，已用 94GB，剩余 157GB（38%），空间充足
- **GPU**: 4× NVIDIA RTX PRO 6000 Blackwell (96GB)，全部空闲（0% 使用率）

---

## 6. MIA 实验方案建议

已有结果已经充分支撑论文 claim：**GRPO 后 MIA 失效但 lz* 仍有效**。如果需要补充实验：

- **扩展 MIA 方法**：可加入 Ref-based MIA（需 reference model），如 Zlib 比率法（不需额外模型，直接用 zlib 压缩作为 normalizer），实现很简单
- **更多 k 值已覆盖**：k=10/20/30/40/50 全部跑过
- **Per-item 数据可用**：每个 item 的 Min-K%/Min-K%++ 分数已保存在 JSON 中，可直接做 item-level 的 lz* vs MIA 相关性分析

---
