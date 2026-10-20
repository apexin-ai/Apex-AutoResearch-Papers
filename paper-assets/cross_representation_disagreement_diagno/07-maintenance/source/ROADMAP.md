# cross_representation_disagreement_diagno — Research Dashboard

> 最后更新: 2026-05-15 07:18 UTC | 更新原因: Dream #1 分析完成，识别结构性问题，更新 framing/plan，启动 re-dream

## 核心方向
跨表征分歧作为诊断信号：同一 LLM 将推理问题形式化为两种可执行表征（FOL/Z3 vs Python），分歧模式以 ~87% 精度检测形式化错误，支持错误分类、定位和选择性修复。详见 paper_framing.md。

## 当前阶段：Research Phase — Dream 迭代中

**MVP 已通过（D009）**：C1=39.6%, C2=86.8%, C3=4 types, C4=+4.65pp (non-sig), C5-committed=94.6%/C5-coverage=53.0%

**Dream #1 结果（D013）**：三档均 3/6 (borderline/weak reject)，未达 best≥weak accept 门槛。
识别 5 个结构性问题：(1) Related work 不足 (2) 引用不完整 (3) Error taxonomy 未验证 (4) Novelty claim 过强 (5) 缺 self-consistency baseline。
已修改 framing+plan，re-dream 进行中 (dream_20260515T071730)。

**投稿目标**：EMNLP 2026 Main (ARR May 25, DDL 10 天)

## 实验计划覆盖率
P0: exp-001✅ / exp-002 / exp-003(pilot running) / exp-004 / exp-005 / exp-007↑ / exp-012(new)
P1: exp-006 / exp-008 / exp-009 / exp-013(new)
P2: exp-010 / exp-011

## 近期任务
- [ ] 等待 re-dream (dream_20260515T071730) 结果 → 达标后批准 P0 实验
- [ ] ProofWriter pilot 运行中 (PID 84823) → 等结果决定全量/切 LogiQA
- [ ] Agent 队列深度 4 — 处理 C5 dual output + repair oracle fix
- [ ] exp-012 self-consistency baseline 代码准备（re-dream 通过后立即启动）
- [ ] exp-004 MATH adapter 已准备，等 re-dream 批准
- [ ] [Dream 观察] exp-004 结果出来后评估 FOL+Z3 vs CoT+SymPy 是否需分开分析
- [ ] [Dream 观察] 全 benchmark 实验完成后评估样本量是否需扩大（power analysis 需 ~280）

## GPU 预算
- 本地: autodl-rtx6000pro (1x RTX 6000 Pro) — exp-003 pilot 占用中
- API: ~$130-200 预估（含 exp-002 DeepSeek + exp-012 k=5 sampling）
- 总 GPU 时长: ~42h（原 36h + exp-012 6h）

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D013 | 2026-05-15 | Dream #1 三档均 3/6 (borderline/weak reject)，识别 5 个结构 | exp-012, exp-013, exp-007 |
| D012 | 2026-05-15 | C5 报告双指标：C5-committed (85.4%, 仅明确预测) + C5-coverage | mvp_pipeline_004 |
| D011 | 2026-05-15 | 统一指标为 per-sample 计算；Claim 3 更新为 GT-label-dependent | mvp_pipeline_004 |
| D010 | 2026-05-15 | D008 假设（prompt bug = C4 根因）未获支撑；C4 reframe 为 error | mvp_pipeline_004 |
| D009 | 2026-05-15 | 通过 MVP gate，C4 作为已知弱点进入 research 阶段解决 | mvp_pipeline_004 |
| D008 | 2026-05-14 | repair.py prompt bug 确认为 C4 下降根因，修复后 repair-only 重 | mvp_pipeline_004 |
| D007 | 2026-05-14 | 撤回 v5 closed-world 方案，改为 v5b：保持 3-way 输出但改进 prompt | mvp_pipeline_004 |
| D006 | 2026-05-14 | MVP v2 结果：FOL crash 78%→10%、C4/C5 翻转为 PASS，但 Code  | mvp_pipeline_002 |
| D005 | 2026-05-14 | MVP 第一轮未通过（2/5），根因是 Z3 prompt 质量（78% crash），非假设失败。 | mvp_baseline_001, mvp_pipeline_001 |
| D004 | 2026-05-14 | 回退 qwen3.6-plus → 要求 Qwen3-32B 或同级开源模型，Reviewer cr | — |


