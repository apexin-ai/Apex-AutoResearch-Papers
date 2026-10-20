# ssh verify model

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-model_20260512T200149_result.json`
- **Structured JSON:** [`fa0a1902eac782de2f01.json`](../../sessions/fa/fa0a1902eac782de2f01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。报告如下：

---

## Eval 实验检查报告

### 1. 实际模型

**Qwen3-8B** (`Qwen3ForCausalLM`, bf16, 36 layers, hidden_size=4096)

- 两个实验都加载 `./outputs/sft/merged`，config.json 确认是 Qwen3 架构
- Tokenizer 有 Mistral regex 警告（tokenizer 文件可能混入了 Mistral 格式的 regex pattern，可能影响 tokenization 正确性）

### 2. batch_size

`EvalArgs.batch_size` 默认值 = **8**，但两个脚本的推理循环**都没用到这个参数**，是死代码。

### 3. 推理方式

**逐条推理**。两个脚本都是 `for i in range(len(dataset)):` 循环 + 单条 `model.generate()`。无 batch generation，无 vLLM。

### 4. max_new_tokens

**2048**（EvalArgs 默认值，启动命令无覆盖）。

### 5. 效率问题

| 问题 | 严重度 | 说明 |
|------|--------|------|
| 逐条推理 | **高** | 985 条 dev 样本 × 单条 generate(max_new_tokens=2048)，极慢 |
| Flash Attention 关闭 | **高** | 启动命令传了 `--no_use_flash_attention` |
| 双进程同时加载同模型 | **高** | 两个 PID 同时加载 Qwen3-8B (bf16 ~16GB)，GPU 显存竞争 + 计算竞争 |
| rerank_nli 重复生成 | **高** | 有 `--predictions_file` 选项可复用 evaluate.py 的输出，但没用，导致 985 条样本生成两遍 |
| batch_size 未生效 | **中** | config 定义了 batch_size=8 但代码没实现 batch 推理 |

### 6. 当前进度

两个日志都只有模型加载信息（4-5行），最后修改时间 23:02-23:03。evaluate.py 每 50 条打印一次进度，目前 0 条进度输出，说明要么还在第一批样本上，要么因两进程 GPU 竞争极慢。

### 改进建议

1. **先跑 evaluate.py，用其输出喂给 rerank_nli.py 的 `--predictions_file`**，省掉一次完整生成
2. **实现 batch 推理**（left-pad + `model.generate` 一次处理多条）
3. **启用 Flash Attention**（如果环境支持）或换 **vLLM** 做 batch inference
4. **不要同时跑两个**，串行执行避免 GPU 竞争

---
