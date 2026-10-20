# Training Configuration (Appendix)

## Fine-tuning Hyperparameters

All models are fine-tuned using LLaMA Factory with LoRA (SFT stage). Both models share identical hyperparameters except for the base model and chat template.

| Parameter | Qwen3-8B | LLaMA-3.1-8B |
|-----------|----------|---------------|
| Base model | Qwen/Qwen3-8B | Meta-Llama-3.1-8B-Instruct |
| Fine-tuning method | LoRA (SFT) | LoRA (SFT) |
| LoRA rank (*r*) | 32 | 32 |
| LoRA alpha (*α*) | 64 | 64 |
| LoRA dropout | 0.0 | 0.0 |
| Target modules | all (q, k, v, o, gate, up, down proj) | all (q, k, v, o, gate, up, down proj) |
| Learning rate | 2 × 10⁻⁴ | 2 × 10⁻⁴ |
| LR scheduler | cosine | cosine |
| Warmup ratio | 0.1 | 0.1 |
| Per-device batch size | 2 | 2 |
| Gradient accumulation steps | 8 | 8 |
| Effective batch size | 16 | 16 |
| Epochs | 5 | 5 |
| Max sequence length | 2048 | 2048 |
| Precision | bf16 | bf16 |
| Gradient checkpointing | ✓ | ✓ |
| Max gradient norm | 1.0 | 1.0 |
| Optimizer | AdamW (default) | AdamW (default) |
| Weight decay | 0 (default) | 0 (default) |
| Eval strategy | every 100 steps | every 100 steps |
| Save strategy | every 100 steps (keep best 3) | every 100 steps (keep best 3) |
| Chat template | qwen3 | llama3 |
| Seed | 42 | 42 |

### Dataset-Specific Variations (CoNLL-2003, WNUT-17)

For CoNLL-2003 and WNUT-17, all models use the same LoRA and optimizer settings above, with the following changes:

| Parameter | CoNLL-2003 | WNUT-17 |
|-----------|-----------|---------|
| Eval/save interval | 200 steps | 200 steps |
| Save total limit | 5 | 5 |
| Load best model at end | ✓ (by eval_loss) | ✓ (by eval_loss) |
| Qwen3 enable_thinking | false | false |

## Dataset Statistics (SciERC)

| Split | Sentences |
|-------|-----------|
| Train | 1,861 |
| Dev | 275 |
| Test | 551 |

Data format: ShareGPT (LLaMA Factory). Each instance is a single-turn conversation with the extraction prompt as the human message and the gold JSON output as the assistant response.

## Prompt Template

### Training Prompt (used for SFT)

```
Extract all structured information (entities and relations) from the following text. Output a JSON object.

Text: {text}
Entity types: Generic, Material, Method, Metric, OtherScientificTerm, Task
Relation types: COMPARE, CONJUNCTION, EVALUATE-FOR, FEATURE-OF, HYPONYM-OF, PART-OF, USED-FOR

Output format: {"entities": [...], "relations": [...], "events": []}
```

### Example (SciERC)

**Input**:
```
Extract all structured information (entities and relations) from the following text. Output a JSON object.

Text: English is shown to be trans-context-free on the basis of coordinations of the respectively type that involve strictly syntactic cross-serial agreement .
Entity types: Generic, Material, Method, Metric, OtherScientificTerm, Task
Relation types: COMPARE, CONJUNCTION, EVALUATE-FOR, FEATURE-OF, HYPONYM-OF, PART-OF, USED-FOR

Output format: {"entities": [...], "relations": [...], "events": []}
```

**Expected output**:
```json
{"entities": [{"text": "English", "type": "Material", "start": 0, "end": 7}, {"text": "coordinations", "type": "OtherScientificTerm", "start": 58, "end": 71}, {"text": "strictly syntactic cross-serial agreement", "type": "OtherScientificTerm", "start": 110, "end": 151}], "relations": [], "events": []}
```

### Inference Prompt Templates

At inference time, separate subtask-specific templates are also available:

- **NER-only**: "Extract named entities from the following text. ..."
- **RE-only**: "Extract all relations (head entity, relation type, tail entity) from the following text. ..."
- **Full (train-aligned)**: Same as training prompt above (default for experiments)

All templates instruct the model to output a JSON object with `entities`, `relations`, and `events` fields.

## Schema Constraint (Constrained Decoding)

Inference uses **vLLM** with **XGrammar**-based JSON constrained decoding. The JSON schema enforces the output structure at the token level:

```json
{
  "type": "object",
  "properties": {
    "entities": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "text": {"type": "string"},
          "type": {"type": "string"},
          "start": {"type": "integer"},
          "end": {"type": "integer"}
        },
        "required": ["text", "type", "start", "end"]
      }
    },
    "relations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "head": {"type": "string"},
          "tail": {"type": "string"},
          "type": {"type": "string"},
          "head_start": {"type": "integer"},
          "head_end": {"type": "integer"},
          "tail_start": {"type": "integer"},
          "tail_end": {"type": "integer"}
        },
        "required": ["head", "tail", "type", "head_start", "head_end", "tail_start", "tail_end"]
      }
    },
    "events": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "trigger": {
            "type": "object",
            "properties": {
              "text": {"type": "string"},
              "type": {"type": "string"},
              "start": {"type": "integer"},
              "end": {"type": "integer"}
            },
            "required": ["text", "type", "start", "end"]
          },
          "arguments": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "text": {"type": "string"},
                "role": {"type": "string"},
                "start": {"type": "integer"},
                "end": {"type": "integer"}
              },
              "required": ["text", "role", "start", "end"]
            }
          }
        },
        "required": ["trigger", "arguments"]
      }
    }
  },
  "required": ["entities", "relations", "events"]
}
```

This guarantees that every sampled output is valid JSON conforming to the UIE schema, enabling reliable multi-sample aggregation without parse failures.
