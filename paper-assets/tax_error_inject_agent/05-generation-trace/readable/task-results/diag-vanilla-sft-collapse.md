# diag vanilla sft collapse

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_vanilla-sft-collapse_20260514T105746_result.json`
- **Structured JSON:** [`3157dda2c2807feddad7.json`](../../sessions/31/3157dda2c2807feddad7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**找到根因了。**

## 诊断结论：A + B 复合 — 训练/eval 格式不匹配 + 小数据过拟合

### 关键证据

同一个 vanilla adapter，不同输入格式，行为截然不同：

| 输入格式 | 模型输出 | 正确性 |
|----------|---------|--------|
| **多轮** (和训练一致) | `I need to locate the soapbottle first...` → `go to cabinet 1` | ✅ 正确推理 |
| **多轮中间步** | `take soapbottle 1 from countertop 1` | ✅ 正确执行 |
| **单轮** (eval 实际用的) | `go to toilet 1` | ❌ 直奔目标，跳过找物品 |

三个模型在 **同一个单轮 eval prompt** 上的表现：

| 模型 | 首步输出 | 说明 |
|------|---------|------|
| Base Qwen3-8B | 详细推理 → `go to cabinet 1` | 正确搜索物品 |
| TaxEI SFT | `go to countertop 1` | 正确（soapbottle 常在 countertop） |
| Vanilla SFT | `go to toilet 1` | ❌ 直奔目的地，不找物品 |

### 根因链

1. **训练数据是多轮 messages 格式**：每个 observation 是独立的 user turn，每个 action 是独立的 assistant turn
2. **Eval 是单轮格式**：`build_prompt()` 把历史/观察/admissible actions 拼成一个长字符串，包在单个 user message 里
3. **278 样本 + lr=1e-4** 导致 vanilla 严重过拟合到多轮格式，丧失了处理单轮长 prompt 的能力
4. 面对不熟悉的单轮格式，模型退化为 "直奔目标" 捷径 → 所有需要多步推理的任务全部失败（50 步超时）
5. TaxEI 有 1030 样本（3.7x），过拟合程度较轻，仍能泛化到单轮格式

### Loss 曲线（排除训练崩溃）

| | Vanilla | TaxEI |
|---|---------|-------|
| 起始 loss | 2.13 | 2.23 |
| 终止 loss | 0.63 | 0.46 |
| token_acc | 80.7% | 85.2% |
| 总步数 | 54 | 195 |

Loss 正常下降，没有坍缩到 0。不是训练过程 bug。

### 修复方案

**优先级 1（修 eval，立竿见影）**：改 `ModelInference.generate()` 为多轮格式，把历史 observation/action 作为独立的 user/assistant turns 传入，而不是拼成单个字符串。

**优先级 2（降低过拟合风险）**：lr 从 1e-4 降到 2e-5，vanilla 278 样本用 1e-4 太激进。

**优先级 3（备选）**：反过来改训练数据为单轮格式（和 eval 对齐），但工作量大。

要我现在改 eval 代码吗？

---
