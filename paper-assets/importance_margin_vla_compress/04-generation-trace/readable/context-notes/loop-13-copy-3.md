# reviewer / loop_13.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_13.md`
- **Structured JSON:** [`6774421f9378edb0efec.json`](../../sessions/67/6774421f9378edb0efec.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-05-23T19:54:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-38929 上 X-VLA 实验用 `eval_xvla_pruning_libero.py`，mode flag 是 `--mode l2_norm`（带下划线）；OpenVLA 用 `eval_openvla_l2norm_libero.py`，mode flag 是 `--mode l2norm_prune`（完全不同）。Agent 已在这两个 flag 上各踩过 2+ 次坑。
- X-VLA eval 脚本的 `--domain_id` 默认=3 对所有 suite 正确。之前 domain_id=2 导致 Goal=0% 的假数据（D182 已 VOIDED）。
- π0.5 k=0.925 文件名会被截断为 `k0.93`（格式化 bug），不要误认为是 k=0.93 的实验。
- L2norm pruning 是确定性的（不受 CPU RNG fix 影响），random pruning 需要 CPU RNG fix 后的 v2 数据才可信。

### 2. 🖥️ 基础设施快照
| 服务器 | GPU | 工作目录 | Python |
|--------|-----|---------|--------|
| westd-38929 | 4× RTX PRO 6000 98GB | `/root/autodl-tmp/importance_margin_vla_compress` | conda base `/root/miniconda3/bin/python` |
| westd-27271 | 2× RTX PRO 6000 98GB | 同上 | 同上 |
| westd-41074 | 4× RTX PRO 6000 98GB | 同上 | 同上 |
| cqa1-33015 | 4× 4090D 24GB | 同上 | 同上 |

- 日志：`/root/runs/importance_margin_vla_compress/`
- 评估结果 JSON：`/root/autodl-tmp/importance_margin_vla_compress/eval_results/`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/`

### 3. 📊 当前状态
**刚完成**：X-VLA L2 k=0.5 Goal v3 = **59.0%** (295/500)，JSON 验证通过。L2 < Random (-8.2pp) 确认。

**正在运行**：
- westd-38929 GPU 0: L2 k=0.5 **Spatial v3** — **8/10 tasks** (T8 ep 46/50 即将完成)，running avg 59.0%。这是 D185 evidence table 最后一个缺口。
- westd-38929 GPU 2/3: L2 k=0.3 Spatial / Goal v4（bonus 数据）
- westd-27271 GPU 0: OpenVLA L2 k=0.5 Goal v3（刚启动，~5h ETA）
- westd-27271 GPU 1: OpenVLA Long baseline（5/10 tasks，avg 55.6%）
- westd-41074: 3 个 π0.5 实验（GPU 0 空闲——seed43 刚完成 90.8%）
- cqa1-33015: 4 个 π0.5 Goal 实验

**Registry 问题**：多个僵尸 RUNNING 条目（如 `eval_e5_xvla_attn_mean_goal_k03` 早已完成未更新）。D184 gap-fill 实验部分未在 registry 注册。

### 4. 📋 待办
- L2 k=0.5 Spatial v3 完成（~5-10 min）→ 从 JSON 验证最终 SR + domain_id → 发送**D185 最终 evidence table** 给 Director（4 suite 全部 L2 < Random）
- OpenVLA Long baseline 完成 → 验证 JSON，记录 SR
- OpenVLA L2 k=0.5 Goal v3 完成（~5h）→ 验证 mode=l2norm_prune + SR → 更新跨架构对比
- westd-41074 GPU 0 空闲 → 如果 Agent 未部署新实验，提醒 Director
- Director 可能在 Spatial 完成后 dispatch Paper Agent D185 rewrite → 准备进入论文章节审查模式（按 §5 标准）

### 5. 🎯 战略上下文
**D185 核心结论**（即将用全部数据确认）：L2 norm 在 entangling connector (X-VLA BART) 上全 4 suite 反信息性（-8 到 -27pp vs Random），per-task 方差极端（0-100%）；在 linear connector (π0.5) 上有效（+15-32pp vs Random）。Attention scoring 在两种架构上均有效，X-VLA 所有 suite k=0.5 均 90%+。

**易错点**：
- ROADMAP 曾把 Long attention 写成 ~65%（实际 94.8%），已修正但可能回退
- 不要因 L2 Goal 前 3 tasks 高（80/92/98%）就认为 L2 有效——后续 T5=0%, T6=24%, T9=0% 彻底拉低
- L2 k=0.5 Goal running mean 一度达到 80.8%（3 tasks）→ 76%（4 tasks）→ 67.3%（6 tasks）→ **59.0%（10 tasks）**，早期数据严重误导
- Random Goal k=0.5 也有 T5=0%——T5 ("push plate to stove") 在 50% token 下对所有 non-attention 方法都难
- π0.5 disruption peak 是真的：Random Goal k=0.9 (62.2%) < k=0.7 (78.2%) < k=0.95 (83.8%)


---
