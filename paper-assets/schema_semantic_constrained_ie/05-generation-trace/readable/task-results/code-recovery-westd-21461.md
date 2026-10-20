# code recovery westd 21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_recovery_westd_21461_20260518T021622_result.json`
- **Structured JSON:** [`97d897e117e5cf9f5108.json`](../../sessions/97/97d897e117e5cf9f5108.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整报告。

---

## 服务器状态报告 (westd-21461)

### GPU 状态
| GPU | 显存使用 | 利用率 | 运行任务 |
|-----|---------|--------|---------|
| cuda:0 | 31.8 / 97.9 GB | 73% | Mistral v2 16K retry |
| cuda:1 | 18.9 / 97.9 GB | 87% | Qwen grammar_only |

### tmux Sessions
| Session | 状态 |
|---------|------|
| `mistral_v2_retry_16k` | **运行中** — Mistral 16K retry |
| `qwen_grammar_only` | **运行中** — Qwen 刚加载完模型，开始推理 |
| `mistral_restart` | 空闲（已完成） |
| `mistral_wikievents` | 已完成（unconstrained 12 docs） |

### 输出文件
| 文件 | 行数 | 最后修改 | 状态 |
|------|------|---------|------|
| `ee_mistral_wikievents_constrained_v2_full.jsonl` | 190/246 | 10:14 | **运行中**（16K retry） |
| `ee_mistral_wikievents_constrained_v2_full.jsonl.bak_before16k` | 246 | 09:44 | 备份（v2 4K 完整结果） |
| `ee_qwen_wikievents_grammar_only.jsonl` | 46/246 | 10:15 | **运行中** |
| `mistral_constrained_full.jsonl` | 246 | 07:22 | **已完成**（v1 grammar_only） |
| `wikievents_mistral_unconstrained_full.jsonl` | 246 | 04:32 | **已完成** |

---

### 已完成实验结果

#### 1. Mistral v1 grammar_only (`mistral_constrained_full.jsonl`, 246 docs)
**Violation Check:** 184 checked, 62 parse failures
| Violation | Count | Rate |
|-----------|-------|------|
| RoV | 2314 | 54.8% |
| AC | 813 | 19.2% |
| CF | 33 | 0.7% |
| **Go/No-go** | | **0.7405** |

**Eval:** Entity F1=0.1271, Trigger F1=0.0468, Argument F1=0.0042

#### 2. Mistral v2 constrained 4K（备份, 246 docs, 68 parse failures）
**Violation Check:** 178 checked, 68 parse failures
| Violation | Count | Rate |
|-----------|-------|------|
| RoV | 2 | 0.1% |
| AC | 667 | 16.6% |
| CF | 642 | 13.9% |
| **Go/No-go** | | **0.1666** |

**Eval:** Entity F1=0.1245, Trigger F1=0.0508, Argument F1=0.0047

#### 3. Mistral v2 constrained 16K retry（进行中, 190/246 docs, 3 parse failures）
**Violation Check:** 187 checked, **仅 3 parse failures**（从 68 降至 3）
| Violation | Count | Rate |
|-----------|-------|------|
| RoV | 17 | 0.4% |
| AC | 770 | 16.8% |
| CF | 690 | 13.6% |
| **Go/No-go** | | **0.1718** |

**Eval:** Entity F1=0.1221, Trigger F1=0.0466, Argument F1=0.0042

---

### 关键发现

1. **16K retry 大幅减少 parse failures**: 68 → 3（12 docs retried so far, 56 remaining）
2. **v2 constrained vs v1 grammar_only**: RoV 从 54.8% 降至 0.1-0.4%，说明 v2 schema 约束有效控制了 role vocab violations
3. **AC violations 仍然高** (~16-17%)，v1 和 v2 都未解决
4. **所有方法的 eval F1 极低**: Entity ~12%, Trigger ~5%, Argument <1%，可能是 eval 脚本与输出格式对齐问题
5. **Unconstrained 文件格式不兼容** eval 脚本（list vs dict），需要适配
6. 诊断脚本 `diagnose_entity_type_tokens.py` 不存在

### 建议下一步
1. **等待两个运行中任务完成**（Mistral 16K retry 还剩 ~56 docs, Qwen grammar_only 还剩 ~200 docs）
2. **排查 eval F1 极低的原因** — 可能是输出格式与 gold 标注的 schema 不匹配，需要检查 eval 脚本的解析逻辑
3. **解决 AC violations 16-17%** — 这是当前 constrained decoding 的主要瓶颈
4. **统一 unconstrained 输出格式** 使其兼容 eval 脚本，以获得可比较的 baseline

---
