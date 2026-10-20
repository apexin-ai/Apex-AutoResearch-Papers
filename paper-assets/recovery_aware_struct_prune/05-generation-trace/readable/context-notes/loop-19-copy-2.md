# agent / loop_19.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_19.md`
- **Structured JSON:** [`3c75c7821cf32d0b751b.json`](../../sessions/3c/3c75c7821cf32d0b751b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: idle_timeout
updated: '2026-05-19T10:14:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: cuda:0,1,2,3。westd-11672 已宕机 >24h，不可用
- westb-23072 磁盘极度紧张（仅 ~9.5GB 可用）。grpo_cka_only_20_seed123 完成前必须清理 grpo_unstructured_20/ 或 pruned_unstructured_20/（各 ~15GB），否则 checkpoint 写入会磁盘满崩溃
- eval_humaneval.py 已修复 PATH bug（bare `python` → `sys.executable`）。旧 HumanEval 0% 结果（SFT CKA-only v1）是假结果，不可引用
- Bootstrap CI 结论约束论文措辞：CKA-only vs Standard 可说 "significantly"（p=0.002）；CKA-only vs RASP 在 7B 只能说 "numerically higher"（CI 含 0）
- MATH-500 GRPO eval 超慢（GRPO 模型 ~2-4 min/problem），配置 --max_new_tokens 2048（不是 4096）

### 2. 🖥️ 基础设施快照
- **westb-23072**: root@, 工作目录 /root/recovery_aware_struct_prune, Python /root/miniconda3/bin/python, 数据盘 /autodl-pub 250GB（~9.5GB 可用 ⚠️）
- **westd-29022**: root@, 工作目录 /root/recovery_aware_struct_prune, Python /root/miniconda3/bin/python, 数据盘 /autodl-tmp ~816GB 可用
- 模型路径: /root/autodl-tmp/recovery_aware_struct_prune/ (westd), /root/autodl-pub/recovery_aware_struct_prune/ (westb)
- HF cache: /root/.cache/huggingface (两台机器均有 MATH-500/GSM8K 缓存，网络不通时自动 fallback)
- submit_training_job 命令格式: westd 用 `bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=X python ...'`
- GRPOConfig 应设 `save_only_model=True` 防磁盘满

### 3. 📊 当前状态
**刚处理**: eval_math500_grpo_standard_20_fair 失败诊断——v2 进程在 19/500 无声死亡，v1 interim Acc@100=36.0%。已向 Director 汇报，需重试。

**RUNNING (5)**:
| exp_id | server:gpu | 摘要 |
|--------|-----------|------|
| eval_gsm8k_grpo_standard_20_fair_v2 | westd:cuda:0 | 替换 phantom 58.91%，GSM8K N=1319 |
| eval_humaneval_sft_cka_only_20_2048_v2 | westd:cuda:1 | v1 的 0% 是 PATH bug，v2 重跑 |
| eval_humaneval_grpo_standard_20_fair_2048_v3 | westd:cuda:2 | GRPO Standard fair HumanEval |
| eval_humaneval_sft_standard_20_2048_v3 | westd:cuda:3 | SFT Standard HumanEval |
| grpo_cka_only_20_seed123 | westb:cuda:1 | 多 seed 验证，29/100 步，~8h 后完成 |

**Worker 池 = 0**，所有 20 个历史 Worker 已完成。westb cuda:0 空闲。

**等待中**: 无 pending Worker 回调。5 个 RUNNING 实验各有 cron 监控。

### 4. 📋 待办（条件触发式）
- eval_gsm8k_grpo_standard_20_fair_v2 完成 → 替换 phantom 58.91%，更新 Tab2 GSM8K 列，如与 SFT 接近则强化 C1 decoupling
- eval_humaneval_sft_cka_only_20_2048_v2 完成 → 验证 SFT CKA-only 真实 HumanEval（v1 的 0% 是 bug）。与 GRPO CKA-only 20.12% 对比
- eval_humaneval_*_v3 完成 → 填 HumanEval 矩阵剩余格子
- grpo_cka_only_20_seed123 完成 → 与 seed42 (64.37%) 对比。**完成前必须清理 westb 磁盘**（grpo_unstructured_20/ ~15GB）
- westb cuda:0 空闲 → 应铺下一个任务（eval_gsm8k_grpo_rasp_20_1p5b 或 seed456）
- eval_math500_grpo_standard_20_fair 需重试 → 诊断 Worker 已完成，根据根因修复后在 westd cuda 空闲时重试
- 所有 MATH-500 + HumanEval evals 完成 → 进入 Paper Agent patch（1.5B table + MATH-500 table + HumanEval table + E2 figure + E3 heatmap）

### 5. 🎯 战略上下文
**核心结论**: Pruning criterion determines post-RLVR recovery capacity. Recovery gradient: CKA-only >> importance-based (Standard ≈ RASP)。跨 7B 和 1.5B 一致。

**决策链关键节点**:
- D058: Fair v5 config 4-method comparison 完成，消除了 confound
- D056: paper_framing.md 全面改写，Core Insight = "Redundancy-Stability Tradeoff"
- D055: C1 收窄为 in-distribution decoupling（MATH-500 OOD 不 transfer）
- D054: C2 = recovery capacity hierarchy（不是 collapse gradient）

**易错点**:
- 1.5B GRPO delta 全为负/近零，不要在 paper 中强调 GRPO delta 的跨尺度一致性——用 "cross-scale ordering consistency" 代替
- GRPO CKA-only HumanEval = 20.12%，不是 interim 的 ~33%（前 20 题样本偏差）
- Standard GRPO GSM8K 当前是 phantom 58.91%（从未验证），eval_gsm8k_grpo_standard_20_fair_v2 正在修正这个数字
- MATH-500 所有 GRPO 方法收敛到 ~26-28%（方法差异消失），这是 C1 decoupling 证据而非 negative
- 投稿截止 ARR May 25 = **6 天**


---
