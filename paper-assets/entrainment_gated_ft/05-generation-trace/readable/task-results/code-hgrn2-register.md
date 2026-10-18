# code hgrn2 register

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_hgrn2_register_20260518T142924_result.json`
- **Structured JSON:** [`896aa1e57cbc2730f8c5.json`](../../sessions/89/896aa1e57cbc2730f8c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载进度正常，约 20-40 MB/s 聚合速度。预计 ~5-10 分钟完成 HGRN2-pure 的 4.65GB。后续还有 3 个模型要补。

让我汇报当前完成的产出。

---

## 产出汇总

### 1. 脚本关键变更 (`/root/entrainment_gated_ft/run_lmeval_clean.py`)

三处修改：
- **Import**: 添加 `from fla.models.hgrn2 import HGRN2Config, HGRN2ForCausalLM`
- **注册**: `AutoConfig.register("hgrn2", HGRN2Config)` + `AutoModelForCausalLM.register(HGRN2Config, HGRN2ForCausalLM)`
- **`_tied_weights_keys` monkey-patch**: `HGRN2ForCausalLM._tied_weights_keys = {"lm_head.weight": "model.embeddings.weight"}` — fla 的 HGRN2 将此定义为 `list`，transformers 5.8.1 的 `post_init()` 期望 `dict`，不 patch 会崩

原有的通用 tying 修复 (`if tie_word_embeddings: model.lm_head.weight = model.model.embeddings.weight`) 自动覆盖 HGRN2，无需额外处理。

### 2. Smoke test 结果

**HGRN2-hybrid-12-1**（完整模型）:
- 加载成功，`_tied_weights_keys` dict patch 解决了 `AttributeError: 'list' object has no attribute 'keys'`
- 加载后权重已自动 tied（`data_ptr()` 相同），脚本的手动 tying 作为 safety net 仍会执行

### 3. HGRN2 × lambada 评测结果

```
Model: 1.3B-100B-HGRN2-hybrid-12-1
lambada_openai: acc=0.5030, ppl=10.28
```

ppl=10.28，在合理范围（10-50），确认 tying 修复正确生效。

### 4. 发现的问题

**模型文件不完整**：4 个模型缺失 safetensors shard（下载脚本的 skip 逻辑有 bug：只检查是否存在任何 `.safetensors` 文件，不验证完整性）：
- `1.3B-100B-HGRN2-pure`: 缺 shard-1（主权重 ~4.65GB）
- `1.3B-100B-HGRN2-hybrid-3-1`: 缺 shard-2
- `1.3B-100B-HGRN2-hybrid-6-1`: 缺 shard-2
- `1.3B-100B-RetNet-hybrid-24-1`: 缺 shard-1

已启动后台修复下载（PID 316952, `/tmp/fix_downloads.py`），进度可通过 `cat /tmp/fix_downloads.log` 查看。HGRN2-pure 正在下载中（~270MB/4.65GB），其余三个排队中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "lm_head.weight": "model.embeddings.weight"
  }
}
```

</details>

---
