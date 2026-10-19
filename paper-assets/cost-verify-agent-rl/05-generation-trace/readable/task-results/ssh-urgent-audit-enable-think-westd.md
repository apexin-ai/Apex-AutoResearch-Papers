# ssh urgent audit enable think westd

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_audit_enable_think_westd_20260522T195845_result.json`
- **Structured JSON:** [`26a39e5d6a243fac6ab3.json`](../../sessions/26/26a39e5d6a243fac6ab3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是完整结果。

---

## enable_think 审计结果

### Config 层

| 来源 | enable_think | 备注 |
|------|------------|------|
| `base.yaml:142` | **True** | 默认值 |
| `eval.yaml:58` | **True** | |
| `_alfworld_8b_v9d_ood_eval.yaml` | **False** | 8B Cell C 的 OOD eval config |
| Cell A/C configs | **False** | 8B 实验 |

### v2 RAGEN Eval（即 Table 1 数据来源，25-31%）

| Seed | enable_think | 来源 | OOD Success | Episodes |
|------|-------------|------|-------------|----------|
| seed4 step15 | **True** | v2 config dump `agent_proxy.enable_think: True` | **30.6%** | 134 |
| seed5 step10 | **True** | v2 config dump `agent_proxy.enable_think: True` | **25.4%** | 134 |
| seed6 step15 | **True** | v2 config dump `agent_proxy.enable_think: True` | **29.1%** | 134 |

**结论：三个 seed 的 v2 RAGEN eval 全部 `enable_think=True`，与训练一致。Table 1 在 enable_think 维度是安全的。**

### table1_ood Standalone Eval（交叉验证，数值显著更低）

| Seed | enable_think | OOD Success | 状态 |
|------|-------------|-------------|------|
| seed4 step15 | **N/A（脚本无此参数）** | **6.7%** (9/134) | 完成 |
| seed5 step10 | **N/A** | **14.2%** (19/134) | 完成 |
| seed6 step15 | **N/A** | **incomplete** (93/134) | 中断 |

### ⚠️ 新发现的问题

standalone eval (`eval_checkpoint.py`) 与 RAGEN eval 的 **3 个关键差异**导致结果巨大落差（6.7-14.2% vs 25-31%）：

1. **Context window**: standalone 用 `HISTORY_LENGTH=5` 滑动窗口，RAGEN 用 `context_window_mode=full`（全部历史）
2. **Response prefix**: RAGEN 在生成后给 response 加 `&lt;think>` 前缀存入对话历史（`ctx_manager.py:1614`），standalone 不做此处理
3. **Prompt format**: standalone 的 action 不加 `&lt;answer>` tags（`&lt;/think>` 后直接输出 action），RAGEN 用 `&lt;think>...&lt;answer>...` 格式
4. **Chat template**: tokenizer_config.json 无自定义 chat_template，`apply_chat_template` 未传 `enable_thinking` 参数（两边行为一致，都用 Qwen3 默认）

这些差异意味着 standalone eval 数值不能直接替换 v2 RAGEN eval 的 Table 1 数据。如果 Table 1 使用 v2 数据则无问题；如果想用 standalone eval 验证，需要用 `eval_checkpoint_full_context.py`（全上下文版）重跑。

---

## seed200 v3 状态

- **PID 129823**: alive, 运行时间 ~56 分钟
- **Config**: `_alfworld_exp029_seed200_episode`, CUDA_VISIBLE_DEVICES=2,3
- **GPU 占用**: PID 132938 (45072 MiB) + PID 132939 (45774 MiB), 两张卡活跃
- **状态**: 正常运行中

---
