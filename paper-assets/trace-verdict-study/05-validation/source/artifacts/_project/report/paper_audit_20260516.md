# 论文初稿审计报告 — 2026-05-16

**项目**: trace-verdict-study  
**目标会议**: EMNLP 2026 ARR (DDL: May 25, 距今 9 天)  
**论文目录**: `docs/paper/`

---

## 1. 章节完成度

| 章节 | 文件 | 完成度 | 关键缺失 |
|------|------|--------|----------|
| Abstract | main.tex L18-25 | 95% | 无 DeepSeek full_trace v3 结果 |
| Introduction | introduction.tex | 95% | 无 DebugBench/trace length ablation 数据 |
| Method | method.tex | 95% | 完整：task def + dataset + trace reps + models + training + loss ablation |
| Experiments | experiments.tex | 85% | 缺 DeepSeek full_trace v3 (79.16%)；缺 trace length ablation；缺 DebugBench |
| Discussion | discussion.tex | 90% | 5 个 subsection 完整；可加 trace length 讨论 |
| Related Work | related_work.tex | 90% | 3 段，引用充分 |
| Conclusion | conclusion.tex | 95% | DebugBench 仅提及为 future work |
| Appendix | appendix.tex | 90% | per-class + training details + examples + full results + irreducible analysis |
| Figures | 3 figures | 90% | fig1 trace overview, fig2 calibration, fig3 cross-model gap — 均有 PDF+PNG |
| references.bib | 存在 | — | 未审查完整性 |

**整体完成度: ~90%**。核心叙事和 claims 已完整。主要缺口是新实验结果的整合。

---

## 2. 新实验结果整合状态

### 2.1 DeepSeek full_trace v3 (acc=79.16%)

- **Registry 状态**: DONE
- **论文现状**: experiments.tex Table 1 中 DeepSeek full_trace 标为 "N/A" + 脚注说明 label truncation bug
- **行动**: 应更新 Table 1, 将 N/A 替换为 79.16%，移除 $^\ddag$ 脚注，改为正常数据行。同时更新 abstract/introduction 中相关叙述。
- **影响**: 补全 cross-model 对比的最后一个空缺，显著增强论文完整性

### 2.2 DebugBench VOTA (acc=99.77%, n=426)

- **Registry 状态**: DONE (debugbench_vota_seed42)
- **论文现状**: 仅在 conclusion.tex L20 作为 future work 提及
- **行动建议**: 
  - 可加入 experiments.tex 作为 "External Validation" subsection（1段 + 1 小表/行内数字）
  - debugbench_exception_only_seed42 为 QUEUED, debugbench_no_trace_seed42 为 RUNNING — 若完成可构成完整 DebugBench ablation
- **优先级**: 中。单个数据点（VOTA only）说服力有限，但 99.77% 与 Qwen VOTA 99.41% 一致，支持 generalization

### 2.3 Trace Length Ablation

| 条件 | 状态 | 精度 |
|------|------|------|
| 256tok | DONE | 78.82% |
| 512tok | DONE | 80.42% |
| 1024tok | RUNNING | — |
| 2048tok | QUEUED | — |

- **论文现状**: 完全未提及
- **行动建议**:
  - 如 1024tok/2048tok 在 DDL 前完成，可加入 discussion 或 appendix 作为 trace length sensitivity analysis
  - 即使只有 256/512 两个点，也可支持 "full_trace 81.76% 与 max_length=2048 吻合" 的论点
- **优先级**: 低-中。不是核心 claim 的支撑，但增加 robustness

---

## 3. D034 叙事一致性检查

**检查项**: 论文是否仍有 "label truncation/corruption" 旧叙事应用于 VOTA（D034 要求修正为 "trace content truncation"）

### 逐文件检查结果

| 文件 | 行号 | 内容 | 状态 |
|------|------|------|------|
| introduction.tex | L24 | "truncating diagnostic trace content while preserving the verdict label" | ✅ 正确 |
| method.tex | L77 | "truncated from the input content while preserving the complete verdict label" | ✅ 正确 |
| experiments.tex | L39 | 明确区分: full_trace "right-truncation removed the verdict label" vs VOTA "preserves the verdict label but truncates the trace content" | ✅ 正确 |
| discussion.tex | L12 | "the verdict label is preserved, but the trace content is truncated" | ✅ 正确 |
| discussion.tex | L19 | "truncating trace content while preserving the verdict label" | ✅ 正确 |
| appendix.tex | L199 | "label truncated (context overflow)" — 针对 DeepSeek full_trace | ✅ 正确（full_trace 确实是 label truncation）|
| main.aux | L1028-1029 | "label truncation bug" — 针对 full_trace 表格标题 | ✅ 正确（full_trace 确实是 label truncation）|

**结论: D034 修正已全面落实。** 论文正确区分:
- DeepSeek **full_trace**: verdict label 被截断 → 训练坍塌 (28.5%, N/A)
- DeepSeek **VOTA**: verdict label 保留, trace content 被截断 → 84.45% (信息损失)

⚠️ **潜在改进**: appendix.tex Table 10 (tab:full_deepseek) 标题仍用 "label truncation bug"，此处仅指 full_trace，语义正确但读者可能误解为泛指。建议改为 "context overflow causing label loss" 以区分 full_trace vs VOTA 截断机制。

---

## 4. Bootstrap 统一方案

### 4.1 当前状况

论文 experiments.tex L7 声明:
> "Pairwise comparisons use paired bootstrap resampling ($B{=}10{,}000$, seed=42)"

但根据 agent_context:
- **Qwen 实验**: 有逐样本预测文件 → paired bootstrap ✅
- **DeepSeek 实验 (VOTA, no_trace)**: 无 save_predictions → 实际用 unpaired bootstrap ⚠️

Registry 检查确认: 所有 16 个关键实验的 outputs 字段均为空 `{}`，无 predictions 文件记录。Qwen 的 predictions 文件可能存在于服务器但未注册到 registry。

### 4.2 需要统一的实验

**同一张表不能混用 paired/unpaired bootstrap。** 统一方案:

#### 方案 A: 全部 paired bootstrap（推荐）

重跑以下 DeepSeek eval（仅推理，无需重训）+ `--save_predictions`:

| 实验 | 模型 | 已有精度 | 预计 eval 时间 |
|------|------|---------|---------------|
| deepseek_vota_seed42 | DeepSeek | 84.45% | ~10 min |
| deepseek_no_trace_seed42 | DeepSeek | 73.36% | ~5 min |
| deepseek_exception_only_seed42 | DeepSeek | 99.33% | ~5 min |
| deepseek_exception_only_seed123 | DeepSeek | 91.09% | ~5 min |
| deepseek_exception_only_seed456 | DeepSeek | 99.33% | ~5 min |
| deepseek_full_trace_seed42_v3 | DeepSeek | 79.16% | ~10 min |

**同时验证 Qwen predictions 文件是否存在**（检查服务器 output 目录）。

**总工作量**: ~40 min GPU 时间 + 脚本准备。**无需重新训练。**

#### 方案 B: 全部 unpaired bootstrap

- 优点: 无需重跑任何实验
- 缺点: 信息损失（unpaired CI 更宽），且需修改论文中已报告的 Qwen paired bootstrap CI
- **不推荐**: 已有 paired 数据降级为 unpaired 是浪费

#### 方案 C: 分表报告

- Qwen 表用 paired，DeepSeek 表用 unpaired
- 在 footnote 中说明
- **可接受但不理想**: 审稿人可能质疑方法不一致

### 4.3 建议

**采用方案 A**。工作量 <1 小时，收益明确:
1. 统一 bootstrap 方法，论文方法学一致
2. 获得 DeepSeek 逐样本预测，可做更细粒度的 error overlap 分析
3. 验证 DeepSeek 结果可复现

---

## 5. 论文交付时间线建议

| 日期 | 里程碑 | 关键动作 |
|------|--------|---------|
| **5/16 (今天)** | 审计完成 | 确认 DeepSeek full_trace v3 可整合；启动 bootstrap 重跑 |
| **5/17** | 数据整合 | 更新 Table 1 加入 DeepSeek full_trace v3 (79.16%)；bootstrap 统一完成；检查 1024tok 结果 |
| **5/18** | 可选数据 | 如 DebugBench no_trace/exception_only 完成，加入 external validation；trace length ablation 整合 |
| **5/19-20** | 文本打磨 | 审查所有表格数据一致性；检查 CI 和 p-value；related work 最终版 |
| **5/21-22** | 内部审阅 | 通读全文；检查 contribution/claim 与 evidence 对应关系；figure 质量 |
| **5/23** | 最终校对 | 格式（ACL 模板）、页数限制、reference 完整性、LaTeX 编译无 warning |
| **5/24** | Buffer | 意外问题处理 |
| **5/25** | 提交 | ARR submission |

### 关键风险

1. **1024tok/2048tok 实验可能未完成**: 如果 DDL 前未完成，论文不纳入 trace length ablation（非核心 claim）
2. **DebugBench 实验部分缺失**: debugbench_exception_only 为 QUEUED — 如果来不及，仅在 conclusion 提 99.77% 作为 preliminary external validation
3. **Bootstrap 重跑失败**: 方案 C (分表) 作为 fallback
4. **DeepSeek full_trace v3 整合需修改多处**: abstract, introduction, experiments Table 1, discussion — 需确保一致性

---

## 6. 立即行动清单

**P0 (今天)**:
- [ ] 在服务器上验证 Qwen experiments 的 predictions 文件是否存在
- [ ] 启动 6 个 DeepSeek eval-only 重跑 with --save_predictions
- [ ] 将 DeepSeek full_trace v3 (79.16%) 整合到 Table 1

**P1 (5/17)**:
- [ ] Bootstrap 统一后更新所有 CI 和 p-value
- [ ] 检查 1024tok 实验结果
- [ ] 更新 abstract/introduction 中 "N/A" 相关叙述

**P2 (5/18-19)**:
- [ ] 评估 DebugBench 数据是否足够加入 main paper
- [ ] Trace length ablation 整合（如数据就绪）
- [ ] Appendix Table 10 标题措辞优化（"label truncation bug" → 更精确表述）
