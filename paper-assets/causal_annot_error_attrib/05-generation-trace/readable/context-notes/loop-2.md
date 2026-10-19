# reviewer / loop_2.md

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`cbc03c733f336b35a1ff.json`](../../sessions/cb/cbc03c733f336b35a1ff.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-21T17:54:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `home-1x5090(sonny)`，代码根 `/home/sonny/causal_annot_error_attrib`，GPU 白名单需查 `execution.gpu_ids`
- `ppi_empirical_validation.json` 当前工作区版本（Agent 重算的真实 PPI++ 数据）与 HEAD 提交版本（含 theoretical_Cinv 伪装数据）不同——**HEAD 版本的 IV=100% 和 96.2% grand mean 不可引用为 PPI++ 结果**
- VAST/CC 的混淆矩阵在旧 JSON 中是 approximate（diagonal + uniform off-diagonal），不是真实 LLM 标注矩阵——论文中"real LLM confusion matrices"措辞必须修正
- Plan_011 frontier annotations 正在远程跑（PID 712156），~5500 API calls，预计 3-5h，不要 kill

### 2. 🖥️ 基础设施快照
- 服务器：`home-1x5090`，用户 `sonny`，代码 `/home/sonny/causal_annot_error_attrib`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/`
- Python 环境：远程用 `/tmp/hf_venv/bin/python`（plan_011 脚本依赖此路径）
- 活跃进程：plan_011 frontier annotation nohup PID 712156（qwen3_zero-shot 429/1500，后续 5 configs pending）
- 无 wandb 配置，无训练任务——本项目纯 MC 模拟 + API 标注

### 3. 📊 当前状态
**刚完成**：向 Director 提交两份 CRITICAL/WARNING 报告：
1. **[CRITICAL] PPI++ 实证验证三重数据完整性问题**：IV 用 theoretical_Cinv 非 PPI++（100%→实际-79.2%）、10/18 config 用近似矩阵非真实 LLM 矩阵、|mean_bias| 度量对无偏估计量系统性膨胀（96.2%→实际 39.0%）
2. **[WARNING] Plan_007 合成评估 93.8% 同源度量缺陷**：`plan_007_correction_guidance.py` L610-616 确认使用 `1 - |mean(τ̂)-τ_true| / |mean(τ̂_uncorr)-τ_true|`，N_sim=1000 下 PPI++ 因无偏性自动趋近 100%。RMSE 数据已有但论文未用。

**等待中**：
- Director 对 PPI++ CRITICAL 报告的决策（是否重写 §5.6 correction 段落）
- Plan_011 frontier annotation 远程进程完成（~3-5h）
- Plan_011 前一个 worker 报告 API auth blocker（tum_* key 401），但后续 worker 用另一端点部分跑通

### 4. 📋 待办
- Plan_011 annotation 完成 → 审查新混淆矩阵质量（parse rate, class distribution），确认是否可纳入论文
- Director 决定重算 correction 数字 → 审查新度量（RMSE reduction 或 MAE）下的 PPI++ vs MC-SIMEX 排名是否变化
- 论文 §5.6 / L150-151 被重写 → 对抗审查新版本，验证数字与新 JSON 一致
- `table3_source_data.txt` 中 MC-SIMEX 的 sign flip（frontdoor: 论文 +8.7% vs JSON -55.7%）尚未被修复 → 如果 Director 启动 correction 段落重写，需同步检查

### 5. 🎯 战略上下文
- **核心危机**：论文 correction 叙事的两个支柱数字（合成 93.8%、实证 96.2%）都受度量缺陷影响。96.2% 还叠加了 IV 伪装和近似矩阵问题。审稿人复现任一实验都会发现不一致。
- **决策链**：D017（sign-flip footnote + K=2 ASV-unsafe）已完成。PPI++ 修正尚无 D 编号，等 Director 决策。
- **易错判断**：
  - PPI++ 不是"完全不行"——confounding/frontdoor 拓扑下确实有效（即使用 RMSE 度量也 >80%），但 IV 有害、exposure 不如 MC-SIMEX。下一个"你"不要矫枉过正把 PPI++ 说成无用。
  - 93.8% 和 96.2% 的差异（论文称"real matrices more diagonally dominant"）是假解释——真实原因是 IV theoretical_Cinv 和近似矩阵。但合成 93.8% 本身也膨胀，所以不能简单用"合成数字是对的，实证数字是错的"来修正。
  - Plan_006 的 18 valid configs（去掉 12 个 zero-matrix 后）vs 论文引用的 18 configs（含 VAST/CC 近似矩阵）——这是两个不同的"18"，不要混淆。


---
