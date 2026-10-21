# director / loop_4.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`357da50da0dce3889d0e.json`](../../sessions/35/357da50da0dce3889d0e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-15T11:29:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU: westb-13313 上 2× RTX 5090 (cuda:0, cuda:1)，不可使用其他服务器 GPU
- paper_framing.md 的数据源声明：主文只引用 plan-012-full (11 tasks / 245 eps) [A]，prescreening 30-task 数据 [B] 仅 appendix。绝不引用 death_decomposition_report.json（文件名误导，实际是 30-task 数据）
- 绝不引用 results/plan_c_test_labels/implicit_sft.jsonl（标签损坏，no-preference→internal 映射错误）
- MATH framing 必须用 "directionally outperforms"（+4.3pp, p=0.079 未达显著性），禁止称 "significantly"
- Llama cross-model 定位为 "preliminary directional evidence"，禁止做 performance 对比（Llama 太弱）
- Introduction 的 router balanced accuracy 用 ~58% 或 57-59% 区间，不写具体 57.6% 或 58.1%

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313 (connect.westb.seetacloud.com)，root 用户
- 工作目录：/root/autodl-tmp/simgate-modular-routing
- Python：AutoDL aml-train 镜像，conda base 环境，/root/miniconda3/bin/python
- 模型路径：Qwen2.5-7B-Instruct + Qwen3-1.7B (router) + Llama-3.1-8B-Instruct 在 /root/autodl-tmp/ 下
- 论文本地路径：projects/simgate-modular-routing/docs/paper/（main.tex + 各章节 .tex）
- 活跃进程：无。所有实验已完成，GPU 空闲

### 3. 📊 当前状态
**刚完成**：Long paper 全部章节扩写 + cosmetic 修复 + 编译验证。12 页 PDF（8 body + 2 refs + 2 appendix），0 errors / 0 undefined refs / 0 overfull >10pt。

**已提交**：fresh long paper review（apr_20260515T104409_t4pu），等待用户确认 review mode。

**刚派给 Agent**：3 个并行任务利用空闲 GPU——(1) 扩展 Llama cross-model 到 5-6 个 high-death tasks / N=35-40 pairs（GPU0），(2) plan-005 routing pattern 分析（CPU-only），(3) plan-010 cross-task transfer（GPU1）。Agent 刚收到指令（om_x100b6f447b494cacc37abd7ed8a6516），尚未回复。

**Registry RUNNING/PREPARING**：无。全部 DONE。

**等待中**：Agent 回复（Llama 模型状态 + pipeline 可复用性评估）；用户确认 fresh review 审批。

### 4. 📋 待办
- Agent 回复 Llama 模型就绪 → 审批 Llama 扩展实验 + allocate GPU0
- Agent 回复 plan-005 分析结果 → 评估是否加入论文作为 temporal analysis figure
- Agent 回复 plan-010 cross-task transfer → 评估是否值得加入 paper（strengthens C2）
- 用户确认 fresh review → review 自动启动，等审稿报告
- 收到审稿报告 → 必须 Read `review-report-action.skill.md`，按 Holistic Pass + Per-Comment Action Matrix 处理（禁止"已知悉"式回复）
- Llama 扩展实验完成 → 更新 experiments.tex §4.4 + paper_framing.md C3 + 重新编译
- 所有实验/修复完成 → 再提交一轮 review（recommend continue mode）
- 终稿确认 → 5/23-24 准备 ARR 提交材料

### 5. 🎯 战略上下文
**核心发现**：Death avoidance accounts for ~90% of routing signal on ScienceWorld (DAF=90.41%, r=0.9698)。贡献是 empirical finding + diagnostic methodology，不是 router architecture。

**决策链关键节点**：
- D050: Short→Long paper 升级（用户指令"目标是投main，long paper"）
- D053: MATH clean N=300 最终数据（+4.3%, p=0.079, borderline）
- D054→D055: Llama 方向一致性修正（Reviewer 初报 "方向反转" 是误判，D055 纠正为 "方向一致"）
- D013: 不再 claim "selective > unconditional"，router ≈ always-det 本身就是 finding
- D014: Keyword routing 结构性失败（ScienceWorld 用 generic verbs 不是 science keywords）

**最容易判断错的事**：
1. Llama cross-model 不是 performance comparison，是 mechanism verification（Llama 太弱，大部分 score=0）。只看 death pattern 方向是否一致
2. MATH 是 negative contrast（internal > code），不是 positive validation。Label distribution inversion (30:17 vs 9:86) 是独立的强证据线，不依赖 p 值
3. 论文里 57.6% vs 58.1% 是不同测量：57.6±0.5% 是 ablation retrain (plan-013)，58.1±0.8% 是 4-seed mean (plan-004)。正文用区间 "57-59%" 回避冲突
4. Formula (3) 用 ≈ 不是 =，残差 0.23 来自 death-asymmetry episodes 中存活策略的非零分
5. 论文 Related Work 引用了 4 篇 2026 concurrent works（CogRouter, ARES, when2tool, tool-use-tax），审稿人可能要求更新引用信息


---
