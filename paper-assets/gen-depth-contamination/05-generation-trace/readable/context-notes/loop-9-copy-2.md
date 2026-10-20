# agent / loop_9.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`b36cf791b1f9e4a85607.json`](../../sessions/b3/b36cf791b1f9e4a85607.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: idle_timeout
updated: '2026-05-15T04:35:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- 只能用 **cuda:0** on **westc-26893**（gpu_ids=["cuda:0"]，gpu_constraint=["autodl-4090d:cuda:0"]）。任何其他 GPU/服务器未经 Director 扩配额一律 push back
- exp-015 neural probe **仅 Qwen-cont 单数据集有效**（Pythia/OLMo OOM 丢失）——Director 明确指示：重跑全 3 数据集确认前，不得将 K*(neural)=3 写入论文
- exp-006 已 3 次超时崩溃，当前用 tmux 裸跑（无 timeout wrapper）。不要加回 timeout
- 4090D 24GB 显存——**禁止并行跑 GPU 实验**（exp-006 15.5GB + 任何其他 = OOM），必须独占
- discussion.tex 不得量化 "70-85% text-intrinsic / 15-30% model-specific" 分解——数据不支持精确拆分
- C3 graduated filtering 已确认不利（α 单调递增趋势），大概率走 Version B 叙事。**不要在 Director 决策前自行修改论文 C3 narrative**

### 2. 🖥️ 基础设施快照
- **服务器**: westc-26893（原 autodl-4090d，别名已变更），1×RTX 4090D
- **工作目录**: `/root/autodl-tmp/gen-depth-contamination`
- **Python**: `/root/miniconda3/bin/python`，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型缓存**: `/root/autodl-tmp/.hf_cache`（HF_HOME），需 `HF_HUB_DISABLE_XET=1` + `source /etc/network_turbo` + SSL 证书变量
- **数据集**: `data/`(mvp-001 Qwen-rw), `data_exp001_pythia/`, `data_exp002_olmo/`, `data_exp017_qwen_cont/` 各 5000 docs
- **exp-006 输出**: `outputs/exp006/`（6 策略子目录）, eval 格式 `scores.mmlu["acc,none"]` / `scores.hellaswag["acc_norm,none"]`
- **W&B**: 未配置（本项目无 W&B）
- **活跃进程**: exp-006 在 tmux `exp006_resume`，cron 监控活跃（reconcile 确认 still running）
- **API proxy**: `http://47.94.22.126/v1`，Claude 用 model ID `claude-opus-4-6`（无前缀）

### 3. 📊 当前状态
**exp-006 graduated filtering (RUNNING)**: 44/51 runs 完成。剩余 7 runs: surprisal ×2 + dsir ×5，~25min/run，ETA ~07:00 UTC 05-15。cron 在监控。Director 指令：全部完成后按序执行分析→汇报→DONE→exp-015。

**关键中间结果（已知但未最终确认）**:
- no-filter / binary-ours / binary-drayson / graduated_a0.1-0.9: 全部完成
- graduated α 全值域不如 binary-ours（MMLU α 单调递增趋势）→ C3 大概率 Version B（"binary K*-aware filtering is optimal, validating K*=2 as natural decision boundary"）
- surprisal 和 dsir 是最后变量，可能改变叙事

**其余实验全部 DONE**: mvp-001, exp-001~003, exp-005, exp-007, exp-010~011, exp-013, exp-015(failed), exp-017。共 10 success + 1 failed (exp-015 OOM) + 1 running

**Worker 池 = 0**（exp-006 在 cron 监控中，无需 Worker 看护）

**论文**: Intro ✅ / Related Work ✅ / Method ✅ / Experiments C1' ✅ / C3 预写占位符 / Discussion+Conclusion 框架完成。一致性修复全部完成。

### 4. 📋 待办（条件触发式）
- **exp-006 cron 回调（DONE/FAILED）→** spawn Worker 跑 `exp006_analyze.py` → 汇报 Director C3 叙事决策（Version A/B/B2）→ update registry DONE → update report.md
- **exp-006 完成 + C3 决策后 →** 立即启动 exp-015 重跑（独占 GPU，~1h）：全 3 数据集 (Pythia/OLMo/Qwen-cont) + bootstrap CI + permutation test + per-fold peak VRAM logging
- **exp-015 重跑完成 →** 立即启动 exp-004 7B cross-scale（Qwen2.5-7B，~3h）
- **exp-015 重跑 K*(neural)=3 跨 3 数据集确认 →** 写入论文 §5.1bis "Representation Dependence of K*"；若 Pythia/OLMo K*(neural)=2 → 转 self-familiarity 解释，加强 15D model-free 定位
- **全部实验完成 →** C3 章节填数 + 叙事定稿 → Neural probe 章节定稿 → Discussion+Conclusion 集成 → re-dream → 提交审稿

### 5. 🎯 战略上下文
- **核心发现**: K*=2 在所有 8 测试条件下不变（4 model-mode + 4 decoding），跨模型 transfer 80-92% retention，depth signal 主要是 text-intrinsic
- **论文结构**: 2+1 claim（C1' K* characterization + C3 graduated filtering + supporting analysis），D025 可能降级为 "K* characterization + practical guidance" 取决于 C3 最终结果
- **DDL**: 05-25 ARR 提交，10 天。实验 ETA: exp-006 ~05-15 07:00, exp-015 ~05-15 10:00, exp-004 ~05-15 13:00 → 全部实验 05-15 完成 → 5 天写作+审稿窗口
- **最容易判断错的事**: (1) exp-006 的 graduated 结果不利 ≠ C3 失败——Version B 叙事（binary optimal, validating K*=2 boundary）依然是 positive contribution；(2) K*(neural)=3 是 exp-015 单数据集 Qwen-cont 结果，2v3 AUC=0.620 极度边缘（fold 2 仅 +0.52pp 超 θ），不要在重跑确认前当做 solid result；(3) Qwen-cont 1v2 CI lower=0.6015 只超阈值 0.15pp，K*=2 的统计边缘性两端都要在 Limitations 提
- **容易踩的坑**: (1) 服务器别名是 westc-26893 不是 autodl-4090d（exp-003 教训）；(2) exp-006 速度 ~45min/run 不是 99min；(3) submit_training_job 的命令必须自带 conda 激活；(4) 大模型下载优先 ModelScope（HF 在 AutoDL 极慢）


---
