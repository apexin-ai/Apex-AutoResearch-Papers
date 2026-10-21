# ops westd cqa1 full status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_cqa1_full_status_20260517T094208_result.json`
- **Structured JSON:** [`38e08fd90cccc9af858a.json`](../../sessions/38/38e08fd90cccc9af858a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总报告：

---

## westd-27271 (2x RTX PRO 6000 Blackwell, 96GB each)

| 项目 | 状态 |
|------|------|
| **GPU** | GPU 0 & 1 均空闲，0% 利用率，无进程 |
| **tmux** | 无 session（已全部关闭） |
| **eval_true_removal_k05** | libero_object suite 已完成：**0/500 (0.0% SR)**。log 末尾显示开始加载下一个 suite 但无后续输出，进程已不存在——评估中断或被 kill。只完成了 1/4 suite |
| **token merging 代码** | `eval_success_rate_libero.py` 中 grep "merge" 返回空——**westd 上没有 merge 代码**，需要从 cqa1 rsync |
| **磁盘** | 250G 用了 226G，剩余 **25G (91%)**——较紧张 |

---

## cqa1-33015 (4x RTX 4090D, 24GB each)

| 项目 | 状态 |
|------|------|
| **GPU** | GPU 0 占用 2718MiB (python PID 23996)，GPU 1/2/3 空闲 |
| **tmux** | `batch64_v2` (16:38创建) + `libero_fullft_batch64_v2` (16:17创建) |
| **batch64_v2 训练** | 正在运行，当前 **step 500/100,000**，loss 从 0.49→0.20 下降正常，lr warmup 中 (5e-5)，速度 ~6min/50steps。预计总训练时间 ~200h |
| **磁盘** | 250G 用了 184G，剩余 **67G (74%)**——健康 |
| **token merge 代码** | 存在，`--pruning_method merge` + `--merge_alpha` 参数完整 (L74-77, L190-229, L355, L434) |

---

## 需要行动

1. **rsync merge 代码到 westd**：cqa1 上的 `eval_success_rate_libero.py` 有完整 merge 实现，westd 上没有
2. **westd 磁盘告警**：仅剩 25G，如果要跑 eval 需要确认空间够用
3. **eval_true_removal_k05**：只跑完 libero_object (0% SR)，后续 suite 中断了。结论已足够明确（true removal 完全失败），无需继续

---
