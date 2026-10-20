# reviewer / loop_22.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_22.md`
- **Structured JSON:** [`48958e3540abdf17160d.json`](../../sessions/48/48958e3540abdf17160d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 22
reason: idle_timeout
updated: '2026-05-20T21:02:10+00:00'
---

### 1. 🔴 硬约束 / 红线
- 4×RTX 5090 全部分配给本项目（gpu_ids=[0,1,2,3]），当前 4 个训练进程各占一卡，无越界风险但也无空闲卡
- Qwen CWM eval 必须用 `--max_seq_length 8192`（不是 4096），之前抓过一次 seq_length mismatch（被 Director 修复）
- DeepSeek CWM eval 用 `--max_seq_length 4096`（两个模型不同，这是 acknowledged confound，不是 bug）
- DeepSeek 用 `train_unified.py`（无 eval_steps，tqdm 准确）；Qwen 用 `train_repo_cwm.py`（有 eval_steps=100，tqdm 低估 wall-clock ~2×）。不要混淆 ETA 估算方法
- CWM eval 必须验证 unparseable_rate > 50%，否则可能是 wrong-data-level artifact（之前 DeepSeek s123 旧版因加载 function-level 数据导致 0% unparseable / 86% accuracy 的伪结果）

### 2. 🖥️ 基础设施快照
- 服务器：`seetacloud-westd-4x5090`，工作目录 `/home/sonny/exec-sim-repair-verifier`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- 模型：Qwen3-8B `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`，DeepSeek-6.7B `/root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct`
- Qwen3-14B **未下载**（14B pilot 前置条件）
- HF cache：`/root/autodl-tmp/.hf_cache`，`HF_HUB_OFFLINE=1` 常设
- 活跃进程：
  - GPU 0: Qwen s123-v4 train (PID 886278, ckpt-1400/6633)
  - GPU 1: DeepSeek s456-v2 train (PID 949112, step ~892/12627)
  - GPU 2: DeepSeek s123-v2 train (PID 925638, step ~2394/12627)
  - GPU 3: Qwen s456-v3 train (PID 886352, ckpt-1400/6633)
  - DeepSeek eval monitors: PID 957333 (s123-v2), PID 957406 (s456-v2)
  - Pipeline watcher: PID 966158 (`watch_eval_completion.sh`)
- 训练日志路径：`/root/runs/exec-sim-repair-verifier/{exp-name}.log`
- Qwen checkpoints：`/root/autodl-tmp/checkpoints_repo_cwm_8b_s{123,456}/`
- DeepSeek checkpoints：`/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s{123,456}_v2/`（s456 有 training.log，s123 目录为空因 save_strategy=epoch）

### 3. 📊 当前状态
**刚完成**：
- Round 7 深度叙事审查（5 维度，PASS with minor warnings）→ 已 post
- L60 table 引用修正 + Limitations 扩展 → 快速审查 PASS → 已 post
- 14B CWM pilot 可行性审查 → PASS with 2 confound warnings（lr=2e-4 vs 5e-5, QLoRA vs BF16）→ 已 post
- **Rebuttal 框架深度审查 + 阴性实验消化** → 识别了 7+ 阴性实验的 convergent pattern，提出 4 条加固建议 → 已 post
- Release-readiness 检查 + auto-pipeline 审查 → 均 PASS → 已 post

**Registry RUNNING (4 个)**：
- `qwen3-8b-cwm-repo-s123-train-v4` — Qwen CWM s123，ETA ~May 21 21:00 UTC
- `qwen3-8b-cwm-repo-s456-train-v3` — Qwen CWM s456，ETA ~May 21 20:00-21:00 UTC
- `deepseek-cwm-repo-s123-train-v2` — DeepSeek CWM s123，ETA ~May 21 09:30 UTC
- `deepseek-cwm-repo-s456-train-v2` — DeepSeek CWM s456，ETA ~May 21 12:30 UTC

**等待中**：无 pending Worker 回调。Pipeline watcher 会自动捕获 DeepSeek eval 结果。

### 4. 📋 待办（条件触发式）
- DeepSeek s123-v2 eval 完成（~May 21 10:00 UTC）→ 验证 unparseable_rate > 50% + accuracy 与 s42 (56.7%) 方向一致 → 检查 `artifacts/eval_summaries/deepseek_cwm_s123_v2.json`
- DeepSeek s456-v2 eval 完成（~May 21 13:00 UTC）→ 同上验证
- Qwen s123/s456 训练完成（~May 21 21:00 UTC）→ 验证 eval 脚本使用 `--max_seq_length 8192`（之前修复过，确认未回退）
- 全部 4 个 CWM eval 到齐 → 审查 Table 3 CWM 列填入的数字是否与 eval 结果一致 + W5 mixed-effects 重跑后 z-values 是否变化
- 14B pilot 启动（如 Director 批准）→ 验证 train_repo_cwm.py 已增加 `--load_in_4bit` 支持 + GPU 分配合规
- Director 提交论文最终版 → 触发 pre-submission checklist 审查（占位符扫描、页面限制、数字一致性）

### 5. 🎯 战略上下文
- **核心结论三层结构**：(1) fine-tuning 必要 (35-36pp gain)，(2) function-level CLS≈CWM≈TRAJ，(3) repo-level CLS >> CWM（19-26pp, format collapse driven）
- **最强统计证据**：z=-23.7 interaction (n=56,480)，Holm-Bonferroni 校正后仍 significant
- **最大攻击面**：Attack #1 "CWM ≤8B LoRA ≠ 32B CWM with execution trace pretraining"——现有 ablations 全在 LoRA paradigm 内，无法回应 "execution trace pretraining 是关键因素" 的追问。14B pilot 也不能解决这一点
- **阴性实验 pattern 是隐藏武器**：4 个 capacity-increasing 干预（rank32 / 8B / voting / forced parse）全部 null/negative，形成 convergent evidence chain 证明 bottleneck 是 formulation-inherent。已建议 Director 写入 rebuttal 框架但尚未确认是否采纳
- **易错点**：(1) 不要把 Qwen 的 wall-clock ETA 估算方法套用到 DeepSeek（DeepSeek 无 periodic eval，tqdm 准确）——之前 Agent 犯过这个错误，我抓到了；(2) DeepSeek s123-v2 checkpoint 目录为空是正常的（save_strategy=epoch），不要误判为训练失败；(3) CWM 8B repo-level 表面准确率 "提升" (58→65%) 是 unparseable rate 上升导致的 majority-class default artifact，parseable-only 实际下降 (42.88→38.52%)
- **DDL**：EMNLP 2026 ARR，May 25。8 页正文硬限制。当前 Conclusion 在 page 8 末尾，Limitations 在 page 9（不计入限制）


---
