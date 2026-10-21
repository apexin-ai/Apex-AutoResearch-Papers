"""EXP-4: DD OOD Adversarial Perturbation + Full Variant Evaluation.

Step 1: Paraphrase user turns in DD OOD data using Qwen3-8B
Step 2: Evaluate all DeBERTa variant checkpoints on clean vs perturbed DD OOD
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/hf_cache"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import sys
import json
import re
import random
import argparse
import numpy as np
import torch
from pathlib import Path
from sklearn.metrics import f1_score, precision_score, recall_score

sys.path.insert(0, "/root/persuasion_turn_jailbreak_detect")
from src.models.deberta_multitask import DeBERTaMultiTask
from src.models.deberta_topic import DeBERTaTopic
from src.models.gru_classifier import GRUClassifier
from transformers import AutoTokenizer, AutoModel, AutoModelForCausalLM

PROJ = Path("/root/persuasion_turn_jailbreak_detect")
DEVICE = torch.device("cuda:0")
LOCAL_MODEL = "/root/autodl-tmp/hf_cache/hub/models--microsoft--deberta-v3-base/snapshots/8ccc9b6f36199bec6961081d44eb72fb3f7353f3"
MAX_LENGTH = 256
GRU_HIDDEN = 256
GRU_LAYERS = 2
GRU_DROPOUT = 0.3

PARAPHRASE_PROMPT = """Aggressively rewrite the following message. Change vocabulary, sentence structure, and tone significantly while preserving the core meaning. Use different words, rearrange ideas, and vary formality. The rewritten version should be hard to match to the original via keyword overlap. Output only the rewritten message.

Original: {turn_content}"""

DD_OOD_PATH = PROJ / "data/generated/deceptive_delight_all.jsonl"
TEST_PATH = PROJ / "data/plan_002_splits/test.jsonl"
PERTURBED_PATH = PROJ / "data/dd_ood_perturbed/perturbed.jsonl"
QWEN_PATH = "/root/autodl-tmp/hf_cache/Qwen/Qwen3-8B"

CKPT = PROJ / "checkpoints"
BACKUP = Path("/root/autodl-tmp/checkpoints_backup")

VARIANTS = {
    "9class": {
        "encoder_type": "deberta_multitask",
        "num_classes": 9,
        "seeds": {
            42:  {"deberta_dir": CKPT / "plan_002/deberta_multitask/best",
                  "gru_path": CKPT / "plan_002/gru/treatment/best.pt"},
            123: {"deberta_dir": CKPT / "plan_002_seed123/deberta_multitask/best",
                  "gru_path": CKPT / "plan_002_seed123/gru/treatment/best.pt"},
            456: {"deberta_dir": CKPT / "plan_002_seed456/deberta_multitask/best",
                  "gru_path": CKPT / "plan_002_seed456/gru/treatment/best.pt"},
        }
    },
    "binary": {
        "encoder_type": "deberta_multitask",
        "num_classes": 2,
        "seeds": {
            42:  {"deberta_dir": BACKUP / "plan_013_none_collapse/deberta_multitask/best",
                  "gru_path": BACKUP / "plan_013_none_collapse/gru/treatment/best.pt"},
            123: {"deberta_dir": CKPT / "mf1_binary_seed123/deberta_multitask/best",
                  "gru_path": CKPT / "mf1_binary_seed123/gru/treatment/best.pt"},
            456: {"deberta_dir": CKPT / "mf1_binary_seed456/deberta_multitask/best",
                  "gru_path": CKPT / "mf1_binary_seed456/gru/treatment/best.pt"},
        }
    },
    "scrambled": {
        "encoder_type": "deberta_multitask",
        "num_classes": 9,
        "seeds": {
            42:  {"deberta_dir": CKPT / "plan_003_scrambled_fix/deberta_multitask/best",
                  "gru_path": CKPT / "plan_003_scrambled_fix/gru/best.pt"},
            123: {"deberta_dir": CKPT / "mf1_scrambled_seed123/deberta_multitask/best",
                  "gru_path": CKPT / "mf1_scrambled_seed123/gru/best.pt"},
            456: {"deberta_dir": CKPT / "mf1_scrambled_seed456/deberta_multitask/best",
                  "gru_path": CKPT / "mf1_scrambled_seed456/gru/best.pt"},
        }
    },
    "jb_mlm": {
        "encoder_type": "automodel",
        "seeds": {
            42:  {"encoder_dir": CKPT / "plan_017_mlm/best",
                  "gru_path": CKPT / "plan_017_mlm/gru/best.pt"},
            123: {"encoder_dir": CKPT / "plan_017_mlm_seed123/best",
                  "gru_path": CKPT / "plan_017_mlm_seed123/gru/best_gru.pt"},
            456: {"encoder_dir": CKPT / "plan_017_mlm_seed456/best",
                  "gru_path": CKPT / "plan_017_mlm_seed456/gru/best_gru.pt"},
        }
    },
    "wiki_mlm": {
        "encoder_type": "automodel",
        "seeds": {
            42:  {"encoder_dir": CKPT / "plan_018_wiki_mlm/best",
                  "gru_path": CKPT / "plan_018_wiki_mlm/gru/best_gru.pt"},
            123: {"encoder_dir": CKPT / "plan_018_wiki_mlm_seed123/best",
                  "gru_path": CKPT / "plan_018_wiki_mlm_seed123/gru/best_gru.pt"},
            456: {"encoder_dir": CKPT / "plan_018_wiki_mlm_seed456/best",
                  "gru_path": CKPT / "plan_018_wiki_mlm_seed456/gru/best_gru.pt"},
        }
    },
    "topic": {
        "encoder_type": "deberta_topic",
        "seeds": {
            42:  {"deberta_dir": CKPT / "plan_016v2_topic/best",
                  "gru_path": CKPT / "plan_016v2_topic/gru/best.pt"},
            123: {"deberta_dir": CKPT / "plan_016v2_topic_seed123/best",
                  "gru_path": CKPT / "plan_016v2_topic_seed123/gru/gru_best.pt"},
            456: {"deberta_dir": CKPT / "plan_016v2_topic_seed456/best",
                  "gru_path": CKPT / "plan_016v2_topic_seed456/gru/gru_best.pt"},
        }
    },
    "vanilla": {
        "encoder_type": "vanilla",
        "seeds": {
            42: {"gru_path": CKPT / "plan_002/gru/baseline/best.pt"},
        }
    },
}


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


# ── Step 1: Paraphrasing ──

def strip_thinking(text):
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    return text.strip()


def paraphrase_turn(model, tokenizer, text, device):
    prompt_text = PARAPHRASE_PROMPT.format(turn_content=text)
    messages = [{"role": "user", "content": prompt_text}]
    input_text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True, enable_thinking=False,
    )
    inputs = tokenizer(input_text, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs, max_new_tokens=512, temperature=0.7, do_sample=True, top_p=0.9,
        )
    generated = outputs[0][inputs["input_ids"].shape[1]:]
    result = tokenizer.decode(generated, skip_special_tokens=True)
    return strip_thinking(result).strip()


def perturb_dd_ood(skip_if_exists=True):
    if skip_if_exists and PERTURBED_PATH.exists():
        n = sum(1 for _ in open(PERTURBED_PATH))
        print(f"Perturbed file already exists ({n} lines), skipping. Use --force_perturb to redo.", flush=True)
        return

    print("Loading Qwen3-8B...", flush=True)
    tokenizer = AutoTokenizer.from_pretrained(QWEN_PATH)
    model = AutoModelForCausalLM.from_pretrained(QWEN_PATH, torch_dtype=torch.float16, device_map="cuda:0")
    model.eval()
    print("Qwen3-8B loaded.", flush=True)

    convs = load_jsonl(DD_OOD_PATH)
    print(f"Paraphrasing {len(convs)} DD OOD conversations...", flush=True)

    PERTURBED_PATH.parent.mkdir(parents=True, exist_ok=True)
    total_turns = 0
    success_turns = 0

    with open(PERTURBED_PATH, "w") as fout:
        for ci, conv in enumerate(convs):
            new_turns = []
            for ti, turn in enumerate(conv["turns"]):
                if turn["role"] == "user":
                    total_turns += 1
                    result = paraphrase_turn(model, tokenizer, turn["content"], DEVICE)
                    if result:
                        new_turn = dict(turn)
                        new_turn["original_content"] = turn["content"]
                        new_turn["content"] = result
                        new_turns.append(new_turn)
                        success_turns += 1
                    else:
                        new_turns.append(turn)
                        print(f"  [WARN] Empty paraphrase conv {ci} turn {ti}, keeping original", flush=True)
                else:
                    new_turns.append(turn)
            new_conv = dict(conv)
            new_conv["turns"] = new_turns
            fout.write(json.dumps(new_conv, ensure_ascii=False) + "\n")
            fout.flush()
            if (ci + 1) % 10 == 0 or ci == len(convs) - 1:
                print(f"  Perturbed {ci+1}/{len(convs)} conversations ({success_turns}/{total_turns} turns)", flush=True)

    del model, tokenizer
    torch.cuda.empty_cache()
    print(f"Perturbation complete: {success_turns}/{total_turns} turns successful", flush=True)
    print(f"Output: {PERTURBED_PATH}", flush=True)


# ── Step 2: Evaluation ──

def extract_user_turns(conv, use_original=False):
    turns = []
    for t in conv["turns"]:
        if t["role"] == "user":
            if use_original and "original_content" in t:
                turns.append(t["original_content"])
            else:
                turns.append(t["content"])
    return turns


def get_label(conv):
    return 1 if conv["label"] == "jailbreak" else 0


def load_encoder(variant_name, seed_cfg, variant_cfg):
    enc_type = variant_cfg["encoder_type"]

    if enc_type == "deberta_multitask":
        num_cls = variant_cfg["num_classes"]
        model = DeBERTaMultiTask(model_name=LOCAL_MODEL, num_persuasion_classes=num_cls)
        sd = torch.load(seed_cfg["deberta_dir"] / "model.pt", map_location="cpu", weights_only=True)
        model.load_state_dict(sd)
        enc = model.deberta.to(DEVICE).eval()
        for p in enc.parameters():
            p.requires_grad = False
        tok = AutoTokenizer.from_pretrained(LOCAL_MODEL)
        return enc, tok

    elif enc_type == "deberta_topic":
        model = DeBERTaTopic(model_name=LOCAL_MODEL)
        sd = torch.load(seed_cfg["deberta_dir"] / "model.pt", map_location="cpu", weights_only=True)
        model.load_state_dict(sd)
        enc = model.deberta.to(DEVICE).eval()
        for p in enc.parameters():
            p.requires_grad = False
        tok = AutoTokenizer.from_pretrained(LOCAL_MODEL)
        return enc, tok

    elif enc_type == "automodel":
        enc_path = str(seed_cfg["encoder_dir"])
        enc = AutoModel.from_pretrained(enc_path).to(DEVICE).eval()
        for p in enc.parameters():
            p.requires_grad = False
        tok = AutoTokenizer.from_pretrained(enc_path)
        return enc, tok

    elif enc_type == "vanilla":
        enc = AutoModel.from_pretrained(LOCAL_MODEL).to(DEVICE).eval()
        for p in enc.parameters():
            p.requires_grad = False
        tok = AutoTokenizer.from_pretrained(LOCAL_MODEL)
        return enc, tok

    else:
        raise ValueError(f"Unknown encoder type: {enc_type}")


def load_gru(gru_path, embed_dim=768):
    gru = GRUClassifier(input_dim=embed_dim, hidden_dim=GRU_HIDDEN,
                        num_layers=GRU_LAYERS, dropout=GRU_DROPOUT)
    gru.load_state_dict(torch.load(gru_path, map_location="cpu", weights_only=True))
    gru.to(DEVICE).eval()
    return gru


def embed_turns(encoder, tokenizer, turns, k=None):
    t = turns[:k] if k is not None else turns
    if len(t) == 0:
        t = [""]
    enc = tokenizer(t, max_length=MAX_LENGTH, padding=True, truncation=True, return_tensors="pt").to(DEVICE)
    with torch.no_grad():
        out = encoder(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
        return out.last_hidden_state[:, 0, :].float()


def eval_set(encoder, gru, tokenizer, data, k=None, use_original=False):
    all_preds, all_labels = [], []
    for c in data:
        turns = extract_user_turns(c, use_original=use_original)
        embs = embed_turns(encoder, tokenizer, turns, k=k)
        embs_batch = embs.unsqueeze(0)
        lengths = torch.tensor([embs.size(0)], dtype=torch.long).to(DEVICE)
        with torch.no_grad():
            logits = gru(embs_batch, lengths)
            pred = logits.argmax(dim=1).item()
        all_preds.append(pred)
        all_labels.append(get_label(c))

    y_true = np.array(all_labels)
    y_pred = np.array(all_preds)
    return {
        "f1_macro": round(float(f1_score(y_true, y_pred, average="macro", zero_division=0)), 4),
        "precision": round(float(precision_score(y_true, y_pred, average="macro", zero_division=0)), 4),
        "recall": round(float(recall_score(y_true, y_pred, average="macro", zero_division=0)), 4),
        "accuracy": round(float((y_pred == y_true).mean()), 4),
    }


def build_dd_ood_datasets():
    test_data = load_jsonl(TEST_PATH)
    benign_test = [c for c in test_data if c["label"] == "benign"]

    dd_clean = load_jsonl(DD_OOD_PATH)
    dd_perturbed = load_jsonl(PERTURBED_PATH)

    clean_convs = dd_clean + benign_test
    perturbed_convs = dd_perturbed + benign_test

    n_jb_clean = sum(1 for c in clean_convs if c["label"] == "jailbreak")
    n_bn_clean = sum(1 for c in clean_convs if c["label"] == "benign")
    print(f"DD OOD clean: {len(clean_convs)} total ({n_jb_clean} jailbreak, {n_bn_clean} benign)", flush=True)
    print(f"DD OOD perturbed: {len(perturbed_convs)} total", flush=True)

    return clean_convs, perturbed_convs


def evaluate_all_variants():
    clean_convs, perturbed_convs = build_dd_ood_datasets()

    k_values = {"k1": 1, "k2": 2, "k3": 3, "k5": 5, "full": None}
    all_results = {}

    for vname, vcfg in VARIANTS.items():
        print(f"\n{'='*60}", flush=True)
        print(f"Evaluating variant: {vname}", flush=True)
        print(f"{'='*60}", flush=True)

        per_seed = {}
        for seed, scfg in vcfg["seeds"].items():
            gru_path = scfg["gru_path"]
            if not Path(gru_path).exists():
                print(f"  [SKIP] seed={seed}: GRU not found at {gru_path}", flush=True)
                continue

            set_seed(seed)
            print(f"\n  seed={seed}", flush=True)

            encoder, tokenizer = load_encoder(vname, scfg, vcfg)
            embed_dim = encoder.config.hidden_size
            gru = load_gru(gru_path, embed_dim)

            seed_results = {"clean": {}, "perturbed": {}, "delta": {}}

            for k_label, k_val in k_values.items():
                r_clean = eval_set(encoder, gru, tokenizer, clean_convs, k=k_val, use_original=False)
                r_pert = eval_set(encoder, gru, tokenizer, perturbed_convs, k=k_val, use_original=False)
                delta_f1 = round(r_pert["f1_macro"] - r_clean["f1_macro"], 4)

                seed_results["clean"][k_label] = r_clean["f1_macro"]
                seed_results["perturbed"][k_label] = r_pert["f1_macro"]
                seed_results["delta"][k_label] = delta_f1

                print(f"    {k_label}: clean={r_clean['f1_macro']:.4f}  pert={r_pert['f1_macro']:.4f}  delta={delta_f1:+.4f}", flush=True)

            per_seed[f"seed{seed}"] = seed_results

            del encoder, gru, tokenizer
            torch.cuda.empty_cache()

        seeds_with_data = [s for s in per_seed.values()]
        mean_std = {}
        if len(seeds_with_data) > 0:
            for k_label in k_values:
                for metric_type in ["clean", "perturbed", "delta"]:
                    key = f"{metric_type}_{k_label}"
                    vals = [s[metric_type][k_label] for s in seeds_with_data]
                    mean_std[key] = {
                        "mean": round(float(np.mean(vals)), 4),
                        "std": round(float(np.std(vals)), 4),  # population std
                    }

        all_results[vname] = {"per_seed": per_seed, "mean_std": mean_std}

        if mean_std:
            print(f"\n  Summary ({vname}, {len(seeds_with_data)} seeds):", flush=True)
            for k_label in k_values:
                cm = mean_std[f"clean_{k_label}"]
                pm = mean_std[f"perturbed_{k_label}"]
                dm = mean_std[f"delta_{k_label}"]
                print(f"    {k_label}: clean={cm['mean']:.4f}+/-{cm['std']:.4f}  "
                      f"pert={pm['mean']:.4f}+/-{pm['std']:.4f}  "
                      f"delta={dm['mean']:+.4f}+/-{dm['std']:.4f}", flush=True)

    return all_results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip_perturb", action="store_true")
    parser.add_argument("--force_perturb", action="store_true")
    parser.add_argument("--skip_eval", action="store_true")
    args = parser.parse_args()

    set_seed(42)

    if not args.skip_perturb:
        print("=" * 60, flush=True)
        print("Step 1: Paraphrase DD OOD user turns", flush=True)
        print("=" * 60, flush=True)
        perturb_dd_ood(skip_if_exists=not args.force_perturb)

    if not args.skip_eval:
        print("\n" + "=" * 60, flush=True)
        print("Step 2: Evaluate all variants on clean vs perturbed DD OOD", flush=True)
        print("=" * 60, flush=True)
        all_results = evaluate_all_variants()

        test_data = load_jsonl(TEST_PATH)
        n_benign = sum(1 for c in test_data if c["label"] == "benign")
        dd_data = load_jsonl(DD_OOD_PATH)

        output = {
            "n_conversations": len(dd_data),
            "n_benign_test": n_benign,
            "n_total": len(dd_data) + n_benign,
            "perturbation_method": "adversarial paraphrasing via Qwen3-8B",
            "variant_results": all_results,
        }

        out_path = PROJ / "results/exp4_dd_ood_perturbation.json"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w") as f:
            json.dump(output, f, indent=2)
        print(f"\nResults saved to {out_path}", flush=True)

        print("\n" + "=" * 80, flush=True)
        print(f"{'EXP-4: DD OOD Adversarial Perturbation Results':^80}", flush=True)
        print("=" * 80, flush=True)
        print(f"{'Variant':<12} {'Seeds':>5} {'K':<5} {'Clean':>8} {'Perturbed':>10} {'Delta':>8}", flush=True)
        print("-" * 55, flush=True)
        for vname, vres in all_results.items():
            ms = vres["mean_std"]
            n_seeds = len(vres["per_seed"])
            for ki, k_label in enumerate(["k1", "k2", "k3", "k5", "full"]):
                cm = ms.get(f"clean_{k_label}", {})
                pm = ms.get(f"perturbed_{k_label}", {})
                dm = ms.get(f"delta_{k_label}", {})
                if cm:
                    label = vname if ki == 0 else ""
                    seeds_str = str(n_seeds) if ki == 0 else ""
                    print(f"{label:<12} {seeds_str:>5} {k_label:<5} "
                          f"{cm['mean']:>8.4f} {pm['mean']:>10.4f} {dm['mean']:>+8.4f}", flush=True)
            print(flush=True)


if __name__ == "__main__":
    main()
