# code test gen full

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_test-gen-full_20260514T052735_result.json`
- **Structured JSON:** [`ca7cb37c11848be7b732.json`](../../sessions/ca/ca7cb37c11848be7b732.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已足够。汇总报告：

---

## 全量结果报告

### Phase 1: Pilot (20 条)
- Solution pass rate: **16/20 = 80.0%** (≥80% 阈值，自动启动全量)
- Both correct: 16/20 = 80.0%

### Phase 2: 全量生成
- 目标: 683 条
- 成功生成: **627 条**
- API 失败: **56 条**（原因: 402 Insufficient balance，API 余额耗尽）

### Phase 3: 验证统计

| 指标 | 数量 | 比率 |
|------|------|------|
| 总生成数 | 627 | 627/683 = 91.8% |
| Solution pass | 514 | 514/627 = 82.0% |
| Buggy fail | 496 | 496/627 = 79.1% |
| **Both correct (有效样本)** | **496** | **496/683 = 72.6%** |

**有效样本 496 < 500，低于 73% 产出率预警线。**

### 失败原因分布（131 条无效）
- Solution 测试失败: 113 条（主要是 assertion error: 期望值不正确）
- Buggy code 意外通过: 18 条（测试未覆盖到 bug 点）

### 按 category 分组

| Category | 有效/总计 | 有效率 |
|----------|----------|--------|
| syntax error | 211/260 | 81.2% |
| logic error | 152/196 | 77.6% |
| reference error | 133/227 | **58.6%** |

### 按 level 分组

| Level | 有效/总计 | 有效率 |
|-------|----------|--------|
| easy | 167/205 | 81.5% |
| medium | 223/303 | 73.6% |
| hard | 106/175 | **60.6%** |

### 问题与建议
1. **API 余额不足**导致 56 条未生成，这是有效样本不足 500 的主要原因。如果补齐这 56 条（按 80% 有效率估算 +45 条），总有效样本约 541，可达标。
2. **reference error 类别有效率最低** (58.6%)，主要因为这类 bug 较隐蔽，测试不易覆盖。
3. **hard 题有效率偏低** (60.6%)，assertion error 占多数（LLM 对复杂题目的期望输出判断不准）。
4. 建议：充值 API 后用断点续传补跑剩余 56 条，预计可突破 500 有效样本线。

---
