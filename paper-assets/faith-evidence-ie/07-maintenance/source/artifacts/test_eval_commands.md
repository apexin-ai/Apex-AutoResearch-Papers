# Test Set Eval: 诊断 + 命令模板 + 代码修改方案

## 1. plan_002_test_eval_s44 失败诊断

**根因**：`DocREDProcessor.process("test")` 返回 0 samples。

test.json 结构：1000 docs，keys = `[vertexSet, title, sents]`，**无 `labels` 字段**。
`process()` 遍历 `doc.get("labels", [])` 构建 RelationSample → test split 得到 0 样本 → 0 eval items → 0 inference → 全部指标为 0。

日志确认（`/root/autodl-tmp/eval_results/test_rsft_s44.log`）：
```
Processed 0 relation samples from 1000 documents
Prepared 0 eval documents, 0 gold triples
Inference: 0.0s (0.00 s/doc)
F1: 0.0000
```

**结论**：不是运行时错误，是代码逻辑不支持 test split。

---

## 2. 必需的代码修改

### 2.1 `eval/inference.py`：新增 `prepare_test_data()`

test split 无 labels，需要直接从 `vertexSet` 构建 entity list + prompt，不依赖 RelationSample。

```python
def prepare_test_data(data_dir, tokenizer, include_evidence=True, system_prompt=SYSTEM_PROMPT):
    """Test split: 从 vertexSet 构建 prompt，不依赖 labels。"""
    test_file = Path(data_dir) / SPLIT_FILENAMES["test"]
    with open(test_file) as f:
        raw_docs = json.load(f)

    eval_items = []
    for doc in raw_docs:
        doc_id = doc.get("title", "")
        sents = [" ".join(s) for s in doc["sents"]]
        vertex_set = doc["vertexSet"]

        numbered_sents = "\n".join(f"[{i}] {s}" for i, s in enumerate(sents))

        entity_list = set()
        for entity in vertex_set:
            name = entity[0]["name"]
            etype = entity[0].get("type", "UNK")
            entity_list.add(f"{name} ({etype})")
        entity_str = ", ".join(sorted(entity_list))

        if include_evidence:
            instruction = (
                "Extract all relation triples from the document. "
                "For each triple, provide the head entity, relation, tail entity, "
                "and the sentence IDs that serve as evidence. "
                "Output as a JSON list."
            )
        else:
            instruction = (
                "Extract all relation triples from the document. "
                "For each triple, provide the head entity, relation, and tail entity. "
                "Output as a JSON list."
            )

        input_text = f"Document:\n{numbered_sents}\n\nEntities: {entity_str}"
        prompt = build_prompt(tokenizer, instruction, input_text, system_prompt=system_prompt)
        eval_items.append({"doc_id": doc_id, "prompt": prompt})

    logger.info("Prepared %d test documents for inference", len(eval_items))
    return eval_items, raw_docs
```

### 2.2 `eval/inference.py`：新增 `convert_to_codalab()`

DocRED test set 通过 CodaLab 评测，提交格式为 `[{title, h_idx, t_idx, r, evidence}, ...]`。

```python
def convert_to_codalab(raw_results, raw_docs):
    """将模型预测转换为 CodaLab 提交格式。"""
    from freige.data.docred_processor import DOCRED_REL_INFO
    rel_name_to_code = {v.lower().strip(): k for k, v in DOCRED_REL_INFO.items()}

    doc_entity_map = {}
    for doc in raw_docs:
        doc_id = doc.get("title", "")
        name_to_idx = {}
        for idx, entity in enumerate(doc["vertexSet"]):
            name = entity[0]["name"].lower().strip()
            if name not in name_to_idx:
                name_to_idx[name] = idx
        doc_entity_map[doc_id] = name_to_idx

    submissions = []
    for r in raw_results:
        doc_id = r["doc_id"]
        name_to_idx = doc_entity_map.get(doc_id, {})
        for triple in r["parsed_triples"]:
            h_name = triple["head"].lower().strip()
            t_name = triple["tail"].lower().strip()
            rel_name = triple["relation"].lower().strip()

            h_idx = name_to_idx.get(h_name)
            t_idx = name_to_idx.get(t_name)
            r_code = rel_name_to_code.get(rel_name)

            if h_idx is None or t_idx is None or r_code is None:
                continue

            entry = {
                "title": doc_id,
                "h_idx": h_idx,
                "t_idx": t_idx,
                "r": r_code,
                "evidence": triple.get("evidence", []),
            }
            submissions.append(entry)

    return submissions
```

### 2.3 `eval/inference.py` `main()` 修改

```python
# 替换 prepare_eval_data 调用处
if args.split == "test":
    eval_items, raw_docs = prepare_test_data(
        args.data_path, tokenizer,
        include_evidence=_include_evi, system_prompt=_sys_prompt,
    )
    gold, gold_by_doc = [], {}
else:
    eval_items, gold, gold_by_doc = prepare_eval_data(
        args.data_path, args.split, tokenizer,
        include_evidence=_include_evi, system_prompt=_sys_prompt,
    )

# ... run_inference 不变 ...

# 替换 evaluate 调用处
if args.split == "test":
    metrics = {"note": "test split - submit to CodaLab for evaluation"}
    # CodaLab 提交文件
    codalab_preds = convert_to_codalab(raw_results, raw_docs)
    codalab_path = output_dir / "codalab_submission.json"
    with open(codalab_path, "w") as f:
        json.dump(codalab_preds, f, ensure_ascii=False)
    logger.info("CodaLab submission → %s (%d predictions)", codalab_path, len(codalab_preds))
else:
    metrics = evaluate(all_predictions, gold, raw_outputs_for_eval, args.data_path, args.split)

# 保存 metrics/predictions 不变，但 test split 的控制台汇总需调整
if args.split == "test":
    print("\n" + "=" * 50)
    print(f"  Test Documents: {n_total}")
    print(f"  Predictions:    {len(all_predictions)}")
    print(f"  CodaLab file:   {len(codalab_preds)} entries")
    print(f"  Format OK:      {n_format_ok}/{n_total} ({metrics.get('format_ok_rate', 0):.1%})")
    print(f"  Truncated:      {n_truncated}/{n_total}")
    print("=" * 50)
else:
    # 原有的 dev 汇总打印
    ...
```

---

## 3. 命令模板（代码修改后可用）

### D076 统一协议参数
- batch_size=4, max_new_tokens=1024, --no-quantize, seed=42
- 必须 CUDA_VISIBLE_DEVICES=X（C002 约束）
- 提交前 nvidia-smi 确认目标 GPU 空闲（C001 约束）

### 3.1 SFT Baseline Test Eval
```bash
CUDA_VISIBLE_DEVICES=0 nohup python -m freige.eval.inference \
    --model_path /root/autodl-tmp/sft_output \
    --data_path /root/autodl-tmp/data/docred \
    --output_dir /root/autodl-tmp/eval_results/test_sft_baseline \
    --batch_size 4 --max_new_tokens 1024 --no-quantize \
    --split test --seed 42 \
    > ~/runs/faith-evidence-ie/test_sft_baseline.log 2>&1 &
```

### 3.2 RSFT CED (best seed) Test Eval
```bash
CUDA_VISIBLE_DEVICES=0 nohup python -m freige.eval.inference \
    --model_path /root/autodl-tmp/rsft_output_ced_s43 \
    --sft_adapter /root/autodl-tmp/sft_output \
    --data_path /root/autodl-tmp/data/docred \
    --output_dir /root/autodl-tmp/eval_results/test_rsft_ced_s43 \
    --batch_size 4 --max_new_tokens 1024 --no-quantize \
    --split test --seed 42 \
    > ~/runs/faith-evidence-ie/test_rsft_ced_s43.log 2>&1 &
```

### 3.3 RSFT Flat-NLI (best seed s44) Test Eval
```bash
CUDA_VISIBLE_DEVICES=0 nohup python -m freige.eval.inference \
    --model_path /root/autodl-tmp/rsft_output_flat_nli_s44/checkpoint-507 \
    --sft_adapter /root/autodl-tmp/sft_output \
    --data_path /root/autodl-tmp/data/docred \
    --output_dir /root/autodl-tmp/eval_results/test_rsft_flat_nli_s44 \
    --batch_size 4 --max_new_tokens 1024 --no-quantize \
    --split test --seed 42 \
    > ~/runs/faith-evidence-ie/test_rsft_flat_nli_s44.log 2>&1 &
```

### 3.4 GRPO CED (kl001 best checkpoint) Test Eval
```bash
CUDA_VISIBLE_DEVICES=0 nohup python -m freige.eval.inference \
    --model_path /root/autodl-tmp/grpo_ced_kl001/checkpoint-100 \
    --sft_adapter /root/autodl-tmp/sft_output \
    --data_path /root/autodl-tmp/data/docred \
    --output_dir /root/autodl-tmp/eval_results/test_grpo_ced_kl001 \
    --batch_size 4 --max_new_tokens 1024 --no-quantize \
    --split test --seed 42 \
    > ~/runs/faith-evidence-ie/test_grpo_ced_kl001.log 2>&1 &
```

### 3.5 GRPO G8-BF16 (plan_011 best) Test Eval
```bash
CUDA_VISIBLE_DEVICES=0 nohup python -m freige.eval.inference \
    --model_path /root/autodl-tmp/grpo_ced_g8_bf16/checkpoint-100 \
    --sft_adapter /root/autodl-tmp/sft_output \
    --data_path /root/autodl-tmp/data/docred \
    --output_dir /root/autodl-tmp/eval_results/test_grpo_g8_bf16 \
    --batch_size 4 --max_new_tokens 1024 --no-quantize \
    --split test --seed 42 \
    > ~/runs/faith-evidence-ie/test_grpo_g8_bf16.log 2>&1 &
```

---

## 4. 预估运行时间

Dev split (985 docs, batch_size=4, no-quantize): ~60min (SFT) / ~2.5h (RSFT/GRPO with adapter)
Test split (1000 docs): 类似 dev，预估 ~60-170min 每个模型。

## 5. 提交 Checklist

1. [ ] 代码修改：`prepare_test_data()` + `convert_to_codalab()` + `main()` 分支
2. [ ] 本地 dry-run：`--split test` 跑 1 个 batch 验证 prompt 构建正确
3. [ ] nvidia-smi 确认 GPU 空闲（C001）
4. [ ] CUDA_VISIBLE_DEVICES 显式设置（C002）
5. [ ] nohup 后台运行 + 日志路径
6. [ ] CodaLab 提交文件格式验证
