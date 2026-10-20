# director / loop_2.md

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`937879ecb6d7b1989227.json`](../../sessions/93/937879ecb6d7b1989227.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-16T10:21:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只用 autodl-5090 的 cuda:0/1/2/3（项目配置白名单）
- detection_rate 指标是假阳性（"back" 关键词触发），**禁止在论文中引用或作为 claim 支撑**（Reviewer critical D046 后确认）
- LLaMA 模型必须是 3.1-8B-Instruct（3.3 只有 70B，3.2 只有 1B/3B，之前踩过坑）
- Scale-up 收集不占 GPU（纯 API + CPU），但 /tmp 空间紧张——所有训练进程必须设 `TMPDIR=/root/autodl-tmp/tmp`
- 训练框架 ms-swift 4.2.0，Qwen 和 LLaMA 共用同一套脚本无需改代码

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090 (connect.bjb2.seetacloud.com)，账号 root
- 工作目录：`/root/autodl-tmp/tax_error_inject_agent`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型路径：
  - Qwen3-8B: `/root/autodl-tmp/models/Qwen3-8B/`
  - LLaMA-3.1-8B-Instruct: `/root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct/`
- Eval 结果：`/root/autodl-tmp/tax_error_inject_agent/eval_results/`
- 训练输出：`/root/autodl-tmp/tax_error_inject_agent/output/`
- Scale-up 收集：后台 8 workers，~239/1051 成功轨迹
- 活跃进程：llama31-taxei-s0 重启后 GPU 1 (~2h)，llama31-random-s0 GPU 2 (~65min)，eval-rp-s7 GPU 3 (~15min)

### 3. 📊 当前状态
刚处理完 /tmp 磁盘满导致 llama31-taxei-s0 崩溃，已修复重启（设了 TMPDIR）。

**RUNNING**:
- llama31-vanilla-s0: GPU 0, 92% 即将完成
- llama31-taxei-s0: GPU 1, 重启从头 (~2h)
- llama31-random-s0: GPU 2, 48% (~65min)
- eval-rp-s7: GPU 3, 9/47 episodes (~15min)

**关键已完成结果**:
- LLaMA s42: Vanilla=74.5%, TaxEI=74.5%, Random=76.6% → **TaxEI 对 LLaMA 中性（0pp），对 Qwen 有害（-9pp）**
- TaxEI-RP s7 训练 DONE，eval 在跑
- Recovery eval 10/15 完成

**等待**: LLaMA s0 三组 eval → s123 训练 → 论文 framing 最终定稿

### 4. 📋 待办
- llama31-vanilla-s0 完成 → 立即 eval on GPU 0 → eval 完成后该 GPU 跑 recovery eval
- eval-rp-s7 完成 → GPU 3 启动 recovery eval（剩余: TaxEI s7, Random s0/s123/s1/s7）
- llama31-random-s0 完成 → eval on GPU 2
- llama31-taxei-s0 完成 → eval on GPU 1
- LLaMA s0 三组 eval 全部出来 → 启动 s123 V/T/R 训练
- LLaMA s0+s123 结果确认跨模型趋势 → 更新 paper_framing.md（从 "universal negative" → "model-proficiency-dependent effect"）
- Scale-up 收集完 1000+ → 启动 3-seed V+T 训练（~17 GPU-h DDP）

### 5. 🎯 战略上下文
**核心发现（待 s0/s123 确认）**: Error injection 效果是 model-dependent。Qwen 受害 -9pp，LLaMA 免疫 0pp。两者 TaxEI ≈ Random（taxonomy 标签零收益跨模型成立）。Detection rate 不是解释变量（假阳性已证实），真实解释可能是模型基线能力差异。

**决策链**: D043(RP有害) → D044(scale-up暂停) → D045(scope决策) → D046(撤销D044，scale-up重启)

**易错点**:
- 不要再用 detection_rate 做任何分析或 claim——Reviewer 已证明是正则假阳性
- LLaMA s42 只有 1 seed，0pp 差异可能是噪声——必须等 s0/s123 确认后才改 framing
- /tmp 可能再次爆满——所有新训练必须带 TMPDIR=/root/autodl-tmp/tmp
- Paper framing 更新要等 3-seed 统计显著性确认，不要基于单 seed 改叙事


---
