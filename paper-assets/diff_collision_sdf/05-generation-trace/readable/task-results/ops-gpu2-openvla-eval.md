# ops gpu2 openvla eval

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu2_openvla_eval_20260525T224420_result.json`
- **Structured JSON:** [`38bb179de788fed8566c.json`](../../sessions/38/38bb179de788fed8566c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认了。汇报结果：

## 问题汇总

### 1. OpenVLA 模型下载不完整

模型目录 `/root/autodl-tmp/openvla-7b-raw/` 只有 **权重文件和基础配置**：
- `model-000{1,2,3}-of-00003.safetensors` — 权重看起来完整（6.5G + 6.5G + 1.1G ≈ 14.1G，与 index 标称 ~14.05G 吻合）
- `config.json`, `generation_config.json`, `model.safetensors.index.json`

**缺失关键文件**（无法加载模型）：
| 缺失文件 | 用途 |
|----------|------|
| `configuration_prismatic.py` | 自定义 Config 类（`auto_map` 引用） |
| `modeling_prismatic.py` | 自定义模型架构（`OpenVLAForActionPrediction`） |
| `tokenizer.json` / `tokenizer.model` / `tokenizer_config.json` | 分词器 |
| `special_tokens_map.json` | 特殊 token 映射 |
| `preprocessor_config.json` | 图像预处理 |

`.aria2` 残留文件表明下载工具只拉了 safetensors + json，漏掉了 `.py` 和 tokenizer 文件。

### 2. Eval 脚本不存在

`eval_safelibero_openvla.py` 不存在。现有脚本：
- `eval_safelibero.py` — pi0 系列（baseline/a1/a3）
- `eval_pi05_safelibero.py` — pi0.5（websocket client）

两者都依赖 openpi 框架，OpenVLA 使用完全不同的推理管线（HuggingFace `AutoModelForVision2Seq` + 离散 action token），需要新写。

### 3. GPU 2 状态

GPU 2 空闲（0MiB, 0%），可用。GPU 0 和 GPU 3 被占用。

---

**需要的操作**：
1. **补全模型下载** — 从 HuggingFace `openvla/openvla-7b` 重新下载缺失文件（~几 MB 的 .py + tokenizer 文件），或重新完整下载
2. **编写 `eval_safelibero_openvla.py`** — 基于现有 eval 框架，替换模型加载和 action 推理部分

是否继续执行这两步？

---
