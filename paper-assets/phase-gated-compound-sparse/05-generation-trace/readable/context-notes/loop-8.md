# director / loop_8.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`25acef098f43d930b510.json`](../../sessions/25/25acef098f43d930b510.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-16T00:21:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:0/1/2/3（westd-22162 项目配额内）
- DS accuracy 数据在论文中仅作**定性观察**（D086），不做定量 claim——截断率过高（s020 58%, s025 76%），QW 是 accuracy 定量主力
- DS 8k v2 系列是验证性重跑（D088），目的是支撑"generation length inflation"叙事，不是推翻 D086
- QW b2_fix 只跑了 s020 和 s025（Director 决策：其他条件不跑，截断影响可忽略 <1pp）
- batch1 v2 rescore 已全量完成，所有条件 accuracy unchanged，数据已可信

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162 (connect.westd.seetacloud.com)，root 账号
- 工作目录：/root/autodl-tmp/pacs
- Python：aml-train 镜像，conda base 环境（/root/miniconda3/bin/python）
- 活跃进程（截至 handoff 时）：
  - cuda:0: acc_ds_s015_8k_v2 (pid 287691) — 44/50 进度，接近完成
  - cuda:2: acc_ds_s030_8k_v2 (pid 288901) — 24/50 进度
  - cuda:1/3: 空闲（gsm8k 和 s025 已完成）

### 3. 📊 当前状态
**已完成关键结果**：
- QW dose curve (n=100, final): dense=0.40, s015=0.36, s020=0.36, s025=0.33, s030=0.19 ✅
- C10 GSM8K random masking: s025_v2 PASS, s030_v2 PASS ✅ — compound interaction 与 masking strategy 无关
- DS 8k: dense=0.74(16%截断), s020=0.30(58%), s025=0.08(76%) ✅
- DS s015 interim: ~44%(极少截断), DS s030 interim: ~9%(大量截断)

**仍在跑**：
- acc_ds_s015_8k_v2 (cuda:0) — 接近完成，预计很快
- acc_ds_s030_8k_v2 (cuda:2) — 约一半进度

**QUEUED**: 无

**等待**：DS s015 + s030 完成后 → 5-point DS dose curve 完整 → 编译数据 → Round 10 审稿

### 4. 📋 待办
- DS s015 完成 → 提取结果，更新 registry，确认非截断准确率
- DS s030 完成 → 同上
- 两者都完成 → 编译完整 DS 8k dose-response table（含截断率 + 非截断准确率分解）+ QW final dose curve → consistency check → 准备 Round 10 审稿材料
- Round 10 数据编译后 → 检查 experiment_plan.yaml（当前为空，Reviewer warning）
- cuda:1/3 空闲 → 如有新实验需求（post-Round-10 ablation）可立即分配；目前无 QUEUED 实验

### 5. 🎯 战略上下文
- 项目核心发现：compound sparsity interaction 是 sparsity 固有属性（C10 证实 random masking 同样存在），DS reasoning model 对 pruning 敏感度远超 QW（DS -44pp @ s020 vs QW -4pp）
- DS 数据的双重退化模式（Reviewer 发现）：s020→s025 不仅截断加剧，**非截断样本推理质量也断崖下降**（71.4%→33.3%），论文可强调这个 compound failure mode
- DS dense 8k=0.74 vs QW dense=0.40：reasoning model 在充足 token budget 下远强于 QW，但 pruning 抹平甚至反转差距（s030: DS 0.08 vs QW 0.19）——好的 paper story
- 距 EMNLP 截稿约 10 天，审稿阶段已启动（Group C 并行处理）
- GPU 1 多次被 Reviewer flag 空闲——下一轮注意及时回填或明确说明原因
- experiment_plan.yaml 为空是治理债务，Reviewer 已 warning，完成 DS dose curve 后应建最小版本


---
