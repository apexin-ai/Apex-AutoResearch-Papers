# diagnose eval no evi failure

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-no-evi-failure_20260520T112726_result.json`
- **Structured JSON:** [`a90763599e318c5749f3.json`](../../sessions/a9/a90763599e318c5749f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：

### 失败原因

**不是 tokenizer 库缺失，而是 SCP 嵌套导致路径错误。**

日志显示 eval 尝试从 `/root/autodl-tmp/sft_output_llama_3_1_8b` 加载 tokenizer，但该目录下没有任何模型文件——只有一个同名子目录 `sft_output_llama_3_1_8b/`。`AutoTokenizer.from_pretrained` 找不到 tokenizer 文件，报 `ValueError`。

### sft_output_llama_3_1_8b 目录结构 — 嵌套确认

```
/root/autodl-tmp/sft_output_llama_3_1_8b/
└── sft_output_llama_3_1_8b/          ← SCP 嵌套
    ├── adapter_model.safetensors
    ├── adapter_config.json
    ├── tokenizer.json / tokenizer_config.json
    ├── checkpoint-190/
    └── checkpoint-570/
```

Adapter 实际路径：`/root/autodl-tmp/sft_output_llama_3_1_8b/sft_output_llama_3_1_8b/adapter_model.safetensors`

### 其他 SCP 目录 — 同样嵌套

| 目录 | 嵌套情况 |
|------|---------|
| `sft_output_14b/` | `sft_output_14b/sft_output_14b/` |
| `rsft_generations_14b/` | `rsft_generations_14b/rsft_generations_14b/` |

SCP 嵌套是系统性问题，所有 SCP 传输的目录都受影响。

### LLaMA SFT s43 状态

正常训练中，进度 62/570 steps (~11%)，~4.2s/step。

### 修复方案

最简单：在服务器上 `mv` 把内层内容提到外层：
```bash
# 以 sft_output_llama_3_1_8b 为例
mv /root/autodl-tmp/sft_output_llama_3_1_8b/sft_output_llama_3_1_8b/* /root/autodl-tmp/sft_output_llama_3_1_8b/
rmdir /root/autodl-tmp/sft_output_llama_3_1_8b/sft_output_llama_3_1_8b
```

三个目录都需要做。或者修复 SCP 命令源头（用 `scp -r local_dir/* remote:path/` 而非 `scp -r local_dir remote:path/`）。

---
