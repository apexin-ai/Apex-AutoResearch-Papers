"""Dual-track local impact measurement: full-generation ablation + LDIM logit divergence.

Input: traces JSONL from trace_collection.py
Output: JSONL with per-message impact metrics.
"""

import argparse
import json
import logging
import os

import numpy as np
import yaml
from openai import OpenAI
from sentence_transformers import SentenceTransformer

from utils import extract_final_answer

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def load_config(path: str) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def _assign_role(msg: dict, receiver_name: str) -> str:
    """Assign OpenAI role based on who sent the message relative to the receiver."""
    return "assistant" if msg.get("sender") == receiver_name else "user"


def build_prompt_pair(messages: list[dict], target_idx: int) -> tuple[list[dict], list[dict]]:
    """Build with/without prompt pairs for the response after target message."""
    response_idx = target_idx + 1
    if response_idx >= len(messages):
        return [], []

    receiver_name = messages[response_idx]["sender"]
    with_ctx = []
    without_ctx = []
    for i in range(response_idx):
        role = _assign_role(messages[i], receiver_name)
        entry = {"role": role, "content": messages[i]["content"]}
        with_ctx.append(entry)
        if i != target_idx:
            without_ctx.append(entry)

    return with_ctx, without_ctx


def _get_neutralize_text(msg: dict, cfg_neutralize: dict) -> str:
    """Get role-appropriate neutralize text based on the message sender's agent role."""
    sender = msg.get("sender", "")
    role_texts = cfg_neutralize if isinstance(cfg_neutralize, dict) else {}
    for role_key, text in role_texts.items():
        if role_key.lower() in sender.lower():
            return text
    return cfg_neutralize.get("default", "Acknowledged.") if isinstance(cfg_neutralize, dict) else str(cfg_neutralize)


def build_neutralize_pair(messages: list[dict], target_idx: int, neutralize_text) -> tuple[list[dict], list[dict]]:
    """Build with-original/with-neutralized prompt pairs for the response after target message."""
    response_idx = target_idx + 1
    if response_idx >= len(messages):
        return [], []

    if isinstance(neutralize_text, dict):
        replacement = _get_neutralize_text(messages[target_idx], neutralize_text)
    else:
        replacement = str(neutralize_text)

    receiver_name = messages[response_idx]["sender"]
    with_ctx = []
    neutralized_ctx = []
    for i in range(response_idx):
        role = _assign_role(messages[i], receiver_name)
        entry = {"role": role, "content": messages[i]["content"]}
        with_ctx.append(entry)
        if i == target_idx:
            neutralized_ctx.append({"role": role, "content": replacement})
        else:
            neutralized_ctx.append(entry)

    return with_ctx, neutralized_ctx


def generate_response(client: OpenAI, model: str, messages: list[dict], max_tokens: int,
                      temperature: float = 0) -> str:
    resp = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=1.0,
        max_tokens=max_tokens,
    )
    return resp.choices[0].message.content or ""


def get_logprobs(client: OpenAI, model: str, messages: list[dict], top_k: int, max_tokens: int = 5,
                 temperature: float = 0) -> list[dict]:
    """Get top-k logprobs for the first max_tokens generated tokens."""
    resp = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=1.0,
        max_tokens=max_tokens,
        logprobs=True,
        top_logprobs=top_k,
    )
    choice = resp.choices[0]
    if choice.logprobs and choice.logprobs.content:
        all_tokens = []
        for token_info in choice.logprobs.content:
            token_entry = {"token": token_info.token, "logprob": token_info.logprob}
            if token_info.top_logprobs:
                token_entry["top_logprobs"] = [{"token": t.token, "logprob": t.logprob} for t in token_info.top_logprobs]
            all_tokens.append(token_entry)
        return all_tokens
    return []


def normalize_text(text: str) -> str:
    return " ".join(text.lower().split())


def classify_action_level(original: str, ablated: str, semantic_similarity: float) -> str:
    orig_answer = extract_final_answer(original)
    abl_answer = extract_final_answer(ablated)
    answers_differ = False
    if orig_answer != abl_answer:
        try:
            if orig_answer and abl_answer and abs(float(orig_answer) - float(abl_answer)) > 1e-6:
                answers_differ = True
        except ValueError:
            answers_differ = True
    if answers_differ:
        return "final_answer"
    if semantic_similarity >= 0.95:
        return "surface_only"
    return "reasoning_step"


def compute_fullgen(
    client: OpenAI, model: str, messages: list[dict], target_idx: int,
    max_tokens: int, embed_model: SentenceTransformer,
    mode: str = "remove", neutralize_text: str = "Acknowledged.",
    temperature: float = 0,
) -> dict:
    if mode == "remove":
        with_ctx, alt_ctx = build_prompt_pair(messages, target_idx)
    else:
        with_ctx, alt_ctx = build_neutralize_pair(messages, target_idx, neutralize_text)

    if not with_ctx or not alt_ctx:
        return {"action_level": "surface_only", "semantic_similarity": 1.0,
                "original_preview": "", "ablated_preview": ""}

    response_idx = target_idx + 1
    original_text = messages[response_idx]["content"]
    ablated_text = generate_response(client, model, alt_ctx, max_tokens, temperature=temperature)

    embeddings = embed_model.encode([original_text, ablated_text], normalize_embeddings=True)
    similarity = float(np.dot(embeddings[0], embeddings[1]))
    action_level = classify_action_level(original_text, ablated_text, similarity)

    return {
        "action_level": action_level,
        "semantic_similarity": round(similarity, 4),
        "original_preview": original_text[:200],
        "ablated_preview": ablated_text[:200],
    }


def compute_ldim(
    client: OpenAI, model: str, messages: list[dict], target_idx: int,
    top_k: int, ldim_max_tokens: int = 5, temperature: float = 0,
) -> dict:
    with_ctx, without_ctx = build_prompt_pair(messages, target_idx)
    if not with_ctx or not without_ctx:
        return {"top1_match": True, "top5_overlap": 1.0, "logprob_shift": 0.0, "token_match_rate": 1.0}

    lp_with = get_logprobs(client, model, with_ctx, top_k, max_tokens=ldim_max_tokens, temperature=temperature)
    lp_without = get_logprobs(client, model, without_ctx, top_k, max_tokens=ldim_max_tokens, temperature=temperature)

    if not lp_with or not lp_without:
        return {"top1_match": True, "top5_overlap": 1.0, "logprob_shift": 0.0, "token_match_rate": 1.0}

    top1_match = lp_with[0]["token"] == lp_without[0]["token"]

    first_with_tops = lp_with[0].get("top_logprobs", [{"token": lp_with[0]["token"]}])
    first_without_tops = lp_without[0].get("top_logprobs", [{"token": lp_without[0]["token"]}])
    tokens_with = {t["token"] for t in first_with_tops[:5]}
    tokens_without = {t["token"] for t in first_without_tops[:5]}
    overlap = len(tokens_with & tokens_without) / max(len(tokens_with | tokens_without), 1)

    logprob_shift = lp_with[0]["logprob"] - lp_without[0]["logprob"]

    n_compare = min(len(lp_with), len(lp_without))
    token_matches = sum(1 for i in range(n_compare) if lp_with[i]["token"] == lp_without[i]["token"])
    token_match_rate = token_matches / n_compare if n_compare > 0 else 1.0

    return {
        "top1_match": top1_match,
        "top5_overlap": round(overlap, 4),
        "logprob_shift": round(logprob_shift, 4),
        "token_match_rate": round(token_match_rate, 4),
    }


def main():
    parser = argparse.ArgumentParser(description="Dual-track local impact measurement")
    parser.add_argument("--config", type=str, default="configs/mvp.yaml")
    parser.add_argument("--traces", type=str, default=None)
    parser.add_argument("--output", type=str, default=None)
    parser.add_argument("--temperature", type=float, default=None,
                        help="Override model temperature from config")
    args = parser.parse_args()

    cfg = load_config(args.config)
    traces_path = args.traces or os.path.join(cfg["output"]["trace_dir"], "traces.jsonl")
    output_path = args.output or os.path.join(cfg["output"]["impact_dir"], "impact.jsonl")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    client = OpenAI(base_url=cfg["model"]["api_base"], api_key=[REDACTED]"model"]["api_key"])
    model = cfg["model"]["name"]
    max_tokens = cfg["model"].get("max_tokens", 2048)
    temperature = cfg["model"].get("temperature", 0)
    if args.temperature is not None:
        temperature = args.temperature
    top_k = cfg["local_impact"].get("logprobs_top_k", 20)
    ldim_max_tokens = cfg["local_impact"].get("ldim_max_tokens", 5)
    neutralize_text = cfg["local_impact"].get("neutralize_text", "Acknowledged.")

    embed_model_name = cfg["local_impact"].get("embedding_model", "all-MiniLM-L6-v2")
    logger.info("Loading embedding model: %s", embed_model_name)
    embed_model = SentenceTransformer(embed_model_name)

    done_tasks = set()
    if os.path.exists(output_path):
        with open(output_path) as f:
            for l in f:
                l = l.strip()
                if not l:
                    continue
                try:
                    done_tasks.add(json.loads(l)["task_id"])
                except (json.JSONDecodeError, KeyError):
                    pass
        logger.info("Resuming: %d tasks already processed", len(done_tasks))

    with open(traces_path) as fin, open(output_path, "a") as fout:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            try:
                task = json.loads(line)
            except json.JSONDecodeError:
                logger.warning("Skipping malformed line")
                continue
            task_id = task["task_id"]
            if task_id in done_tasks:
                continue
            messages = [m for m in task["messages"] if m.get("round", 0) > 0]

            for msg_idx in range(len(messages)):
                if msg_idx == 0 or msg_idx + 1 >= len(messages):
                    continue

                logger.info("Task %s msg %d: measuring impact", task_id, msg_idx)

                remove = compute_fullgen(client, model, messages, msg_idx, max_tokens, embed_model,
                                         mode="remove", temperature=temperature)
                neutralize = compute_fullgen(client, model, messages, msg_idx, max_tokens, embed_model,
                                             mode="neutralize", neutralize_text=neutralize_text,
                                             temperature=temperature)
                ldim = compute_ldim(client, model, messages, msg_idx, top_k, ldim_max_tokens,
                                    temperature=temperature)

                record = {
                    "task_id": task_id,
                    "message_index": msg_idx,
                    "sender": messages[msg_idx]["sender"],
                    "receiver": messages[msg_idx]["receiver"],
                    "remove": remove,
                    "neutralize": neutralize,
                    "ldim": ldim,
                }
                fout.write(json.dumps(record, ensure_ascii=False) + "\n")

    logger.info("Impact results saved to %s", output_path)


if __name__ == "__main__":
    main()
