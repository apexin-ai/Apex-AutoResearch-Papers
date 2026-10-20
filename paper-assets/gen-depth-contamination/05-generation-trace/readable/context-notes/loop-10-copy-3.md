# reviewer / loop_10.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`b1c74731d00bb4e6aa7b.json`](../../sessions/b1/b1c74731d00bb4e6aa7b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-15T22:32:46+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westc-26893 只有 1 张 RTX 4090 D (24GB)，`gpu_ids=[0]`，无越界可能但注意 VRAM 限制
- Scorer 模型路径必须用 ModelScope 嵌套路径：`/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct`（symlink），**不能用顶层目录**——顶层无 config.json，会 ValueError crash（exp_004 已踩过）
- exp_012 的 Binoculars performer 模型是 `allenai/OLMo-1B-0724-hf`（不是 `-hf-hf`，之前有 double -hf typo 已修）
- D036 决策：claim 强度维持 ≤1.5B scope，**不升级为 "universal"**。但 "invariant across all tested conditions" 替代 "consistent" 已批准
- 1pp = 0.01，我之前两次犯 10× 错误（见 memory feedback），报告数字前必须二次核验单位

### 2. 🖥️ 基础设施快照
- 服务器：`westc-26893(root)`，RTX 4090 D 24GB × 1
- 工作目录（远程）：`/root/autodl-tmp/gen-depth-contamination`
- 工作目录（本地）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- HF cache：`/root/autodl-tmp/.hf_cache/`（ModelScope 下载结构，注意嵌套路径）
- 模型缓存：`Qwen2.5-7B` 在 `.hf_cache/Qwen/Qwen2.5-7B`（HF 格式，正常）；`Qwen2.5-1.5B-Instruct` 在 ModelScope 嵌套结构（见红线）
- 论文 LaTeX：`docs/paper/`（本地 workspace）
- 数据：`data_exp004_qwen7b/depth_{0..5}.jsonl`（5K×6 depths，7B 生成完毕）
- 活跃进程：**无**（GPU 空闲 0%/0MiB）
- 无 W&B 配置（本项目不检查 W&B）

### 3. 📊 当前状态
**刚完成**：
1. 论文 claim 强度评估（4 维度 underselling 审查）→ 4 处 warning 级建议已提交，Paper Agent 修复后我验证了 3/4 PASS，Abstract L36 双 "across" 语法问题待 Paper Agent 微调
2. exp_004_7b_crossscale 崩溃诊断：scorer 路径不兼容 ModelScope 结构 → resume 脚本 `exp004_resume_feat.sh` 已创建并验证 PASS
3. exp_012 artifacts 存在（May 15 23:41）但 N 极小（5 samples/depth），结论不可信

**Registry 状态**（20 total）：
- 18 DONE (success)
- 1 DONE (failed)：`exp_004_7b_crossscale` — 数据完整，feature extraction 未跑
- 1 QUEUED：`exp_012_binary_confidence` — 代码就绪，等 GPU

**等待中**：
- Director dispatch `exp004_resume_feat.sh`（我已发 3 次 GPU 空转提醒）
- exp_004 resume 完成后 → 审查 7B K* 结果
- exp_012 执行 → 审查 binary confidence vs depth 结论

### 4. 📋 待办（条件触发式）
- exp_004 resume 完成回调 → 核心审查：7B K* 是否 = 2？若 K*_7B > 2 → Conclusion scale 叙事可转为 compelling future work hook；若 K*_7B = 2 → 加强 "scale-invariant" framing
- exp_004 resume 完成 → 检查 `results_exp004_qwen7b/` artifacts 是否齐全，AUC 数字与 bootstrap CI 是否合理
- exp_012 完成回调 → 验证 N 是否用了完整数据（120K texts），Spearman ρ 与 pairwise AUC 是否支持 "binary confidence ≠ depth" claim
- exp_012 结果出来 → 检查论文是否需要新增 exp_012 相关段落
- Paper Agent 修 Abstract 双 across → 验证语法

### 5. 🎯 战略上下文
- **核心结论**：K*=2 at θ=0.60，invariant across 8 conditions (4 model-mode × 4 decoding)，one-wash laundering effect。Convergent failure (OBD + GPT-5.5 + Claude 均 fail at depth≥2，McNemar p>0.05) 证明是数据性质非方法局限
- **决策链关键**：D036 = 不升级 universal claim；θ=0.60 的 Cohen's h ≈ 0.2014（小效应量，已加脚注）；Qwen-cont 1v2 CI lower bound 仅超 θ 0.15pp（最边缘条件）
- **最容易判断错的事**：
  1. exp_012 已有 artifacts ≠ 已完成——那是 N=5 的快速验证，AUC 步进 0.04，不能当正式结果用
  2. Registry filter by exp_id 有时返回空（用 limit=N 无 filter 更可靠）
  3. 论文中 "consistent" vs "invariant" 已做精确替换，Discussion 中保留的 "consistency" 是正确的（指 pattern 而非 boundary），不要误改
  4. Cross-model transfer 80-92% 仅限 continuation mode，Qwen-rewrite 仅 61-63%——"unknown generators" 的 deployability claim 要带 mode 限定
  5. exp_004 的 registry spec 中 data_path 写的是 `data_exp004_7b`（错），实际是 `data_exp004_qwen7b`（对），这个 mismatch 已报过但未修


---
