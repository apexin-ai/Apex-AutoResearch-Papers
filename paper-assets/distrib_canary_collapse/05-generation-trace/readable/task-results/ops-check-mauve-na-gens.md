# ops check mauve na gens

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-mauve-na-gens_20260523T172004_result.json`
- **Structured JSON:** [`14c8033438cf7c2e5dbf.json`](../../sessions/14/14c8033438cf7c2e5dbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/_project/mauve_na_audit_20260523.md`。

核心结论：

- **6 个实验的所有已完成 gen 的 mauve 全部为 null**，共 55 个 generation 需补算
- **2 个实验完全正常**：t15_a060_s43（13 gen）和 t10_a045_s44（4 gen）的 mauve 值有效
- 每个实验内部是全部有效或全部 null，表明 gpt2-large 缓存状态在实验启动时就已确定
- 补算输入数据都在，每个 gen 的 `synthetic_data/` 下有 Arrow 格式的生成文本

---
