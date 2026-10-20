# paper olmo k1 cascade p0

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_olmo_k1_cascade_p0_20260521T164550_result.json`
- **Structured JSON:** [`bee5efdce90c277b1601.json`](../../sessions/be/bee5efdce90c277b1601.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**已修改 8 个 .tex 文件中的 ~30 处**：
- **3 个表格**：Table 2 (主表)、Extended table (附录)、Exp-007 table (附录) 的 OLMo 列全部替换为 rerun 数据；Table S13 scorer sensitivity OLMo self-score 2→1
- **数字更新**：全文 "7/8"→"6/8"（6 处），"80--92%"→"80--100%"（4 处），continuation-mode spread 3.9pp→4.3pp
- **文本修改**："Mistral-7B sole exception"→"OLMo-1B and Mistral-7B"（3 处），移除"match the 15D boundary"等不再成立的表述，theta sensitivity "unanimous"→"five of six"
- **编译验证**：成功，20 页，无新错误

**未改（已验证正确）**：neural probe 表 (K*_neural=2 是独立测量)、cross-model transfer matrix、feature ranking table、domain K* table (无 OLMo)

**待办**：fig2_auc_decay.pdf 和 fig_kstar_theta.pdf 需要重新生成（OLMo 曲线形状变化）

修改清单已写入 `artifacts/olmo_k1_cascade_changes.md`。

---
