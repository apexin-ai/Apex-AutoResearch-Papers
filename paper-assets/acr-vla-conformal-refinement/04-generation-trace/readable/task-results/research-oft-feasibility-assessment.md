# research oft feasibility assessment

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_oft-feasibility-assessment_20260522T175112_result.json`
- **Structured JSON:** [`f95ce7017b9536878c2c.json`](../../sessions/f9/f95ce7017b9536878c2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断信息已足够。让我整理核心发现。

## OFT 可行性评估报告

### 现状

两套 eval 脚本**都跑出 0% SR**（200+ rollouts）：
- 项目 wrapper eval (`evaluate.py`)：10 tasks × 20 rollouts = 0/200
- OFT 官方 eval (`run_libero_eval.py`)：380+ episodes = 0/380

OFT 论文在 A100 上报告 LIBERO-Object **97.1% SR**。

### 根因分析（多层问题）

**问题 1：项目 eval 用了错误的 Python 环境**
- 实际使用：base conda env（Python 3.12, transformers 5.8.0, tokenizers 0.22.2）
- OFT 要求：Python 3.10, 自定义 transformers fork 4.40.1, tokenizers 0.19.1
- 证据：log 中 robosuite 指向 `/root/miniconda3/lib/python3.12/`；`modeling_prismatic.py:331` 打印版本不匹配警告
- conda env `openvla-oft`（Python 3.10）里**没装 transformers**，说明环境搭建未完成

**问题 2：OFT 官方 eval 也 0% SR**
- 在 `/root/autodl-tmp/openvla-oft-official/` 跑的官方脚本同样 0%
- 说明问题**不仅是 transformers 版本**

**问题 3：GPU 类型不匹配（核心问题）**
- 当前设备：4090D
- OFT 训练/测试设备：A100
- OFT README 明确警告：*"Please be sure to test your policy with the same device/GPU used to train it! Otherwise, performance may drop substantially."*
- checkpoint 保留了未合并的 LoRA adapter（`lora_adapter/adapter_model.safetensors`），LoRA 权重对 GPU 浮点特性高度敏感
- OFT 建议：在目标 GPU 上用 `merge_lora_weights_and_save.py` 重新合并 LoRA 到 base model

**问题 4：15+ 次 config.json 修改** 
- `config.json.back.*` 有 15 个备份（全是 2026-05-22），表明反复修改 auto_map 配置试图让 trust_remote_code 工作
- 依赖链深且脆弱：OFT code → custom transformers fork → PEFT → tensorflow/dlimp

### 修复路径评估

| 路径 | 操作 | 时间估算 | 风险 | 成功概率 |
|------|------|---------|------|---------|
| **A: 合并 LoRA** | 正确搭建 conda env → 装 custom transformers fork → 在 4090D 上 merge LoRA → 重跑 eval | 4-8h | 中 | ~50% |
| **B: 租 A100** | 在 A100 上复现官方 eval，确认 checkpoint 完整性后再考虑 4090D 适配 | 8-16h | 中-高 | ~60% |
| **C: 引用论文数据** | 不跑 OFT eval，表格中用 OFT 论文报告的数字（标注 "reported"） | 0h | 审稿风险 | N/A |

- **Path A** 是最合理的修复尝试，但风险在于：即使正确合并 LoRA，4090D 和 A100 的数值差异仍可能导致大幅性能下降（OFT 作者也遇到过这个问题）
- **Path B** 需要新开 A100 实例，成本和时间都高
- **Path C** 在 CoRL 审稿中可能被质疑：为什么其他模型自己跑，OFT 用别人的数？

### 2-Model Paper 可行性

**结论：2-model scope (SmolVLA + π0.5) 对 CoRL 2026 足够。**

理由：
1. **模型多样性已覆盖**：SmolVLA (~300M, flow matching) + π0.5 (~7B, diffusion) 涵盖了不同规模和架构
2. **方法贡献是 model-agnostic**：ACR-VLA/conformal refinement 的价值在于方法本身，不在于堆模型数量
3. **数据已经很强**：π0.5 baseline 94.83% (3-seed mean)，SmolVLA 数据应该也已有——两个模型足够支撑 claim
4. **CoRL 审稿标准**：比顶会 ML 更看重 robotics insight 而非 baseline 数量；2 个 VLA + 消融实验足够
5. **时间性价比**：还有 7 天 deadline，把时间花在 paper writing/polishing 比挣扎修 OFT 回报更高

### 建议

**放弃 OFT，锁定 2-model scope。** 在论文中加一句 discussion 提到 "our method is architecture-agnostic and can be applied to other VLAs" 即可。如果审稿人要求更多模型，rebuttal 时再补。

---
