# code implement random injector

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_implement-random-injector_20260514T103238_result.json`
- **Structured JSON:** [`a58861478446c965dada.json`](../../sessions/a5/a58861478446c965dada.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实现完成。总结：

---

### 产出文件

**`injection/random_injector.py`** — RandomInjector 实现

### 扰动类型（6 种，均匀随机选择）

| 扰动 | 效果 | 对应 TaxEI |
|------|------|-----------|
| `swap_adjacent` | 交换相邻两步 | 类似 P1，但不限 window |
| `delete_step` | 删除随机一步 | 类似 P2，但不定向 critical action |
| `truncate_prefix` | 截断早期历史 | 类似 C1，但 ratio 随机 |
| `mask_observation` | 替换 observation 为通用文本 | 类似 C4，但不限 max_masks |
| `replace_action_target` | 替换 action 中的对象/容器名 | TaxEI 无对应 |
| `shuffle_segment` | 打乱连续 2-4 步的顺序 | TaxEI 无对应 |

### 公平性约束如何保证

- **注入数量**：pipeline 的 `plan_injections()` 按 `num_variants` 分配，与 mode 无关。`--mode random --num_variants 800` 生成与 TaxEI 组相同数量的 800 条。
- **注入位置**：使用同一个 `select_injection_point()` 函数，位置分布一致。
- **Recovery teacher**：同一个 `call_recovery_api()`，同一个 GPT-5.2 模型。

### Pipeline 调用

```bash
# Random baseline
python data/inject_and_generate.py --mode random --num_variants 800 --dry_run

# TaxEI (默认，不变)
python data/inject_and_generate.py --mode taxei --num_variants 800 --dry_run
```

### 验证结果
- 100/100 inject+validate 通过
- formatter 兼容性通过
- pipeline dry-run 19/20 成功（1 个失败是短轨迹 margin 限制，TaxEI 也一样）

---
