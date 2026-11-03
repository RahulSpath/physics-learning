# Atomic and Molecular Physics, Data First

Lecture notes for Section VII (Atomic & Molecular Physics) of the CSIR-UGC NET Physical Sciences syllabus.

Every topic starts from real data from a classic experiment found in standard textbooks. The theory is then developed to explain that data. This is also how the subject grew: Balmer fitted the hydrogen lines in 1885, almost 30 years before Bohr explained them.

**Start with [Lecture 0](lecture-0-spectroscopy-as-response.md).** It sets up the common language for the whole course: a spectrum measures the atom's response function, as in linear-response theory in condensed matter.

## How each lecture works

1. **Data:** a spectrum, a table of lines or a measured curve. A short **How it is measured** box describes the apparatus, what is recorded and the resolution needed.
2. **Puzzle:** what the simple theory cannot explain.
3. **Model:** the theory that explains it.
4. **Numbers from the data:** constants such as the Rydberg constant, a bond length or a g-factor.
5. **Test a prediction** against more data.
6. **In response language:** one or two sentences linking the lecture back to Lecture 0.
7. **Problems** in CSIR-NET style, with answers.

## Units

| Unit | Lectures | Syllabus topics | Notes |
|---|---|---|---|
| 0. What a spectrum measures | 0 | The common language for selection rules, line widths, Einstein coefficients, ESR, NMR and Raman spectra | [Lec 0](lecture-0-spectroscopy-as-response.md) |
| 1. The hydrogen atom | 1–3 | Quantum states of an electron in an atom | [Unit 1](unit-1-hydrogen.md) |
| 2. Spin, fine and hyperfine structure | 4–6 | Electron spin; relativistic corrections for the energy levels of hydrogen; hyperfine structure and isotope shift | [Unit 2](unit-2-spin-fine-hyperfine.md) |
| 3. Many-electron atoms | 7–10 | Spectra of helium and alkali atoms; LS and jj coupling; width of spectral lines | Planned |
| 4. Atoms in fields | 11–13 | Zeeman, Paschen–Back and Stark effects; electron spin resonance; nuclear magnetic resonance and chemical shift | Planned |
| 5. Molecules | 14–17 | Born–Oppenheimer approximation; electronic, rotational, vibrational and Raman spectra of diatomic molecules; selection rules; Franck–Condon principle | Planned |
| 6. Lasers | 18–20 | Spontaneous and stimulated emission; Einstein A and B coefficients; optical pumping, population inversion, rate equations; modes of resonators and coherence length | Planned |

## Lectures

0. What a spectrum measures: spectroscopy as linear response
1. The hydrogen spectrum and the Rydberg formula
2. Energy levels are real: Franck–Hertz, Bohr and the reduced mass
3. Quantum states: the Schrödinger hydrogen atom and selection rules
4. Electron spin: Stern–Gerlach and the sodium doublet
5. Fine structure of hydrogen: relativistic corrections and the Dirac formula
6. Hyperfine structure (the 21 cm line) and isotope shifts
7. Alkali spectra and the quantum defect
8. Helium: exchange, singlets and triplets
9. LS and jj coupling
10. Widths of spectral lines
11. Zeeman and Paschen–Back effects
12. The Stark effect
13. Magnetic resonance: ESR and NMR
14. The Born–Oppenheimer approximation and rotational spectra
15. Vibrational spectra
16. Raman spectra
17. Electronic spectra and the Franck–Condon principle
18. Einstein A and B coefficients
19. Population inversion, rate equations and optical pumping
20. Resonator modes and coherence length

## Experiments for each syllabus topic

| Syllabus topic | Textbook experiment and data | Theory it leads to |
|---|---|---|
| Quantum states of an electron in an atom | Hydrogen Balmer lines at 656.3, 486.1, 434.0 and 410.2 nm. Franck–Hertz: in mercury vapour the current drops every 4.9 V | Rydberg formula, Bohr model, Schrödinger hydrogen atom: $`E_n = -13.6\ \text{eV}/n^2`$; quantum numbers n, l, m |
| Electron spin | Stern–Gerlach: a silver beam splits in two. The sodium D line is a doublet at 589.0 and 589.6 nm | Spin ½, spin magnetic moment, spin–orbit coupling |
| Alkali spectra | Sodium's sharp, principal and diffuse series, converging to the ionization energy of 5.14 eV | Quantum defect, $`E = -13.6\ \text{eV}/(n - \delta_l)^2`$, with $`\delta_s = 1.35`$, $`\delta_p = 0.86`$, $`\delta_d \approx 0`$; core penetration |
| Helium spectrum | Two separate line systems (singlet and triplet). The 1s2s levels at 19.82 eV (triplet) and 20.62 eV (singlet). Ground state at −79.0 eV | Pauli principle and exchange energy. Perturbation theory gives −74.8 eV; the variational method gives −77.5 eV |
| Relativistic corrections for hydrogen | Hα is a close doublet; the n = 2 fine structure is 0.365 cm⁻¹ | Relativistic kinetic energy, spin–orbit and Darwin terms; the Dirac energy formula |
| Hyperfine structure and isotope shift | Hydrogen's 21 cm line at 1420.4 MHz. Deuterium Hα at 656.10 nm against 656.28 nm for hydrogen | Coupling to the nuclear magnetic moment ($`F = I + J`$); reduced-mass correction |
| Width of spectral lines | Sodium D line: natural width about 10 MHz (lifetime 16 ns); Doppler width about 1.3 GHz at room temperature | Lifetime (Lorentzian), Doppler (Gaussian) and pressure broadening |
| LS and jj coupling | Calcium 4s4p ³P levels 52 and 106 cm⁻¹ apart (ratio 2). The np² level pattern changes from LS in carbon to jj in lead | Term symbols, Hund's rules, Landé interval rule, the jj limit |
| Zeeman and Paschen–Back effects | Cadmium 643.8 nm splits into three lines, 0.019 nm apart at 1 T. Sodium D1 splits into 4 lines and D2 into 6. Lithium's 2p doublet (0.34 cm⁻¹) reaches the strong-field regime at a few tesla | Normal Zeeman effect and e/m, Landé g-factor, anomalous Zeeman effect, decoupling of L and S |
| Stark effect | Hydrogen Balmer lines split in proportion to the electric field; alkali lines shift as its square | Degenerate perturbation theory ($`\pm 3ea_0F`$ for n = 2); polarizability |
| Electron spin resonance | DPPH absorbs at g = 2.0036 (9.5 GHz at 0.34 T). Mn²⁺ gives six lines | $`h\nu = g\mu_B B`$; hyperfine splitting into 2I + 1 lines |
| NMR and chemical shift | The 1951 proton spectrum of ethanol: three peaks with areas 3 : 2 : 1 | Larmor precession (42.58 MHz/T), shielding, chemical shift in ppm |
| Born–Oppenheimer approximation | Vibrational frequencies of H₂, HD and D₂: 4401, 3813 and 3116 cm⁻¹; H₂/D₂ = 1.413 ≈ √2 | Electronic and nuclear motion separate; all isotopes share one potential curve |
| Rotational spectra | CO microwave lines every 3.84 cm⁻¹, the first at 115.3 GHz | Rigid rotor, ΔJ = ±1, bond length 1.13 Å, centrifugal distortion |
| Vibrational spectra | HCl infrared band at 2886 cm⁻¹: P and R branches, no Q branch, doublets from ³⁵Cl and ³⁷Cl, overtone at 5668 cm⁻¹ | Harmonic oscillator, then the Morse potential; anharmonicity; vibration–rotation coupling |
| Raman spectra | N₂ rotational Raman lines every 8 cm⁻¹, with intensities alternating 2 : 1. CCl₄ lines at 218, 314, 459 and 762/790 cm⁻¹ | Polarizability, ΔJ = 0, ±2, nuclear-spin statistics, mutual exclusion (CO₂) |
| Electronic spectra and Franck–Condon principle | I₂ visible absorption bands, converging near 499 nm | Franck–Condon factors; Birge–Sponer extrapolation to the dissociation energy |
| Einstein A and B coefficients | Sodium 3p lifetime of 16 ns, so A = 6.2 × 10⁷ s⁻¹ | Spontaneous and stimulated emission; $`A/B \propto \nu^3`$ |
| Optical pumping, population inversion, rate equations | He–Ne laser: helium's 2¹S level (20.62 eV) matches a neon level (20.66 eV). A laser diode's light output jumps at a threshold current. Rubidium optical pumping | Three- and four-level systems, rate equations and threshold, optical pumping |
| Resonator modes and coherence length | A 30 cm He–Ne cavity has modes 500 MHz apart. Michelson interferometer with a sodium lamp: the fringes fade every 0.29 mm of mirror travel | Longitudinal and transverse modes; coherence length ≈ λ²/Δλ |

## Where the data comes from

- **Atoms:** Haken & Wolf, *The Physics of Atoms and Quanta*; White, *Introduction to Atomic Spectra*; Foot, *Atomic Physics*; Eisberg & Resnick, *Quantum Physics of Atoms, Molecules, Solids, Nuclei, and Particles*.
- **Molecules:** Banwell & McCash, *Fundamentals of Molecular Spectroscopy*; Herzberg, *Spectra of Diatomic Molecules*.
- **Lasers:** Svelto, *Principles of Lasers*; Thyagarajan & Ghatak, *Lasers: Fundamentals and Applications*.
- **Checking numbers:** the NIST Atomic Spectra Database and the NIST Chemistry WebBook.

## Conventions

- Visible wavelengths are given in air, as in most textbooks, unless marked "vacuum". To convert, multiply the air wavelength by $`n_\text{air} \approx 1.00028`$.
- Constants are CODATA 2018 values.
- Every derived number in the notes was checked with a short calculation.
