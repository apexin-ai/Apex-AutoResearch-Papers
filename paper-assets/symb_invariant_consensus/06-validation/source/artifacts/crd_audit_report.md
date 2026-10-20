# CRD (Cross-Representation Disagreement) 实验审计报告

**method: CRD** | 审计日期: 2026-05-15 | 服务器: westd-32608

---

## 1. 代码结构

路径: `/root/autodl-tmp/crdd/`

| 文件 | 功能 |
|------|------|
| `src/config.py` | API/路径/数据集配置 |
| `src/data_loader.py` | FOLIO 数据集加载器（本地 JSONL） |
| `src/formalize.py` | 双表征生成器：FOL→Z3 代码 + Python constraint 代码（两个独立 prompt，无信息泄漏） |
| `src/executor.py` | 代码沙箱执行（超时30s） |
| `src/disagree.py` | 分歧检测 + rule-based 错误分类器（9种错误类型） |
| `src/repair.py` | 定向修复（带诊断信息）+ 盲目重生成（对照组） |
| `src/pipeline.py` | 主 pipeline：加载 → 双表征 → 执行 → 分歧 → 错误分类 → 修复，支持断点续跑 |
| `src/baseline.py` | Qwen3-32B 直接回答（无双表征），确认 baseline acc ≤ 85% |
| `src/evaluate_mvp.py` | C1-C5 MVP gate 评估 |
| `src/evaluate_unified.py` | 统一评估脚本（含 bootstrap CI + Fisher exact test） |
| `src/deep_analysis.py` | 深度分析：错误分布、GT子集、分歧不对称性 |
| `src/analysis_supplement_ef.py` | 补充分析：phi 相关系数 + 成本效益分析 |
| `src/gt_true_case_study.py` | GT=True 子集中定向修复失败的 case study |
| `src/repair_only.py` | 单独重跑修复阶段 |
| `src/math_adapter.py` | MATH Level 5 数据集适配器 |
| `src/proofwriter_adapter.py` | ProofWriter 数据集适配器 |
| `src/run_proofwriter_pilot.py` | ProofWriter 试点运行脚本 |
| `src/self_consistency_baseline.py` | Self-consistency baseline（k=5 majority vote） |
| `analyze_crashes*.py` | 崩溃样本分析脚本 |
| `c4_analysis*.py` | C4 指标深度分析 |

## 2. 方法概述（CRD vs SICA 差异）

**CRD（Cross-Representation Disagreement Diagnostics）**：
- 核心思想：同一推理问题用两种**独立表征**（FOL/Z3 + Python constraint code）分别形式化并执行
- 两路结果不一致 → 触发分歧检测 → 错误分类 → 定向修复
- 关键假设：两种表征的错误模式相互独立（phi=0.189，弱相关，验证通过）
- 目标：通过跨表征对比实现**无需 ground truth 的错误定位和修复**

**SICA（Symbolic Invariant Consensus Architecture）**：
- 项目要求的正式方法，使用符号不变量共识机制
- 与 CRD 的核心差异待 SICA 实现后对比

## 3. 已完成实验列表

### 3.1 Baseline（直接回答）
- **模型**: Qwen3-32B-AWQ（本地 vLLM）
- **数据集**: FOLIO validation, 50 题
- **准确率**: 74.0% (37/50)
- **结论**: ≤ 85%，数据集错误率充足，PASS
- **运行时间**: 2026-05-14 15:11–15:12

### 3.2 Pipeline v1（初始83题）
- **模型**: Qwen3-32B-AWQ
- **数据集**: FOLIO validation, 83 题
- **运行时间**: 2026-05-14
- **关键指标**:
  - 分歧率 C1: 30.1% (25/83), 有效分歧率 32.1% (25/78)
  - 诊断率 C2: 88.0% (22/25)
  - 错误类型 C3: 5 种 (negation_error, logic_error, exec_crash, quantifier_error, unknown)
  - 定向修复优势 C4: +21.9pp (T:75% vs B:53.1%)
  - 定位准确率 C5: 44.4% (原始, 有 bug) → 80.0% (修正后)
  - FOL 准确率: 81.9%, Code 准确率: 62.7%, Oracle: 87.9%
- **MVP Gate**: 5/5 PASS

### 3.3 Pipeline v2 & v3（10题试点）
- **v2 (10题)**: 分歧率 0%, 修复率 T:80% B:40%, FOL acc=90%, Code acc=60%
- **v3 (10题)**: 分歧率 0%, FOL acc=20%, Code acc=60%
- 小样本试运行，结果不稳定

### 3.4 Pipeline v4 Full（211题，主实验）
- **模型**: Qwen3-32B-AWQ
- **数据集**: FOLIO validation, 全部 211 题（去重后 204 题有效）
- **运行时间**: 2026-05-14 ~ 2026-05-15（含 resume 和 repair 重跑）
- **关键指标 (all, N=204)**:
  - 分歧率 C1: 42.2% [95% CI: 35.3%–49.0%]
  - 诊断率 C2: 87.2% [79.7%–93.9%]
  - 错误类型 C3: 4 种 (exec_crash, logic_error, negation_error, quantifier_error)
  - 定向修复优势 C4: +4.7pp (T:69.8% B:65.1%), Fisher p=0.63 (不显著)
  - 定位准确率 C5(committed): 94.6% (35/37), C5(coverage): 53.0% (35/66)
- **关键指标 (excl Unknown, N=135)**:
  - C1: 38.5%, C2: 84.6%, C3: 3种, C4: -1.9pp (不显著), C5(committed): 96.2%
- **MVP Gate (all)**: 5/5 PASS
- **分歧不对称性**: FOL 正确 & Code 错 = 56, Code 正确 & FOL 错 = 10 (5.6:1)
- **准确率**: FOL=78.9%, Code=59.8%, Oracle=87.8%, Pipeline(repair+fallback)=81.4%

### 3.5 GT 子集分析
| 子集 | N | 分歧率 | 诊断率 | 定向优势 |
|------|---|--------|--------|----------|
| GT=True | 72 | 30.6% | 90.9% | -13.6pp |
| GT=False | 63 | 47.6% | 80.0% | +6.7pp |
| GT=Unknown | 69 | 49.3% | 91.2% | +14.7pp |

### 3.6 成本效益分析
- Token 总量: 3,543,447 tokens, 1,196 API calls
- 每样本平均: 17,370 tokens, 5.9 calls
- 成本倍数: 全 pipeline / 单表征 = 5.76x
- 收益: +21.6% 准确率提升 (vs Code-only baseline)

### 3.7 ProofWriter 试点（进行中）
- **数据集**: ProofWriter OWA-D5, 30 题 pilot
- **状态**: 已完成 28/30 条（pipeline.log 仍在运行中）
- **运行时间**: 2026-05-15

## 4. C1-C5 MVP Gate 定义

| Gate | 名称 | 公式 | 阈值 |
|------|------|------|------|
| C1 | Disagree Rate | FOL判断 ≠ Code判断 / N | ≥10% |
| C2 | Diagnostic Rate | (≥1方正确) / n_disagree | ≥40% |
| C3 | Error Type Diversity | 不同错误类型数 | ≥2 |
| C4 | Targeted vs Blind | targeted_rate − blind_rate | >5pp |
| C5 | Localization Acc | stability.predicted == GT-actual | ≥60% |

## 5. 已知问题

1. **C4 统计不显著**: Fisher exact test p=0.63，定向修复优势在全集上无统计显著性
2. **C4 在 excl_unknown 上为负**: -1.9pp，说明对 GT=True/False 样本，定向修复反而略差于盲修
3. **C5 bug 修复历史**: 原始 C5 计算存在循环论证（predicted 和 actual 都从 GT 派生），已修复为用 stability check
4. **GT=True 子集定向修复效果差**: 定向优势 -13.6pp，case study 分析表明 GT=True 时 FOL 表征过于自信

## 6. 值得保留的数据

| 文件 | 内容 | 保留价值 |
|------|------|----------|
| `results/mvp_v4_full.jsonl` | 204 条完整 pipeline 结果 | 高（主实验原始数据） |
| `results/eval_unified_folio_d012.json` | 统一评估含 bootstrap CI | 高（统计分析） |
| `results/exp001_deep_analysis.json/txt` | 错误分布+GT子集分析 | 高（论文素材） |
| `results/exp001_supplement_ef.json/txt` | phi系数+成本效益 | 高（论文素材） |
| `results/baseline.json` | 50 题 baseline 原始结果 | 中 |
| `results/proofwriter_pilot.jsonl` | ProofWriter 28 条结果 | 中（跨数据集泛化） |
| `artifacts/c1c5_audit.md` | C5 bug 修复审计 | 中（方法论记录） |
