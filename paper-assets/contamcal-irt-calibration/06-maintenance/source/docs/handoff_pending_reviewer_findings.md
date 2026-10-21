# Pending Reviewer Findings — 2026-05-15 (Pre-Reset)

## ⚠️ [CRITICAL — 最高优先级] lora_alpha 全部为 32，D051/D055 前提错误

**Reviewer 独立验证 adapter_config.json 发现**：所有 s123 checkpoint 实际都是 alpha=32，不是命令行指定的 alpha=16。train_sft.py 旧版本存在 bug（DEFAULT_LORA_CONFIG alpha=32 覆盖了 args），后来被修复但旧 checkpoint 已产出。

**连锁影响**：
- **D051（"s123 alpha=16 接受"）→ 废弃**：前提错误，s123 实际是 alpha=32
- **D055（alpha 混用警告）→ 更新**：所有 checkpoint 均为 alpha=32，无混用问题
- **D062/D063（alpha 过滤策略）→ 简化**：不再需要按 alpha 分组，所有数据可直接聚合
- **给 Paper Agent 的 alpha 约束 → 撤回**：已通知 Paper Agent 按 alpha 分组，但实际不需要了

**下一个 session 必须执行**：
1. `log_decision` 废弃 D051，记录"所有 checkpoint 实际 alpha=32"
2. `log_decision` 更新 D055，记录"alpha 混用问题不存在"
3. 通知 Paper Agent：撤回 alpha 分组约束，所有数据可统一处理
4. 通知 Agent：确认所有 s42 checkpoint 也验证 adapter_config.json 中的 alpha 值
5. 修复 git 中 train_sft.py 的 lora-alpha bug，确保 future runs 参数正确

**好消息**：跨种子对比比之前预想更干净，不需要分 alpha 引用。

---

## ⚠️ [CRITICAL] GSM8K d005 s123 异常：63.08% 远超预期

**三重不一致**：
1. 跨种子：d005 s42 = 20.77%，d005 s123 = 63.08%（差 42pp，仅 seed 不同）
2. 跨剂量：d000 s123 = 18.12%，d005 s123 = 63.08%（+45pp，仅 5% 污染）
3. 非单调：d005 (63%) > d025 (52.5%)

**排除因素**：
- evaluate.py 修改时间早于两次 eval，脚本版本一致
- d000/d005/d025 s123 全部使用相同超参（lr=5e-5, alpha=32, r=16, batch=16）
- lr 差异无法解释同一 seed 内的 45pp 跳变

**下一个 session 必须执行**：
1. 用 d005_s123 checkpoint 单独重跑 GSM8K eval，验证 63% 是否可复现
2. 若可复现，检查 sft_dosage_005.jsonl 中 GSM8K 相关样本的 CoT 格式
3. 在调查清楚前，不可将 d005 s123 GSM8K 数据用于 IRT calibration

---

## [WARNING] d000 s123 eval 可能使用旧版 checkpoint

- eval 使用 adapter: `Qwen2.5-3B_d000_s123/lora_adapter`（May 14 08:15）
- registry 中 exp_001_sft_3B_d000_s123 输出到: `Qwen2.5-3B_d000_v2_s123`（May 15 08:02）
- d000 s123 baseline 可能来自不同训练运行
- 需确认 v1 vs v2 checkpoint 差异，或用 v2 重跑 d000 eval

---

## [ACTION REQUIRED] exp_001_eval_3B_d100_s123_para_aligned — Cron 判断请求

CRON 检测到该实验进程已退出，输出目录为空（Reviewer 确认静默失败）。已通过 D063 urgent message 指令 Agent 标 FAILED 并在 cuda:2 重提。

---

## [DONE] Paper Agent writing_plan.yaml 审批 → 已通过

已批准并开始 Step 2 (Plot Generation)。但注意：之前给 Paper Agent 的 alpha 分组约束需要撤回（见上方 alpha 发现）。

---

## [DONE] cuda:4 母进程问题 → D063 urgent message 已发

已通过 urgent_agent_message 指令 Agent 杀 PID 590507（母进程）。

---

## GPU 状态快照 (截至 RESET 前)

| GPU | 实验 | 进度 | 预计完成 |
|-----|------|------|---------|
| cuda:0 | d100 s123 a32 SFT v2 | 37% | +3h |
| cuda:1 | d100 s42 a32 SFT v2 | 41% | +3h18m |
| cuda:2 | d025 s42 a32 SFT (或 d100 para eval 重提) | 刚提交/待提交 | NEW |
| cuda:3 | signals_3B v3 | 提交中 | 4-8h |
| cuda:4 | d000 v3 SFT (需杀 PID 590507 母进程) | 36% | +2h41m |
| cuda:5 | d025 v3 SFT | 54% | +1h47m |
