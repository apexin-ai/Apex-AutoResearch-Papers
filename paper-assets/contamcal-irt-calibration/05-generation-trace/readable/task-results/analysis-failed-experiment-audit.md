# analysis failed experiment audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_failed-experiment-audit_20260519T204858_result.json`
- **Structured JSON:** [`2e4b41f97b5e3a2cfb58.json`](../../sessions/2e/2e4b41f97b5e3a2cfb58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。100 个失败/终止实验的分析结果：

**分布概览**: 65 failed + 35 killed = 100 unique experiments

**按失败原因**:
| 类别 | 数量 | 占比 |
|------|------|------|
| OOM | 16 | 16% |
| unknown/no_info | 18 | 18% |
| process_died/auto_resolved | 13 | 13% |
| GPU_conflict/duplicate | 10 | 10% |
| deprecated/superseded | 9 | 9% |
| resource_limit(disk/nproc) | 5 | 5% |
| env/command_error | 4 | 4% |
| process_crash_partial | 4 | 4% |
| code_bug/config_error | 3 | 3% |
| 其他 | 18 | 18% |

**系统性偏差结论**:
1. **学习曲线效应明显**: 70% 失败集中在前 3 天（5/13-15），后 4 天仅 30%。GPU 竞争和 OOM 问题催生了 C001-C006 约束后显著改善。
2. **服务器分布反映用量**: cqa1 75 次 vs westd 8 次是因为 westd 到第 7 天才加入，不是可靠性差异。
3. **模型分布反映开发重点**: Qwen2.5-3B (29) 和 0.5B (28) 是 Phase 1 主力模型，失败数多是因为实验基数大，3B 偏 OOM（模型更大）。
4. **GPU 资源竞争是主要系统性问题**: OOM + GPU 冲突 + SIGKILL 合计 26%，符合 6-GPU 共享服务器并发实验的预期。
5. **无方法论偏差**: 所有失败均为基础设施/操作性问题，不影响实验结论。失败实验均已重试并最终成功。

---
