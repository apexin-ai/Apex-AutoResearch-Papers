# diag gsm8k v2 v3 rootcause

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gsm8k-v2-v3-rootcause_20260514T231051_result.json`
- **Structured JSON:** [`a04526aaabac6fe9e55e.json`](../../sessions/a0/a04526aaabac6fe9e55e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全，以下是根因分析结论。

---

## GSM8K v2 vs v3_rrf Gamma 矛盾根因分析

### 1. Exposure 值对比

| Model | v2 exposure | v3_rrf exposure | v2 normalized | v3_rrf normalized |
|-------|------------|----------------|--------------|------------------|
| 0.5B_d000 | 0.000 | 0.000 | 0.00 | 0.00 |
| 0.5B_d005 | 0.016 | 0.000 | 0.08 | 0.00 |
| 0.5B_d025 | 0.065 | 0.021 | 0.33 | **0.69** |
| 0.5B_d100 | 0.197 | 0.004 | 1.00 | **0.12** |
| 1.5B_d000 | 0.000 | 0.000 | 0.00 | 0.00 |
| 1.5B_d005 | 0.016 | 0.014 | 0.08 | **0.44** |
| 1.5B_d025 | 0.065 | 0.005 | 0.33 | **0.16** |
| 1.5B_d100 | 0.197 | 0.031 | 1.00 | 1.00 |

- v2 单调性：0.5B ✓, 1.5B ✓ | Spearman vs oracle = **1.000**
- v3_rrf 单调性：0.5B **✗**, 1.5B **✗** | Spearman vs oracle = **0.700**

### 2. 根因：`load_exp002_signals` 代码在两次运行之间被修改

时间线：
- **06:00–06:22**：v2 运行（使用旧版代码）
- **06:55**：git initial commit（代码已被修改）
- **06:57**：v3_rrf 运行（使用新版代码 = D023/D030 3-signal RRF fusion）

证据：
- v2 baseline = 0.6131（两个 scale 相同）
- v3_rrf baseline = 0.188 (0.5B) / 0.164 (1.5B) — 完全不同的数值范围
- Git 只有 1 个 initial commit，无法追溯旧代码

### 3. 为什么 gamma 差 10 倍

当前代码的 3-signal RRF fusion (S1+S2_flipped+S4) 产生的 per-model mean RRF 几乎是噪声：

```
Raw RRF means: 0.153 ~ 0.209 (range=0.056, 全部在 0.15~0.21 窄带内)
```

D024 delta 减去 d000 baseline 后，微小的正负波动被 clip 到 0，产生完全非单调的 exposure：
- **0.5B: d025 (0.021) >> d100 (0.004)** — d100 反而比 d025 低！
- **1.5B: d005 (0.014) >> d025 (0.005)** — d025 反而比 d005 低！

IRT 模型面对这种自相矛盾的 exposure：
- 被迫把 gamma 推高到 2.1 来放大微弱信号
- 扭曲 theta（0.5B d025: -2.12 vs v2 的 -0.92）
- PPP = 0.0（模型完全无法拟合数据）

### 4. 哪个版本正确（D027 同源 signal 约束）

**两个都有问题**：
- **v2**：exposure 单调，但两个 scale 值完全相同（可疑，暗示旧代码有 scale 处理 bug 或使用了非 scale-specific 的信号）
- **v3_rrf**：3-signal RRF mean 在 model-level 基本是噪声，不能作为 contamination exposure

核心问题是 **per-model mean RRF 不是有效的 contamination proxy**。item-level RRF 能区分被污染和未被污染的 item，但对所有 item 取 mean 后，信号被大量 clean item 稀释（d005 只有 5% item 被污染，mean 几乎不变），导致 model-level 分辨率丧失。

### 5. 建议修复方向

RRF signal 应该用作 **per-item tau**（哪些 item 更可能被污染），而不是 per-model exposure（哪个模型被污染多少）。Per-model exposure 应回退到 oracle dosage 或使用 top-K% RRF 分位数代替 mean。

---
