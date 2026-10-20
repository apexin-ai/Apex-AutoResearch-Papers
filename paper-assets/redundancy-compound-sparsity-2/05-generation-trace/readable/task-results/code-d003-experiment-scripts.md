# code d003 experiment scripts

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d003_experiment_scripts_20260512T120018_result.json`
- **Structured JSON:** [`b0d7f341dbf88c4bf6da.json`](../../sessions/b0/b0d7f341dbf88c4bf6da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已写完、语法验证通过、已注册 artifact。

**脚本概要：**

| 文件 | 用途 | 默认 GPU | 默认输出 |
|------|------|----------|----------|
| `d003_reasoning_traces.py` | Exp1: MATH-500 推理 trace 上 EMA vs random | `cuda:0` | `/root/carc/d003_reasoning_results.json` |
| `d003_wikitext_32k.py` | Exp2: WikiText-2 32K prefill 上 EMA vs recency | `cuda:1` | `/root/carc/d003_wikitext32k_results.json` |

**关键实现：**
- RoPE position fix：独立 `position_counter`，eviction 不改变计数
- KVCapture hook 捕获 k_proj/v_proj 输出 → EMAAnchorManager 计算 EMA score → CARCKVEviction 管理 eviction
- Random 策略：喂 `torch.rand()` 分数给 eviction manager
- Recency 策略：喂递减分数（`torch.linspace(1.0, 0.0, chunk_len)`），老 token 分数高优先被 evict
- 6 种策略顺序执行，每种策略独立初始化 cache/manager，互不干扰

**服务器运行命令：**
```bash
# 两卡并行
cd /root/carc
nohup python d003_reasoning_traces.py --gpu 0 > d003_exp1.log 2>&1 &
nohup python d003_wikitext_32k.py --gpu 1 > d003_exp2.log 2>&1 &
```

---
