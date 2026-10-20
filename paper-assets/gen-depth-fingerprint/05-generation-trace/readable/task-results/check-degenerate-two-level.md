# check degenerate two level

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_degenerate-two-level_20260516T101139_result.json`
- **Structured JSON:** [`90d1c8abd39627fcf56e.json`](../../sessions/90/90d1c8abd39627fcf56e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果：

---

## Llama-3.2-3B rp=1.0

| Depth | Total | Strict Degen | Soft Degen | Usable |
|-------|-------|-------------|-----------|--------|
| 0     |   593 |    0 ( 0.0%) |    0 ( 0.0%) |  593 (100.0%) |
| 1     |   585 |    0 ( 0.0%) |   31 ( 5.3%) |  554 (94.7%) |
| 2     |   559 |   14 ( 2.5%) |  157 (28.1%) |  388 (69.4%) |
| 3     |   531 |   26 ( 4.9%) |  258 (48.6%) |  247 (46.5%) |
| 4     |   511 |   33 ( 6.5%) |  294 (57.5%) |  184 (36.0%) |
| ALL   |  2779 |   73 (2.6%) |  740 (26.6%) | 1966 (70.7%) |

**Extrapolation to 995 seeds:**
- Depth 2: projected usable = 651 **[OK]**
- Depth 3: projected usable = 414 **[INSUFFICIENT]**
- Depth 4: projected usable = 308 **[INSUFFICIENT]**

**Depth 2+ Usable Samples:**

[Sample 1] depth=2, seed=1, unique_ratio=0.504, 4gram_repeat=0.038
> Text: theta )\sin \theta \,d\theta }$ where ${\displaystyle R_{s}}$ is the spectral albedo, ${\displaystyle \lambda }$ is the wavelength and ${\displaystyle \theta }$ is the zenith angle of the Sun. The geometric albedo is the ratio of the reflected solar radiation to the radiation incident on the surfac...

[Sample 2] depth=3, seed=1, unique_ratio=0.543, 4gram_repeat=0.011
> Text: ${\displaystyle \rho }$ is the surface reflectance ${\displaystyle \tau }$ is the surface transmittance. These quantities are important in planetary science, where they are used to describe the reflectance of the surface, atmosphere, and the combined reflectance of both. ## Surface albedo in pla...

[Sample 3] depth=4, seed=1, unique_ratio=0.267, 4gram_repeat=0.335
> Text: 0.3. The Earth's surface reflects about 30% of the incoming solar radiation, and the remaining 70% is absorbed by the atmosphere. The albedo of the Earth's surface varies from about 0.05 in the polar regions to about 0.4 in the equatorial regions. ### Moon The albedo of the Moon is about 0.1. The ...

---

## Mistral-7B rp=1.0

| Depth | Total | Strict Degen | Soft Degen | Usable |
|-------|-------|-------------|-----------|--------|
| 0     |   626 |    0 ( 0.0%) |    0 ( 0.0%) |  626 (100.0%) |
| 1     |   626 |    2 ( 0.3%) |   12 ( 1.9%) |  612 (97.8%) |
| 2     |   604 |    5 ( 0.8%) |   72 (11.9%) |  527 (87.3%) |
| 3     |   595 |   14 ( 2.4%) |  153 (25.7%) |  428 (71.9%) |
| 4     |   579 |   16 ( 2.8%) |  214 (37.0%) |  349 (60.3%) |
| ALL   |  3030 |   37 (1.2%) |  451 (14.9%) | 2542 (83.9%) |

**Extrapolation to 995 seeds:**
- Depth 2: projected usable = 837 **[OK]**
- Depth 3: projected usable = 680 **[OK]**
- Depth 4: projected usable = 554 **[OK]**

**Depth 2+ Usable Samples:**

[Sample 1] depth=2, seed=0, unique_ratio=0.443, 4gram_repeat=0.197
> Text: and 18th centuries, the word was used to describe a state of nature, without government or law, and it was used in this sense by the French philosopher Jean-Jacques Rousseau in his 1762 book, The Social Contract.^{[2]} The word was later used by William Godwin in his 1793 book An Enquiry Concerning ...

[Sample 2] depth=3, seed=0, unique_ratio=0.561, 4gram_repeat=0.054
> Text: also used it to describe a society without property.^{[6]} In 1884, the English writer William Morris used the word to describe a society without government or law, and he also used it to describe a society without property.^{[7]} ### 19th century In 1863, the French anarchist Pierre-Joseph Proudh...

[Sample 3] depth=4, seed=0, unique_ratio=0.508, 4gram_repeat=0.067
> Text: of land and of other natural monopolies should be vested in the community at large, and not in private individuals".^{[10]} In 1918, the German economist and sociologist Max Weber wrote "The term Socialism is in any case ambiguous in the extreme. In the most general sense it means the negation of c...

---

## Gemma-2-2B rp=1.0 (对比)

| Depth | Total | Strict Degen | Soft Degen | Usable |
|-------|-------|-------------|-----------|--------|
| 0     |   582 |    0 ( 0.0%) |    0 ( 0.0%) |  582 (100.0%) |
| 1     |   581 |   61 (10.5%) |  503 (86.6%) |   17 ( 2.9%) |
| 2     |   580 |   77 (13.3%) |  489 (84.3%) |   14 ( 2.4%) |
| 3     |   580 |   79 (13.6%) |  488 (84.1%) |   13 ( 2.2%) |
| 4     |   580 |   79 (13.6%) |  487 (84.0%) |   14 ( 2.4%) |
| ALL   |  2903 |  296 (10.2%) | 1967 (67.8%) |  640 (22.0%) |

**Extrapolation to 995 seeds:**
- Depth 2: projected usable = 23 **[INSUFFICIENT]**
- Depth 3: projected usable = 22 **[INSUFFICIENT]**
- Depth 4: projected usable = 23 **[INSUFFICIENT]**

---

## 结论

| Generator | Depth 2 | Depth 3 | Depth 4 | 判定 |
|-----------|---------|---------|---------|------|
| **Mistral-7B rp=1.0** | 837 OK | 680 OK | 554 OK | **全部可用** |
| **Llama-3.2-3B rp=1.0** | 651 OK | 414 ✗ | 308 ✗ | **Depth 3+ 不足** |
| Gemma-2-2B rp=1.0 | 23 ✗ | 22 ✗ | 23 ✗ | 严重退化，不可用 |

**Mistral rp=1.0 确认可用**——所有 depth 外推后都 ≥500。

**Llama rp=1.0 仅 depth 2 可用**，depth 3/4 的 soft degeneration（4-gram 重复率 >50%）太严重，分别只有 46.5% 和 36.0% 的样本能通过两级过滤。Llama 的 depth 4 样本虽然"通过"了过滤（如 Sample 3），但 unique_ratio=0.267 + 4gram_repeat=0.335 已经很边缘。

---
