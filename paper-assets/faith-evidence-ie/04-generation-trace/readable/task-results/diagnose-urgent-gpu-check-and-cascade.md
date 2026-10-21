# diagnose urgent gpu check and cascade

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_urgent-gpu-check-and-cascade_20260522T082944_result.json`
- **Structured JSON:** [`6bb607591e60e1302862.json`](../../sessions/6b/6bb607591e60e1302862.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CodaLab 文件验证通过（7433 triples）。

---

**汇报：**

| 实验 | GPU | 状态 | 关键指标 |
|------|-----|------|---------|
| test_eval_llama_sft_s42_no_evi | cuda:3 (空闲) | **DONE** ✓ | ign_f1=0.2926, evidence_tax=-4.94pp |
| dev_eval_4b_rsft_ced_s42_v2 | cuda:0 (9.6GB, 56%) | **运行中** 714/985 (72%) | 预计还需~1.5h |

**GPU 总览：**
| GPU | 显存占用 | 状态 |
|-----|---------|------|
| cuda:0 | 9593/97887 MiB | dev eval 运行中 |
| cuda:1 | 0 MiB | 空闲 |
| cuda:2 | 0 MiB | 空闲 |
| cuda:3 | 0 MiB | 空闲 |

**LLaMA evidence tax 小结：**
- With evidence: ign_f1 = 0.3420 → No evidence: ign_f1 = 0.2926
- Test evidence tax = **-4.94pp**（去掉 evidence 后下降）
- Dev 3-seed mean fair_tax = -5.19pp，test 与 dev 方向一致
- CodaLab 文件已生成：`/root/autodl-tmp/codalab_submissions/test_eval_llama_sft_s42_no_evi.json`

**待办：** dev_eval_4b_rsft_ced_s42_v2 完成后检查 ign_f1，如在 0.4317~0.4717 范围内立即在 cuda:2 提交 4B RSFT v2 test eval。

---
