# research 14b cwm pilot

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_14b-cwm-pilot_20260520T121236_result.json`
- **Structured JSON:** [`55a9dec83561011e187b.json`](../../sessions/55/55a9dec83561011e187b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件均已在服务器创建完毕。以下是可行性报告核心内容：

---

## 14B CWM Pilot 可行性报告

### 推荐模型: Qwen3-14B (14.8B)
与现有 Qwen3-8B 保持系列一致性。HF 上已发布，支持 thinking/non-thinking 双模式。

### VRAM 估算

| 方案 | 模型权重 | 总 VRAM | 单卡 5090 (32GB) |
|------|---------|---------|------------------|
| BF16 LoRA | ~29.6 GB | ~32-33 GB | ❌ 极度紧张，大概率 OOM |
| **QLoRA 4-bit** | **~7.4 GB** | **~12-14 GB** | **✅ 余量充足** |

### 训练时间估算
- 8B 基准: ~12 s/step @ seq=2048, bs=1, grad_accum=32
- 14B 外推: ~18-24 s/step（模型 1.85x，QLoRA 前向/反向仍过全模型）
- 总步数: 70748 / 32 × 3 ≈ 6633 steps
- **总时间: ~33-44 小时**

### 代码修改需求
`train_repo_cwm.py` 和 `eval_repo_cwm.py` **均不支持 QLoRA**，需添加 ~15 行代码：
1. `from transformers import BitsAndBytesConfig`
2. 新增 `--load_in_4bit` 参数
3. `from_pretrained()` 传入 `quantization_config=BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch.bfloat16, bnb_4bit_use_double_quant=True)`

`bitsandbytes` 已安装在服务器上，无需额外装包。Qwen3-14B 权重需下载（~28GB），脚本中已含自动下载逻辑。

### 结论: **可行**
May 22 GPU 释放后预计 ~1 小时完成前置工作（代码改动 + 模型下载 + dry-run），然后启动 ~40h 训练。

---

**产出清单（均在服务器 `/home/sonny/exec-sim-repair-verifier/`）**：
- `train_14b_cwm_pilot.sh` — 训练脚本
- `eval_14b_cwm_pilot.sh` — 评估脚本（含 unparseable rate + gen_text 长度验证）
- `artifacts/14b_pilot_feasibility.md` — 完整可行性报告

---
