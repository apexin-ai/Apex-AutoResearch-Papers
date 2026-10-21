# agent / loop_22.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_22.md`
- **Structured JSON:** [`f17a584852cb3f6c35c9.json`](../../sessions/f1/f17a584852cb3f6c35c9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 22
reason: idle_timeout
updated: '2026-05-19T11:27:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-29999 gpu_ids=[0,1,2,3]，cqa1-21977 gpu_ids=[0]（config 里 cqa1 还写了 0-3 但实际只有 1 卡）
- westd 离线环境：必须 `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`，模型/数据已在本地
- evaluate.py v1 有 ARC logprob bug（chat template 下 "The answer is " 在 user turn 内，logprob 位置错误）——**所有 v1 eval 数据作废**，只用 v2（D148 修复后）
- 投稿 EMNLP 2026 ARR May 25（距今 6 天），不要暗示换会议
- Phi-4 LoRA targets 与其他模型不同：`qkv_proj,o_proj,gate_up_proj,down_proj`（非标准 q/k/v 拆分）
- OLMo-2 需 bf16 显式指定（默认 float32 会 OOM）
- Gemma-2-9B 需 batch_size=1 grad_accum=16（特殊 chat_template）

### 2. 🖥️ 基础设施快照
- **westd-29999**（主力）: 4× RTX PRO 6000 Blackwell 96GB
  - 工作目录: `/root/autodl-tmp/exp001/`
  - Python: `/root/miniconda3/bin/python`
  - HF cache: `/root/autodl-tmp/.hf_cache`
  - 训练 checkpoints: `/root/autodl-tmp/exp001/{family}_{dosage}/` (25 个)
  - Eval 输出 v2: `/root/autodl-tmp/exp001/eval_results_v2/{family}_{dosage}/`
  - Phase 2 日志: `/root/autodl-tmp/exp001/phase2_logs/gpu{0-3}.log`
- **cqa1-21977**: 1× RTX 4090D, 当前空闲
- **活跃进程**: 全部为 0。Cron reconcile 显示 4 个 phase2_eval cron 全部 "Process gone, no sentinel"——进程已结束（完成或 crash），需要 SSH 检查 log 确认
- **Worker 池**: 0 个活跃 Worker

### 3. 📊 当前状态
**刚做完**: 25/25 SFT 训练全部完成，evaluate.py ARC logprob bug 修复（D148），Phase 2 全量重跑已于 ~10:43 UTC 启动（4 GPU 并行，25 个 eval）

**关键悬念**: Phase 2 eval 进程已消失（cron escalating, miss 3-4/5），但 registry 里 4 个 phase2_eval 实验仍为 PREPARING。需要立即 SSH 查 `/root/autodl-tmp/exp001/phase2_logs/gpu{0-3}.log` 确认：
  - 正常完成？→ 收集 v2 结果，进入分析
  - crash？→ 诊断修复重跑

**Registry**: 293 DONE, 29 PREPARING, 1 QUEUED, 0 RUNNING

**待处理的 Director 决策**:
  - D145: Variant A/B 暂缓——14B MMLU +2.28pp 处于灰色地带，但这是 v1 数据（bug），v2 结果出来后需要重新判定
  - D147: MMLU vs ARC benchmark-specific contamination direction——同样基于 v1 数据，v2 可能改变结论

### 4. 📋 待办（条件触发式）
- **Phase 2 eval 完成（25/25 v2 结果齐全）→**:
  1. v1 vs v2 对比分析（量化 ARC bug fix 影响，MMLU 应无变化）
  2. 汇总 5 families × 5 dosages × 2 benchmarks 完整结果表
  3. 重新判定 D145 Variant A/B（用 v2 数据）
  4. 重新验证 D146/D147 结论（scale × benchmark 交互）
  5. 向 Director 汇报 v2 完整结果 + 更新后的 Variant 建议
- **Phase 2 eval crash →**: 查日志定位原因，修复，重跑失败的 GPU batch
- **Variant A/B 确定后 →**: 更新 paper_framing.md，IRT fitting（Stan NUTS），TOST equivalence test
- **IRT 完成后 →**: 更新论文所有表格和图表，Round 7 review
- **Cross-family eval（OLMo-2, Gemma 等）→**: D143 说 Qwen2.5-7B 做 full S1 signal，其他 family 只做 Δacc；尚未执行

### 5. 🎯 战略上下文
**核心结论链**:
- D039: 从 "calibration" pivot 到 "characterization first"——4 claims 重排序
- D108/D115: MMLU domain heterogeneity confirmed（Simpson's paradox: aggregate γ≈0 masks STEM gradient）
- D139: Round 6 review 得 3.0 Findings，识别 4 MF + 8 SF 待修
- D141: 5-family matrix 确认（Qwen×2 + Phi-4 + OLMo-2 + Gemma-2）
- D146/D147: scale × benchmark 交互——ARC 效应随 scale 消失，MMLU 随 scale 增强（**但这是 v1 数据，v2 可能改变**）
- D148: ARC bug fix 是最新决策，全量重跑是当前最高优先级

**最容易判断错的事**:
1. **不要用 v1 eval 数据做任何论文 claim**——v1 ARC 数据全部作废（Gemma d005 ARC 从 22.95% 修正到 77.82%，差异巨大）
2. **D145/D146/D147 的结论都基于 v1 数据**——v2 出来后必须重新验证，不能直接沿用
3. **cqa1 已放弃**——之前在 cqa1 跑的 eval 数据与 westd 有 +10-12pp ARC 差异（v1 bug），所有分析以 westd v2 为准
4. Phase 2 eval 的 cron 状态 PREPARING 不准确——它们实际启动过（有 PID），只是未走 submit_training_job 流程所以 registry 没更新到 RUNNING。需要手动检查日志确认结果


---
