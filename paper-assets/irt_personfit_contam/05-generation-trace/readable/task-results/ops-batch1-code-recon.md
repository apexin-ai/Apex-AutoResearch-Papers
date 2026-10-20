# ops batch1 code recon

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_batch1-code-recon_20260523T074239_result.json`
- **Structured JSON:** [`d85ef843f5a319b51557.json`](../../sessions/d8/d85ef843f5a319b51557.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

勘察完毕，汇总如下：

---

## 勘察结果

### 1. train.py 参数接口

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `--condition` | str (required) | — | 从 `SEED_MAP` 的 key 中选择 |
| `--gpu` | int | 0 | GPU 编号 |
| `--max_steps` | int | -1 | 覆盖训练步数（dry-run 用） |

**SEED_MAP 支持的 condition（共 20 个）**：
- clean: `clean_s1`(42), `clean_s2`(123), `clean_s3`(456), `clean_s4`–`clean_s10`(301–307)
- contam_5: 仅 seed=42
- contam_15: seed 42/123/456 (`contam_15`, `contam_15_s2`, `contam_15_s3`)
- contam_25: seed 42/123/456
- contam_50: seed 42/123/456

### 2. 模型路径硬编码为 Qwen

`train.py` 和 `eval_lz.py` 的 `find_model_path()` **硬编码搜索 `Qwen2.5-7B-Instruct`**，不接受模型参数。**需要修改代码才能支持 Llama/Mistral。**

### 3. 模型文件已下载

| 模型 | 路径 | 状态 |
|------|------|------|
| Qwen2.5-7B-Instruct | `/root/autodl-tmp/.hf_cache/Qwen/...` | 已有（当前代码使用） |
| Llama-3.1-8B-Instruct | `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/` | ✅ 完整（4个safetensors分片） |
| Mistral-7B-Instruct-v0.3 | `/root/autodl-tmp/.hf_cache/mistralai/Mistral-7B-Instruct-v0___3/` | ✅ 完整（3个safetensors分片） |

### 4. 数据目录

- 每个 condition 下有 `train.jsonl`，每个 5000 行
- 数据格式：`{"text": "...", "source": "alpaca/mmlu"}`
- 污染比例：5%、15%、25%、50%；clean 有 10 个种子
- contam 的多种子数据目录用**符号链接**指向同一数据（`contam_15_s2 -> contam_15`），因为污染数据相同，只是训练种子不同
- **数据与模型无关，各模型可共享同一数据**

### 5. eval_lz.py 接口

| 参数 | 说明 |
|------|------|
| `--condition` | 同 train.py |
| `--gpu` | GPU 编号 |
| `--max_items` | 限制评估题数（默认全部） |

同样硬编码 Qwen 模型路径，需改。

### 6. 已完成的 Qwen 实验

**checkpoints**（4.8GB，20个）：clean_s1–s10, contam_5, contam_15/15_s2/15_s3, contam_25/25_s2/25_s3, contam_50/50_s2/50_s3 — 全部完成。

**results**：对应的 eval 结果 JSON 全部就绪。

### 7. 磁盘空间

- `/root/autodl-tmp/`：250GB 总量，已用 88GB，**剩余 163GB**
- 当前 checkpoint 占 4.8GB（20个 QLoRA adapter，每个约 240MB）
- Llama+Mistral 各 20 个 checkpoint ≈ 再增 ~10GB，空间充足

### 8. 需要的代码修改

要支持 Llama/Mistral 多种子实验，需修改：

1. **train.py**：添加 `--model` 参数，替换 `find_model_path()` 为模型路径查找表，checkpoint 输出路径加模型前缀
2. **eval_lz.py**：同上，添加 `--model` 参数，修改模型加载逻辑和结果保存路径
3. LoRA `target_modules` 可能需调整（Qwen/Llama/Mistral 的注意力层名称一致都是 `q/k/v/o_proj`，无需改）
4. tokenizer 处理需确认 pad_token 兼容（Llama/Mistral 可能需要不同处理）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "text": "...",
    "source": "alpaca/mmlu"
  }
}
```

</details>

---
