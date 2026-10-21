# reviewer / loop_14.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_14.md`
- **Structured JSON:** [`e49d5bfa7ff9cef337ea.json`](../../sessions/e4/e49d5bfa7ff9cef337ea.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-05-19T10:30:00+00:00'
---

### 1. 🔴 硬约束 / 红线
- **gpu-6000pro-2**: 14B 实验专用，当前 qwen25_14b_temp09 (cuda:0) 和 qwen25_14b_topk50 (cuda:1) 正在跑，不可 kill
- **westd-48862**: accumulation v3 专用，accum_v3_mix50 (cuda:0, PID 114337) 和 accum_v3_mix25 (cuda:1, PID 114478) 正在跑，不可 kill
- accumulation v3 脚本已修复两个 CRITICAL bug（target_modules 和 reference model），当前运行的是修复后版本，不要回退到 .bak
- Introduction L30 "7--14B (54--70%)" 中 70% 来自 Llama-3.1-8B-Instruct QLoRA (cross_scale_llama3_8b_003)，但 Llama BASE 同 scale 仅 59.9%——我已报告此处跨模型/跨量化范围合并误导，Director 尚未回应是否改写
- accum_mix50 / accum_mix25（旧 v1 feature-level mixing）应标 INVALIDATED 而非 "failed"，已报告两次未确认执行

### 2. 🖥️ 基础设施快照
- **gpu-6000pro-2**: `/root/autodl-tmp/recursive_gen_depth_est`，Python via miniconda3，Qwen2.5-14B cached at `/root/autodl-tmp/.hf_cache/`
  - 活跃: qwen25_14b_temp09 (tmux, cuda:0, PID 776596), qwen25_14b_topk50 (tmux, cuda:1, PID 787051)
- **westd-48862**: `/root/autodl-tmp/recursive_gen_depth_est`，Python 3.10.12 (no conda)，GPT-2 XL + Pythia-1.4B cached at `/root/autodl-tmp/.hf_cache/hub/`
  - 活跃: accum_v3_mix50 (tmux=accum_v3_mix50, cuda:0, PID 114337), accum_v3_mix25 (tmux=accum_v3_mix25, cuda:1, PID 114478)
- **本地 workspace**: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/`
  - 论文: `docs/paper/` (D047 编译通过，≤8 页正文，0 errors)
  - 14B 场景模板: `docs/paper/drafts/14b_scenarios.tex`
  - Binoculars baseline 脚本: `artifacts/binoculars_baseline/binoculars_ordinal_eval.py` (code review PASS，尚未运行)

### 3. 📊 当前状态
刚完成 Director 要求的两部分并行审查并已 post：
1. **14B 三场景叙事分析** — 对 Scenario A/B/C 分别给出 §5.4 写法、Abstract 放置、分数影响评估
2. **Paper story 完整性审查** — 8 个 warning (跨尺度数据引用、instruct 泛化、LoRA ablation 缺失、Binoculars baseline 缺失、accumulation Discussion 待数据、Claim 3 覆盖弱)，0 个 critical

**Registry RUNNING**:
- `qwen25_14b_temp09` — 14B temperature 策略 (ETA ~May 20 05:00 UTC)
- `qwen25_14b_topk50` — 14B top-k 策略 (ETA ~May 20 06:00 UTC)
- `accum_v3_mix50` — 50/50 accumulation GPT-2 XL (ETA ~May 19 14:30 UTC)
- `accum_v3_mix25` — 25/75 accumulation GPT-2 XL (ETA ~May 19 14:30 UTC)

**待回调**: Binoculars baseline 脚本已写好待部署运行，尚未收到 worker_done 通知

### 4. 📋 待办
- **accum_v3 完成 →** 核实 mix50/mix25 RF accuracy 与 Discussion §6 预测是否一致（"signal should attenuate"）；如果 signal 不衰减，Discussion 需要大幅改写，立即 CRITICAL 报告
- **14B temp09/topk50 完成 →** 根据实际数字选择 Scenario A/B/C 模板；核实 strategy ranking 是否与 1-1.5B 一致；检查 14b_scenarios.tex 中的 QLoRA 数据是否被清除
- **Binoculars baseline 运行完成 →** 核实 ordinal accuracy（预期 30-40%），确认 RF_multi 11-feature 是否显著优于 RF_single，与现有 DetectGPT/Min-K% 30-33% 对比
- **Director 回应跨尺度数据 warning →** 如果决定保留 "54-70%" 范围，要求补充 QLoRA confound 说明；如果删除，跟踪 introduction.tex L30 改写
- **plan_018 标记 →** Binoculars 脚本运行完成后 plan_018 应从 "planned" 改为相应状态

### 5. 🎯 战略上下文
- **项目定位**: EMNLP 2026 Main (ARR May 25)，empirical study + task formalization，DCOL 已放弃，Atlas/EDD 为 PRIMARY contribution
- **论文核心叙事**: 全替换链→perplexity tail features→EDD→cross-strategy bottleneck。主线一致，D044/D047 修复了循环论证和 self-reference 问题
- **最易判断错的事**:
  1. 14B EDD_{0.70}=0 看起来像"失败"，实际上 d1-d3 discrimination 持续（d1v2=0.713, d2v3=0.728 都>0.70）。14B 叙事焦点应该是 "d0/d1 boundary vanishes but d1-d3 ordinal structure persists"，不是"14B 失败了"
  2. cross_scale_llama3_8b_001/002 确实失败了，但 _003 成功了（70.2%）——不要因为看到前两个失败就认为所有 Llama 8B 都没结果
  3. Qwen7B (60.1%) 有 U-shape AUC pattern（非单调），与 Llama8B (70.2%, 单调) 矛盾——paper_framing.md 说"QLoRA results contradictory" 主要指 Qwen7B 的 U-shape，不是所有 QLoRA
  4. Discussion accumulation 段落目前是纯预测语言，accum_v3 结果出来之前不要 finalize
  5. 页数已经在极限（D047 刚好 8 页），任何新增内容必须同时压缩等量文本


---
