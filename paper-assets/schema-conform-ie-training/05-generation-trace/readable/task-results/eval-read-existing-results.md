# eval read existing results

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_read_existing_results_20260513T155106_result.json`
- **Structured JSON:** [`309beee438f0264a5fab.json`](../../sessions/30/309beee438f0264a5fab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件均完整读取，文件信息：

| 文件 | 大小 | 修改时间 |
|------|------|----------|
| eval_D2_ckpt400 | 2596 bytes | May 13 20:09 |
| eval_D2_final | 2594 bytes | May 13 22:08 |
| eval_D1_v4 | 2588 bytes | May 13 22:22 |

---

## eval_D2_ckpt400

### scierc_test (n=551)
| 指标 | mean |
|------|------|
| entity_f1 | 0.5325 |
| relation_f1 | 0.2379 |
| f1_correctness | 0.3912 |
| structural_validity | 1.0 |
| type_conformance | 0.9873 |
| relational_constraint | 0.918 |
| structural_completeness | 0.9873 |
| valid_json_rate | 1.0 |

### crossner_politics (n=651)
| 指标 | mean |
|------|------|
| entity_f1 | 0.478 |
| relation_f1 | 0.0 |
| f1_correctness | 0.4744 |
| structural_validity | 1.0 |
| type_conformance | 0.9971 |
| relational_constraint | 0.0 |
| structural_completeness | 0.989 |
| valid_json_rate | 1.0 |

### crossner_science (n=543)
| 指标 | mean |
|------|------|
| entity_f1 | 0.6057 |
| relation_f1 | 0.0 |
| f1_correctness | 0.5753 |
| structural_validity | 0.9982 |
| type_conformance | 0.9793 |
| relational_constraint | 0.0 |
| structural_completeness | 0.9561 |
| valid_json_rate | 0.9982 |

---

## eval_D2_final

### scierc_test (n=551)
| 指标 | mean |
|------|------|
| entity_f1 | 0.5211 |
| relation_f1 | 0.2363 |
| f1_correctness | 0.3844 |
| structural_validity | 1.0 |
| type_conformance | 0.98 |
| relational_constraint | 0.9298 |
| structural_completeness | 0.98 |
| valid_json_rate | 1.0 |

### crossner_politics (n=651)
| 指标 | mean |
|------|------|
| entity_f1 | 0.4821 |
| relation_f1 | 0.0 |
| f1_correctness | 0.4764 |
| structural_validity | 1.0 |
| type_conformance | 0.997 |
| relational_constraint | 0.0 |
| structural_completeness | 0.9878 |
| valid_json_rate | 1.0 |

### crossner_science (n=543)
| 指标 | mean |
|------|------|
| entity_f1 | 0.6053 |
| relation_f1 | 0.0 |
| f1_correctness | 0.5699 |
| structural_validity | 0.9982 |
| type_conformance | 0.9711 |
| relational_constraint | 0.0 |
| structural_completeness | 0.9544 |
| valid_json_rate | 0.9982 |

---

## eval_D1_v4

### scierc_test (n=551)
| 指标 | mean |
|------|------|
| entity_f1 | 0.4966 |
| relation_f1 | 0.2913 |
| f1_correctness | 0.3924 |
| structural_validity | 1.0 |
| type_conformance | 1.0 |
| relational_constraint | 0.972 |
| structural_completeness | 1.0 |
| valid_json_rate | 1.0 |

### crossner_politics (n=651)
| 指标 | mean |
|------|------|
| entity_f1 | 0.4783 |
| relation_f1 | 0.0 |
| f1_correctness | 0.3069 |
| structural_validity | 0.9923 |
| type_conformance | 0.9209 |
| relational_constraint | 0.0 |
| structural_completeness | 0.6714 |
| valid_json_rate | 0.9923 |

### crossner_science (n=543)
| 指标 | mean |
|------|------|
| entity_f1 | 0.628 |
| relation_f1 | 0.0 |
| f1_correctness | 0.384 |
| structural_validity | 0.9982 |
| type_conformance | 0.8589 |
| relational_constraint | 0.0 |
| structural_completeness | 0.7221 |
| valid_json_rate | 0.9982 |

---
