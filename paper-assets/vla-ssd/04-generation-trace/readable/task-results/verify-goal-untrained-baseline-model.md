# verify goal untrained baseline model

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_goal_untrained_baseline_model_20260521T110241_result.json`
- **Structured JSON:** [`23079bb26451ea52ec31.json`](../../sessions/23/23079bb26451ea52ec31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，汇总结论。

---

## 结论

### 1. `untrained_libero_goal/goal_classification/` 加载的是 **openvla-7b**（OXE 预训练 VLA），不是 raw Llama-2

**证据链：**

| # | 证据 | 来源 |
|---|------|------|
| 1 | 服务器无 raw Llama-2 checkpoint。`/root/autodl-tmp/vla-ssd/checkpoints/` 只有 `openvla-7b`（32层）作为唯一的 Llama-2 架构 ckpt | `ls checkpoints/` |
| 2 | Object pipeline 显式声明 `UNTRAINED_CKPT = openvla-7b` | `libero_object_full_pipeline.py:29` |
| 3 | 对应 trained ckpt `openvla-7b-finetuned-libero-goal` 存在 | `ls checkpoints/` |
| 4 | Untrained goal classification L1-L32 准确率 99.71%-100%。random init 在 32 层随机变换后不可能维持 99%+ | `summary.csv` |
| 5 | `openvla-7b/config.json` 确认 `hf_llm_id: meta-llama/Llama-2-7b-hf` | config.json |
| 6 | 全项目 scripts 无任何 `llama` / `Llama` 引用（grep 返回空） | grep |

### 2. "Goal untrained L1=0/32" 来自**不同实验**

`results/attention/l1_attention_untrained_summary.json` 是一个**三条件对比实验**（random init / Llama-2 base / trained OpenVLA），跑在 LIBERO-Goal 数据上：

| 条件 | checkpoint | L1 instruction-dominant | 文件 |
|------|-----------|------------------------|------|
| untrained (random init) | 随机初始化权重 | **0/32** | `attention/l1_attention_untrained_summary.json` |
| llama2base | meta-llama/Llama-2-7b-hf | **~9/32** (text>image) | `attention/l1_attention_llama2base_summary.json` |
| trained | openvla-7b-finetuned | **~25-26/32** | `attention/l1_attention_trained_summary.json` |

这与 `untrained_libero_goal/goal_classification/` 是**完全不同的实验**。Goal classification pipeline 的 "untrained" = openvla-7b（与 Object 一致），attention 三条件的 "untrained" = random init。

### 3. 所有已跑 untrained 实验的 baseline 清单

| 实验 | 架构 | Suite | Untrained 模型 | 备注 |
|------|------|-------|----------------|------|
| libero_object_untrained | OpenVLA (Llama-2-7B) | Object | **openvla-7b** | 脚本明确声明 |
| libero_long | OpenVLA (Llama-2-7B) | Long/10 | **openvla-7b** | 脚本明确声明 |
| untrained_libero_goal (goal_classification) | OpenVLA (Llama-2-7B) | Goal | **openvla-7b** (推断) | 无脚本留存，由证据链推断 |
| attention/ untrained | OpenVLA (Llama-2-7B) | Goal | **random init** | 三条件对比，0/32 |
| attention/ llama2base | Llama-2-7B | Goal | **Llama-2-7b-hf** | 三条件对比，~9/32 |
| nora_goal untrained | NORA (Qwen2.5-VL-3B) | Goal | **qwen25-vl-3b-base** | 脚本明确声明 |
| phi3v_r2_untrained | Phi3V (Phi-3-mini) | Object | **phi3v-base** | 结果目录存在 |

### 关键警告

**memory.md "base LLM OpenVLA (Llama-2) = 0/32" 标注可能有误。** 0/32 实际来自 random init，不是 Llama-2 base。Llama-2 base 在 LIBERO-Goal 上有 ~9/32 instruction-attending heads。如果论文/报告中引用了 "base LLM = 0/32"，需要复核数据来源。

---
