# director / loop_16.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_16.md`
- **Structured JSON:** [`34dc8c483f5afe65bef5.json`](../../sessions/34/34dc8c483f5afe65bef5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_messages
updated: '2026-05-21T15:14:47+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd cuda:0-3（4张）、westb cuda:0-1（2张），共6张。严禁使用其他卡
- westd 磁盘 ~32GB free，westb ~14GB free——新实验前必须 `df -h` 确认，禁止存 optimizer.pt
- nohup 命令必须用 `nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python ...'` wrapper
- RASP seed456 模型已损坏，不可 eval
- MATH-500 eval 必须用 `--max_new_tokens 2048`（D097 决策，论文 20% 数据统一 @2048）
- EMNLP 2026 ARR DDL: May 25（~3天）
- Dense baseline 用 81.27%（Dense+SFT），不是 90.83%（原始未 SFT 模型）

### 2. 🖥️ 基础设施快照
- **westd-29022**: `connect.westd.seetacloud.com` / 4× RTX PRO 6000 / `/root/recovery_aware_struct_prune`
  - Python: `/root/miniconda3/bin/python`，conda base
  - 模型: `/root/runs/recovery_aware_struct_prune/` + `/root/autodl-tmp/recovery_aware_struct_prune/`
- **westb-23072**: `connect.westb.seetacloud.com` / 2× RTX PRO 6000 / `/root/recovery_aware_struct_prune`
  - Standard 25% GRPO: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100`
  - SFT Standard 25%: `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870/`
- 论文编译源: 本地 `projects/recovery_aware_struct_prune/docs/paper/`
- Paper Agent 工作副本: 本地 `projects/recovery_aware_struct_prune/paper/`（已双向同步）
- 无 W&B，无 Git remote

### 3. 📊 当前状态
**本轮完成的关键工作**：
1. 收割全部 25% GSM8K eval 结果：CKA-only SFT 60.12% / GRPO 59.59%，Standard SFT 50.87% / GRPO 51.86%
2. 发现 MATH-500 @4096 vs @2048 confound → D097 决策 kill 全部 @4096，用 @2048 重跑
3. Paper Agent 完成 25% patch（Appendix 表 + §4.3 C1 极端案例），编译通过 8 页
4. Round 4 审稿已提交（approval_id: apr_20260521T145013_qbke，pending 用户审批）

**RUNNING 实验（全部是 MATH-500 @2048）**：
| exp_id | 服务器 | GPU | 预估完成 |
|--------|--------|-----|----------|
| eval_math500_grpo_cka_only_25_v2 | westd:0 | cuda:0 | ~4h (从 ~139/500) |
| eval_math500_grpo_random_20_v2 | westd:1 | cuda:1 | ~10h |
| eval_math500_sft_cka_only_25_v2 | westd:2 | cuda:2 | ~4h (从 ~139/500) |
| eval_math500_sft_random_20 | westd:3 | cuda:3 | ~12h |
| eval_math500_grpo_standard_25_v2 | westb:0 | cuda:0 | ~6h |

**空闲**: westb cuda:1（无本地模型可跑，SCP 太慢不值得）

### 4. 📋 待办
- Round 4 审稿报告到达 → 按 `review-report-action` skill 处理（Holistic Pass + Per-Comment Action Matrix）
- MATH-500 @2048 eval 完成 → complete_experiment 更新 registry → 如果 DDL 前到手，派 Paper Agent patch MATH-500 25% 数据入论文
- MATH-500 SFT Standard 25% v1 = 13.0% @2048 已确认可用，不需重跑
- MATH-500 CKA-only 25% SFT 和 GRPO 早期信号均为 19.0%@100（C1 decoupling 跨 benchmark 验证）
- westb cuda:1 空闲 → 如果有需要 SCP 模型的 eval 且剩余时间充足，可考虑填充

### 5. 🎯 战略上下文
- **核心结论**: Pruning criterion shapes post-RLVR recovery capacity，CKA-only >> Standard >> Random >> RASP
- **已入论文的硬数据**: 15% 3-seed (+7.20pp, p<0.001)、20% 3-seed (+4.55pp, p=0.0009)，25% 单 seed (+7.73pp GRPO / +9.25pp SFT) 在 Appendix
- **D096 framing 定调**：25% 补强覆盖不升级 claim（analysis paper），C1 decoupling 加极端案例（Standard reward≈0 但 accuracy 不变 = "silent collapse"），不讨论 gap 趋势方向（非单调，单 seed 无法确定）
- **D097 MATH-500 统一**：全部 @2048，@4096 数据作废
- **Round 3 审稿 3.0/5，34 issue 全 resolved**。Reviewer 评估加入 25% 后可达 3.5，有望摸 4.0
- **易错点**: (1) docs/paper/ 是编译源，paper/ 是 Paper Agent 工作副本——修改需双向同步 (2) Registry 状态经常与实际不符，断言前先 tail 日志 (3) Agent 倾向被动等 cron 回调——必须推它主动 tail 收割 (4) Dense baseline 用 81.27% 不是 90.83%


---
