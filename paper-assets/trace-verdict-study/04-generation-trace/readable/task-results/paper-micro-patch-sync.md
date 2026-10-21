# paper micro patch sync

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_micro_patch_sync_20260520T060444_result.json`
- **Structured JSON:** [`bdce21d61ebc11120cb6.json`](../../sessions/bd/bdce21d61ebc11120cb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终汇报

### 编译结果
| 项目 | 结果 |
|------|------|
| 编译是否通过 | **通过** |
| 错误数 | **0** |
| 页数 | **21 页**（≤21 ✓） |
| 未定义引用 | **0** |

### 实验进度

| 实验 | PID | 状态 | Accuracy | Fail Recall | Pass Recall |
|------|-----|------|----------|-------------|-------------|
| `deepseek_exception_only_seed123_v2` | 591985 | **已完成** (exit 0) | **99.50%** | 100% | 99.29% |
| `codellama13b_ae_only_seed123` | 583496 | **已完成** | **99.08%** | 100% | 98.71% |

两个实验均已完成，DeepSeek exception_only seed123 v2 达到 99.50% accuracy（较之前 seed123 的 91.09% 大幅改善），CodeLlama-13B ae_only seed123 达到 99.08% accuracy。

---
