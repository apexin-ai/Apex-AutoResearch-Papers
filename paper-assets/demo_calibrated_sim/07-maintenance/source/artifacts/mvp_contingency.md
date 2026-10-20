# DemoCalib MVP 预案

## 当前状态

Qwen 2.5 7B + τ-Bench retail (20 tasks)。3-task quick test 结果：
- Baseline: q=0.65, p=0.45 (H1 PASS，但 q 异常高)
- BCP aave_target: q=0.74, p=0.66, completion=0% (H2/H3 FAIL)

---

## 场景 A: BCP 部分成功

**条件**: 全量 20-task 中 H2 pass — 至少一个 BCP variant 将 question_rate 且 politeness_rate 偏差均缩小 ≥30% relative，且 H3 task completion ≥ baseline×0.80。

**行动步骤**:
1. 锁定最佳 BCP variant，记录其行为率 (q, p) 和 completion rate
2. 对最佳 variant 跑 3 次 seeds 确认稳定性
3. 进入 Phase C：准备 DPO 训练数据（用 BCP 成功的行为目标作为 target distribution）
4. DPO LoRA 微调 Qwen 7B，对比 BCP 结果
5. 论文写作：BCP 作为 lightweight baseline，DPO 作为 stronger method，贡献在于对比两种校准路径的 cost-accuracy tradeoff

**论文 framing**: "Prompt-level calibration provides partial control; fine-tuning achieves tighter alignment" — 两种方法形成自然梯度，故事完整。

**时间线**:
- Day 1-2: 全量 BCP 实验 + 结果确认
- Day 3-4: DPO 数据构造 + LoRA 训练
- Day 5: 对比分析 + 论文 results 初稿

---

## 场景 B: BCP 完全失败

**条件**: 所有 BCP variants（含不同 target rate、不同 prompt template）在 20-task 上均 H2 fail，行为偏差缩小 <30% relative 或 H3 completion 崩塌。

**行动步骤**:
1. 记录所有 BCP variant 结果，量化失败程度（偏差缩小比例、completion 下降比例）
2. 分析失败模式：是行为率没变（prompt 被忽略）还是 completion 崩了（行为改变但破坏任务能力）
3. 立即启动 Phase C DPO：
   - 构造 preference pairs：target behavior response (chosen) vs uncalibrated response (rejected)
   - LoRA rank=16, lr=5e-7, 1-2 epochs
4. DPO 结果评估：
   - 若 H2+H3 pass → 论文 story pivot 成功
   - 若 DPO 也 fail → 启动 kill 流程（见下）
5. Kill 流程触发条件：BCP 全 fail + DPO H2 fail → 项目 pivot 或终止

**论文 framing**: "Prompt-level calibration is insufficient for dialect behavior distribution alignment — fine-tuning is necessary." BCP 失败本身是有价值的 negative result，证明 behavioral calibration 不能仅靠 prompting。

**时间线**:
- Day 1: 确认 BCP 全量失败 + 开始 DPO 数据准备
- Day 2-3: DPO 训练 + 评估
- Day 4: 若 DPO pass，写 results；若 fail，执行 kill 决策

**Kill 流程**:
1. 检查是否为检测器问题（场景 C 排查）
2. 若检测器无误，尝试最后一搏：换 target behavior（只校准单维度而非双维度）
3. 仍 fail → 写 negative result report，项目终止或 pivot 到 "calibration hardness characterization"

---

## 场景 C: Baseline 率不符预期

**条件**: H1 fail — baseline question_rate <15% 或 politeness_rate <30%。当前 3-task 显示 q=0.65 反而异常高（Seshadri 论文报告 GPT-4o 仅 18.8%），需要在 20-task 上确认。

**行动步骤**:
1. 全量 20-task baseline 跑完后，检查 q 和 p 的 per-task 分布，找异常 task
2. 检测器诊断：
   - 从 20-task 对话中随机抽 50 条 turn，人工标注 question/politeness
   - 计算检测器 precision 和 recall
   - 若 precision <0.8：检测器 false positive 过高，行为率被高估
   - 若 recall <0.8：检测器漏检，行为率被低估
3. 检测器修复路径：
   - Regex 检测器问题 → 调整 pattern（例如排除 rhetorical questions）
   - Regex 不够 → 换 LLM-based 检测（用 Qwen 7B 本身做 few-shot classification）
4. 若检测器准确但 baseline 率确实异常：
   - 可能原因：Qwen 7B 行为模式与 GPT-4o 本质不同
   - 调整方案 a: 接受不同 baseline，调整 H1 阈值为 Qwen-specific
   - 调整方案 b: 换 user model（Qwen 72B / Llama 70B）验证是否 model-specific
   - 调整方案 c: 检查 τ-Bench retail task 的 system prompt 是否诱导了特定行为

**论文 framing**: 若 baseline 率因模型而异，这本身是发现 — "dialect behavior rates are model-dependent, not task-dependent"，支撑 calibration 的必要性论证。

**时间线**:
- Day 1 上午: 全量 baseline 结果 + 检测器抽样验证
- Day 1 下午: 检测器修复（若需要）
- Day 2: 用修复后的检测器重跑 baseline，确认 H1

---

## 决策树总结

```
全量 20-task baseline
├─ H1 FAIL → 场景 C（检测器诊断，1天）→ 修复后回到 H1 判断
├─ H1 PASS
│  ├─ 跑 BCP variants
│  │  ├─ H2 PASS (≥1 variant) → 场景 A（DPO 对比，Day 3-5）
│  │  └─ H2 FAIL (all variants) → 场景 B（DPO 救场，Day 2-4）
│  │     ├─ DPO H2 PASS → 论文 pivot 成功
│  │     └─ DPO H2 FAIL → kill / pivot
```
