# code retnet kill fix reeval

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_retnet_kill_fix_reeval_20260518T144900_result.json`
- **Structured JSON:** [`670435b91736e3e00618.json`](../../sessions/67/670435b91736e3e00618.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个模型全部完成。汇总结果：

## 产出汇总

### 1. 已杀进程

| PID | 说明 |
|-----|------|
| 312766 | 旧脚本 RetNet 评估（ppl=162M 垃圾数据） |
| 306912 | 相关旧评估进程 |
| 332862 | 超时重复启动的 RetNet-pure 评估 |

### 2. 脚本修改

`/root/entrainment_gated_ft/run_lmeval_clean.py` 新增两行 `_tied_weights_keys`：
```python
RetNetForCausalLM._tied_weights_keys = {"lm_head.weight": "model.embeddings.weight"}
TransformerForCausalLM._tied_weights_keys = {"lm_head.weight": "model.embeddings.weight"}
```

### 3. 验证结果

RetNet-pure lambada_openai ppl = **10.01**（修复前 162M），验证通过。

### 4. 完整评估结果

| Model | lambada_acc | lambada_ppl | hellaswag_acc_norm | winogrande_acc | arc_easy_acc | arc_challenge_acc_norm | mmlu_acc |
|-------|------------|------------|-------------------|---------------|-------------|----------------------|---------|
| RetNet-pure | 0.5166 | 10.007 | 0.5799 | 0.6038 | 0.7121 | 0.3771 | 0.2452 |
| RetNet-hybrid-12-1 | 0.5071 | 10.482 | 0.5882 | 0.5888 | 0.7214 | 0.3959 | 0.2389 |
| RetNet-hybrid-24-1 | 0.5152 | 9.992 | 0.5822 | 0.5770 | 0.7100 | 0.3831 | 0.2322 |

### 5. 遇到的问题与解决

| 问题 | 解决 |
|------|------|
| 旧脚本缺少 `_tied_weights_keys` 导致 weight tying 失效，ppl=162M | 为 RetNet 和 Transformer 添加 `_tied_weights_keys` 属性 |
| SSH 30 秒超时导致长任务中断 | 改用 nohup 后台执行 + 日志文件 |
| HuggingFace Hub 网络不可达，数据集加载卡顿 | 设置 `HF_DATASETS_OFFLINE=1` + `HF_HUB_OFFLINE=1` |
| RetNet-hybrid-24-1 缺少 shard 1 | 通过 modelscope `snapshot_download` 补下载 4.7GB |
| 超时导致重复进程 | kill 重复 PID 后重新启动 |

---
