# agent / loop_2.md

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`2895dde0cb937a45f8b3.json`](../../sessions/28/2895dde0cb937a45f8b3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-21T19:25:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-33183 是唯一服务器，GPU 只有 cuda:0。registry 中 gpu_ids 白名单需确认后再用
- FITD 对话只有 2-3 轮，Table 7 中 K=3/K=5 必须填 "--"，不要跑推理
- 所有 std 计算用 population std (ddof=0)，不是 sample std。这是本项目 Critical 级审稿修正（checklist.tex 和 appendix.tex 已从 "sample std" 改为 "population std"，experiments.tex 原本就正确）
- Table 7 FITD Vanilla 数值刚从 seed-42-only 改为 3-seed mean（K1: .990→.954, K2: 1.000→.952）。Director 已被通知但尚未确认。如果 Director 要求回滚，需改回旧值
- exp40 Llama Guard 3 8B 结果已报 Director，但 Director 尚未决定是否加入论文。不要自行添加到任何 paper 文件

### 2. 🖥️ 基础设施快照
- 服务器：westd-33183，工作目录 /root/persuasion_turn_jailbreak_detect/
- Python：/root/miniconda3/bin/python (conda base)，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型 checkpoints：/root/persuasion_turn_jailbreak_detect/checkpoints/（plan_002 = 主 pipeline，seeds 42/123/456）
- HF cache / 大模型：/root/autodl-tmp/.hf_cache/（Llama Guard 3 8B 在 LLM-Research/Llama-Guard-3-8B）
- 数据：/root/persuasion_turn_jailbreak_detect/data/（generated/{dd,aa,fitd}_all.jsonl, plan_002_splits/）
- per-sample predictions：/root/persuasion_turn_jailbreak_detect/per_sample_predictions/（exp35 生成，production 级）
- 论文本地路径：/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/paper/
- 活跃进程：无。GPU 空闲，无 Worker、无 Cron、无 tmux session

### 3. 📊 当前状态
刚完成 Table 7 FITD per-seed std 补全（appendix.tex 已更新）。已向 Director 汇报 Vanilla 数值变更。

Registry 关键状态：
- RUNNING：v4-taxei-fixed-inject25-r2, v4-fixed-inject10, v4-vanilla-seed123（这三个是其他项目残留，不属于本项目主线）
- PREPARING：exp37_length_matched_benign, exp36_frozen_mlm_probing, exp13_meanpool_multiseed 等（均已有结果但 status 未推进到 DONE，实际 conclusion 已记录）
- DONE (近期)：exp40_llama_guard_baseline (success), exp39_extra_seeds_tost (success), exp38_wildcat_calibration (negative)
- 总计：成功 54 / 负向 21 / 失败 0

无等待中的 Worker 回调、Cron 或 Director 决策（Table 7 FITD Vanilla 变更通知已发，等 Director 回复）。

### 4. 📋 待办
- Director 回复 Table 7 Vanilla 变更 → 确认保留新值或回滚
- Director 决定 exp40 Llama Guard 是否入论文 → 若入，在 Table 1 或新增 baseline 行加数据
- Director 下发 Round 9 审稿应对任务 → 按指令执行（DDL 2026-05-25）
- GPU 空闲且 Director 无新指令 → 检查 ROADMAP 是否有低优先级 filler 任务
- 任何新实验需要 GPU → 确认 gpu_ids 白名单后再 submit

### 5. 🎯 战略上下文
项目核心结论链：9-class DAPT >> MLM ≈ vanilla (OOD)；classification structure >> label semantics (scrambled ≈ 9-class on DD/FITD, TOST confirmed)；BiGRU ≈ mean pooling（时序建模非必要）；Llama Guard 3 完全失败（recall≈0）证明需要专门方法。

关键 negative 发现已 positioned as Limitations：WildChat domain shift (AUC=0.70)、AA padding attention dilution (-57.9pp)。

TOST 5-seed 结果有两个 Director 需修正的偏差：DD 2pp p=0.0016（非<0.001）、AA Cohen's d=0.092（非0.18）。已报 Director 但确认状态未知。

易错点：
- Registry 中很多实验 status=PREPARING 但 conclusion 已有值，这是历史遗留（早期 session 跳过了状态推进）。不要因为 status=PREPARING 就重跑
- registry filter `filters={"exp_id": "exp32"}` 不工作，用 `limit=N` + fields filter 替代
- exp27_mean_pooling 全 1.000±.000 看起来可疑，可能有 bug，与 exp13 meanpool 结果不一致


---
