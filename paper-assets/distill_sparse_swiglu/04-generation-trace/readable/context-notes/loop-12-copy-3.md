# reviewer / loop_12.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_12.md`
- **Structured JSON:** [`a74d5b48c2322dc6155f.json`](../../sessions/a7/a74d5b48c2322dc6155f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-22T18:42:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**：westd-34887 cuda:0/1，westd-41718 cuda:0/1。越界立即 CRITICAL。
- **cron 误报模式**：WANDB_MODE=disabled 的 pipeline 实验（K=4 s123/s456 等）进程正常退出后 cron 会报 on_failed——先查 results.json 和日志尾部再判断，不要盲信 cron 状态。已发生 6+ 次。
- **Table 2 数据来源**：50% global 行的 downstream 之前是 s42 单 seed（bench_kl50_global），现在 s123 已补全，更新表格时必须用 3-seed mean±std，不能继续用 s42 单值。
- **submit_training_job 必须带 conda 激活**：`bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ..."` 否则 EXIT_CODE=127。perlayer_kl_k4_50_s42_ppl 已因此失败一次。

### 2. 🖥️ 基础设施快照
- **westd-34887**：`/root/distill_sparse_swiglu/`，conda base，`/root/miniconda3/bin/python`
  - 模型：`/root/autodl-tmp/models/llama-3.1-8b`
  - HF cache：`/root/autodl-tmp/.hf_cache`
  - 双卡空闲（截至 handoff 时 0%/0MiB）
- **westd-41718**：同结构，Qwen-14B 在 `/root/autodl-tmp/models/qwen2.5-14b/`
- **WANDB**：大部分实验 disabled/offline
- **活跃进程**：无（双服务器 GPU 全空闲）
- **关键 checkpoint**：
  - K=4 50% s42：`checkpoints/perlayer_kl_k4_50_s42/predictor_perlayer_kl_k4.pt` (152MB, 训练完成, PPL eval 待补)
  - K=4 30% 3-seed：`checkpoints/perlayer_kl_k4_s{42,123,456}/` 全部完好

### 3. 📊 当前状态
**刚完成**：R16-R19 系列审查——K=4 3-seed 数据验证、审稿方案独立审查、W4 数据落地确认、K=4 50% PPL 失败诊断。

**Registry 关键状态**：
- `perlayer_kl_k4_50_s42_ppl`：FAILED（EXIT_CODE=127，conda 未激活，需重试 5min）← **N2 rebuttal 关键缺失数据**
- `perlayer_kl_k4_50_s42`：ANALYZING（训练完成，PPL=未知，等上面那个 eval）
- `kl50_global_s123_downstream_v2`：cron 报 failed 但实际成功（results.json 完好，metrics 已验证）
- 无 RUNNING 实验

**等待**：Director 对 R17（审稿方案审查）和 R18-R19 的回应。

### 4. 📋 待办
- `perlayer_kl_k4_50_s42_ppl` 重试成功 → 计算 50% mismatch vs coupling 分解：gap_closure = (K4_PPL - K1_PPL) / (E2E_PPL - K1_PPL)，其中 K1=34.85, E2E=11.84。结果直接影响 N2 rebuttal 措辞。
- Paper Agent 提交修订稿 → 按 §5 模板做写作审查（N1 claim 降级、N2 97.5% 替换、N3 trade-off 讨论、W4 Table 2 3-seed 更新、W7 Abstract 拆句、W8 BoolQ 删除）
- Table 2 更新后 → 交叉验证 KL 50% global 3-seed mean：ARC-c=36.3±3.2, WG=63.8±0.3, MMLU=28.3±0.7, GSM8K=2.7±1.3（注意 s42 是 ARC-c/GSM8K 最差 seed）
- Qwen-14B s123 GSM8K 若被调度 → 验证 Table 13 "32.0±5.2" 是否需要更新（当前已确认 3-seed 可验证：s42=35.5%, s123=34.4%, s456=26.1%）

### 5. 🎯 战略上下文
- **论文定位**：EMNLP 2026 ARR，DDL 2026-05-25（3 天）。R22 给 3.0 Findings，目标 3.5。
- **核心叙事**：output-distribution alignment > intermediate loss for sparsity prediction。2D 分解（signal type × coupling scope）。KL predictor 发现的 mask pattern 可 transfer（C1 ablation）。
- **审稿方案**（R17 已审查）：N1 target-swap claim 降级（删 "not the training mechanism itself"）、N2 97.5% 改定性（+K4 50% PPL 数据）、N3 MMLU/GSM8K trade-off 用 remove_valley 因果证据。
- **易错点**：
  1. GSM8K K=4 30% per-seed gap closure 符号翻转（s42=-38%, s123/s456=+118%/+122%），3-seed mean 70.6% 掩盖了极端不稳定性——审稿人可能自己算
  2. KL 50% global 更新为 3-seed 后 ARC-c (36.3) 超过 uniform (33.8)——需调整 global vs uniform narrative
  3. perlayer_kl_50_s42（K=1 50%）registry 状态仍 ANALYZING 未改 DONE
  4. 不要把 cron on_failed 当真——WANDB_MODE=disabled 实验必须查 results.json 确认


---
