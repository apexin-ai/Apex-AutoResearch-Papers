# agent / loop_23.md

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_23.md`
- **Structured JSON:** [`5c91185cead6176a3b0b.json`](../../sessions/5c/5c91185cead6176a3b0b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 23
reason: idle_timeout
updated: '2026-05-23T20:47:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-32935 cuda:0/1/2/3 + westb-23072 cuda:0/1（共 6 张）。其他 GPU 一律不可用
- westd-29022 已不在 servers 列表中（曾用过但现已移除），不要向该服务器提交任何任务
- westd 网络离线：所有 eval 命令必须带 `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1`，否则 HF datasets HEAD 请求导致崩溃
- MATH-500 eval 必须用 fixed script（D114 决定），旧 eval 数据点全部作废。已完成的 fixed 结果：sft_cka_only_20=27.4%, sft_rasp_alpha1p0_20=21.6%
- grpo_standard_25 checkpoint 丢失，Director 决定不重训，paper 中该格填 '--'
- grpo_random_20_retrain_v3 已被 Director 取消：v2 结果可用（paper 中注明 max_completion_length=512 差异）
- Cron 监控对 eval 实验有误判倾向（无 W&B → 标记 failed）。收到 eval failed 回调时，**先 tail 日志确认是否实际完成**再决定重跑

### 2. 🖥️ 基础设施快照
- **westd-32935**: 4× RTX PRO 6000, 工作目录 `/root/recovery_aware_struct_prune`, Python `/root/miniconda3/bin/python`, conda base 环境（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **westb-23072**: 2× RTX PRO 6000, 同上路径和环境
- 模型/数据盘：`/root/autodl-tmp/recovery_aware_struct_prune/`（checkpoint、results、pruned models 均在此）
- HF cache: `/root/autodl-tmp/.hf_cache`（两台服务器）
- 代码 repo: `/root/recovery_aware_struct_prune`（git, commit ~e6ce5f70）
- 匿名仓库已就绪（65 files, c9a2a2b）
- 活跃进程（7 个 RUNNING eval）：

| exp_id | 服务器 | GPU | PID | 预估剩余 |
|--------|--------|-----|-----|---------|
| eval_math500_grpo_standard_20_fixed | westd | cuda:2 | 142477 | ~0-1h |
| eval_math500_sft_standard_20_fixed | westd | cuda:1 | 145167 | ~0-1h |
| eval_math500_grpo_rasp_alpha1p0_20_fixed | westd | cuda:1 | 145167 | ~0-1h |
| eval_math500_sft_standard_25_fixed | westd | cuda:0 | 159065 | ~4h |
| eval_math500_sft_standard_20_fixed_v2 | westd | cuda:3 | 161691 | 刚启动 ~6h |
| eval_math500_grpo_cka_only_20_fixed | westb | cuda:0 | 321423 | ~4h |
| eval_math500_sft_random_20_fixed | westb | cuda:1 | 322086 | ~4h |

- 活跃 Worker: `worker_code_update_math500_table_script_20260523T204459`（正在更新 MATH-500 表格脚本）
- Cron: 7 个 active（对应上述 7 个 RUNNING 实验的监控）

### 3. 📊 当前状态
**阶段：EMNLP 2026 提交收尾，DDL 5/25（~27h）。**

刚完成：D114 决定重跑所有 19 个 MATH-500 eval（旧脚本有 expression extraction + space normalization bug）。已完成 2/19（sft_cka_only_20=27.4%, sft_rasp_alpha1p0_20=21.6%），6 个正在跑，11 个待启动。

sft_standard_20_fixed v1 在 328/500 crash，已启动 v2 替代。

**PREPARING 队列中关键的待启动 eval（等 GPU 释放）**：
- dose-response α=0.5/2.0/4.0 × SFT（3 个）+ α=0.5 SFT（eval_math500_sft_rasp_alpha0p5_20_fixed 等）
- grpo_rasp_alpha3p0_20_retrain 需先重训 GRPO（checkpoint 被删），然后才能 eval
- eval_math500_grpo_random_20_fixed 依赖 grpo_random_20_retrain 完成（v2 结果可用但需确认）
- eval_math500_grpo_cka_only_25_fixed、eval_math500_grpo_standard_25_fixed

**论文修复全部完成**：floor ablation 附录、数据审计、匿名仓库、C1 scope 修复、新引用验证、Conclusion 扩充、GRPO 超参审计、编译通过。

**等 fixed eval 全部完成后的收尾**：更新 tab_math500.tex 全部数值 → 更新 inline MATH-500 数值 → paper_compile_and_check → submit_paper_to_review → 最终提交。

### 4. 📋 待办（条件触发式）
- 任一 RUNNING eval 的 cron 回调到达 → tail 日志确认完成（防误判）→ 提取 accuracy → `update_registry(conclusion=success, metrics={...})` → 更新 report.md
- westd cuda:1 或 cuda:2 释放（grpo_standard_20_fixed / grpo_rasp_alpha1p0_20_fixed 完成）→ 立即启动待排队的 dose-response SFT eval（alpha0p5/2p0/4p0）
- 全部 19 个 MATH-500 fixed eval 完成 → spawn Worker 一次性更新 `tab_math500.tex` + `experiments.tex:85` + `appendix.tex:110` inline 数值 → `paper_compile_and_check` + `check_paper_consistency` → `submit_paper_to_review` 最终审查
- grpo_rasp_alpha3p0_20_retrain 需要 GPU 来重训（checkpoint 被删），完成后才能跑 eval_math500_grpo_alpha3p0_20_fixed
- Worker `worker_code_update_math500_table_script` 完成 → 检查产出，确认表格更新脚本就绪
- DDL 前若 11 个待启动 eval 无法全部完成 → 汇报 Director 哪些格子可能空缺，讨论是否用已有数据提交

### 5. 🎯 战略上下文
**核心 story**: Pruning criterion shapes recovery capacity。CKA-only >> Standard in reward (4.4×) and accuracy (4.55pp)。Reward-accuracy decoupling: SFT ≈ GRPO accuracy despite vastly different rewards。Dose-response: α=2.0 optimal（inverted-U 曲线）。

**决策链关键节点**：
- D114: 旧 eval 脚本 bug → 全部 19 个 MATH-500 重跑（当前唯一 blocking 项）
- D113: Floor ablation 改为 GRPO-only（已完成）
- D112/D111: C1 scope 修正为 "universal accuracy-reward decoupling"，max |Δ| = 1.34pp
- D109: Dose-response 纯 inverted-U narrative，α=2.0 无争议最优

**易错点**：
1. **Cron 误判 eval 为 failed**——这个项目反复发生（memory.md 记录了至少 3 次）。eval 不用 W&B，cron 检测不到 sentinel → 标记 failed。**必须先 tail 日志**
2. **westd 网络离线**——忘加 `HF_DATASETS_OFFLINE=1` 会导致看起来诡异的 HF repo id 错误
3. **PREPARING 里有大量历史残留**（41 个），绝大多数是旧实验的残骸，不要试图启动它们。只关注 `eval_math500_*_fixed` 系列
4. **grpo_random_20 的 checkpoint 状况复杂**：v1 失败（`--save_only_model` 不支持），v2 用了 max_completion_length=512（与其他方法的 1024 不同），v3 被 Director 取消。paper 中用 v2 结果 + 注明差异
5. **时间极紧**：DDL 5/25，~27h。6 个 eval 各需 2-6h，完成后还有 11 个待启动。GPU 是瓶颈——每完成一个立即启动下一个，零空窗


---
