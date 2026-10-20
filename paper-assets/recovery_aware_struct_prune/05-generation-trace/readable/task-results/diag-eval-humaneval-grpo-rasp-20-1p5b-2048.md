# diag eval humaneval grpo rasp 20 1p5b 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval_humaneval_grpo_rasp_20_1p5b_2048_20260519T183658_result.json`
- **Structured JSON:** [`4b2087c36225d4d90a73.json`](../../sessions/4b/4b2087c36225d4d90a73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 失败根因

**模型路径错误**：`--model_path` 指向 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/`，但该目录下没有模型和 tokenizer 文件。实际文件在 `checkpoint-100/` 子目录中。

## 完整 Traceback

```
Traceback (most recent call last):
  File "/root/recovery_aware_struct_prune/src/eval_humaneval.py", line 211, in &lt;module>
    main()
  File "/root/recovery_aware_struct_prune/src/eval_humaneval.py", line 167, in main
    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
  File ".../transformers/tokenization_utils_base.py", line 1933, in _from_pretrained
    tokenizer = cls(*init_inputs, **init_kwargs)
ValueError: Couldn't instantiate the backend tokenizer from one of:
(1) a `tokenizers` library serialization file,
(2) a slow tokenizer instance to convert or
(3) an equivalent slow tokenizer class to instantiate and convert.
You need to have sentencepiece or tiktoken installed to convert a slow tokenizer to a fast one.
```

## 目录结构

```
grpo_rasp_20_1p5b/
├── README.md              ← 仅 README，无模型文件
├── checkpoint-100/        ← 实际模型和 tokenizer 在这里
│   ├── config.json
│   ├── model.safetensors
│   ├── tokenizer.json
│   └── tokenizer_config.json
└── completions/
```

tiktoken 和 sentencepiece 均已安装，不是缺包问题。

## 修复方案

将 `--model_path` 改为指向 checkpoint 子目录：

```
--model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/checkpoint-100
```

---
