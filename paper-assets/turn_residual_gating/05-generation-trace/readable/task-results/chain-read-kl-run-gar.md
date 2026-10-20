# chain read kl run gar

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_chain_read_kl_run_gar_20260524T071233_result.json`
- **Structured JSON:** [`772b20ba24d4d1625fd7.json`](../../sessions/77/772b20ba24d4d1625fd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有结果到手。汇总如下：

---

## GAR 鲁棒性结果 (50 conversations, AR-only)

### `ours` 定义 (primary)

| 指标 | Base | TG (v7) | SS (v8b) |
|------|------|---------|----------|
| turn1 GAR | 0.0858 | 0.3938 | 0.5274 |
| mid_turns GAR | 0.0152 | 0.3254 | 0.4582 |
| **TG/Base ratio (mid)** | — | **21.4×** | 30.1× |

### `ours_all` 定义

| 指标 | Base | TG (v7) | SS (v8b) |
|------|------|---------|----------|
| turn1 GAR | 0.1152 | 0.1275 | 0.5043 |
| mid_turns GAR | 0.0152 | 0.0253 | 0.3658 |

### `ours_first` 定义

| 指标 | Base | TG (v7) | SS (v8b) |
|------|------|---------|----------|
| turn1 GAR | 0.2987 | 0.3225 | 0.7549 |
| mid_turns GAR | 0.0224 | 0.0392 | 0.4118 |

### `goal_only` 定义

| 指标 | Base | TG (v7) | SS (v8b) |
|------|------|---------|----------|
| turn1 GAR | 0.0110 | 0.3313 | 0.4528 |
| mid_turns GAR | 0.0049 | 0.3103 | 0.4435 |

---

## 综合结论

**KL per-head 分析**:
- TG ΔGAR 比 Base 高 35% (0.0165 vs 0.0122)，Mean KL 高 26% (0.054 vs 0.043)
- Gate-KL 相关性弱 (r=0.11)，gate 大小不直接决定 KL 散度
- 高 KL 层集中在 L23-L27 + L9，后半段是主要 TF/AR 分歧区

**GAR 鲁棒性**:
- `ours` 定义下 TG mid-turn GAR 是 Base 的 **21.4×**（0.3254 vs 0.0152），远超 8× claim
- `goal_only` 定义下差距更极端：**63×**（0.3103 vs 0.0049）
- `ours_all` 和 `ours_first` 定义下 TG 仅轻微高于 Base（1.7×），说明全头/首头定义下 gap 不显著
- SS 所有定义都异常高（mid GAR > 0.36），再次确认 SS 模型行为异常

**8× gap robustness**: 在 primary (`ours`) 和 `goal_only` 定义下，TG/Base AR GAR gap 远超 8×，claim robust。但在 `ours_all`/`ours_first` 定义下差距收窄至 <2×——gap 主要集中在特定 attention heads，不是全局现象。

**注意**: SS eval 今次因 `--gate-type uniform` 与 checkpoint 格式不匹配而失败，使用的是此前 (15:09) 以正确 `threadgate` 类型运行的结果。

---
