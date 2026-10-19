# Reviewer coordination (archived snapshot) — Part 4 of 4

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../reviewer-coordination-20260522-184212.md) · [Structured JSON](../../../sessions/51/5140454174eab892db59.json)

## Round 115

### User

_source line 2270 · 2026-05-22T18:41:19.592522+00:00_

[WRITE HANDOFF] 请立即写你的 handoff。

**格式硬约束**:
- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹
- 禁止在标签外写任何寒暄 / 说明 / 确认（"好的"/"我开始写"/"写完了"等）

**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:

### 1. 🔴 硬约束 / 红线
  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。
  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。
  下一个"你"第一眼看到的就是这里，写错了会被 Director CRITICAL。

### 2. 🖥️ 基础设施快照
  - 服务器名 + 工作目录 + Python 路径 + conda env
  - 模型路径 / 数据集路径 / wandb config / HF cache
  - 活跃进程：PID + tmux session + cron 任务 ID
  写一次就稳定，下一个"你"不用再 SSH 探查。

### 3. 📊 当前状态
  - 你刚做完什么 / 正在做什么
  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要
  - 等待中的 Worker 回调 / Cron / Director 决策

### 4. 📋 待办（条件触发式）
  格式 "条件 X 满足 → 动作 Y"。例如:
  - "Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交"
  - "pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result"

### 5. 🎯 战略上下文
  - 项目核心结论 / 决策链（D001..）
  - 下一个"你"最容易判断错的事 / 容易踩的坑

**写作原则**：
- 第 1 节必须是项目特定的（不是通用 L1 红线）
- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查
- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff

示例格式:
&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）
- submit_training_job 不支持 shell builtin（source/conda activate 全不行）

### 2. 🖥️ 基础设施快照
- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases
- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）
- 模型：/root/autodl-tmp/qwen35_4b_direct
- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)

### 3. 📊 当前状态
我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。
registry: pilot_011 RUNNING；其他全 DONE。

### 4. 📋 待办
- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算
- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪

### 5. 🎯 战略上下文
Falcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。
易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_9377f94f5f31e719154474b70f5c3d18:reviewer",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 2271 · 2026-05-22T18:42:12.106284+00:00_

&lt;handoff>
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
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9377f94f5f31e719154474b70f5c3d18:reviewer"
}
```

</details>

---
