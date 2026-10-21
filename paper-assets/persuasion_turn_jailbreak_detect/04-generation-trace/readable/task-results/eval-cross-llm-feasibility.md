# eval cross llm feasibility

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cross-llm-feasibility_20260519T053355_result.json`
- **Structured JSON:** [`61edf70f9be218e7ab81.json`](../../sessions/61/61edf70f9be218e7ab81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 可行性评估

### 可用模型

服务器上**没有**非 Qwen 模型权重。已有模型全部是 Qwen 系列：

| 模型 | 路径 | 大小 |
|------|------|------|
| Qwen3-8B | `/root/autodl-tmp/hf_cache/Qwen/Qwen3-8B` | 16G |
| Qwen2.5-7B-Instruct | `/root/autodl-tmp/hf_cache/Qwen/Qwen2___5-7B-Instruct` | 15G |
| Qwen3-30B-A3B | `/root/autodl-tmp/hf_cache/Qwen/Qwen3-30B-A3B` | 1.7M (不完整/仅 config) |

其他缓存模型为 DeBERTa-v3-base、RoBERTa-base/large、sentence-transformers/all-MiniLM-L6-v2，均为 encoder 模型，不适合做 target LLM。

**无 Llama、Mistral、Gemma 等非 Qwen 模型。**

### 数据生成代码

三套生成脚本架构不同：

| 脚本 | 加载方式 | 模型参数 |
|------|----------|----------|
| `scripts/generate_crescendo.py` | **vLLM API**（`http://localhost:8000/8001`） | 顶部常量 `ATTACKER_MODEL="Qwen/Qwen3-30B-A3B"`, `TARGET_MODEL="Qwen/Qwen2.5-7B-Instruct"` |
| `scripts/generate_deceptive_delight.py` | **transformers 直接加载** | `find_model_path()` 硬编码搜索 Qwen3-8B |
| `scripts/generate_actorattack.py` | **transformers 直接加载** | `find_model_path()` 硬编码搜索 Qwen3-8B |

**支持换 LLM 吗？**
- Crescendo：改顶部两个常量 + 启动对应 vLLM server 即可，**最易改**
- DD / ActorAttack：需改 `find_model_path()` 的 candidates 列表，改造量小（~5 行），但 prompt 模板中无模型相关硬编码，**可行**
- 三个脚本的 prompt 模板、strategy 定义等均与模型无关，换 target LLM 不需要改 prompt 逻辑

**改造难度：低**。每个脚本改 1 个函数 / 2 个常量即可。

### 磁盘空间

| 分区 | 总容量 | 已用 | 可用 | 使用率 |
|------|--------|------|------|--------|
| `/` (overlay) | 30G | 20G | 11G | 65% |
| `/root/autodl-tmp` | **350G** | **53G** | **298G** | 15% |

模型缓存存储在 `/root/autodl-tmp/`，可用 **298G**，下载一个 ~16G 的 8B 模型**完全没问题**。

### 结论

**可行。**

- 需要下载一个非 Qwen 8B 模型（推荐 **Llama-3.1-8B-Instruct** 或 **Mistral-7B-Instruct-v0.3**，均为主流 target LLM，审稿人认可度高）
- 代码改造量极小：每个脚本改 `find_model_path()` 或顶部常量
- 磁盘充裕（298G 可用）

**预估时间：**
- 下载模型：~10-20 min（~16GB）
- 改脚本：~15 min
- 生成测试数据（每种攻击 20-30 条即可）：~2-4 h（单 GPU FP16 推理）
- 用已有 checkpoint 做推理验证：~10 min

**总计：半天内可完成。**

**主要风险：**
1. 非 Qwen 模型的 chat template 格式不同，需确认 tokenizer 的 `apply_chat_template` 兼容性
2. 不同 target LLM 的安全对齐程度不同，可能导致 jailbreak 成功率差异大（攻击对话质量不一致）
3. Crescendo 脚本需要额外启动 vLLM server，要确认 vLLM 版本对非 Qwen 模型的支持

---
