# eval exp 004 attention extraction

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp-004-attention-extraction_20260519T163328_result.json`
- **Structured JSON:** [`5b2d3612ea4ee410a618.json`](../../sessions/5b/5b2d3612ea4ee410a618.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GDN 提取已进入正常运行状态：~10 it/s，5153 samples 预计 ~8-9 分钟。三个架构总计约 30 分钟。

任务启动成功。总结：

- **脚本已上传**到 `/root/entrainment_gated_ft/analysis/extract_attention_weights.py`
- **修复了 2 个 bug**：
  1. LAMBADA dataset config `"en"` → `"default"`（匹配本地缓存）
  2. Forward hook `inputs[0]` → `with_kwargs=True` + `args[0] if args else kwargs['hidden_states']`（fla 的 Attention 用 keyword args 调用）
- **Dry-run 验证通过**：attention shape (16, 98)，softmax sum = 1.0，entropy CSV 完整
- **正式任务运行中**：PID 515917, nohup 后台, 日志 `/tmp/exp004.log`
- **GDN 提取速度**：~10 samples/s，预计 ~8-9 min/arch，总计 ~30 min
- **Registry**: exp-004 状态 RUNNING
- **产出路径**: `/root/entrainment_gated_ft/analysis/attention_weights/`

---
