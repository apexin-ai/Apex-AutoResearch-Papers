#!/usr/bin/env python3
"""Convert codalab_submission.json from dict format to CodaLab list format.

Input format (current):  {title: [{r, h, t, evidence}, ...]}
Output format (CodaLab): [{title, h_idx, t_idx, r, evidence}, ...]

Usage:
    python convert_codalab.py ./outputs/eval_results
"""
import json
import sys
import os

def convert(input_path):
    with open(input_path) as f:
        data = json.load(f)
    
    if isinstance(data, list):
        print(f"  {input_path}: already list format, skipping")
        return
    
    output = []
    for title, triples in data.items():
        for triple in triples:
            entry = {"title": title}
            if "h_idx" in triple:
                entry["h_idx"] = triple["h_idx"]
            elif "h" in triple:
                entry["h_idx"] = triple["h"]
            if "t_idx" in triple:
                entry["t_idx"] = triple["t_idx"]
            elif "t" in triple:
                entry["t_idx"] = triple["t"]
            entry["r"] = triple.get("r", "")
            entry["evidence"] = triple.get("evidence", [])
            output.append(entry)
    
    output_path = input_path.replace(".json", "_codalab.json")
    with open(output_path, "w") as f:
        json.dump(output, f)
    print(f"  {input_path} -> {output_path} ({len(output)} triples)")

if __name__ == "__main__":
    for path in sys.argv[1:]:
        if os.path.exists(path):
            convert(path)
        else:
            print(f"  {path}: not found")
