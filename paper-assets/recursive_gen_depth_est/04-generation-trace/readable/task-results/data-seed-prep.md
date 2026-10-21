# data seed prep

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_seed-prep_20260514T095557_result.json`
- **Structured JSON:** [`0b24f1fefabf94056e01.json`](../../sessions/0b/0b24f1fefabf94056e01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

种子数据准备完成。

### 产出报告

| 项目 | 值 |
|------|-----|
| 数据来源 | Wikipedia (wikimedia/wikipedia, 20231101.en) |
| 样本数量 | 5000 条 |
| Token 范围 | min=256, max=512, mean=491 |
| 文件路径 | `/root/autodl-tmp/recursive_gen_depth_est/data/depth_0.jsonl` |
| 文件大小 | 11MB |
| 全部 depth=0 | Yes |

**Token 长度分布：**
- 256-299: 131 (2.6%)
- 300-399: 344 (6.9%)
- 400-499: 310 (6.2%)
- 500-512: 4215 (84.3%)

大部分样本被截断到 512 tokens（Wikipedia 文章通常较长），符合预期。

**前 2 条样本预览（截断）：**
1. "Anarchism is a political philosophy and movement that is skeptical of all justifications for authority..." (512 tokens, wikipedia)
2. "Albedo is the fraction of sunlight that is diffusely reflected by a body..." (512 tokens, wikipedia)

---
