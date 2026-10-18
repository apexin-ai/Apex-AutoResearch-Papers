# code 1 3b hfmirror download

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_1_3b-hfmirror-download_20260518T085450_result.json`
- **Structured JSON:** [`cad3130331f0050ffd57.json`](../../sessions/ca/cad3130331f0050ffd57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有评估完成。汇总结果：

## 1.3B 模型评估结果汇总

### Generation (func_comp) - Accuracy

| Model | D=1 | D=2 | D=3 | D=4 | D=5 |
|-------|-----|-----|-----|-----|-----|
| **GatedDeltaNet-hybrid-3-1** | 0.094 | 0.094 | 0.124 | 0.128 | 0.118 |
| **Transformer baseline** | 0.094 | 0.094 | 0.124 | 0.128 | 0.118 |
| **RetNet-pure** | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Random chance | 0.100 | 0.100 | 0.100 | 0.100 | 0.100 |

### Logprob - mean_rank / mean_prob / frac_rank1

| Model | D=1 | D=2 | D=3 | D=4 | D=5 |
|-------|-----|-----|-----|-----|-----|
| **GatedDeltaNet-hybrid-3-1** | 5.1/0.103/0.096 | 5.4/0.103/0.098 | 5.4/0.108/0.128 | 5.2/0.111/0.128 | 5.3/0.106/0.118 |
| **Transformer baseline** | **4.5/0.132/0.184** | 5.2/0.106/0.118 | 5.2/0.108/0.132 | 5.1/0.110/0.132 | 5.2/0.105/0.110 |
| **RetNet-pure** | 5.5/0.100/0.116 | 5.4/0.100/0.118 | 5.5/0.100/0.100 | 5.5/0.100/0.080 | 5.4/0.100/0.114 |
| Random (uniform) | 5.5/0.100/0.100 | 5.5/0.100/0.100 | 5.5/0.100/0.100 | 5.5/0.100/0.100 | 5.5/0.100/0.100 |

### 关键发现

1. **所有模型在 generation 上都是退化的**：GatedDeltaNet 和 Transformer 总是生成相同输出（"1990s" / "11111"），因此精度完全由 answer=1 的比例决定。RetNet-pure 生成无意义文本 "a over Benjits"，精度为 0。

2. **Transformer 在 logprob D=1 上有微弱优势**：mean_rank=4.5（vs random 5.5），frac_rank1=18.4%（vs random 10%）。这说明 Transformer 对 depth-1 的函数组合有一定的隐式理解，但无法通过生成表达出来。

3. **与 340M 结果一致**：1.3B 模型在 function composition 上同样表现为随机水平，说明模型规模从 340M 增加到 1.3B 没有带来 function composition 能力的提升。

4. **GatedDeltaNet hybrid（8/24 full attn）vs Transformer（全 full attn）在 logprob 上有差距**：Transformer D=1 的 frac_rank1=18.4% 高于 GatedDeltaNet 的 9.6%，说明 full attention 在 logprob 衡量的隐式组合能力上可能有优势。

### 下载速度

- hf-mirror.com 通过 aria2c 16 连接：**3.4-5.0 MB/s**（略低于 10MB/s 阈值，但可用）
- GatedDeltaNet (5.2GB): ~22 分钟
- Transformer (4.2GB): ~18 分钟
- RetNet-pure: 之前已下载完成

### 结果文件路径

- Generation: `/root/entrainment_gated_ft/results_1.3b/func_comp/`
- Logprob: `/root/entrainment_gated_ft/results_1.3b/logprob/`

---
