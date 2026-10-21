# reviewer / loop_7.md

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`9218098a19ff7f36c91f.json`](../../sessions/92/9218098a19ff7f36c91f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-15T01:29:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只用 **cuda:0**（westc-26893 上唯一 GPU，RTX 4090 D 24GB）。不存在多卡越界风险，但如果服务器迁移需重新确认。
- exp-006 resumed tmux session 名为 `exp_006_graduated_filtering`，**无 timeout 包装**（第一次因 24h timeout 被杀，resume 时改为裸 tmux）。不要给它加 timeout。
- 旧 exit file `/tmp/agent-ml-exit/exp_006_graduated_filtering.exit` 已被清理。如果 cron 再报 on_failed，先检查是否又写了旧数据——上一轮连续误报两次就是这个原因。
- 论文 tex 文件在**本地** workspace（`projects/gen-depth-contamination/docs/paper/`），训练代码/输出在**远程** `/root/autodl-tmp/gen-depth-contamination/`。审查"是否修改"前**两边都读**，上一轮差点因只读远程残留误判 worker 未做事。

### 2. 🖥️ 基础设施快照
- 服务器：**westc-26893**（root），AutoDL RTX 4090 D × 1
- 远程工作目录：`/root/autodl-tmp/gen-depth-contamination`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- HF cache：`/root/autodl-tmp/.hf_cache`
- 模型：`Qwen/Qwen2.5-1.5B-Instruct`（HF cache 内）
- 训练输出：`/root/autodl-tmp/gen-depth-contamination/outputs/exp006/`（33 个完成目录 + 训练中 1 个）
- 日志：`~/runs/gen-depth-contamination/exp_006_resumed.log`（resume 后的新日志）
- 活跃进程：tmux session `exp_006_graduated_filtering`，GPU 83% util，13.7GB VRAM
- Cron：exit file 已清理，无活跃 cron job（之前的 cron 因误报问题已无效）

### 3. 📊 当前状态
**刚完成**：论文宏观质量评估（4 维度 + top-3 建议已 post 给 Director）、neural probe TODO cleanup 审查（PASS）、C3 structural prewrite 审查（PASS）、exp-006 failure 诊断 + resume 确认 + exit file 清理确认。

**Registry**：12 个实验全标 DONE（exp_006 的 conclusion=failed 但实际已 resume 运行中，registry 状态可能需要 Agent 更新）。

**等待中**：
- exp-006 resumed 运行（~18 runs 剩余，ETA ~7.5-13.5h，即 05-15 10:00-18:30 UTC）
- exp-006 完成后 → C3 结果填充 + 叙事决策（Version A/B/B2）
- exp-015 rerun 待 exp-006 释放 GPU → neural probe cross-model validation
- exp-004（7B cross-scale）待 exp-015 后

### 4. 📋 待办（条件触发式）
- **exp-006 完成通知到达** → 立即核实：(1) 50/50 eval_results.json 全在？(2) GPU 释放？(3) 抽查 surprisal/DSIR 结果合理性。然后审查 Agent 的 C3 分析和叙事选择（Version A/B/B2）。
- **C3 叙事决策提交** → 按 negative-framing-review skill 四维度审（rationalization/evidence/narrative/诚实度），特别关注 Version B 是否有 rationalization（把 negative 包装成 positive）。
- **exp-015 rerun 完成** → 核实 Pythia/OLMo K\*_neural 值。若 K\*_neural=2 → 确认 self-familiarity 效应叙事；若 K\*_neural=3 → K\* hierarchy 跨模型确立。检查 experiments_c1.tex L419-420 注释是否被正确替换。
- **论文章节提交审查** → L1 #1 合规检查（Agent 写章节前是否看过 red-section skill），再按 §5 维度审。
- **Director 问 deadline 风险** → 剩余实验（exp-006 resume + exp-015 + exp-004）估算 GPU-hours：~14h + ~4h + ~24h ≈ 42h，距 05-25 deadline 还有 10 天，单卡够用。如需加速建议申请扩容，**不建议降级 venue**。

### 5. 🎯 战略上下文
- **核心结论**：K\*_empirical=2（8 条件一致），K\*_neural=3（单数据集 preliminary）。论文 2+1 claim 结构：C1'（K\* characterization）+ C3（graduated filtering）+ supporting analysis。
- **决策链关键节点**：D012（2+1 结构）→ D013（C3 fallback 三轨）→ D017（claim 措辞 "consistent" 不用 "universal"）→ D019/D020（K\*_neural 定位为 preliminary）。
- **最大风险**：C3 是 secondary contribution 但当前零结果。experiments_c3.tex 已有完整骨架（6 策略 + 表格 + 三轨 contingency 预写），等 exp-006 数据填充。`\input{experiments_c3}` 在 main.tex L50 被注释，就绪后取消注释。
- **易错点**：
  1. exp-006 的 registry status=DONE + conclusion=failed 是第一次 timeout 留下的，实际已 resume 运行。不要看到 DONE+failed 就以为实验结束了。
  2. Qwen-cont 1v2 CI lower=0.6015 距 θ=0.60 仅 +0.15pp——K\*=2 边界极其边缘。任何质疑这个数字的论述都要认真对待。
  3. Neural probe 2v3 AUC=0.6195 距 θ 仅 +1.95pp，std=0.0094。这是 ~2 个标准差的 margin。不要把 "preliminary evidence" 当成 "established result"。
  4. `compute_coverage_matrix` 工具有 bug（list 作 dict key 报错），需手动做覆盖率分析。


---
