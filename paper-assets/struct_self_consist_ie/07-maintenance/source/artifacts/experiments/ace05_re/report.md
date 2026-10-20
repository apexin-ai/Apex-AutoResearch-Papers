# exp_a3_ace05_re — RE SC Diagnostic: Spec & Code Deliverable Report

## 数据可用性结论

| 数据集 | License | 可用性 | 适合度 |
|--------|---------|--------|--------|
| **ACE05** | LDC restricted | 不可直接下载，需付费 LDC 会员 | 高（NER+RE+EAE 三任务），但 **blocked** |
| **SciERC** | Public (DyGIE++) | ✅ 已集成在 pipeline 中 | **高**——6 entity types + 7 relation types，joint NER+RE |
| **SemEval 2010 Task 8** | CC BY 3.0 | 公开 | 中——仅 sentence-level RE，无 entity span 标注 |
| **TACRED / Re-TACRED** | LDC (付费) | 需 LDC 会员 | 高（41 relation types），但 **blocked** |
| **FewRel** | CC BY-SA 4.0 | 公开 | 中——Wikipedia 域，无 span offset 标注 |
| **DocRED** | MIT | 公开 | 低——document-level，不适合 sentence-level SC |

**结论：使用 SciERC test split 作为 RE 数据源。**

理由：
1. 已在 `data_utils.load_scierc()` 中完整实现，零额外开发成本
2. 有 entity + relation 的 span 标注，与 UIE JSON schema 完全匹配
3. NER 实验已在 SciERC 上跑过，RE 可直接做 cross-task 对比（控制变量）
4. 无 license blocker

## 推荐 RE 数据集

**Primary**: SciERC test split (~551 sentences, 筛选后 ~200-300 有 relation 的实例)

**Future expansion** (如果需要更多数据点):
- FewRel (70K sentences, 100 relation types) — 需写 data loader，适合大规模验证
- 如获得 LDC 权限：ACE05 + TACRED 可作为 cross-domain validation

## Pipeline 复用程度

| 模块 | 复用率 | 说明 |
|------|--------|------|
| VLLMSampler + XGrammar | 100% | UIE_JSON_SCHEMA 已包含 relations 字段 |
| Prompt templates | 100% | `_RE_TEMPLATE` 和 `_TRAIN_ALIGNED_TEMPLATE` 已存在 |
| Output parsing | 100% | `_validate_relations()` 已实现 |
| Span realignment | 100% | 处理 head/tail span |
| Sampling pipeline | 100% | `run_sampling_pipeline(subtask="re")` 直接可用 |
| Fleiss' κ (surface) | 100% | RE surface keys `(head, tail, type)` 已实现 |
| Soft Jaccard | 100% | `_re_soft_jaccard_pair()` 已实现 |
| Oracle best-of-N | 100% | 通过 `per_instance_f1(subtask="re")` |
| `relation_strict_match` | 100% | evaluation.py 已有 |
| `compute_re_f1` | 100% | evaluation.py 已有 |
| Consensus construction | **30%** | NER 版本基于 entity key，需改为 relation key → **已实现 `consensus_construct_re()`** |
| Degeneracy detection | **30%** | NER 版本基于 entity set，需改为 relation set → **已实现 `is_degenerate_re()`** |
| Bootstrap test | **50%** | 需 RE-specific key 提取 → **已实现 `run_bootstrap_re()`** |

**总复用率: ~85%**。仅 consensus construction、degeneracy detection、bootstrap 需要 RE 适配（均已在 `run_re_sc.py` 中完成）。

## 已交付产出

1. **`spec.md`** — 完整实验 spec（数据、prompt、schema、评估指标、F1-F4 定义、GPU 需求）
2. **`prepare_re_data.py`** — 数据准备脚本（SciERC 加载、RE 过滤、few-shot prompt 构建、JSONL 输出）
3. **`run_re_sc.py`** — 推理 + 评估框架（VLLMSampler 采样、RE consensus construction、failure mode 分类、paired bootstrap）
4. **Registry** — `exp_a3_ace05_re` 已注册为 QUEUED

## Blockers

无。SciERC 数据公开可用，pipeline 基础设施完整，代码框架已就绪。

## 下一步（执行时）

1. SSH 到 autodl-5090，确认 SciERC 数据在 `/root/autodl-tmp/` 下
2. 运行 `prepare_re_data.py` 生成 RE test instances
3. 运行 `run_re_sc.py` 启动采样 + 评估
4. 分析 F1-F4 failure mode 分布，与 NER 结果对比
