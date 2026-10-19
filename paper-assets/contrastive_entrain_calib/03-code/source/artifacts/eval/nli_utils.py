"""Shared NLI utilities for evaluation and training scripts.

Provides dynamic entailment index detection and stance consistency checking.
All NLI-dependent code should use these functions instead of hardcoding label indices.
"""
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer


def get_entailment_idx(model) -> int:
    """Get entailment label index from model config, with fallback heuristic."""
    id2label = getattr(model.config, "id2label", {})
    for idx, label in id2label.items():
        if "entail" in str(label).lower():
            return int(idx)
    label2id = getattr(model.config, "label2id", {})
    for label, idx in label2id.items():
        if "entail" in str(label).lower():
            return int(idx)
    raise ValueError(f"Cannot determine entailment index. id2label={id2label}, label2id={label2id}")


def get_contradiction_idx(model) -> int:
    """Get contradiction label index from model config."""
    id2label = getattr(model.config, "id2label", {})
    for idx, label in id2label.items():
        if "contradict" in str(label).lower():
            return int(idx)
    label2id = getattr(model.config, "label2id", {})
    for label, idx in label2id.items():
        if "contradict" in str(label).lower():
            return int(idx)
    raise ValueError(f"Cannot determine contradiction index. id2label={id2label}, label2id={label2id}")


def load_nli_model(model_name: str, device: torch.device):
    """Load NLI cross-encoder model and tokenizer."""
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)
    model.eval()
    ent_idx = get_entailment_idx(model)
    con_idx = get_contradiction_idx(model)
    return model, tokenizer, ent_idx, con_idx


def check_stance_consistency(nli_model, nli_tokenizer, initial_response: str,
                             new_response: str, device: torch.device,
                             entailment_idx: int, contradiction_idx: int) -> tuple[bool, float]:
    """Check if new_response maintains same stance as initial_response.

    Returns (is_consistent: bool, entailment_prob: float).
    entailment_prob is the continuous score for RC-AUC computation.
    """
    inputs = nli_tokenizer(
        initial_response, new_response,
        return_tensors="pt", truncation=True, max_length=512, padding=True,
    ).to(device)
    with torch.no_grad():
        logits = nli_model(**inputs).logits
    probs = torch.softmax(logits, dim=-1)[0]
    ent_prob = probs[entailment_idx].item()
    con_prob = probs[contradiction_idx].item()
    is_consistent = ent_prob > con_prob
    return is_consistent, ent_prob
