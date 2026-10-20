# director / loop_17.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_17.md`
- **Structured JSON:** [`f1fc036dc4e7f124873d.json`](../../sessions/f1/f1fc036dc4e7f124873d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_messages
updated: '2026-05-17T11:20:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- seetacloud GPU 只有 cuda:0-3（westd-4x5090），不可用其他 GPU
- D116: framing 是 "design space characterization"，不是 CLS advocacy。语言必须 neutral
- D120: re-repair 已 drop（genuine negative），不再投入，不写入论文 core claims
- D119: "tokenizer-specific" 归因已验证正确（DeepSeek LlamaTokenizer 32K ≠ Qwen Qwen2Tokenizer 151K），但最终是否成立取决于 DeepSeek CWM repo unparseable 结果
- D115: 放弃全局单调序 CLS≥CWM≥TRAJ
- 论文中模型名：Qwen3-4B, Qwen3-8B, DeepSeek-Coder-6.7B（不是 DeepSeek-R1）
- Abstract/Introduction/Conclusion 还没更新到 D116 framing——等 DeepSeek repo 结果后统一改

### 2. 🖥️ 基础设施快照
- **seetacloud-westd-4x5090**: connect.westd.seetacloud.com, 工作目录 `/home/sonny/exec-sim-repair-verifier`
  - cuda:0-3 全部 RUNNING DeepSeek repo 训练
  - 训练脚本: `train_unified.py`（有 eval_loss NaN bug 的 fix，但当前 4 个训练加载时在 fix 前，需独立 eval）
  - eval 脚本: `eval_repo_cls.py`（支持 DeepSeek via detect_model_family）
  - Checkpoint 目录: `checkpoints_deepseek_cls_repo_v4/`, `checkpoints_deepseek_cwm_repo/`, `checkpoints_deepseek_cls_repo_s123/`, `checkpoints_deepseek_cwm_repo_s123/`
- **home-1x5090**: RTX 5090 32GB, Docker v29.1.3
  - 工作目录: `/home/sonny/exec-sim-repair-verifier`（部分文件，非完整镜像）
  - eval 环境已预装: transformers 4.57.6, torch 2.10.0, peft 0.19.1, DeepSeek base model cached
  - `eval_repo_cls.py` 已传输就绪，dry-run 通过
  - Repo-level test data: `swebench_test.jsonl` (9784) + `swebench_val.jsonl` (9335)
  - 两台服务器无法直接互联，checkpoint 传输需中间节点 relay
  - CLS v5 checkpoint: `/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_v5/checkpoint-4600`
- **论文本地路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/`
- Cron 监控 DeepSeek 4 个训练实验（自动回调）

### 3. 📊 当前状态
**刚做完：**
- Dream dream_20260517T034206 full review 分析完成（D117），6 项确认行动项中 A1/A2/A5/A6 全部完成，A3/A4 由 Paper Agent 完成
- Paper Agent 完成两轮 Patch：Title 更新、Table 1 补 DeepSeek TRAJ、TOST sensitivity §5.4、CLS-TRAJ 效率段落、Qualitative Error Analysis §5.7、Related Work 7 段 39 引用、Repo-level table 结构（DeepSeek 行 TBD）
- Bibliography 审计通过（45 篇，0 幻觉）
- Round 1 审稿 17 issues 逐条审计完成：12 完全修复、3 部分修复、2 等 DeepSeek 数据
- Re-repair Docker eval 完成分析 → genuine negative (D120)，已 drop

**RUNNING 实验（registry）：**
- `deepseek-cls-repo-v4` (cuda:0, ~66%, ETA ~7h from handoff time)
- `deepseek-cwm-repo` (cuda:1, ~78%, ETA ~6.8h)
- `deepseek-cls-repo-s123` (cuda:2, ~71%, **最早完成 ~6.2h**)
- `deepseek-cwm-repo-s123` (cuda:3, ~48%, **最晚 ~16.7h**)

**等待中：**
- Reviewer 的 Round 1 逐条审计报告已收到（severity: warning，见上方对话）
- Agent 的 efficiency benchmark 任务（home GPU）已派出，未回报
- DeepSeek 训练 cron 回调

### 4. 📋 待办（条件触发式）
- **DeepSeek cls-repo-s123 训练完成（最早）→** 立即 relay checkpoint 到 home → `eval_repo_cls.py` eval 所有 epoch checkpoint → 报告 accuracy/F1/unparseable
- **任一 DeepSeek CWM repo 完成 →** 关键节点：CWM unparseable rate 决定 "tokenizer-specific" vs "model-agnostic" narrative。<20% → tokenizer-specific 成立；>40% → 需改为 complexity-dependent
- **4 个 DeepSeek repo eval 全部到手 →** (1) 填入论文 Table 4 TBD cells (2) 确定 Path A vs B narrative (3) 更新 Abstract/Introduction/Conclusion (4) 补 W8 appendix 表（val-test mutation distribution）(5) 提交 Round 2 审稿
- **Reviewer Round 1 审计中的 must-fix →** W8 补 appendix 定量表（val vs test per-mutation-type 分布），1h 工作量
- **Agent efficiency benchmark 回报 →** 数据写入论文 efficiency section，补独立 table
- **所有论文更新完成 →** `submit_paper_to_review` 提交 Round 2

### 5. 🎯 战略上下文
- **DDL**: EMNLP 2026 ARR May 25（剩余 ~7.5 天）
- **核心决策链**: D108(scope扩展) → D116(framing pivot to design space) → D117(dream分析) → D118(D112覆盖) → D119(tokenizer验证) → D120(re-repair drop)
- **论文 3 core claims**: (1) func-level equivalence (TOST confirmed for Qwen, consistent for DeepSeek), (2) complexity-dependent divergence at repo-level (tokenizer-specific or model-agnostic, 待 DeepSeek 结果), (3) CLS efficiency + diagnostic granularity (6-9x speedup, error complementarity oracle 90.63%/91.5%)
- **最容易判断错的事**: (a) Reviewer 和 Agent 反复引用 D112 说 re-repair 不入论文——D112 已被 D118/D120 覆盖，re-repair 是因为 genuine negative 才 drop，不是因为 D112 (b) Dream reviewer 担心 "tokenizer-specific" 归因错误（假设 DeepSeek-R1-Qwen3 共享 tokenizer）——实际模型是 DeepSeek-coder-6.7b，tokenizer 完全不同，D119 已验证 (c) Abstract/Intro/Conclusion 还是旧 framing 残留，别忘了 DeepSeek 结果到手后必须全面更新 (d) 两台服务器不能直接连，checkpoint 传输需要 relay，预留时间
- **Dream 分数参考**: best 4/6 含 re-repair（现在 drop 了），实际论文预期在 best 3.5-4/6 之间。median 3/6。提升空间在 DeepSeek 跨模型验证的强度
- **Round 1 审稿 overall weak reject**，但 17 issues 中 12 个已完全修复。最大 blocker 是 DeepSeek repo 结果


---
