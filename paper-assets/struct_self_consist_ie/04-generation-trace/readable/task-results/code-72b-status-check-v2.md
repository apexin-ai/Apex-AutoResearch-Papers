# code 72b status check v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_72b_status_check_v2_20260519T085211_result.json`
- **Structured JSON:** [`51eff75cfb62fbd92301.json`](../../sessions/51/51eff75cfb62fbd92301.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

## Server B 72B 推理状态

**GPU**: 4× RTX 5090 全部 100% 负载，vLLM TP=4 运行中

**已完成**:
| 数据集 | samples.jsonl 行数 | 预期 | 状态 |
|---------|-------------------|------|------|
| SciERC | 551 | 551 | **完成** (每行含8个sample) |
| CoNLL2003 | 3,453 | 3,453 | **完成** |

**Signal 分析**: `full_signal_report.json` 已生成，包含 scierc + conll2003 两个数据集的 signal (SJ/FK/LP/EM/VC) 和 baseline 结果。

**FewNERD**: 正在推理中，**尚无输出目录**（fewnerd 目录未创建，说明还在内存中处理）。
- 日志显示进度: **28,536 / 301,184** ≈ **9.5%**
- 速度: ~7,120 toks/s input, ~1,810 toks/s output
- 预估 ETA: ~4-5 小时（日志显示 est. 3h46m-6h35m 波动）
- 进程启动时间: 15:58，已运行约 55 分钟

**总结**:
- CoNLL 推理 **已完成**，signal 计算 **已完成**
- FewNERD 推理 **已开始**，进度约 9.5%，预计还需 ~4-5 小时
- Entity construction 尚未进行（需等 FewNERD 完成后 signal report 更新）
- 进程稳定运行中，无中断迹象

---
