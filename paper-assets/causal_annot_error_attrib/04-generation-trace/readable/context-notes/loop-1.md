# agent / loop_1.md

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`efa17ec4e3770a67b3ed.json`](../../sessions/ef/efa17ec4e3770a67b3ed.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: idle_timeout
updated: '2026-05-21T10:48:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- home-1x5090 上 sonny 账户**无权访问 `/root/miniconda3/`**。提交命令必须用 `python3`（系统路径）或绝对路径 `/usr/bin/python3`，**禁止** `source /root/miniconda3/...`
- `submit_training_job` 的 command 如果用 `| tee`，**必须加 `set -o pipefail`**，否则 tee 掩盖退出码导致 cron 误判 clean exit（本 session plan009 被坑两次）
- plan009 脚本 `plan_009_pathological_matrices.py` **没有 `--device` 参数**，只接受 `--M/--N/--K/--topos/--dry-run`。GPU 由 `CUDA_VISIBLE_DEVICES` 环境变量控制（submit_training_job 自动注入）
- plan003 的 3 个标注进程（llama4/qwen3/deepseek）是 nohup 启动的，**不是 submit_training_job 管理的**，没有 cron 监控。需要手动 SSH 检查 PID 存活和进度

### 2. 🖥️ 基础设施快照
- 服务器：home-1x5090，账户 sonny，工作目录 `/home/sonny/causal_annot_error_attrib/`
- Python：`/usr/bin/python3` (3.10.12)，torch 2.10.0+cu128，**不用 conda**
- GPU：1× RTX 5090，当前 plan009 retry#2 可能正在用 cuda:0
- 数据集：`/home/sonny/causal_annot_error_attrib/data/`（humaid.jsonl, vast.jsonl, civil_comments.jsonl）
- API endpoint：`http://47.94.22.126/v1`（Llama4/Qwen3/DeepSeek），key=OPENROUTER_API_KEY
- 活跃进程：
  - plan003 标注：PID 438497(llama4), 438843(qwen3), 439116(deepseek) — nohup，无 cron 监控
  - plan009 retry#2：Worker `worker_fix_plan009_pathological_matrices_r2_20260520T184507` 刚派出重提交，PID 待确认
- 磁盘：`/` 318G/1.1T 可用(69%)，`/home/sonny/ssd2` 481G/2.0T 可用(75%)

### 3. 📊 当前状态
- **刚做完**：plan009 连续失败两次的诊断修复（#1 conda权限 → #2 --device 参数错误），已派 Worker 第二次重提交
- **等待中**：
  - Worker `worker_fix_plan009_pathological_matrices_r2` 回调 → 确认 plan009 是否成功启动
  - plan003 RUNNING（3 路并行 LLM 标注），qwen3 最慢约 5/21 17:00 UTC 完成，无 cron 需手动查
- **Registry 状态**：plan009 ANALYZING（等 retry#2 覆盖），plan003 RUNNING，其余 9 个 DONE(success)

### 4. 📋 待办
- Worker plan009 回调到达 → 检查是否真正启动（tail log 看输出不是 argparse error）→ 成功则等 cron 完成回调分析结果
- plan009 如果 retry#2 仍失败 → 停止自动修复，汇报 Director 让人工介入（已达自主修复上限）
- plan009 成功完成 → on-experiment-done 流程：提取 metrics（spectral gap/diagonal dominance/effective rank threshold）、更新 registry、report.md、汇报 Director
- plan003 预计 5/21 完成 → 手动 SSH 检查 3 个 PID 是否存活 + 进度 → 完成后解锁 plan006 + plan007
- plan003 完成 → 并行启动 plan006（ASV 实证验证）+ plan007（correction guidance MC 框架）

### 5. 🎯 战略上下文
- **核心方向**：多分类 LLM 标注误差在 7 种 DAG 拓扑下的偏差传播 + ASV 灵敏度框架，目标 AAAI 2027（DDL 7/28，~68 天）
- **关键发现链**：5/7 拓扑 τ_sign_flip=0% 结构性保证；exposure(83%) 和 IV(52%) 危险；ASV 三维排序；K-scaling 稳定；binarization collapse 147x 差异
- **决策链**：D002(exposure优先) → D003(checkpoint gate) → D004(Version A成立) → D005-D008(ASV参数化) → D009(多维ASV排序) → D010(5/7修正) → D011(6→7拓扑)
- **关键瓶颈**：plan003 是 Claim 2(ASV实证) 和 Claim 3(correction guidance) 的唯一阻塞项
- **易错点**：
  - τ_true 必须用 plim(C=I) 而非 DGP 参数（IV plim(I)=0.6598≠β₁=0.5）
  - plan003 没有 cron 监控，容易忘记检查——必须主动 SSH 查进度
  - 之前 plan002 有 RNG ordering artifact，被 SHA-256 deterministic seed 修复——新实验如涉及随机采样注意同样问题


---
