# agent / loop_18.md

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_18.md`
- **Structured JSON:** [`eec543410f928537220b.json`](../../sessions/ee/eec543410f928537220b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: idle_timeout
updated: '2026-05-23T02:42:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：`autodl-5090` cuda:0-3，`autodl-5090-c` cuda:0-3。不可用其他服务器或 GPU
- `exp_fewnerd_pretrained_n32_s42_v2` 正在 autodl-5090 cuda:3 运行（PID 157469），**禁止在该 GPU 上启动其他任务**
- EMNLP 2026 DDL = **2026-05-25**（~2 天），论文修改只剩 n32 结果整合这一步
- n32 实验是 v1 因 UnicodeEncodeError 被 kill 后的重跑，修复已部署在 autodl-5090-c 但 **autodl-5090 的 sampling.py:673 也已修复**（`errors='replace'`），不要重复修
- 多个 PREPARING 实验（mf4v2 系列、B2 系列、A1 spider 等）是历史遗留，DDL 前 **不需要启动**——Director 决策 D243 明确"不追加主要实验"
- Table 44 中 N-scaling 数据必须用 **统一 instance 集 + 统一 greedy baseline**（见 memory.md "N-scaling 关键方法论发现"），不可用独立 greedy

### 2. 🖥️ 基础设施快照
- **服务器**: autodl-5090 / autodl-5090-c，工作目录 `/root/autodl-tmp/struct_self_consist_ie`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，非 venv）
- **模型路径**: `/root/autodl-tmp/models/Qwen2.5-7B-Instruct`（pretrained）；finetuned merged: `qwen3-8b-fewnerd-exp021-merged`
- **数据**: `data/fewnerd/`（37648 instances）、`data/scierc/`、`data/conll2003/`
- **活跃进程**: exp_fewnerd_pretrained_n32_s42_v2, PID 157469, autodl-5090 cuda:3, log `~/runs/struct_self_consist_ie/exp_fewnerd_pretrained_n32_s42_v2.log`
- **Cron**: 1 个活跃 cron 监控 exp_fewnerd_pretrained_n32_s42_v2（reconcile 确认 still running）
- **Worker 池**: 0 running（空）
- **论文**: LaTeX 已编译通过，46 pages total, 0 errors, 主文 ≤8 pages
- **n32 整合模板**: 已准备好 `artifacts/n32_integration_templates.md`（A/B/C 三种模板对应 n32 结果好/平/差）

### 3. 📊 当前状态
- **刚完成**: n16 分析 + 论文整合（MV +4.06pp plateau）、R41 全部 14 项修复 + n16 整合 + 数值修正 + 编译验证
- **RUNNING**: `exp_fewnerd_pretrained_n32_s42_v2`——FewNERD N=32 pretrained Qwen2.5-7B-Instruct，~37% 进度，ETA ~6h（从 ROADMAP 更新时间算起已过约 6h，可能接近完成或已完成）
- **等待**: n32 cron 回调 → 触发分析 + 论文整合 + R41 提交
- **R40 审稿**: pending（14 条全修复，待用户批准审稿卡）；R41 = R40 修复 + n16/n32 整合
- **PREPARING 积压**: 19 个实验处于 PREPARING，均为 DDL 后的后续方向，当前不动

### 4. 📋 待办（条件触发式）
- **n32 cron 回调到达** → spawn Worker 分析结果（MV Δ、degen、sj_rho、capture）→ 按 `n32_integration_templates.md` 选模板（A: MV Δ > +4pp 继续上升 / B: plateau / C: 下降）→ 更新 Table 44 N=32 行 + Discussion → 重编译 → 向 Director 汇报 → 提交 R41
- **n32 失败（进程崩溃）** → 检查是否 Unicode bug 复发 → 如果是新问题，修复后 v3 重跑；如果 Unicode，确认 sampling.py 修复是否生效
- **n32 结果 MV Δ 显著偏离预期**（如 < +2pp 或 > +6pp）→ 检查数据一致性、与 n8/n16 趋势对比，可能需要在 Discussion 中额外说明
- **Director 批准 R41 提交** → 最终编译检查 → 提交 ARR

### 5. 🎯 战略上下文
- **核心论文 framing（D237）**: Self-Consistency for NER 的 Correlation-Selection Gap 诊断框架。三重贡献：QE 信号评估 + 四阶段诊断级联 + entity-level construction。关键 insight = 最优聚合策略是 dataset-dependent
- **Pretrained vs Finetuned 对比是核心叙事**: pretrained MV 3/3 数据集正向（FewNERD +3.9pp, SciERC +1.54pp, CoNLL positive），finetuned MV 3/3 负向。Capability-diversity tension 解释这个翻转
- **n32 是最后一个数据点**: 预期 pretrained FewNERD N=32 MV Δ 在 +3.9pp（N=8）到 +4.06pp（N=16）的 plateau 区间。如果显著上升 → 模板 A（N-scaling gains still increasing）；如果 plateau → 模板 B（确认 diminishing returns）
- **易错点**:
  - N-scaling 数据必须用统一 baseline（不同 N 的独立 greedy 有微漂移）
  - SciERC MV sign flip 已排除（方差大于均值，noise regime）
  - FewNERD 3-epoch vs 5-epoch degen 是非单调的（3-epoch 8.8% < pretrained 11.7%），叙事需要处理
  - R40 审稿卡还没被用户批准，R41 提交取决于 Director/用户动作
- **审稿目标**: Realistic target 3.5（Borderline Conference），当前最高 R1=3.5 / R2=3.0
- **决策链**: D243（不追加主要实验）→ D242（Table 4 透明度修复）→ D241（R40 Action Matrix）→ D237（framing overhaul to diagnostic cascade）


---
