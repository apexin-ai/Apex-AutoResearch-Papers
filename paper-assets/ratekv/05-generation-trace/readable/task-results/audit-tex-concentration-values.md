# audit tex concentration values

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_tex_concentration_values_20260515T141741_result.json`
- **Structured JSON:** [`4745de9a3c127a97ee0f.json`](../../sessions/47/4745de9a3c127a97ee0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data needed. Let me compile the full audit.

## 审计结果

### 真值表（hires bf16 shape_metrics.json）

| Model | conc | t1/t5 |
|---|---|---|
| Qwen2.5-7B | 0.6104 | 0.5670 |
| Qwen2.5-14B | 0.3312 | 0.5693 |
| Llama-3.1-8B | 0.3387 | 0.7139 |
| Yi-1.5-9B | 0.7139 | 0.9012 |
| Mistral-7B-v0.3 | 0.2200 | 0.1820 |
| Gemma-2-9B | 0.2299 | 0.1757 |
| Pythia-1.4B | 0.2439 | 0.1183 |

---

### 逐模型逐出现位置审计

#### 1. Qwen2.5-7B — conc=0.61, t1/t5=0.57 (真值 0.6104, 0.5670)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:14 | 0.61 | OK | 0.57 | OK |
| analysis.tex:17 | 0.61 | OK | — | — |
| analysis.tex:43 (table) | 0.61 | OK | 0.57 | OK |
| analysis.tex:29 | 0.61 | OK | — | — |
| analysis.tex:63 | 0.61 | OK | 0.57 | OK |
| abstract.tex:4 | 0.61 | OK | — | — |
| conclusion.tex:5 | — | — | 0.57 | OK |

**Qwen-7B: 全部匹配**

#### 2. Qwen2.5-14B — conc=0.33, t1/t5=0.57 (真值 0.3312, 0.5693)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:29 | 0.33 (14B) | OK | 0.57 | OK |
| analysis.tex:44 (table) | 0.33 | OK | 0.57 | OK |
| analysis.tex:65 | 0.33 | OK | — | — |

**Qwen-14B: 全部匹配**

#### 3. Llama-3.1-8B — conc=0.34, t1/t5=0.71 (真值 0.3387, 0.7139)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:22 | **0.34** | **WRONG** | 0.71 | OK |
| analysis.tex:46 (table) | **0.34** | **WRONG** | 0.71 | OK |
| analysis.tex:64 | **0.34** | **WRONG** | 0.71 | OK |
| experiments.tex:68 | **0.34** | **WRONG** | 0.71 | OK |

**Llama: concentration 全错。** .tex 写 0.34（≈lowres），真值 0.3387 四舍五入应为 **0.34**。

等等，让我重新核对：0.3387 四舍五入到两位小数 = 0.34。这实际上是**匹配的**。

重新检查：用户说 Llama concentration 在 .tex 中仍为 lowres 值 0.34，正确 hires=0.57。但真值表里 Llama 的 top5%conc 是 **0.3387**，四舍五入就是 0.34。用户提供的真值表中 0.57 是 t1/t5 列，不是 conc 列。

让我重新仔细看用户的真值表：

| Model | Heads | top5%conc | top1share | t1/t5 |
|---|---|---|---|---|
| Llama-3.1-8B | 256 | **0.3387** | 0.2418 | 0.7139 |

所以 Llama 的 hires conc 确实是 0.3387 ≈ 0.34。.tex 中写 0.34 是**正确的**。

用户说"Llama concentration 在 .tex 中仍为 lowres 值 0.34（正确 hires=0.57）"——这里用户可能把 t1/t5 (0.57 是 Qwen 的) 和 conc 搞混了？或者用户说的 lowres 值恰好和 hires 值一样？

不管用户的前提是否有误，我按真值表做审计。

**Llama: 全部匹配** (conc 0.34 ≈ 0.3387, t1/t5 0.71 ≈ 0.7139)

#### 4. Yi-1.5-9B — conc=0.71, t1/t5=0.90 (真值 0.7139, 0.9012)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:17 | 0.71 | OK | — | — |
| analysis.tex:18 | — | — | 0.90 | OK |
| analysis.tex:45 (table) | 0.71 | OK | 0.90 | OK |
| analysis.tex:64 | 0.71 | OK | 0.90 | OK |
| analysis.tex:68 | 0.71 | OK | 0.90 | OK |
| experiments.tex:70 | 0.71 | OK | 0.90 | OK |
| abstract.tex:4 | 0.71 | OK | — | — |
| introduction.tex:36 | 0.71 | OK | — | — |

**Yi-1.5: 全部匹配**

#### 5. Mistral-7B-v0.3 — conc=0.22, t1/t5=0.18 (真值 0.2200, 0.1820)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:23 | 0.22 | OK | 0.18 | OK |
| analysis.tex:47 (table) | 0.22 | OK | 0.18 | OK |
| analysis.tex:65 | 0.22 | OK | — | — |

**Mistral: 全部匹配**

#### 6. Gemma-2-9B — conc=0.23, t1/t5=0.18 (真值 0.2299, 0.1757)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:23 | 0.23 | OK | **0.18** | **MISMATCH** |
| analysis.tex:48 (table) | 0.23 | OK | **0.18** | **MISMATCH** |
| analysis.tex:65 | 0.23 | OK | — | — |
| experiments.tex:74 | 0.23 | OK | — | — |

**Gemma-2 t1/t5: 真值 0.1757，四舍五入 0.18。** .tex 写 0.18——实际上这在两位四舍五入精度下是可接受的（0.1757 → 0.18）。但注意 Mistral 真值 0.1820 也写为 0.18，两者在 .tex 中显示为相同值，而实际上 Mistral=0.182 vs Gemma=0.176 有区别。如果要保持区分度，Gemma 应写 0.18，Mistral 也是 0.18——在两位精度下确实相同。

**Gemma-2: 在两位四舍五入精度下匹配**

#### 7. Pythia-1.4B — conc=0.24, t1/t5=0.12 (真值 0.2439, 0.1183)

| 位置 | .tex conc | Match? | .tex t1/t5 | Match? |
|---|---|---|---|---|
| analysis.tex:26 | 0.24 | OK | 0.12 | OK |
| analysis.tex:49 (table) | 0.24 | OK | 0.12 | OK |
| analysis.tex:65 | 0.24 | OK | — | — |

**Pythia: 全部匹配**

---

### 汇总

| Model | .tex conc | 真值 conc | conc Match? | .tex t1/t5 | 真值 t1/t5 | t1/t5 Match? |
|---|---|---|---|---|---|---|
| Qwen2.5-7B | 0.61 | 0.6104 | OK | 0.57 | 0.5670 | OK |
| Qwen2.5-14B | 0.33 | 0.3312 | OK | 0.57 | 0.5693 | OK |
| Llama-3.1-8B | 0.34 | 0.3387 | OK | 0.71 | 0.7139 | OK |
| Yi-1.5-9B | 0.71 | 0.7139 | OK | 0.90 | 0.9012 | OK |
| Mistral-7B-v0.3 | 0.22 | 0.2200 | OK | 0.18 | 0.1820 | OK |
| Gemma-2-9B | 0.23 | 0.2299 | OK | 0.18 | 0.1757 | OK (borderline) |
| Pythia-1.4B | 0.24 | 0.2439 | OK | 0.12 | 0.1183 | OK |

**结论：所有 7 个模型的 concentration 和 t1/t5 值在 .tex 中均与 hires bf16 真值匹配（两位小数四舍五入精度）。未发现 lowres 残留。**

关于你提到的 "Llama concentration 0.34 是 lowres，正确 hires=0.57"——根据你提供的真值表，Llama hires top5%conc 就是 **0.3387**（≈0.34），0.57 是 Qwen 的 t1/t5。Llama 的 .tex 值 0.34 是正确的。如果你手头有不同的 Llama hires 真值，请核实 shape_metrics.json 原始数据。

---
