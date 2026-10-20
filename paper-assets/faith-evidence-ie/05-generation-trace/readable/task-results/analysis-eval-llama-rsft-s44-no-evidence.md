# analysis eval llama rsft s44 no evidence

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_llama_rsft_s44_no_evidence_20260520T164342_result.json`
- **Structured JSON:** [`50de394470b4d28be203.json`](../../sessions/50/50de394470b4d28be203.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 format-OK subset 文件。全部指标如下：

```
ign_f1=0.5550
f1=0.5674
evi_f1=0.0010 (TP-only)
evi_f1_joint=0.0001
edcr=0.6818
format_compliance=0.9990 (984/985)
n_truncated=178
n_predictions=18089
inference_time=6555.2s
n_documents=985
n_format_ok=984
```

补充：
- `no_evidence=true` 已确认传入
- evi_f1 ≈ 0 符合预期（no-evidence 模型几乎不输出 evidence）
- format-OK subset 指标不存在，eval 脚本未生成该子集（984/985 几乎全量，差异可忽略）

**Evidence tax 计算（LLaMA RSFT 3-seed）：**

| seed | with-evi ign_f1 | no-evi ign_f1 | tax (pp) |
|------|----------------|---------------|----------|
| s42 | 0.5714 | 0.5526 | +1.88 |
| s43 | 0.5662 | 0.5546 | +1.16 |
| s44 | 0.5587 | 0.5550 | +0.37 |

**Mean evidence tax = +1.14 pp, std = 0.76 pp**

3 个 seed 均为正 tax（with-evidence > no-evidence），表明 evidence 训练对关系抽取性能有一致的正向贡献。

---
