# reviewer / loop_3.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`492f5ffc9aa89052c2b1.json`](../../sessions/49/492f5ffc9aa89052c2b1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-13T21:05:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器名是 `westc-26893`（不是旧名 `autodl-4090d`，后者已失效会导致 SSH 失败）
- 只有 1 块 GPU（RTX 4090 D, cuda:0），gpu_ids=[0]，不存在越界风险但也不能并行 GPU 实验
- exp-006 是 C3 关键路径实验，正在 tmux 运行（PID 46129），**绝不能 kill 或干扰**
- paper_framing.md 解码消融表有 4 个错误 AUC 值（我已 CRITICAL 报告，等 Agent 修正前不可引用该表写论文）
- OBD 方向不一致已报告但未修复：代码用 P(Y>k)+argmax，论文写 P(depth≤k)+median，提交前必须统一

### 2. 🖥️ 基础设施快照
- 服务器：`westc-26893(root)`，工作目录 `/root/autodl-tmp/gen-depth-contamination`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型：`/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2___5-1___5B-Instruct`
- HF cache：`/root/autodl-tmp/.hf_cache`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/`
- 论文目录：`docs/paper/`（introduction.tex, method.tex, related_work.tex, experiments_c1.tex）
- 活跃进程：exp-006 PID 46129（tmux, cuda:0），50 runs × ~25min ≈ 21h，[1/50] no-filter_s42 训练中
- exp-015 neural probe：PREPARING 状态，脚本在远程 `scripts/run_exp015_neural_probe.py`，等 exp-006 完成后跑

### 3. 📊 当前状态
**刚完成**：
- exp-003 全 4 config 完成审查（全部 K*=2，D016 universality 确认 8/8）
- exp-006 `bc` 崩溃诊断 + 修复后重启确认（正常训练中）
- paper_framing.md D016 更新审查（发现 CRITICAL 数值错误已报告）
- OBD 方向审计（代码 vs 论文不一致已报告）
- introduction.tex + method.tex 最终质量审查（2 warning 已报告）

**Registry 状态**：
- `exp_006_graduated_filtering`: ALLOCATED（实际 RUNNING，[1/50]）
- `exp_015_neural_probe`: PREPARING
- 其余 9 个实验全部 DONE

**等待中**：
- exp-006 完成回调（预计 ~21h 后）
- Agent 修正 paper_framing.md 解码消融表数值
- Agent 修正 registry config4_t12 的 null 值
- Agent 修正 OBD 方向（论文或代码二选一）

### 4. 📋 待办（条件触发式）
- exp-006 cron 回调 → 审查全部 50 runs 结果：(1) 各策略 MMLU/HellaSwag 对比 base model，(2) graduated vs binary-ours 是否有统计显著差异，(3) α sensitivity，(4) 5 seeds 方差。C3 claim 成败在此
- exp-006 失败/部分失败 → 检查 `${OUTPUT_BASE}/failures.log`，诊断 root cause
- exp-015 注册+启动通知 → 审查脚本合规性（GroupKFold, cuda:0, 数据源）
- exp-015 完成 → 审查 K*_neural vs K*_15D：若 K*_neural > 2 则论文 headline 需改为 "feature-dependent K*"
- paper_framing.md 再次更新通知 → 验证解码消融表数值是否与 registry 一致
- discussion.tex 写作完成 → 检查之前发现的 3 个错误是否修正（7B 模型名、dream data、He et al. 引用）
- introduction.tex "preliminary" 措辞更新 → 确认改为正式结果描述

### 5. 🎯 战略上下文
- **核心结论**：K*_empirical = 2，在 8/8 configs 下 universal（D016）。这是论文 C1' 的承重墙
- **决策链**：D003(K*=2锁定) → D004(K*_emp vs K*_theory区分) → D011(C2升级为qualified claim) → D012(2+1 claim结构) → D016(universality narrative)
- **C3 是关键路径**：exp-006 是唯一实验。D013 已准备 fallback story（graduated ≈ binary → informative negative，纯 characterization paper）
- **最易判断错的事**：
  1. exp-003 的 4 个 ablation config 全部是 **rewrite 模式**（脚本未传 --generation_mode，默认 rewrite），不要误认为 continuation
  2. "8 个测试条件" 不是 "12 个"——framing 中 "4 architectures × 2 modes = 8" 是 overcounting（只有 Qwen 有两种模式）
  3. registry 的 exp_id filter 经常返回空（已知 bug），用 limit 参数 workaround
  4. Qwen-cont CI_lower = 0.6015，仅高于 θ=0.60 **0.15 个百分点**——这是 K*=2 最脆弱的一环，审稿人会攻击


---
