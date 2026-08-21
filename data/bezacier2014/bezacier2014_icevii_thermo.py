#!/usr/bin/env python3
"""Convert the manually transcribed Bezacier et al. (2014) Table I ice VII data to PEARL SI units."""

from pathlib import Path
import re

N_A = 6.02214076e23  # mol^-1, exact SI
Z = 2  # H2O formula units per reported crystallographic unit cell; curator-inferred conversion factor.
RAW = Path(__file__).with_name("bezacier2014_icevii_table1_thermo_raw.dat")
OUT = Path(__file__).with_name("bezacier2014_icevii_thermo.dat")

def parse_parenthetical(token):
    match = re.fullmatch(r"([0-9]+(?:\.[0-9]+)?)\((\d+)\)", token)
    if not match:
        raise ValueError(f"Expected value(parenthetical_uncertainty), got {token!r}")
    value_text, uncertainty_digits = match.groups()
    decimals = len(value_text.split(".")[1]) if "." in value_text else 0
    value = float(value_text)
    uncertainty = int(uncertainty_digits) * 10.0 ** (-decimals)
    return value, uncertainty, value_text, uncertainty_digits

def significant_figures(number_text):
    return len(number_text.replace(".", "").lstrip("0"))

def format_sig(value, sigfigs):
    if value == 0:
        return "0"
    s = f"{value:.{sigfigs - 1}e}"
    return s.replace("e+0", "e").replace("e-0", "e-").replace("e+", "e")

def main():
    factor = 1e-30 * N_A / Z  # A^3 per unit cell -> m^3/mol
    rows = []
    with RAW.open(encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("#") or line.startswith("P[") or not line.strip():
                continue
            fields = line.rstrip("\n").split("\t")
            p_token, t_token, v_token = fields[0], fields[1], fields[2]
            p, dp, p_text, dp_digits = parse_parenthetical(p_token)
            v, dv, v_text, dv_digits = parse_parenthetical(v_token)
            V = format_sig(v * factor, significant_figures(v_text))
            dV = format_sig(dv * factor, len(dv_digits))
            P = format_sig(p * 1e9, significant_figures(p_text))
            dP = format_sig(dp * 1e9, len(dp_digits))
            rows.append((V, dV, P, dP, t_token, "0.4"))

    with OUT.open("w", encoding="utf-8", newline="") as handle:
        handle.write("V[m^3/mol]\tdV[m^3/mol]\tP[Pa]\tdP[Pa]\tT[K]\tdT[K]\n")
        for row in rows:
            handle.write("\t".join(row) + "\n")

if __name__ == "__main__":
    main()
