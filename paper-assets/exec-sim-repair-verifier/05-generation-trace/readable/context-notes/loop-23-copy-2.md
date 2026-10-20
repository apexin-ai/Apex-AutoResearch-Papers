# agent / loop_23.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_23.md`
- **Structured JSON:** [`445f58cc044a3ac6d395.json`](../../sessions/44/445f58cc044a3ac6d395.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 23
reason: max_wall_time
updated: '2026-05-17T11:21:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- seetacloud GPU 白名单: cuda:0/1/2/3（4×5090），4 个 DeepSeek repo-level 训练正在占满，**不要 kill 任何训练进程**
- home-1x5090 只有 1 张 GPU (cuda:0)，当前被 efficiency benchmark 占用（Worker 运行中）
- 两台服务器**无法直接互联**（scp 不通），checkpoint 传输必须走 local relay: seetacloud → local → home
- `eval_deepseek_repo.py` 在 home 上不存在，替代方案: `eval_repo_cls.py --model_name deepseek-ai/deepseek-coder-6.7b-instruct`
- Re-repair 已 drop (D120)，不再投入任何资源

### 2. 🖥️ 基础设施快照
**seetacloud-westd-4x5090**:
- 工作目录: `/home/sonny/exec-sim-repair-verifier/`
- 模型缓存: `/root/autodl-tmp/.hf_cache/`
- Checkpoint 目录: `/root/autodl-tmp/checkpoints_deepseek_{cls_repo_v4,cwm_repo,cls_repo_s123,cwm_repo_s123}/`
- Eval 输出: `/root/autodl-tmp/eval_results/`
- 活跃 PID: 548885 (cls-repo-v4, cuda:0), 479953 (cwm-repo, cuda:1), 542514 (cls-repo-s123, cuda:2), 542906 (cwm-repo-s123, cuda:3)
- 4 个 cron 监控活跃（reconcile_crons 已确认）

**home-1x5090**:
- 工作目录: `/home/sonny/exec-sim-repair-verifier/`
- DeepSeek base model: `~/.cache/huggingface/hub/models--deepseek-ai--deepseek-coder-6.7b-instruct`
- Python deps: transformers 4.57.6, torch 2.10.0+cu128, peft 0.19.1
- Repo test data: `/home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_{test,val}.jsonl`
- GPU: RTX 5090, 32GB VRAM

### 3. 📊 当前状态
**刚完成**: Director 指派的全部 Dream review 补充分析任务:
- A2 bibliography: 45 篇 bib（+9 新增，audit 全通过）→ `docs/paper/references.bib`
- A5 CWM 样本: 2 unparseable + 1 contrast → `artifacts/qualitative_cwm_examples.json`
- A5 CLS 样本: FP + FN + repo FP → `artifacts/qualitative_cls_error_examples.json`
- A6 TOST: 5-margin sensitivity → `artifacts/tost_sensitivity.json`
- Error complementarity: DeepSeek CLS-CWM 完整 breakdown → `artifacts/error_complementarity_deepseek.json`

**等待中的 Worker**:
1. `worker_analysis_inference-efficiency-collect_20260517T112031` — home 上 CLS vs TRAJ efficiency benchmark（重跑中，第一个 Worker 提前退出）
2. `worker_analysis_traj-complementarity_20260517T102958` — seetacloud 上 CLS-CWM-TRAJ 三方互补分析（turn 20，在修正 TRAJ checkpoint 路径后重跑）

**RUNNING 实验** (registry):
- deepseek-cls-repo-v4 (cuda:0): ~66%, ETA ~7h (from 08:44 check)
- deepseek-cwm-repo (cuda:1): ~78%, ETA ~7h
- deepseek-cls-repo-s123 (cuda:2): ~71%, ETA ~6h (最先完成)
- deepseek-cwm-repo-s123 (cuda:3): ~48%, ETA ~17h (最晚)

### 4. 📋 待办（条件触发式）
- efficiency benchmark Worker 回调 → 验证 `artifacts/efficiency_benchmark.json`，注册 artifact，汇报 Director
- TRAJ complementarity Worker 回调 → 验证 `artifacts/traj_complementarity_analysis.json`，注册 artifact，汇报 Director（注意：TRAJ 和 CLS/CWM 可能用不同 test set，Worker 会标注 data_alignment）
- deepseek-cls-repo-s123 cron 完成（最早约 23:00 CST）→ scp checkpoint → local → home → 立即 `eval_repo_cls.py` eval
- 其他 3 个 DeepSeek 训练完成 → 同样 relay + eval 流程
- DeepSeek repo eval 全部完成 → 汇总 repo-level CLS vs CWM accuracy + unparseable rate → 论文 repo-level section 数据

### 5. 🎯 战略上下文
- **Framing (D116)**: Design space characterization，不是 CLS advocacy。CWM 在 repo-level 失败是 tokenizer-specific（Qwen vocab 151K vs DeepSeek vocab 32K 完全不同）
- **Re-repair (D120)**: 已 drop。负向结果根因: 8B 模型无法利用 per-test 诊断（Oracle ≈ Random），且诊断信息导致 "过度修改"
- **关键数字**: func-level CLS acc ~87-88%, CWM ~85-87%, 两者 TOST equivalent at ±2pp (Qwen p=0.007)。DeepSeek complementarity 55.1% vs Qwen 31.2%（CWM fail-bias 驱动）
- **易错点**: (1) Qwen3-8B = Instruct 模型，不存在 Qwen3-8B-Instruct repo (2) DeepSeek tokenizer `apply_chat_template(tokenize=True)` 返回 BatchEncoding 不是 list，len() 返回 2 不是 token count (3) seetacloud ↔ home 不能直接 scp
- **DeepSeek repo 结果是最后的关键数据**: 如果 DeepSeek repo CLS 也高 accuracy + CWM 也高 unparseable，则 "CWM repo failure is model-family-general" 的 claim 成立；如果 DeepSeek CWM repo 反而 work，则 "tokenizer-specific" 叙事需要重新审视


---
