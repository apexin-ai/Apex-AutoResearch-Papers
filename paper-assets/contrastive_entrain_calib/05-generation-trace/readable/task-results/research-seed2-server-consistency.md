# research seed2 server consistency

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_seed2-server-consistency_20260525T151343_result.json`
- **Structured JSON:** [`840564604581894da652.json`](../../sessions/84/840564604581894da652.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Seed2 跨服务器一致性调查报告

### Checkpoint 来源

| Server | 路径 | Checkpoint 列表 | 文件大小/hash |
|--------|------|----------------|--------------|
| westd-29046 | `/root/autodl-tmp/checkpoints/exp003_r3only_seed2/` | 500–8000 (每500步) + final，共17个 | adapter_model.safetensors = 245,405,936 bytes (一致) |
| westd-28034 | ❌ 不可达 (connection refused) | 无法检查 | N/A |

**关键结论：seed2 训练完全在 29046 上从头完成 (training_from_base)，不是从 28034 迁移的 checkpoint。28034 上的 seed2 训练因 OOM 失败，从未产生有效 checkpoint。**

### Eval 数据来源清单（用于 Figure 5）

| ckpt step | eval server | SYCONScore | eval 时间 | 审计状态 |
|-----------|-------------|-----------|----------|---------|
| 500 | westd-29046 | 0.0845 | ~05-20 | ⚠️ 不可审计（无 registry/结果文件）|
| 1000 | westd-29046 | 0.0844 | ~05-20 | ⚠️ 不可审计 |
| 1500 | westd-29046 | 0.1044 | ~05-20 | ⚠️ 不可审计 |
| 2000 | westd-29046 | 0.0846 | ~05-21 | ⚠️ 不可审计 |
| **2500 (旧)** | westd-29046 | **0.1046** | ~05-21 | ⚠️ 不可审计 |
| **2500 (新)** | westd-29046 | **0.1241** | 05-25 | ✅ 完全可审计 (registry) |
| 3000 | westd-29046 | 0.0945 | ~05-21 | ⚠️ 不可审计 |
| 3500 | westd-29046 | 0.0744 | ~05-21 | ⚠️ 不可审计 |
| 4000 | westd-29046 | 0.1430 | 05-22 | ✅ 可审计（结果文件）|
| 7500 | westd-29046 | 0.1241 | 05-23 | ✅ 可审计（结果文件）|
| 8000 | westd-29046 | 0.1240 | 05-23 | ✅ 可审计（结果文件）|

### 环境对比

| 项目 | westd-28034 | westd-29046 |
|------|-------------|-------------|
| 状态 | ❌ 不可达 | ✅ 在线 |
| torch | 无法检查 | 2.12.0+cu130 |
| transformers | 无法检查 | 5.8.1 |
| peft | 无法检查 | 0.19.1 |
| GPU | RTX 5090 32GB | 2× RTX PRO 6000 96GB |
| eval 脚本 | 无法检查 | eval_unified_preset.py (do_sample=False, enable_thinking=False) |

### 结论

1. **是否同一训练 run？** — **是**。所有 seed2 checkpoint 来自 29046 上一次完整训练。
2. **差异来源？** — **不是跨服务器问题，是 eval 可审计性问题**。0.1046 和 0.1241 均来自 29046，但旧值（0.1046）来自没有 registry 记录、没有结果文件的 Agent 临时 session，最可能的原因是旧 eval 使用了不同版本的脚本或参数。
3. **需要在 29046 上重新 eval 的 checkpoint** — **ckpt-500, 1000, 1500, 2000, 2500, 3000, 3500, 4500, 5000, 5500, 6000, 6500, 7000**（所有缺少可审计 eval 结果的 checkpoint）。建议一次性批量 eval 全部 16 个 checkpoint 以获得完整一致的轨迹数据。

报告已写入 memory.md 的"Seed2 跨服务器一致性调查"段落。

---
