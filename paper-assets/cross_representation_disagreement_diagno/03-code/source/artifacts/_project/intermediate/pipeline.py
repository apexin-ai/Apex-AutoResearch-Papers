"""
主流程：数据加载 → 双表征生成 → 执行 → 分歧检测 → 错误分类 → 修复 → 保存。
支持断点续跑（--resume）和数量限制（--max-examples）。
"""

import json
import time
import argparse
import logging
from pathlib import Path
from typing import List, Optional

from config import RESULTS_DIR
from data_loader import load_folio, FolioExample
from formalize import generate_fol_code, generate_python_code
from executor import execute_code
from disagree import detect_disagreement, classify_error, AgreementType
from repair import targeted_repair, blind_regeneration

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(RESULTS_DIR / "pipeline.log"),
    ],
)
log = logging.getLogger(__name__)


def process_one(example: FolioExample) -> dict:
    rec = {
        "id": example.id,
        "premises": example.premises,
        "conclusion": example.conclusion,
        "ground_truth": example.label,
    }

    # --- 1. 双表征生成 ---
    log.info("[%s] generating FOL code …", example.id)
    fol_raw, fol_code = generate_fol_code(example.premises, example.conclusion)
    rec["fol_raw"] = fol_raw
    rec["fol_code"] = fol_code

    log.info("[%s] generating Python code …", example.id)
    code_raw, code_code = generate_python_code(example.premises, example.conclusion)
    rec["code_raw"] = code_raw
    rec["code_code"] = code_code

    # --- 2. 执行 ---
    log.info("[%s] executing FOL code …", example.id)
    fol_ex = execute_code(fol_code)
    rec["fol_exec"] = fol_ex.to_dict()

    log.info("[%s] executing Python code …", example.id)
    code_ex = execute_code(code_code)
    rec["code_exec"] = code_ex.to_dict()

    # --- 3. 分歧检测 ---
    dis = detect_disagreement(fol_ex.verdict, code_ex.verdict, example.label)
    rec["disagreement"] = dis.to_dict()

    # --- 4. 错误分类（非 agree_correct） ---
    if dis.agreement_type != AgreementType.AGREE_CORRECT:
        et = classify_error(
            fol_code, code_code,
            fol_ex.verdict, code_ex.verdict,
            fol_ex.error, code_ex.error,
            example.label, example.premises, example.conclusion,
        )
        rec["disagreement"]["error_type"] = et

    # --- 5. 修复（disagreement / single_error） ---
    rec["repair"] = {}
    if dis.agreement_type in (AgreementType.DISAGREE, AgreementType.SINGLE_ERROR):
        et = rec["disagreement"].get("error_type", "unknown")

        if dis.error_side in ("fol", "both"):
            log.info("[%s] targeted repair FOL …", example.id)
            rec["repair"]["fol_targeted"] = [
                r.to_dict() for r in targeted_repair(
                    example.premises, example.conclusion,
                    fol_code, fol_ex.verdict, code_ex.verdict,
                    et, fol_ex.error, "FOL (Z3)", example.label,
                )
            ]
            log.info("[%s] blind regen FOL …", example.id)
            rec["repair"]["fol_blind"] = [
                r.to_dict() for r in blind_regeneration(
                    example.premises, example.conclusion,
                    "FOL (Z3)", example.label,
                )
            ]

        if dis.error_side in ("code", "both"):
            log.info("[%s] targeted repair Code …", example.id)
            rec["repair"]["code_targeted"] = [
                r.to_dict() for r in targeted_repair(
                    example.premises, example.conclusion,
                    code_code, code_ex.verdict, fol_ex.verdict,
                    et, code_ex.error, "Python code", example.label,
                )
            ]
            log.info("[%s] blind regen Code …", example.id)
            rec["repair"]["code_blind"] = [
                r.to_dict() for r in blind_regeneration(
                    example.premises, example.conclusion,
                    "Python code", example.label,
                )
            ]

    log.info(
        "[%s] done  FOL=%s  Code=%s  GT=%s  type=%s",
        example.id, fol_ex.verdict, code_ex.verdict,
        example.label, dis.agreement_type,
    )
    return rec


def run_pipeline(
    max_examples: Optional[int] = None,
    output_file: Optional[str] = None,
    resume_from: Optional[str] = None,
) -> List[dict]:

    examples = load_folio(max_examples=max_examples)
    log.info("loaded %d FOLIO examples", len(examples))

    done_ids: set = set()
    results: List[dict] = []
    if resume_from and Path(resume_from).exists():
        with open(resume_from) as f:
            results = json.load(f)
        done_ids = {r["id"] for r in results}
        log.info("resumed %d already-done examples", len(done_ids))

    if output_file is None:
        ts = time.strftime("%Y%m%d_%H%M%S")
        output_file = str(RESULTS_DIR / f"results_{ts}.json")

    for i, ex in enumerate(examples, 1):
        if ex.id in done_ids:
            continue

        log.info("[%d/%d] processing %s …", i, len(examples), ex.id)
        try:
            results.append(process_one(ex))
        except Exception as e:
            log.error("[%s] pipeline error: %s", ex.id, e)
            results.append({
                "id": ex.id,
                "premises": ex.premises,
                "conclusion": ex.conclusion,
                "ground_truth": ex.label,
                "pipeline_error": str(e),
            })

        with open(output_file, "w") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

    log.info("pipeline complete → %s", output_file)
    return results


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-examples", type=int, default=None)
    ap.add_argument("--output", type=str, default=None)
    ap.add_argument("--resume", type=str, default=None)
    args = ap.parse_args()

    run_pipeline(
        max_examples=args.max_examples,
        output_file=args.output,
        resume_from=args.resume,
    )
