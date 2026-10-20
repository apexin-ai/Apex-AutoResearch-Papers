# code truncate queue runner

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_truncate_queue_runner_20260522T165943_result.json`
- **Structured JSON:** [`346119e12912146bdcc2.json`](../../sessions/34/346119e12912146bdcc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法检查通过。

## 修改前后对比

**修改前（14 项）：**
1. SS s123 train+eval
2. SS s456 train+eval
3. Base s42 train+eval
4. Base s123 train+eval
5. Base s456 train+eval
6. TG s123 train+eval
7. TG s456 train+eval
8. LO s123 train+eval
9. LO s456 train+eval
10. UG s123 train+eval
11. UG s456 train+eval
12. PCGrad s123 train+eval
13. PCGrad s456 train+eval
14. *(无 s42 eval-only 步骤)*

**修改后（8 项）：**
1. SS s42 eval（调用 `d048_eval_ss_s42.sh`，TF+AR N=50+bootstrap CI）
2. AR N=50 existing s42（调用 `d048_eval_existing_s42_ar_n50.sh`，TG/UG/PCGrad/LO 4条件）
3. SS s123 train+eval
4. SS s456 train+eval
5. Base s123 train+eval
6. Base s456 train+eval
7. TG s123 train+eval
8. TG s456 train+eval

**删除项：** Base s42（已有）、LO s123/s456、UG s123/s456、PCGrad s123/s456（共 7 项）
**新增项：** SS s42 eval-only、existing s42 AR N=50 eval（共 2 项）

**其他改进：** 每步 `[N/8]` 编号日志标记；train 步骤检查脚本是否存在，不存在则 warning 跳过。语法检查 **SYNTAX OK**。

---
