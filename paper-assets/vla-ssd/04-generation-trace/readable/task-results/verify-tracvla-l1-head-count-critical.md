# verify tracvla l1 head count critical

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_tracvla_l1_head_count_critical_20260523T203254_result.json`
- **Structured JSON:** [`0cfe3a3ff66ad5c20f67.json`](../../sessions/0c/0cfe3a3ff66ad5c20f67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整分析结果。

---

## 1. 原始 L1 Instruction-Dominant Head Count

### Per-Suite 分析（较新，2026-05-22）

| Suite | Trained | Untrained |
|-------|---------|-----------|
| Goal | **27**/32 | **32**/32 |
| Spatial | **30**/32 | **32**/32 |
| Object | **30**/32 | **32**/32 |
| Long | **30**/32 | **32**/32 |

分类阈值：`instruction_ratio > 0.5` = instruction_dominant，`< 0.2` = image_dominant，中间 = mixed。
数据来源：`/root/autodl-tmp/vla-ssd/results/tracvla_{suite}/{trained,untrained}/l1_attention_profile.json`

### All-Layer 分析（较旧，2026-05-20）

| Condition | L1 Heads |
|-----------|----------|
| tracevla-phi3v (trained) | **32**/32 |
| phi3v-untrained-base | **28**/32 |

数据来源：`/root/autodl-tmp/vla-ssd/results/attention/phi3v_{,untrained_}attention_profile.json`

---

## 2. Reference 模型身份

脚本明确定义：
```python
TRAINED_CKPT = "/root/autodl-tmp/vla-ssd/checkpoints/tracevla-phi3v/"
UNTRAINED_CKPT = "/root/autodl-tmp/vla-ssd/checkpoints/phi3v-base/"
```
docstring：*"Runs both trained (TracVLA-Phi3V) and untrained (**base Phi-3-Vision**) sequentially."*
JSON model field：`"phi3v-untrained-base"`

**Reference 模型是 Phi-3-Vision (base)，不是 Phi-3-Instruct。**

---

## 3. 矛盾根因

存在**两套独立分析**，方法不同，结论相反：

| | Per-Suite (新) | All-Layer (旧) |
|---|---|---|
| 日期 | 5月22日 | 5月20日 |
| untrained L1 | 32/32 | 28/32 |
| trained L1 | 27-30/32 | 32/32 |
| 结论方向 | 训练**减少**instruction heads | 训练**增加**instruction heads |

同一模型、同一 L1 层，同一个 head_13 在 untrained 上两套分析给出的 instruction_ratio 分别是 **0.6857**（per-suite）和 **0.2227**（all-layer），数值完全不同。原因是两套分析使用了**不同的数据样本集和/或不同的注意力聚合方法**。

---

## 4. 结论：主文和 Appendix 哪个对？

- **主文**说 "reference 32/32 → trained 27-30/32" —— 与 **per-suite 分析一致**（更新更严谨的分析，每个 suite 10个任务 × 50 timesteps × 10 demos）
- **Appendix** 说 "Phi-3-Instruct 28/32 → VLA trained 32/32" —— 与 **all-layer 分析一致**，但有**两个错误**：
  1. **模型名错误**：写了 "Phi-3-Instruct"，实际是 "Phi-3-Vision (base)"
  2. **使用了旧的、已被取代的分析数据**，结论方向与主文矛盾

**主文正确。Appendix 表格需要用 per-suite 数据重写，并修正模型名称。**

---
