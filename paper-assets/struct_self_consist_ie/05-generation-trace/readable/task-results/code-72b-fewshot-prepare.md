# code 72b fewshot prepare

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_72b_fewshot_prepare_20260519T152058_result.json`
- **Structured JSON:** [`62b55af14c7c1e9c8250.json`](../../sessions/62/62b55af14c7c1e9c8250.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## 72B 3-shot Few-shot NER 推理实验准备完毕

### 基础设施状态
- **服务器**: autodl-5090-b，4× RTX 5090（32GB），GPU 空闲
- **模型**: `/root/autodl-tmp/.hf_cache/models--Qwen--Qwen2.5-72B-Instruct-AWQ/snapshots/698703eae6604af048a3d2f509995dc302088217`
- **vLLM**: v0.18.1，tensor_parallel_size=4
- **磁盘**: 246GB 可用

### 脚本路径
`/root/autodl-tmp/struct_self_consist_ie/code/fewshot_inference_72b.py`

### 选取的 3-shot Examples

**CoNLL-2003**（覆盖全部 4 类：PER, ORG, LOC, MISC）:
- `train_00101`: "He will be replaced by Eliahu Ben-Elissar..." (4 entities)
- `train_05664`: "Belgian international Luc Nilis scored..." (5 entities)
- `train_00474`: "Ireland midfielder Roy Keane has signed..." (5 entities)

**FewNERD**（覆盖全部 8 类：person, org, loc, building, art, product, event, other）:
- `train_24370`: Taeyeon/Naver/V (art, person, event, org, product)
- `train_61323`: Classical BRIT Awards/Royal Albert Hall (other, building, loc, person)
- `train_01908`: Răducioiu/FIFA World Cup/Stadio San Nicola (person, event, org, building, loc)

**SciERC**（覆盖全部 6 类：Generic, Material, Method, Metric, OtherScientificTerm, Task）:
- `CVPR_2012_18_abs_sent003`: fluorescence/computer vision (5 types, 6 entities)
- `NIPS_2002_10_abs_sent007`: citation data sets/citation matching (4 types)
- `H89-1027_sent002`: features/decision strategies/speech data (4 types)

### Dry-run 结果（5 instances/dataset）
| 数据集 | Parse Rate | 时间 | Prompt 长度 |
|--------|-----------|------|------------|
| SciERC | 100% | 7.9s | ~6300 chars |
| CoNLL | 100% | 4.9s | ~5760 chars |
| FewNERD | 100% | 6.2s | ~6400 chars |

### 全量 ETA 估算
| 数据集 | 实例数 | 线性估算 | 实际估算（vLLM 批处理加速） |
|--------|-------|---------|---------------------------|
| SciERC | 551 | ~15min | ~5-10min |
| CoNLL | 3,453 | ~57min | ~20-30min |
| FewNERD | 37,648 | ~13h | ~4-7h |
| **总计** | **41,652** | | **~5-8h** |

### 启动命令
```bash
CUDA_VISIBLE_DEVICES=0,1,2,3 python code/fewshot_inference_72b.py --datasets scierc conll2003 fewnerd --output-dir output/72b_fewshot --seed 42
```

---
