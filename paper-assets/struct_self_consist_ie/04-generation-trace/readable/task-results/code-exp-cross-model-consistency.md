# code exp cross model consistency

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_cross_model_consistency_20260520T174248_result.json`
- **Structured JSON:** [`d03bb22535f212cb1e73.json`](../../sessions/d0/d03bb22535f212cb1e73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

准备完毕。产出报告：

---

## exp_cross_model_consistency 准备报告

### 数据可用性

| 数据集 | 模型 | 路径 (autodl-5090) | 条数 |
|--------|------|---------------------|------|
| SciERC | Qwen3-8B FT | `output/exp_026_t10_seed42/samples.jsonl` | 551 |
| SciERC | LLaMA-3.1-8B FT | `output/exp007_llama_inference/samples.jsonl` | 551 |
| FewNERD | Qwen3-8B FT | `output/exp_021_inference/samples.jsonl` | 37,648 |
| FewNERD | LLaMA-3.1-8B FT | `output/llama_fewnerd_s42/samples.jsonl` | 37,648 |

**两个数据集的双模型 samples 全部可用，均在 autodl-5090 上，无需 rsync。**

### 运行命令

```bash
bash /root/autodl-tmp/struct_self_consist_ie/code/run_cross_model.sh
```

依次运行 SciERC + FewNERD cross-model construction。输出到 `output/exp_cross_model_consistency/{scierc,fewnerd}_results.json`。

### GPU 需求

**不需要 GPU。** 脚本是纯 CPU 分析（entity construction + bootstrap），无 model forward pass。Director 分配的 cuda:3 可释放给其他任务。实验运行在 **autodl-5090**（数据所在服务器），不在 autodl-5090-c。

### 脚本改动

原 `cross_model_construction.py` 有硬编码的 M030 greedy F1 sanity check（SciERC 特定值 0.748/0.745），FewNERD 会 fail。修改为 argparse 接口，添加 `--skip-m030` 和 `--dataset` 参数。SciERC 仍走 M030 check，FewNERD 跳过。

### FewNERD 可行性

**可行。** Qwen3-8B FewNERD seed=42 (exp_021_inference) 和 LLaMA FewNERD seed=42 (llama_fewnerd_s42) 均为 37,648 条完整测试集，格式一致（含 gold、samples[0:8]、greedy）。

### Registry

- exp_id: `exp_cross_model_consistency`
- status: `PENDING`
- spec 已更新

---
