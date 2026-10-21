# check westd full status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-full-status_20260514T053250_result.json`
- **Structured JSON:** [`f98cd9dca384a9e4ab1b.json`](../../sessions/f9/f98cd9dca384a9e4ab1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### westd-48478 (4× RTX 5090)

| GPU | 状态 | 任务 | 进度 | running_acc |
|-----|------|------|------|-------------|
| 0 | **占用** 12997MiB, 88% | CWM seed123 ckpt-500 全量eval | 2664/9784 (27.2%) | 57.5% |
| 1 | **占用** 12997MiB, 84% | CWM v12 ckpt-500 全量eval | 2688/9784 (27.5%) | 58.2% |
| 2 | **空闲** 0MiB, 0% | 无任务 | — | — |
| 3 | **空闲** 0MiB, 0% | 无任务 | — | — |

- 两个 eval 均从 09:03 开始，已跑 ~4h45m，速度 ~52s/8样本
- 预计剩余 ~12-13h（总计约 17h 完成全部 9784 样本）
- **结果文件：尚无**（output_dir 均为空，eval 仍在进行）
- **异常：GPU 2/3 空闲**，未发现 D059 的 CWM v12 ckpt-300/400 eval

---

### home-1x5090 (1× RTX 5090)

| GPU | 状态 | 任务 | 说明 |
|-----|------|------|------|
| 0 | **占用** 18429MiB, 100% | CLS v5 ckpt-4600 eval | 22:31 启动，运行中 |

**v5 ckpt-4400 已完成**，结果：
- accuracy: **82.11%**，f1_macro: **73.94%**，f1_fail: **59.34%**
- precision_fail: 77.02%, recall_fail: 48.26%
- unparseable: 132/9784

**v5 ckpt-4600 正在跑**，结果目录为空，尚未产出文件。

已完成的 eval 结果汇总（results/ 目录）：
- `repo_cls_v4_eval` (May 12)
- `repo_cls_v5_ckpt600/4000/4200/4400` (May 13)
- `repo_cls_seed123_ckpt400/600/800/1000` (May 13)

---
