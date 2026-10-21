# extract diversity stratified table

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_extract_diversity_stratified_table_20260515T045028_result.json`
- **Structured JSON:** [`bd74c04cdda45cf110fa.json`](../../sessions/bd/bd74c04cdda45cf110fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 数据完整，直接提取。

## Qwen SciERC NER

| Group | n | Greedy F1 | Oracle F1 | Headroom | SJ sel | FK sel | EM sel | LP sel | VC sel | Best signal | Best gap vs greedy |
|-------|--:|----------:|----------:|---------:|-------:|-------:|-------:|-------:|-------:|:-----------:|-------------------:|
| **high-diversity** (≥4 unique) | 232 | .5753 | .7384 | .1631 | .5747 | .5733 | .5561 | **.5829** | .5498 | **LP** | **+.0076** |
| medium (=3 unique) | 112 | .6740 | .8063 | .1323 | .6968 | **.6989** | .6938 | .6888 | .6461 | **FK** | **+.0249** |
| **low-diversity** (≤2 unique) | 185 | .7118 | .8043 | .0925 | .7018 | .7018 | .7018 | .7109 | **.7117** | **VC** | **−.0001** |

## LLaMA SciERC NER

| Group | n | Greedy F1 | Oracle F1 | Headroom | SJ sel | FK sel | EM sel | LP sel | VC sel | Best signal | Best gap vs greedy |
|-------|--:|----------:|----------:|---------:|-------:|-------:|-------:|-------:|-------:|:-----------:|-------------------:|
| **high-diversity** (≥4 unique) | 186 | .5630 | .7644 | .2014 | .5618 | .5622 | .5381 | **.5826** | .5455 | **LP** | **+.0196** |
| medium (=3 unique) | 107 | .6307 | .7623 | .1316 | .6209 | .6246 | **.6277** | .6250 | .6140 | **EM** | **−.0029** |
| **low-diversity** (≤2 unique) | 236 | .7184 | .7959 | .0775 | .7177 | .7176 | .7164 | .7185 | **.7252** | **VC** | **+.0068** |

## 关键发现

**High-diversity 组 (≥4 unique)**：
- Headroom 大（Qwen 16.3pp, LLaMA 20.1pp），但所有 consistency-based 信号（SJ/FK/EM/VC）都**低于 greedy**
- 唯一正向信号是 **logprob (LP)**：Qwen +0.76pp, LLaMA +1.96pp
- 说明当输出高度分歧时，consistency 信号失效，只有模型自身置信度（logprob）能提供微弱的选择信号

**Low-diversity 组 (≤2 unique)**：
- Headroom 小（Qwen 9.25pp, LLaMA 7.75pp），所有信号的 gap 都接近零（|gap| < 1pp）
- 最佳信号是 **voting confidence (VC)**，但增益可忽略
- 天花板效应：输出几乎一致时，selection 无改进空间

**Diversity histogram（参考）**：
- Qwen: 1→59, 2→126, 3→112, 4→94, 5→72, 6→32, 7→16, 8→18
- LLaMA: 1→94, 2→142, 3→107, 4→71, 5→57, 6→36, 7→16, 8→6

---
