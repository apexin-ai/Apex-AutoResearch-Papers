# Registry Audit & Dream Simulation Readiness Report

> 生成时间: 2026-05-19 | 项目: gen-depth-contamination

---

## Part 1: Registry RUNNING 实验状态

共 4 个 RUNNING 实验：

| exp_id | server | gpu | pid | updated_at (UTC) | 距今 | 异常 |
|--------|--------|-----|-----|-------------------|------|------|
| exp_code_qwen7b | cqa1-22115 | cuda:1 | 110240 | 2026-05-19 00:31 | <1h | 无 |
| exp_code_mistral7b | (未记录) | (未记录) | (未记录) | 2026-05-18 23:51 | ~1h | ⚠️ spec 缺 gpu/pid/log_path |
| exp_code_llama8b | cqa1-22115 | cuda:2 | 96335 | 2026-05-18 21:45 | >3h | ⚠️ 更新超 2h |
| exp_32b_c4 | westd-42896 | cuda:1 | 44715 (spec) / 14637 (top) | 2026-05-18 07:04 | >17h | 🔴 更新超 17h; 双 PID 冲突 |

### 异常详情

1. **exp_code_mistral7b**: spec 中缺少 `gpu`、`pid`、`log_path` 字段。无法远程验证进程存活。建议补全 spec 元数据。
2. **exp_code_llama8b**: 最后更新 >3h 前。可能正常（depth 生成耗时长），但需 SSH 确认进程存活。
3. **exp_32b_c4**: 最后更新 >17h 前。notes 提到 "Resubmit #2"，有两个 PID（top-level 14637 vs spec 44715），可能是重提交后未清理旧 PID。32B 模型在单卡 4090 上运行极慢属预期，但 17h 无 registry 更新仍需确认。

### ROADMAP 对账

ROADMAP 列出 `exp_code_pythia1b4` 为 RUNNING，但 registry 无此条目（可能已完成或 ID 不一致）。Registry 中 `exp_code_qwen7b` 和 `exp_code_mistral7b` 未出现在 ROADMAP 运行中表格（ROADMAP 上次更新 May 18 22:45，这两个实验在其后启动）。

---

## Part 2: Dream Simulation Readiness Checklist

Dream simulation 定义: 模拟 K* 组合 (arXiv=3, C4=2, Code=2, Wiki=1) 在不同数据集混合比例下的检测效果。

| 前置条件 | 状态 | 说明 |
|----------|------|------|
| 4 域 K* 值确定 | ✅ Ready | arXiv=3, C4=2, Code=2, Wiki=1 已确认 (paper_framing.md, D074) |
| ROADMAP 中有任务条目 | ✅ Listed | "Dream simulation (4 域版本)" 在近期任务中，未完成 |
| experiment_plan.yaml 有计划条目 | ❌ Missing | 无独立 dream simulation 实验条目。仅 exp-006/exp-007 描述中有 "[Dream 行动项]" 引用 |
| paper_framing.md 有 claim/section | ❌ Missing | 无 dream simulation 专属 section 或 claim。C3 (K*-Aware Data Curation) 是最相关 claim，但不包含 4 域混合模拟 |
| 4 域实验数据可用 | ⚠️ Partial | C4/Wiki/arXiv 数据已有完整 depth chain。Code 域 cross-model 实验仍在运行中 (3/4 RUNNING) |
| 模拟代码/脚本 | ❓ Unknown | 未检查是否存在 dream simulation 脚本 |

### 结论

- **可启动条件**: 4 域 K* 值已确定，核心数据（C4/Wiki/arXiv）已就绪。Code 域 Qwen-1.5B 数据已有 (exp_code_qwen1b5 SUCCESS)，cross-model 数据仍在生成中。
- **缺失项**: 需在 experiment_plan.yaml 添加 dream simulation 计划条目，明确模拟参数（混合比例、评估指标、baseline）。paper_framing.md 需决定 dream simulation 结果放在哪个 section（建议作为 C3 的扩展分析或 Appendix）。
- **建议**: 可用现有 Qwen-1.5B 4 域数据先跑 CPU-only 模拟原型，不依赖 RUNNING 实验完成。
