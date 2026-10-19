# ops verify plan002v3 and prep plan001

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_plan002v3_and_prep_plan001_20260521T130632_result.json`
- **Structured JSON:** [`297df68040f19b7287c0.json`](../../sessions/29/297df68040f19b7287c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Part A: plan_002_v3 — DEAD

**进程 934594**：不存在。`extract_activations` 进程也不存在。

**GPU 状态**：4× RTX PRO 6000 Black (96GB each)，全部空闲（0% 利用率，0MiB 显存）。无 GPU 进程。

**崩溃原因**（日志末尾）：
```
File "extract_activations.py", line 228, in load_model
    max_memory = get_balanced_memory(
File "accelerate/utils/modeling.py", line 1019, in get_balanced_memory
    if set(no_split_children.keys()) == set(no_split_module_classes):
TypeError: unhashable type: 'set'
EXIT_CODE=1
```
模型解压完成（5076/5076），权重加载完成（8237/8237），在 **dispatch 到 4 GPU 时**因 accelerate 库 bug 崩溃。`no_split_module_classes` 中包含不可哈希的 set 类型。

**服务器上仍在运行的进程**：
- PID 47972: `probing_controls_v2.py`（08:56 启动，CPU 97.2%，纯 CPU 运算）
- PID 322679: `compute_cka.py`（19:04 启动，CPU 2978%，CKA bootstrap 运算）

两者均不占 GPU，**4 卡完全空闲可用于 plan_001**。

---

## Part B: plan_001 准备状态

**Qwen3 模型**：32/32 shards 完整，config.json 存在（1.3K）。

**run_plan_001.sh**：存在，完整 pipeline：
1. 检查 GPTQ 依赖（auto-gptq / gptqmodel）
2. 验证模型（32 shards + tokenizer）
3. `extract_activations_large.py` 提取 activations（20 langs × 24 layers，`--quantization none` 让 HF 自动检测 GPTQ config）
4. 创建 train/eval split symlink 目录
5. 训练 English probes
6. Transfer evaluation（zero-shot, mean-shift, Procrustes, few-shot）

**GPTQ 支持**：
- `extract_activations.py`（plan_002_v3 用的，已崩溃）：有 GPTQ auto-detect 和 compressed-tensors 检查，但撞上 accelerate `get_balanced_memory()` bug
- `extract_activations_large.py`（plan_001 用的）：专为大模型设计，提及 Qwen3-235B。quantization 走 bitsandbytes 路径，`--quantization none` 时由 HF 自动处理 GPTQ。**可能不走同一个 `get_balanced_memory` 调用，但需要注意同一 accelerate 版本是否有类似问题**

**磁盘空间**：

| 项目 | 数值 |
|------|------|
| /root/autodl-tmp 总容量 | 350G |
| 已用 | 252G (72%) |
| 可用 | **99G** |
| activations/ 当前 | 4.0K（空） |

**磁盘预估**：Qwen3-235B hidden_dim 约 4096~7168，24 layers × 20 langs × ~14K samples × hidden_dim × 2 bytes (bfloat16) ≈ **55~96GB**。99GB 可用空间**偏紧**，如果 hidden_dim 较大或存 float32 可能不够。

---

### 关键风险和下一步建议

1. **accelerate bug 是 plan_001 的首要风险**：`extract_activations_large.py` 的 `load_model` 如果也调用了 `get_balanced_memory`，会撞同一个 bug。建议检查 `extract_activations_large.py` 的模型加载逻辑，或升级 accelerate（`pip install -U accelerate`）。
2. **磁盘空间偏紧**：建议先确认 Qwen3 hidden_dim（从 config.json），精确计算后决定是否需要清理空间。
3. **4 GPU 完全空闲**，可以立即启动 plan_001（在 accelerate bug 修复后）。

---
