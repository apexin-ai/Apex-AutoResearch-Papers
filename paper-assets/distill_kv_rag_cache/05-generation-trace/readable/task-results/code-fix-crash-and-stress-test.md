# code fix crash and stress test

**distill kv rag cache** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-crash-and-stress-test_20260514T074814_result.json`
- **Structured JSON:** [`7fdd0d68a698d6188284.json`](../../sessions/7f/7fdd0d68a698d6188284.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全。汇报结果。

---

## 结果汇报

### P0-1: Crash Bug 修复

**根因**：`eval_runner.py` 用 `full_text.index(split_marker)` 做字符串搜索拆分 context/query。`apply_chat_template` 的 Jinja2 模板有 `| trim` 操作，导致某些样本的 question 文本被修改后找不到原始 marker。

**修复**：改用 token-level 拆分。分别用 `apply_chat_template` tokenize 完整 prompt（含 question）和 context-only prefix，通过 token 位置差计算拆分点。不再依赖字符串搜索。

**验证**：10 条样本全部成功拆分，5 条 × 4 config 压力测试无 crash。

### P0-2: 压力测试结果

| Config | Ratio | EM | F1 |
|--------|-------|----|----|
| E | baseline | 0.200 | 0.314 |
| A | 16x | 0.000 | 0.000 |
| A | 24x | 0.000 | 0.000 |
| A | 32x | 0.000 | 0.000 |

Budget=0（无 restoration），16x 起输出已是乱码（`"...................-S........-S-S-S-S"`）。

### 结论：Per-sample PCA 不是唯一根因

Eigenvalue 衰减分析（Sample 0, Head 0）：

| Layer | Top 22 components 覆盖方差 | 99% 方差需要 components |
|-------|---------------------------|----------------------|
| 0 | 90.0% | 54/128 |
| 8 | 69.8% | 89/128 |
| 16 | 77.9% | 83/128 |
| 24 | 78.1% | 100/128 |
| 31 | 75.3% | 106/128 |

6x 压缩（22 active components）只覆盖 **70-90% 方差**，存在 10-30% 信息丢失。Per-sample PCA 并非近乎无损。

**三因素共同导致 config 无差异**：
1. **Per-sample PCA**：最优基底使 6x 压缩覆盖 70-90%（比 shared basis 好但非无损）
2. **20% restoration**：恢复关键 token 的原始 KV，补偿压缩损失
3. **Greedy decoding argmax 不敏感**：logit 微小扰动不改变 top-1 token

16x+budget=0 时，三个保护层全部击穿，质量立即崩塌。

### 建议下一步

1. **扫描有效压缩率边界**：在 budget=0 下测试 ratio=[4, 6, 8, 10, 12]，找到质量开始衰退的拐点
2. **分离三因素**：固定 ratio=8，分别测试 budget=0 vs budget=0.2，量化 restoration 的贡献
3. **考虑 shared PCA basis**：用少量 calibration 样本建共享 PCA basis，测试 6x 下是否出现差异
4. **sampling 解码**：用 temperature=0.6 + top_p=0.9 替代 greedy，放大 logit 差异的可观测性

---
