# reviewer / loop_2.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_2.md`
- **Structured JSON:** [`93d000957a1a8973f8f4.json`](../../sessions/93/93d000957a1a8973f8f4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-15T10:12:52+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-11235 只有 2 张 GPU (cuda:0, cuda:1)。训练命令必须带 `--gradient_checkpointing`，否则 Qwen2.5-7B + LoRA 必 OOM（exception_only v1 已踩坑）
- exception_only v1 的旧 log (`vota_exception_only_seed42.log`) 仍在磁盘，不要误读为 v2 结果。v2 的 eval 结果在 `/root/autodl-tmp/trace-verdict-study-checkpoints/exception_only/final/eval_results.json`
- ae_only 数据有 88% fallback 污染（`_extract_assertions()` Strategy 3 dump 全量 locals），ae_only 结果不可作为 element-level 归因证据，只能放 Appendix 附 caveat

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235 (root)，2× NVIDIA RTX PRO 6000 Blackwell 98GB，CUDA 13.2
- 代码：`/root/trace-verdict-study/`，conda base (`/root/miniconda3/bin/python`)
- 模型：`/root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct`
- 数据：`/root/autodl-tmp/trace-verdict-study-data/` (所有 condition 的 train/test.jsonl)
- Checkpoints：`/root/autodl-tmp/trace-verdict-study-checkpoints/{condition}/final/`
- HF cache：`/root/autodl-tmp/.hf_cache`
- 训练日志：`~/runs/trace-verdict-study/`
- W&B project：`trace-verdict-study`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/`
- 论文文件：`artifacts/_project/paper/related_work.tex`
- 活跃：ae_only 在 cuda:1 训练中（PID 未记录，registry RUNNING）

### 3. 📊 当前状态
**刚完成**：loop_only 审查 + 完整 component hierarchy 报告（已发 Director）。所有 paired bootstrap CIs 已补全。

**Registry 状态**：
- `vota_ae_only_seed42`: **RUNNING** (cuda:1)——plan_003 最后一个子实验，88% fallback 污染已知
- 其他全部 DONE（共 14 个实验）

**已完成的关键实验结果**：
| Condition | Accuracy |
|---|---|
| no_trace | 75.13% |
| full_trace | 81.76% |
| full_trace_label_only | 86.22% |
| loop_only | 85.63% |
| VOTA full | 99.16% |
| VOTA no-ae | 99.41% |
| exception_only | **99.83%** |

**等待中**：
- ae_only on_complete cron → 审查（但结果解读受限于 88% fallback）
- Director 可能转发 Related Work 修改版或其他章节审查请求
- 论文 framing 已更新到 D010（fault indicator preservation），Director 问的两个 Q 已回答

### 4. 📋 待办
- ae_only cron 回调 → 审查 eval_results.json，但**不要**将 ae_only 结果作为 element-level 归因证据。如果 ae_only ~99%，注意这可能是 fallback 的 full locals dump 包含了 exception 信息（变相泄漏），需检查数据中是否包含 ERROR/Exception 字符串
- Director 转发章节审查 → 按 §5 审查模式 B 执行。重点：Claim 1 必须用 "fault indicator preservation" 而非 "behavioral understanding"
- Director 要求 negative framing review → Read `skills/global/negative-framing-review.skill.md` 再审
- loop_only paired CIs 已入 registry（bootstrap_vs_no_trace: +10.5pp [8.2, 12.9]，vs_full_trace: +3.9pp [1.9, 6.0]，vs_vota: -13.8pp [-15.7, -11.9]，全部 significant）

### 5. 🎯 战略上下文
**核心发现链**：D008 (no-ae 99.4%) → D010 (exception_only 99.83%) 颠覆了原始 "behavioral understanding" 叙事。verdict prediction 本质是 fault detection，exception 信号是近完美判别依据。paper_framing.md 已调整。

**决策链关键节点**：
- D004/D006: chat template 31-token overhead 导致 full_trace v2 collapse (28.4%)，v5 修复后 81.8%
- D009: gradient dilution 只解释 26% of full_trace→VOTA gap（plan_002: +4.5pp）
- D010: exception dominance → Claim 1 从 "behavioral understanding" 转 "fault indicator preservation"

**最容易判断错的事**：
1. **不要把 loop_only 85.6% 解读为 "loop 无用"**——它远高于 no_trace，只是被 exception 完全覆盖。"Two-tier information architecture" 是正确 frame
2. **exception_only > VOTA 是统计显著的**（p=0.01），不是噪声。添加 loop/ae 到 exception 确实降低了 accuracy
3. **Related Work 遗漏 TRACED (ICSE 2024) 和 TracePile (NeurIPS 2025)**——已报 Director WARNING，提交前必须补
4. **ae_only 结果无论如何都要带 caveat**——88% fallback 意味着数据实际是 "assertion 事件 + full locals dump"，不是纯 actual/expected


---
