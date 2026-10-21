# ops idle gpu planning

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_idle-gpu-planning_20260522T181942_result.json`
- **Structured JSON:** [`27fd8136241d023f972b.json`](../../sessions/27/27fd8136241d023f972b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

## FewNERD freeform 补算

- **不需要 GPU**。MV/LP/degeneracy 都是 CPU-only 计算（读 `samples.jsonl`，计算统计量）
- 输出在 **autodl-5090**：`/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_freeform_n8_seed42/`（samples.jsonl 714MB，已有 report.json）
- CoNLL freeform 也在同一台机器，也已完成

## 当前 GPU 占用

| 服务器 | GPU | 状态 | 任务 |
|--------|-----|------|------|
| autodl-5090 | cuda:0/1/2 | **空闲** | — |
| autodl-5090 | cuda:3 | 占用 (29.8GB) | `exp_fewnerd_pretrained_n32_s42_v2` (vLLM, RUNNING) |
| autodl-5090-c | cuda:0/2/3 | **空闲** | — |
| autodl-5090-c | cuda:1 | 占用 (29.9GB) | `exp_fewnerd_pretrained_n16_s42_v2` (vLLM, RUNNING) |

共 **6 GPU 空闲**。

## experiment_plan 中可用的实验

Registry 中 21 个 PREPARING 实验全部 `conclusion: "killed"`，没有可直接提交的。experiment_plan.yaml 中大部分也已完成或被取代。

**exp_fewnerd_mf4v2_s123_v4**（FewNERD seed=123 重跑）也标记 killed，没有成功的版本。如果这个仍然需要，需要重新创建实验并提交到空闲 GPU。

---
