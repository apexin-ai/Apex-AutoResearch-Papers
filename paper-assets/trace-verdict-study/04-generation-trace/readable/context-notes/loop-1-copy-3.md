# reviewer / loop_1.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`1cf6b8686023a36423ce.json`](../../sessions/1c/1cf6b8686023a36423ce.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-15T01:48:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**cuda:0 和 cuda:1**（westd-11235）。本 session 已发生一次 GPU 冲突事故（vota 用 `--gpu 0` 与 no_trace 撞卡导致 OOM），务必核对 `--gpu` 参数与 registry `spec.gpu` 字段一致
- vota.py 中**禁止出现 match=True/False**——D002 确认这是信息泄漏。已修复并验证 0 残留，但任何改动 vota.py 后必须 `grep -c "match=True" vota_train.jsonl` 再验证
- 训练数据使用 v5 版本（含 `CHAT_TEMPLATE_OVERHEAD=32` 修正），路径 `/root/autodl-tmp/trace-verdict-study-data/`，时间戳 May 15 09:40+
- Registry 中 v3 及更早实验的 metrics 全部是 **旧数据/已作废**，不可引用。只信 `bootstrap_compare.json` 中的结果

### 2. 🖥️ 基础设施快照
- 服务器：**westd-11235**，account: root
- 代码根目录：`/root/trace-verdict-study`
- Python：`/root/miniconda3/bin/python`（conda base env，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型：`/root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct`
- Checkpoints：`/root/autodl-tmp/trace-verdict-study-checkpoints/{no_trace,vota,full_trace}/final/`
- 数据：`/root/autodl-tmp/trace-verdict-study-data/` （v5 格式化数据）
- HF cache：`/root/autodl-tmp/.hf_cache`
- 新鲜评估结果：`/root/trace-verdict-study/results/bootstrap_compare.json` + `results/predictions/*.json`
- 训练日志：`/root/runs/trace-verdict-study/`
- 活跃进程：截至 handoff 时**两卡空闲**（MVP 训练+评估全部完成）
- W&B project: `trace-verdict-study`

### 3. 📊 当前状态
**MVP 已 PASS（D003）**，项目进入 Research 阶段。

真实评估结果（bootstrap_compare.json，N=10000）：
- no_trace: 75.13% (baseline)
- **VOTA: 95.63%** (+20.5pp, CI [+17.7, +23.4], excludes 0)
- full_trace: 28.49% (100% predict "fail", model collapse)

Registry 中 **vota_seed42_v4 的 accuracy 已修正为 0.9563**（之前是旧的 0.9916）。但 per-class metrics（pass_P/R/F1, fail_P/R/F1）仍是 v3 旧值——真实值见 bootstrap_compare.json。full_trace_seed42_v2 的 metrics 同理部分为旧值。

所有 v4/v2 训练 DONE。paper_framing.md + experiment_plan.yaml 已写。Dream 模拟 dream_20260515T013018 已启动，等待结果。chat-template-overhead 修正已应用，v5 数据已重新生成。

### 4. 📋 待办
- Dream 完成回调 → 审查 dream 报告，评估是否需要调整 framing/plan
- plan_001 启动（去 actual/expected ablation）→ **这是 make-or-break 实验**：如果去 actual/expected 后 acc 仍 >80%，VOTA 是真信号；降到 ~75% 则是字符串比对。审查重点：(1) vota.py 的修改是否只去了 actual/expected 而没引入新 bug，(2) GPU 分配正确
- plan_002 启动（full_trace label-only loss）→ 验证 collapse 根因是 gradient dilution。审查重点：train_sft.py 的 loss mask 实现是否只对 classification token 计算 loss
- plan_001 结果出来 → 审查结论是否支撑 Claim 1 强度，是否需要触发 contingency framing
- plan_003（component ablation）→ 依赖 plan_001，4 个 sub-conditions
- 任何实验 registry 更新 → 交叉验证 metrics 来源（必须来自新鲜 evaluate/bootstrap_compare 运行，不是旧 eval_results.json）

### 5. 🎯 战略上下文
**决策链**：D001（MVP 阈值 ≥2pp + CI excludes 0）→ D002（Round 1 作废：match 泄漏 + label 截断）→ D003（MVP PASS，VOTA 95.63%）

**最容易判断错的事**：
1. **VOTA 95.63% 不等于 "trace 教会了模型理解代码"**。极大概率是 actual==expected 字符串比对。plan_001 的 ablation 结果决定一切——在此之前不要对 Claim 1 的强度下结论
2. **Registry metrics 不可信**——多个实验的 eval 指标来自旧 eval_results.json（v3 时代），被错误写入 registry。始终以 `bootstrap_compare.json` 或新鲜运行的 evaluate.py 为准
3. **full_trace collapse 不是 truncation bug**——smart truncation + chat template overhead 都修了，结果不变（100% predict fail）。根因是 dense trace token 稀释分类梯度，需要 plan_002 的 label-only loss 验证
4. **VOTA 截断率 89%**——"紧凑表示"并不紧凑，`[fallback: full locals]` dump 了大量模块级变量浪费 token。这影响论文 "compact trace" 叙事，但非 P0 阻塞
5. **paper_framing.md 中 Claim 2 的 "gradient dilution" 是假说非结论**——plan_002 未跑之前不要在论文中断言此机制


---
