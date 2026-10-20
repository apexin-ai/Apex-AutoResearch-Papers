# ssh scp compile paper 20260517

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_scp_compile_paper_20260517_20260517T100450_result.json`
- **Structured JSON:** [`7810b597888583968bdc.json`](../../sessions/78/7810b597888583968bdc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. SCP 同步
- **成功**。`figures/shapley_method_contribution.pdf` 已同步，大小 30,750 bytes。

### 2. LaTeX 编译
| 指标 | 结果 |
|------|------|
| Errors | **0** |
| Undefined citations | **0** |
| Undefined references | **0** |
| Pages | **24** |
| Warnings | **2**（均为 `'h' float specifier changed to 'ht'`，无害） |
| Label(s) may have changed | **无** |

编译干净通过。

### 3. GPU 状态
| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| cuda:0 | 46% | 14,391 / 97,887 MiB |
| cuda:1 | 96% | 27,217 / 97,887 MiB |

- **PID 247554**（Pythia-410M, cuda:0）：✅ 存活
- **PID 249384**（OPT-1.3B, cuda:1）：✅ 存活

两个泛化实验均正常运行中。

---
