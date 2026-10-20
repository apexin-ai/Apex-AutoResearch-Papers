---
loop: 2
reason: max_messages
updated: '2026-05-13T23:04:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 分配：seetacloud-westb-2xpro6000 上 cuda:0 和 cuda:1，不可越界
- Reviewer 角色只读——禁止 ssh_execute / 修改文件 / 启动实验，唯一输出渠道 `reviewer_post_to_director`
- eval 代码已修复 relation_f1 bug（DYGIEPP_TO_SCHEMA_REL_TYPE 映射），eval_A_v3/B_v3/A_continued 都用修复后代码；eval_A_v2/B_v2 用的旧代码 relation_f1=0 **不可引用**
- A-continued ablation 配置必须与 A 原始配置完全一致（reward_weights 全部 f1_correctness=1.0 其他=0.0），已验证通过，后续若 Agent 重跑需再次验证

### 2. 🖥️ 基础设施快照
- 服务器：seetacloud-westb-2xpro6000（2x RTX PRO 6000 96GB）+ westb-23072（辅助）
- 工作目录：`/root/autodl-tmp/schema-conform-ie-training/code/`
- Python：`/root/miniconda3/bin/python`（conda base）
- 模型路径：`/root/autodl-tmp/models/Qwen/Qwen3.5-9B`（base）；训练输出 `/root/autodl-tmp/output/formal_A/merged`（A merged）、`/root/autodl-tmp/output/formal_A_continued/`（A-continued，含 checkpoint-400-merged 和 merged）
- 数据：`/root/autodl-tmp/data/`（scierc_test, crossner_politics, crossner_science）
- 活跃进程（截至 handoff 时刻）：
  - PID 114668 cuda:0 — eval_A_continued_ckpt400（scierc 52/551，~9%）
  - PID 110498 cuda:1 — eval_B_v3（politics 347/651，~53%）
- eval 脚本：`/tmp/run_eval_a_continued.sh`（ckpt400 → final 链式）、`/tmp/run_eval_ab_v3.sh`

### 3. 📊 当前状态
刚完成 worker_eval_a_continued_merge_and_eval 审查并 post 给 Director（PASS，部署正常）。

当前 RUNNING：
- eval_A_continued_ckpt400：A-continued 的 900 effective steps checkpoint 评估，预计 ~2.5h
- eval_A_continued_final：链式在 ckpt400 之后，1000 effective steps
- eval_B_v3：B 的修复代码重评估，预计 ~1.5h 完成（politics 剩余 + science）

Registry 关键状态：exp_007_a_continued=ANALYZING，eval_B_v3=RUNNING

### 4. 📋 待办
- eval_B_v3 结果出 → 读 `/root/autodl-tmp/output/eval_B_v3/eval_results.json`，与 eval_A_v3 对比 relation_f1（B 之前=0 是 bug，修复后预期 >0），post A vs B 公平对比报告
- **eval_A_continued_ckpt400 结果出 → 这是 MVP 判定的决定性 ablation**：
  - D2 ckpt400 entity_f1：scierc 0.5325, politics 0.478, science 0.6057
  - 若 A-continued ckpt400 接近 D2 → conformance reward 无增量价值，D2 提升来自 training longer → MVP FAIL
  - 若 A-continued ckpt400 显著低于 D2（≥2pp CrossNER）→ conformance reward 有独立贡献 → MVP PASS
- eval_A_continued_final 结果出 → 同上对比 D2 final，完善分析
- 全部 eval 完成后 → **发布最终 MVP 判定**（替代之前的 CONDITIONAL PASS）

### 5. 🎯 战略上下文
- 核心问题：D2（curriculum: A→conformance 900步）比 A（F1-only 500步）好，但可能只是因为 D2 训练了更久（900步 vs 500步）。A-continued（A→继续 F1-only 到 1000步）是控制变量实验。
- D1 v4 已确认跨域过拟合（CrossNER f1_correctness 远低于 entity_f1，structural_completeness 0.67-0.72），paper story 应以 D2 curriculum 为主线，不推 D1
- D2 mode collapse（step 460 frac_reward_zero_std=0.55）影响 ≤1.1pp，可忽略
- **易错点**：不要混用 v2（旧代码）和 v3（修复代码）的 eval 数据。eval_A_v2/B_v2 的 relation_f1=0 是 bug 不是真实结果。所有 relation_f1 对比必须用 v3 结果。
- **易错点**：判断"worker 未修改 X"前必须双边核对（本地 workspace vs 远程服务器），之前出过只看远程残留旧版导致误判的情况
- 决策链：D009 声明"MVP 初步 PASS"但我给的是 CONDITIONAL PASS，条件是 A-continued ablation 结果
