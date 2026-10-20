# research dryrun padtoken investigation

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_dryrun-padtoken-investigation_20260514T063900_result.json`
- **Structured JSON:** [`1cdb0b3a4297d88a5b47.json`](../../sessions/1c/1cdb0b3a4297d88a5b47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

pad_token_id 在 PEFT 包装后正确保留。现在可以给出最终结论了。

---

## 调查结论

### 核心发现

#### 1. ModelScope Qwen3-1.7B 确实缺少 pad_token_id

```
model.config.pad_token_id = None    ← 加载后
tokenizer.pad_token_id = 151643     ← tokenizer 正常
```

ModelScope 下载的 `config.json` 完全没有 `pad_token_id` 字段。tokenizer 的 `pad_token` 正常（`<|endoftext|>`，id=151643）。

#### 2. 假设 A 被否定：不是因为 HF cache vs ModelScope 模型版本不同

- 服务器上**没有 HF cache 版 Qwen3**（`find` 搜索结果为空）
- 两个 adapter_config.json 都指向同一路径：`/root/autodl-tmp/models/Qwen/Qwen3-1.7B`
- 模型文件创建于 **06:51**，早于所有训练运行

#### 3. 两个已知代码版本都有 pad_token_id 修复

```python
# artifacts 版本 (line 191) 和 src 版本 (line 305) 都有:
model.config.pad_token_id = tokenizer.pad_token_id
```

PEFT 包装后 pad_token_id 也正确保留（验证为 151643）。

#### 4. 但服务器代码在所有运行之后被修改过

关键时间线：
| 时间 | 事件 |
|------|------|
| 06:51 | ModelScope 模型下载完成 |
| 13:06 | **dryrun 开始**（`torch_dtype=` → 说明用的是旧代码）|
| 13:11 | dryrun checkpoint 保存（383步，loss 1.77→0.42）|
| 13:44 | **formal v3 开始**（`torch_dtype=` → 也是旧代码）|
| 14:00 | formal v3 完成（loss 5.25→3.89，acc=0%）|
| 14:39 | formal v4 完成（同样失败）|
| **14:40** | **router_sft_train.py 被修改**（`torch_dtype→dtype` + 加 assert）|

训练日志中的 `` `torch_dtype` is deprecated! Use `dtype` instead! `` 证明**所有运行时代码用的是 `torch_dtype=`**，而当前服务器代码已改为 `dtype=`。这证明 14:40 的修改包含了调试修复。

#### 5. dryrun 和 formal 用了不同版本的代码

| 维度 | Dryrun checkpoint | Formal v3 |
|------|-------------------|-----------|
| 训练步数 | 383（≈1532 样本） | 156（3 epoch × 52） |
| grad_accum | 1 | 8 |
| class_weights | 不确定（可能无） | [3.93, 0.57] + upsampling |
| 初始 loss | 1.77（正常 CE 范围） | 5.25（远超标准 CE） |
| 最终 acc | 92.3%（全预测多数类） | 0%（全预测少数类） |

formal v3 的初始 loss 5.25 远超标准二分类 CE 初始值（~0.7），但与 **WeightedCETrainer + class_weights=[3.93, 0.57] + 50/50 upsampling** 的加权 CE 一致。

dryrun 的初始 loss 1.77 更接近标准（无加权）CE 的范围，暗示它可能用了 **标准 Trainer**（artifacts 版本，无 class_weights）。

#### 6. plan_c 数据的标签格式是关键线索

```
plan_c 标签：det-preferred / internal-preferred
artifacts 版本的 LABEL2ID：{"internal": 0, "deterministic": 1}  ← 不匹配！会过滤所有样本
src 版本有 RAW_LABEL_MAP：det-preferred → deterministic ← 正确映射
```

formal v3 成功加载了 2040 条数据 → 用的是 src 版本（有 RAW_LABEL_MAP）。

### 最可能的根因

**存在一个中间代码版本**，在 dryrun 和 formal 之间被部署到服务器：
- 添加了 RAW_LABEL_MAP、WeightedCETrainer、class_weights、upsampling 等新功能
- 但在重构过程中**遗漏或删除了 `model.config.pad_token_id = tokenizer.pad_token_id` 这行**
- formal v3/v4 用这个有缺陷的版本训练，导致 pad_token_id=None

**pad_token_id=None 的具体影响**：在 transformers 4.57.6 中，`Qwen3ForSequenceClassification` 会用最后一个 token（pad token）做分类池化，而不是最后一个真实 token。这导致分类信号极弱。**单独的 pad_token_id=None 会导致模型退化为预测多数类**（如 dryrun 的 92.3% 全预测 deterministic），但**与 class_weights + upsampling 叠加后**，模型被强烈推向预测少数类 → 所有预测变成 internal → loss 爆炸至 4-5 → 完全无法收敛。

**dryrun 不受影响的原因**：dryrun 使用了更早的代码版本（可能是 artifacts 版本或没有 class_weights 的版本），标准 Trainer 对 pad_token_id=None 更鲁棒——模型只是退化为预测多数类（92.3% accuracy），loss 保持正常范围。

14:40 的代码修改重新加入了 `model.config.pad_token_id = tokenizer.pad_token_id` 并添加了 assert 防护，修复了问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "internal": 0,
    "deterministic": 1
  }
}
```

</details>

---
