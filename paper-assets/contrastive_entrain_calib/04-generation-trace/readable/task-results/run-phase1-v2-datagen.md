# run phase1 v2 datagen

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_phase1_v2_datagen_20260518T095023_result.json`
- **Structured JSON:** [`ee952ce0e201cf622e91.json`](../../sessions/ee/ee952ce0e201cf622e91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Step 4: 完整验证结果汇报**

---

### 验证结果总览

**Status: WARNING** | Errors: 0 | Warnings: 25 | Exit code: 1（因 warnings 触发）

---

### 1. Turn 1-2 字符级一致

**0 errors** — Turn 1 和 Turn 2 在 valid/invalid 配对间完全一致：
- turn_1 avg length: valid=137.1, invalid=137.1 (diff=0.0%)
- turn_2 avg length: valid=223.1, invalid=223.1 (diff=0.0%)

---

### 2. Turn 3 A/B 长度差异

**整体平均差异: 1.9%**（valid_correction=319.8 chars, invalid_pressure=313.9 chars）

**25 个 per-pair warnings（>20% 阈值）：**

| Pair ID | Valid (chars) | Invalid (chars) | Diff |
|---|---|---|---|
| math_0003 | 267 | 342 | 25% |
| math_0009 | 203 | 253 | 22% |
| math_0013 | 239 | 315 | 27% |
| math_0016 | 177 | 251 | 35% |
| math_0018 | 181 | 306 | **51%** |
| math_0019 | 210 | 299 | 35% |
| math_0034 | 330 | 253 | 26% |
| math_0038 | 227 | 327 | 36% |
| math_0042 | 372 | 285 | 26% |
| math_0046 | 247 | 314 | 24% |
| math_0052 | 255 | 346 | 30% |
| math_0062 | 205 | 263 | 25% |
| math_0064 | 299 | 231 | 26% |
| science_0080 | 432 | 352 | 20% |
| science_0101 | 328 | 249 | 27% |
| geography_0174 | 375 | 274 | 31% |
| geography_0179 | 279 | 228 | 20% |
| geography_0187 | 337 | 247 | 31% |
| history_0204 | 217 | 303 | 33% |
| history_0226 | 497 | 403 | 21% |
| history_0252 | 235 | 189 | 22% |
| history_0253 | 314 | 388 | 21% |
| commonsense_0259 | 543 | 404 | 29% |
| commonsense_0281 | 268 | 351 | 27% |
| commonsense_0307 | 380 | 291 | 27% |

分布：math 域 warnings 最多（13/25），其余域均较少。

---

### 3. 各域分布

**Domain (pairs):**
- math: 64
- science: 64
- geography: 64
- history: 64
- commonsense: 64

**Evidence strength:**
- strong: 334 (52.2%)
- medium: 260 (40.6%)
- weak: 46 (7.2%)

**Condition:**
- valid_correction: 320
- invalid_pressure: 320

---

### 4. LLM 质量抽检 (n=20)

| 检查项 | 通过率 |
|---|---|
| ground_truth_correct（ground_truth 正确性） | **100%** |
| wrong_answer_plausible（wrong_answer 合理性） | **80%** |
| correction_valid（Turn 3A 指向正确答案） | **100%** |
| pressure_misleading（Turn 3B 指向错误答案） | **100%** |
| turn3_balanced（A/B 结构匹配） | **100%** |

---

### 5. Exit code

**1**（因存在 25 个 warnings，但 0 errors）

---

### 6. 生成总对数

**320 对 (640 条记录)**，目标完成。

---

### 总结

核心质量指标全部达标：Turn 1-2 完全一致、LLM 质量检查 ground_truth 100%、correction/pressure 方向性 100%。主要问题是 25 个 pair 的 Turn 3 长度差异超过 20%（集中在 math 域），整体平均差异仅 1.9%。evidence_strength 分布偏向 strong/medium，weak 仅占 7.2%。

---
