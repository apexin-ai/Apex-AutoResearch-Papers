# ops disk cleanup and paper status

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-and-paper-status_20260515T023257_result.json`
- **Structured JSON:** [`ad9efc2cae0dd04a4cd8.json`](../../sessions/ad/ad9efc2cae0dd04a4cd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

### 任务 1：磁盘清理

**磁盘实际状态与描述不符**——已经很健康，无需清理：

| 分区 | 容量 | 已用 | 使用率 |
|------|------|------|--------|
| `/root/autodl-tmp/` | 250G | 82G | **33%** |
| `/` (根分区) | 30G | 9.1G | 31% |

**Outputs 目录明细**：

| 目录 | 大小 | 状态 |
|------|------|------|
| `exp1_isr_b03_s43_r3/` | **31G** (含 16G checkpoint-500) | 受保护，eval 中 |
| `exp1_random_b03_s44_r2/` | **31G** (含 16G checkpoint-500) | 受保护，eval 中 |
| `exp1_random_b03_s43_r2/` | 8K | 受保护，训练中 |
| 其余 9 个目录 | 合计 <17M | 太小，清理无意义 |

- 无 `optimizer.pt` 残留
- 模型缓存 `/root/autodl-tmp/models/`: 16G（不删）
- `/root/.cache/`: 44M

**结论：无可清理内容。** 所有大文件都在受保护目录中，非保护目录合计不到 17M。

---

### 任务 2：论文写作状态

论文在 ACL 模板下，已编译出 main.pdf (455KB)。所有主要章节均有内容：

| 文件 | 行数 | 状态 |
|------|------|------|
| `main.tex` | 41 | 主框架，引用各章节 |
| `abstract.tex` | 10 | 有内容 |
| `introduction.tex` | 32 | 有内容（较短） |
| `method.tex` | 63 | 有内容 |
| `experiments.tex` | 110 | 有内容（最长正文章节） |
| `related_work.tex` | 29 | 有内容 |
| `conclusion.tex` | 20 | 有内容 |
| `limitations.tex` | 12 | 有内容 |
| `appendix.tex` | 442 | 有内容（最大，含详细附录） |
| `references.bib` | — | 15.9KB |
| **总计** | **759 行** | |

配套资源：4 张图（fig1-fig4，PDF+PNG），2 个图表生成脚本，ACL 样式文件。本地目录还额外有 `experiments.md` 和 PDF 页面截图。

---
