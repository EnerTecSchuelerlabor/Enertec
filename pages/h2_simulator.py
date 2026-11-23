"""EnerTec – Hydrogen simulations and calculators (DE/EN).

Add as pages/h18_Simulatoren_Rechner.py and link in h2_sidebar().
Uses only existing language.py and navigation.py plus Streamlit, NumPy and Matplotlib.
"""
from __future__ import annotations

import math

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

from language import lang
from navigation import hide_default_sidebar_nav, h2_sidebar

st.set_page_config(page_title="EnerTec | Wasserstoff-Simulatoren / Hydrogen simulators", layout="wide")
hide_default_sidebar_nav()
h2_sidebar()

# Physical constants / model assumptions:
FARADAY_C_PER_MOL = 96485.33212
MOLAR_VOLUME_ML_PER_MOL = 24465.0  # ideal gas, around 25 °C and 1 atm
H2_ENERGY_J_PER_ML = 11.71  # value specified in the EnerTec experiment sheets


def show_number(value: float, decimals: int = 2) -> str:
    """Locale-dependent number display without changing widget state."""
    number = f"{value:,.{decimals}f}"
    from language import get_language
    return number.replace(",", "_").replace(".", ",").replace("_", ".") if get_language() == "DE" else number


def heading(de: str, en: str) -> None:
    st.subheader(lang(de, en))


st.title(lang("Wasserstoff – Simulatoren & Rechner", "Hydrogen – Simulators & Calculators"))
st.write(lang(
    "Probiert verschiedene Einstellungen aus und vergleicht die theoretischen Ergebnisse "
    "mit euren Messungen aus den Wasserstoffversuchen. Alle Rechner befinden sich auf dieser Seite.",
    "Try different settings and compare the theoretical results with your measurements "
    "from the hydrogen experiments. All simulators are on this one page.",
))
st.info(lang(
    "**Wichtig:** Das sind vereinfachte Rechenmodelle, keine Steuerung des echten Versuchskoffers. "
    "Die Simulation verändert keine Geräte. Haltet euch bei echten Experimenten an die Gerätegrenzen "
    "und die Anweisungen der Betreuung.",
    "**Important:** These are simplified calculation models, not controls for the real experiment kit. "
    "Nothing on this page changes the equipment. Follow the device limits and supervisor instructions "
    "during actual experiments.",
))

# ----- 1. Gas production / Faraday's law ------------------------------------
st.divider()
heading("1 – Elektrolyse: Wie viel Gas entsteht?", "1 – Electrolysis: How much gas is produced?")
st.write(lang(
    "Passend zu **Versuch 2**: Mit dem Faradayschen Gesetz lässt sich die theoretisch erzeugte "
    "Wasserstoffmenge aus Stromstärke und Zeit bestimmen. Das Modell nimmt etwa 25 °C und "
    "Umgebungsdruck an. Mit dem einstellbaren Faraday-Wirkungsgrad könnt ihr Gasverluste "
    "bzw. nicht nutzbare Ladungsanteile modellieren.",
    "Related to **Experiment 2**: Faraday's law predicts the theoretical hydrogen volume "
    "from current and time. The model assumes approximately 25 °C and ambient pressure. "
    "The adjustable Faradaic efficiency represents the fraction of electric charge "
    "contributing to collected gas.",
))
a, b, c = st.columns(3)
with a:
    current_ma = st.slider(lang("Stromstärke (mA)", "Current (mA)"), 0, 500, 400, 25, key="sim_h2_current")
with b:
    duration_min = st.slider(lang("Messdauer (min)", "Duration (min)"), 1, 15, 3, 1, key="sim_h2_minutes")
with c:
    faradaic_percent = st.slider(lang("Faraday-Wirkungsgrad (%)", "Faradaic efficiency (%)"), 50, 100, 100, 5, key="sim_h2_faradaic")

current_a = current_ma / 1000.0
time_s = duration_min * 60.0
n_h2 = current_a * time_s / (2 * FARADAY_C_PER_MOL) * faradaic_percent / 100.0
v_h2_ml = n_h2 * MOLAR_VOLUME_ML_PER_MOL
v_o2_ml = v_h2_ml / 2.0
h2_rate_ml_per_min = v_h2_ml / duration_min
k_ml_per_min_a = h2_rate_ml_per_min / current_a if current_a > 0 else None

m1, m2, m3 = st.columns(3)
m1.metric("H₂", f"{show_number(v_h2_ml)} ml")
m2.metric("O₂", f"{show_number(v_o2_ml)} ml")
m3.metric(lang("H₂ pro Minute", "H₂ per minute"), f"{show_number(h2_rate_ml_per_min)} ml/min")

fig1, ax1 = plt.subplots(figsize=(8.5, 3.1))
ax1.bar(["H₂", "O₂"], [v_h2_ml, v_o2_ml], color=["#1689B7", "#47AE9F"])
ax1.set_ylabel("ml")
ax1.set_ylim(0, max(v_h2_ml, 0.5) * 1.3)
ax1.grid(axis="y", alpha=0.2)
for i, value in enumerate((v_h2_ml, v_o2_ml)):
    ax1.text(i, value + max(v_h2_ml, 0.5) * 0.035, f"{value:.2f} ml", ha="center", fontsize=10)
st.pyplot(fig1, use_container_width=True)
plt.close(fig1)

if k_ml_per_min_a is not None:
    st.write(lang(
        f"**Proportionalitätskonstante:** {show_number(k_ml_per_min_a)} ml/(min·A). "
        "Vergleicht diesen theoretischen Wert mit eurer Tabelle aus Versuch 2.",
        f"**Proportionality constant:** {show_number(k_ml_per_min_a)} ml/(min·A). "
        "Compare this theoretical value with your table from Experiment 2.",
    ))
else:
    st.caption(lang("Bei 0 mA ist die Konstante aus dieser Simulation nicht bestimmbar.", "At 0 mA, the constant cannot be determined from this simulation."))
with st.expander(lang("Formeln & Annahmen", "Formulas & assumptions")):
    st.latex(r"n(H_2)=\frac{I\cdot t}{2F}\cdot\eta_F")
    st.latex(r"V(H_2)=n(H_2)\cdot V_m,\qquad V(O_2)=\frac{V(H_2)}{2}")
    st.write(lang(
        "F = 96485 C/mol; molares Gasvolumen ≈ 24,465 l/mol (25 °C, 1 atm). "
        "Der angezeigte Gaswert ist eine Idealisierung; reale Ablesungen hängen auch von "
        "Temperatur, Druck, Wasserstand und Gasverlusten ab.",
        "F = 96485 C/mol; molar gas volume ≈ 24.465 L/mol (25 °C, 1 atm). "
        "The displayed volume is an idealized estimate; real readings also depend on "
        "temperature, pressure, water level and gas losses.",
    ))

# ----- 2. Current-voltage characteristic -------------------------------------
st.divider()
heading("2 – I-U-Kennlinie und Zersetzungsspannung", "2 – I-V curve and decomposition voltage")
st.write(lang(
    "Passend zu **Versuch 1**: Verändert die angenommene Zersetzungsspannung und den "
    "zusätzlichen Spannungsanstieg mit der Stromstärke. Die Kurve zeigt ein **didaktisches "
    "Modell**, keine gemessene Kennlinie eures Elektrolyseurs.",
    "Related to **Experiment 1**: Adjust the assumed decomposition voltage and the "
    "additional voltage increase with current. This is a **teaching model**, not a measured "
    "characteristic curve of your electrolyzer.",
))
c1, c2 = st.columns(2)
with c1:
    onset_v = st.slider(lang("Angenommene Schwellspannung (V)", "Assumed threshold voltage (V)"), 1.0, 2.2, 1.5, 0.05, key="sim_h2_onset")
with c2:
    slope_v_per_a = st.slider(lang("Spannungsanstieg (V/A)", "Voltage rise (V/A)"), 0.1, 2.0, 0.6, 0.1, key="sim_h2_slope")

plot_current_ma = np.linspace(0, 500, 101)
plot_voltage_v = onset_v + slope_v_per_a * (plot_current_ma / 1000.0)
fig2, ax2 = plt.subplots(figsize=(8.5, 3.5))
ax2.plot(plot_current_ma, plot_voltage_v, color="#1689B7", linewidth=2.4)
ax2.scatter([0], [onset_v], color="#D66B37", zorder=5)
ax2.set_xlabel(lang("Strom I (mA)", "Current I (mA)"))
ax2.set_ylabel(lang("Spannung U (V)", "Voltage U (V)"))
ax2.set_xlim(0, 500)
ax2.grid(alpha=0.25)
st.pyplot(fig2, use_container_width=True)
plt.close(fig2)
st.metric(lang("Achsenabschnitt bei I = 0", "Intercept at I = 0"), f"{show_number(onset_v)} V")
st.caption(lang(
    "Die reale I-U-Kennlinie ist häufig nicht über den gesamten Strombereich exakt linear. "
    "Für die Auswertung in Versuch 1 nutzt ihr eure Messdaten und wählt den annähernd geradlinigen Abschnitt.",
    "A real I-V characteristic is often not perfectly linear over the entire current range. "
    "For Experiment 1, use your actual measurements and select the approximately linear region.",
))

# ----- 3. Electrical energy --------------------------------------------------
st.divider()
heading("3 – Elektrische Energie berechnen", "3 – Calculate electrical energy")
st.write(lang(
    "Passend zu **Versuch 3 und 4**: Berechnet die elektrische Energie aus "
    "Spannung, Stromstärke und Zeit. Die Werte könnt ihr aus euren Messungen übernehmen.",
    "Related to **Experiments 3 and 4**: Calculate electrical energy from voltage, "
    "current and time. You can enter values from your own measurements.",
))
e1, e2, e3 = st.columns(3)
with e1:
    voltage_v = st.number_input(lang("Spannung U (V)", "Voltage U (V)"), min_value=0.0, max_value=30.0, value=1.8, step=0.1, key="sim_h2_voltage")
with e2:
    measured_ma = st.number_input(lang("Stromstärke I (mA)", "Current I (mA)"), min_value=0.0, max_value=2000.0, value=400.0, step=10.0, key="sim_h2_energy_current")
with e3:
    measured_s = st.number_input(lang("Zeit t (s)", "Time t (s)"), min_value=0.0, max_value=100000.0, value=120.0, step=10.0, key="sim_h2_time")
energy_j = voltage_v * measured_ma / 1000.0 * measured_s
st.metric(lang("Elektrische Energie", "Electrical energy"), f"{show_number(energy_j)} J")
st.latex(r"E=U\cdot I\cdot t")
st.caption(lang(
    "Falls die Spannung während des Versuchs schwankt, ist die Rechnung mit dem Mittelwert "
    "eine Näherung. Für eine genauere Bestimmung wäre der zeitliche Verlauf von U und I nötig.",
    "If the voltage varies during the experiment, using an average is an approximation. "
    "A more accurate determination would use the voltage and current over time.",
))

# ----- 4. Energy content and efficiencies ------------------------------------
st.divider()
heading("4 – Brennwert und Wirkungsgrade", "4 – Energy content and efficiencies")
st.write(lang(
    "Passend zu **Versuch 5**: Vergleicht zugeführte elektrische Energie, "
    "Energieinhalt des Wasserstoffs und abgegebene elektrische Energie der Brennstoffzelle. "
    "Verwendet für die Vergleichbarkeit den Brennwert aus euren Unterlagen: **11,71 J/ml H₂**.",
    "Related to **Experiment 5**: Compare the electrical input energy, the energy "
    "content of hydrogen and the fuel cell's electrical output energy. "
    "For consistency with your worksheets, use **11.71 J/ml H₂**.",
))
vcol, icol, ocol = st.columns(3)
with vcol:
    volume_ml = st.number_input(lang("Wasserstoffvolumen (ml)", "Hydrogen volume (ml)"), min_value=0.0, max_value=1000.0, value=10.0, step=1.0, key="sim_h2_vol")
with icol:
    electrical_input = st.number_input(lang("Energie Elektrolyseur – Eingang (J)", "Electrolyzer input energy (J)"), min_value=0.0, max_value=100000.0, value=180.0, step=1.0, key="sim_h2_in")
with ocol:
    electrical_output = st.number_input(lang("Energie Brennstoffzelle – Ausgang (J)", "Fuel cell output energy (J)"), min_value=0.0, max_value=100000.0, value=41.0, step=1.0, key="sim_h2_out")

chemical_j = volume_ml * H2_ENERGY_J_PER_ML
eta_electrolyzer = 100.0 * chemical_j / electrical_input if electrical_input > 0 else None
eta_fuel_cell = 100.0 * electrical_output / chemical_j if chemical_j > 0 else None
eta_total = 100.0 * electrical_output / electrical_input if electrical_input > 0 else None

m1, m2, m3 = st.columns(3)
m1.metric(lang("Chemische Energie", "Chemical energy"), f"{show_number(chemical_j)} J")
m2.metric(lang("Elektrolyseur", "Electrolyzer"), f"{show_number(eta_electrolyzer, 1)} %" if eta_electrolyzer is not None else "–")
m3.metric(lang("Brennstoffzelle", "Fuel cell"), f"{show_number(eta_fuel_cell, 1)} %" if eta_fuel_cell is not None else "–")
if eta_total is not None:
    st.metric(lang("Gesamtwirkungsgrad", "Overall efficiency"), f"{show_number(eta_total, 1)} %")

if electrical_input == 0 or chemical_j == 0:
    st.info(lang(
        "Für die entsprechenden Wirkungsgrade muss der jeweilige Nenner größer als 0 sein.",
        "To calculate the corresponding efficiencies, the relevant denominator must be greater than zero.",
    ))
if (eta_electrolyzer is not None and eta_electrolyzer > 100) or (eta_fuel_cell is not None and eta_fuel_cell > 100) or (eta_total is not None and eta_total > 100):
    st.warning(lang(
        "Ein Wirkungsgrad über 100 % weist hier auf nicht zueinander passende Werte, "
        "Mess- oder Einheitenfehler oder unterschiedliche Energiebezugsgrößen hin.",
        "An efficiency above 100% here suggests inconsistent values, "
        "measurement/unit errors or different energy reference conventions.",
    ))

fig4, ax4 = plt.subplots(figsize=(8.5, 3.3))
energy_values = [electrical_input, chemical_j, electrical_output]
ax4.bar(["E in", "H₂", "E out"], energy_values, color=["#1689B7", "#47AE9F", "#D66B37"])
ax4.set_ylabel("J")
ax4.set_ylim(0, max(energy_values + [1]) * 1.25)
ax4.grid(axis="y", alpha=0.25)
st.pyplot(fig4, use_container_width=True)
plt.close(fig4)

with st.expander(lang("Rechenweg anzeigen", "Show formulas")):
    st.latex(r"E_{H_2}=V_{H_2}\cdot 11.71\,\frac{\mathrm{J}}{\mathrm{ml}}")
    st.latex(r"\eta_\mathrm{EL}=\frac{E_{H_2}}{E_\mathrm{ein}}\cdot100\%")
    st.latex(r"\eta_\mathrm{BZ}=\frac{E_\mathrm{aus}}{E_{H_2}}\cdot100\%")
    st.latex(r"\eta_\mathrm{gesamt}=\frac{E_\mathrm{aus}}{E_\mathrm{ein}}\cdot100\%")
    st.caption(lang(
        "Vereinfachte Energiebilanz ohne zusätzliche Verluste beim Speichern oder Transportieren. "
        "Die verwendeten 11,71 J/ml sind der Unterrichtswert aus dem EnerTec-Arbeitsblatt.",
        "Simplified energy balance, excluding additional storage and transport losses. "
        "The value of 11.71 J/ml comes from the EnerTec worksheet.",
    ))

# ----- 5. Scenario explorer -------------------------------------------------
st.divider()
heading("5 – Was bleibt von 100 J übrig?", "5 – What remains from 100 J?")
st.write(lang(
    "Verändert die Wirkungsgrade beider Geräte. So erkennt ihr, warum beim Umweg "
    "von Strom über Wasserstoff zurück zu Strom Energie verloren geht.",
    "Adjust the efficiencies of both devices to see why converting electricity "
    "to hydrogen and back to electricity involves energy losses.",
))
sc1, sc2 = st.columns(2)
with sc1:
    eff_el = st.slider(lang("Wirkungsgrad Elektrolyseur (%)", "Electrolyzer efficiency (%)"), 30, 95, 70, 5, key="sim_h2_eff_el")
with sc2:
    eff_fc = st.slider(lang("Wirkungsgrad Brennstoffzelle (%)", "Fuel cell efficiency (%)"), 20, 80, 50, 5, key="sim_h2_eff_fc")
start_j = 100.0
hydrogen_j = start_j * eff_el / 100.0
recovered_j = hydrogen_j * eff_fc / 100.0
st.metric(lang("Von 100 J zurückgewonnene elektrische Energie", "Electrical energy recovered from 100 J"), f"{show_number(recovered_j, 1)} J")
st.progress(int(round(recovered_j)))
st.caption(lang(
    f"Gesamtwirkungsgrad: {show_number(recovered_j, 1)} %. "
    "Speicher-, Transport- und Hilfsenergieverluste sind nicht berücksichtigt.",
    f"Overall efficiency: {show_number(recovered_j, 1)}%. "
    "Storage, transport and auxiliary-energy losses are not included.",
))

st.divider()
st.caption(lang(
    "EnerTec · Lernsimulationen zu den Wasserstoffexperimenten. Die Simulationswerte sind "
    "keine Musterlösungen für eure eigenen Messdaten.",
    "EnerTec · Educational simulations for the hydrogen experiments. Simulated values "
    "are not answer keys for your own experimental data.",
))
