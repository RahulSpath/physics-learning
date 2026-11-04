# Atomic and Molecular Physics · Course map

**Plan for Version 1: a connected MSc-level course covering CSIR–UGC NET Physical Sciences, Part B, Section VII.** The table gives the whole argument; the sections below give first-pass outlines. All units now have connected first drafts; drafting status and remaining refinements are recorded at the end.

| Unit | Central question and essential content | Connection to the next unit |
|---|---|---|
| **0. How do we learn about the microscopic world?** | How do measurements reveal microscopic properties? Instrument signals, spectra, energy differences and probe-dependent inference. | Lines constrain energy differences. What makes an atom's bound-state energies discrete? |
| **1. The hydrogen atom** | What explains discrete levels and spectral series? Balmer/Rydberg patterns, Franck–Hertz electron-impact evidence, the Coulomb Hamiltonian, quantum numbers and reduced mass. | The Coulomb model explains the main pattern, but precise measurements reveal splittings. Which interactions have we neglected? |
| **2. Spin and atomic fine structure** | What explains the resolved hydrogen excitation resonances? A motivated magnetic-gradient measurement, spin, spin–orbit coupling, relativistic corrections, hyperfine structure and isotope shifts. | These interactions refine a one-electron model. What changes when several electrons repel one another and obey the Pauli principle? |
| **3. Many-electron atoms** | How do interacting electrons change atomic spectra? Helium, exchange, Pauli principle, singlets/triplets, alkalis, quantum defects and LS/jj coupling. | Level patterns suggest state assignments. How can applied fields test them and control the states? |
| **4. Atoms in external fields** | How do fields shift, split and connect states? Zeeman, Paschen–Back and Stark effects; ESR, NMR and chemical shifts. | We can predict shifts and splittings. What determines a line's visibility, intensity and width? |
| **5. Light–matter interaction** | What determines strengths, widths and laser oscillation? Matrix elements, selection rules, Einstein coefficients, lifetimes, broadening, pumping, inversion, rate equations, resonator modes and coherence. | Atomic transitions now have positions, strengths and widths. What new levels arise when nuclei move within a molecule? |
| **6. Molecules and nuclear motion** | How do molecules bind, rotate and vibrate? Potential-energy curves, Born–Oppenheimer approximation, rotational/vibrational levels and rovibrational structure. | Nuclear motion supplies new levels. Which transitions can different probes reveal? |
| **7. Molecular spectroscopy** | How do probes reveal molecular motion and electronic structure? Infrared, Raman and electronic spectra, selection rules, Franck–Condon factors and vibrational progressions. | We can interpret individual transitions. How much can we infer when species overlap and the instrument obscures structure? |
| **8. Putting the ideas together** | What can a complex spectrum establish? Individual Hg, Cd and Ar spectra, mixtures, line identification, resolution, calibration and limits of inference. | Return to Unit 0: which conclusions follow from the measurement, and which further observation would resolve an ambiguity? |

The course develops a recurring investigation: **observation → provisional model → quantitative prediction → proposed experimental test → measured result → assessment and next question**. Before interpreting a new record, explain what is varied, what is measured and which outcomes would distinguish the predictions. Existing measurements can supply the test; the teaching order should make clear why we would seek that measurement.

Agreement establishes the model's useful range and motivates tests at greater precision, under changed conditions or in a different system. A discrepancy prompts checks of preparation, calibration, resolution and the interaction with the probe, alongside possible missing physics. A new observable or probe can also open the next question. The sequence should not require a failed prediction at every step.

This is a reconstruction of scientific reasoning rather than a chronological account of discovery. State which measurements already exist, which experiment is being proposed for the argument and which record remains a visible TODO. Historical context can explain how the questions actually arose, including earlier data reinterpreted by later models. Links to original research papers are useful when they illuminate motivations, experimental difficulties or historical development, while the physical argument remains self-contained. Each unit should develop the cycle in the form its physics needs.

A recurring distinction is that **what we measure is not everything that exists in the system**. An absent peak may reflect a selection rule, an unpopulated state, broadening or limited sensitivity.

**Conventions.** Quoted visible wavelengths are in air unless explicitly marked vacuum. Energy and spectroscopic wavenumber conversions use $`\lambda_{\mathrm{vac}}=n_{\mathrm{air}}\lambda_{\mathrm{air}}`$; use wavelength-dependent refractive indices when precision requires them. Constants are CODATA 2018 values. Distinguish measured records, tabulated measurements and model illustrations.

The first two days establish this map and Unit 0. Then develop each unit in sequence: Day 1 builds its physical argument; Day 2 tests the explanation with a useful example, questions and references. Version 1 needs essential reasoning and equations throughout the syllabus. Available data should strengthen that argument; missing datasets must not prevent its completion.

## Unit 0 · How do we learn about the microscopic world?

**Central question.** We cannot directly see the internal quantum states of an atom or molecule. How do we learn about them through measurements?

**Motivating observation.** A hydrogen discharge produces discrete optical lines, while a sample in a magnetic field, exposed to microwaves, gives a signal at a particular field. What does each instrument record, and what microscopic interpretation requires a model?

**Essential concepts.** Six short sections, using plain language and a single measured hydrogen plot:

1. **What does an experiment actually give us?** Compare an emission spectrum with a resonance signal, described plainly.
2. **An atomic emission spectrum.** Begin with a measured hydrogen spectrum, intensity against wavelength; explain its axes before interpreting its peaks.
3. **What information does a spectral line contain?** Ask about position, strength, width and response to external conditions.
4. **From observations to a mathematical model.** Introduce states, energies and probe-dependent access to transitions.
5. **The same reasoning across physics.** In one short paragraph, carry the distinction between signal, coupling and interpretation beyond the opening examples. Introduce each technique by name when its physics is needed.
6. **Questions that will guide the course.** In connected prose, ask why bound energies are discrete (Unit 1), why lines split (Units 2–4), why transitions differ in visibility and width (Unit 5), and why molecular motion produces new structure (Units 6–7). End with the first unresolved observation: hydrogen's separated wavelengths.

**Indispensable equations.**

```math
H|n\rangle=E_n|n\rangle,\qquad
E_u-E_l=h\nu=\frac{hc}{\lambda_{\mathrm{vac}}}
=hc\tilde{\nu},\qquad
\tilde{\nu}=\frac{1}{\lambda_{\mathrm{vac}}}.
```

A transition’s visibility also depends on the probe’s coupling to the system; no perturbation-theory or susceptibility derivation is needed here.

**Syllabus coverage.** Conceptual preparation for all units. Energy differences, transition strengths and widths appear here as questions; their explanations follow below.

**Connection to Unit 1.** We can translate hydrogen's line positions into photon energies and constrain differences between atomic energies. We have not explained the pattern. What model of the electron and nucleus predicts discrete bound-state energies and the observed separations?

## Unit 1 · The hydrogen atom

**Central question.** What physical model explains hydrogen’s spectral series and their convergence towards ionization?

**Motivating observation.** The Balmer lines crowd towards a series limit. Ask which pattern accounts for their spacings, then what physical model produces it. To test whether internal excitation energies also govern collisions, design an electron-impact measurement before introducing mercury as the Franck–Hertz implementation. Varying nuclear mass tests the reduced-mass prediction; preparing a common initial state tests whether apparently degenerate upper levels remain degenerate at higher resolution.

**Essential concepts.** Balmer and Rydberg patterns; the Ritz combination principle; Franck–Hertz and electron-impact excitation; the Coulomb Hamiltonian; normalizable bound states; quantum numbers $`n,l,m`$; wavefunctions and degeneracy; reduced mass. Use Bohr’s model briefly to connect the observed pattern to energy scales, then explain quantization through the Schrödinger problem.

**Indispensable equations.**

```math
H_C=\frac{p^2}{2\mu}-\frac{Ze^2}{4\pi\varepsilon_0r},
\qquad
\mu=\frac{m_eM}{m_e+M},
\qquad
\psi_{nlm}=R_{nl}(r)Y_{lm}(\theta,\phi).
```

```math
E_n=-hcR_M\frac{Z^2}{n^2},
\qquad
R_M=R_\infty\frac{\mu}{m_e},
\qquad
\tilde{\nu}=Z^2R_M
\left(\frac{1}{n_l^2}-\frac{1}{n_u^2}\right).
```

Here $`n=1,2,\ldots`$, $`l=0,\ldots,n-1`$ and $`m=-l,\ldots,l`$.

**Syllabus coverage.** Quantum states of an electron in an atom. Introduce isotope shifts through reduced mass before Unit 2. Introduce electric-dipole matrix elements and the basic rules $`\Delta l=\pm1`$, $`\Delta m=0,\pm1`$ to explain why 2p and 2s decay differently; rates and the general framework belong to Unit 5.

**Connection to Unit 2.** The hydrogen spectrum suggests that electronic energies are quantized, and the Coulomb Hamiltonian explains their approximate values. But sufficiently precise measurements reveal additional structure that the simplest model cannot explain. What physical degrees of freedom and interactions have we neglected?

## Unit 2 · Spin and atomic fine structure

**Central question.** Why do apparently single atomic levels and spectral lines split?

**Motivating observation.** Unit 1's measured hydrogen 2s → 6p excitation record resolves two resonances where the Coulomb model predicts one. Their separation establishes additional structure but does not identify its cause. Motivate a magnetic-gradient beam measurement as an independent probe of magnetic moment and angular momentum before introducing Stern–Gerlach. Return to the hydrogen interval to test the extended model, then propose measurements of the remaining degeneracies and nuclear contributions.

**Essential concepts.** Electron spin and magnetic moment; addition of orbital and spin angular momenta; spin–orbit coupling; relativistic kinetic-energy and Darwin corrections; nuclear spin and hyperfine coupling; mass and nuclear-volume isotope shifts. Distinguish these mechanisms by their energy scales. Test the remaining 2s–2p degeneracy through a microwave-induced depletion measurement before introducing the Lamb shift, without requiring a QED derivation. Compare isotope line centroids separately from their hyperfine component patterns.

The provisional draft uses sections 2.1–2.8: the resolved hydrogen record; a magnetic probe and spin; angular-momentum addition; fine-structure corrections and the leading 6p estimate; the remaining degeneracy and Lamb shift; hyperfine coupling and contact-density scaling; isotope shifts; and the question of a second electron. Visible TODO boxes mark the missing Stern–Gerlach record, independent fine-structure comparison, Lamb-shift depletion curve, hyperfine resonance and isotope comparison.

**Indispensable equations.**

```math
\boldsymbol{\mu}_s=-g_s\mu_B\frac{\mathbf S}{\hbar},
\qquad s=\frac12,
\qquad \mathbf J=\mathbf L+\mathbf S.
```

```math
H_{\mathrm{fs}}=
-\frac{p^4}{8m_e^3c^2}
+\frac{1}{2m_e^2c^2r}\frac{dV}{dr}\,\mathbf L\cdot\mathbf S
+\frac{\hbar^2}{8m_e^2c^2}\nabla^2V.
```

For a point nucleus of infinite mass, through the leading fine-structure correction,

```math
E_{nj}\simeq E_n^{(0)}
\left[1+\frac{(Z\alpha)^2}{n^2}
\left(\frac{n}{j+\tfrac12}-\frac34\right)\right].
```

For magnetic-dipole hyperfine structure,

```math
H_{\mathrm{hf}}=A_{\mathrm{hf}}\frac{\mathbf I\cdot\mathbf J}{\hbar^2},
\qquad
E_F=\frac{A_{\mathrm{hf}}}{2}
\left[F(F+1)-I(I+1)-J(J+1)\right].
```

Here $`\mathbf F=\mathbf I+\mathbf J`$ and $`A_{\mathrm{hf}}`$ has energy units. Additional hyperfine interactions are needed where nuclear quadrupole moments contribute.

**Syllabus coverage.** Electron spin; relativistic corrections to hydrogen energy levels; hyperfine structure and isotopic shift. Sodium and other alkali doublets belong with the electronic structure and angular-momentum coupling developed in Unit 3. Intensity ratios require the transition and population framework of Unit 5.

**Connection to Unit 3.** Spin, relativistic corrections and nuclear properties explain structure absent from the Coulomb model. Yet helium cannot be described by putting two independent electrons into hydrogenic levels. What changes when electrons repel one another and the total state must obey the Pauli principle?

## Unit 3 · Many-electron atoms

**Central question.** How do electron interactions produce helium’s two spectral systems, alkali series and different angular-momentum coupling schemes?

**Motivating observation.** Unit 2 ends by proposing a controlled change from He⁺ to helium: keep nuclear charge fixed and add a second electron. Ionization thresholds test the independent-electron binding prediction. Helium's repeated excitation families then motivate Pauli symmetry and exchange. Move to alkali series to test a closed-core approximation, and use multiplet intervals to investigate how several angular momenta couple.

**Essential concepts.** Electron repulsion, a short variational estimate, screening and correlation; antisymmetry and the Pauli principle; direct and exchange energies; helium singlets, triplets and metastability; central-field approximations; alkali core penetration and quantum defects; term symbols, Hund’s rules and the Landé interval rule. Compare residual electrostatic interactions with spin–orbit coupling to distinguish LS, jj and intermediate coupling. Include the correlated mass shift left open in Unit 2.

The provisional draft uses sections 3.1–3.8: the He⁺–He binding test; repulsion and screening; Pauli symmetry; exchange and accessible helium lines; alkali series and a held-out sodium-level prediction; LS terms, Hund ordering and a calcium interval test; jj and intermediate coupling; and external fields as the next probe. Visible TODO boxes mark helium ionization thresholds, calibrated helium spectra and preparation, an alkali series, multiplet reconstruction and state assignments, and a comparison across coupling regimes.

**Indispensable equations.**

```math
H=\sum_i\left(\frac{p_i^2}{2m_e}
-\frac{Ze^2}{4\pi\varepsilon_0r_i}\right)
+\sum_{i<j}\frac{e^2}{4\pi\varepsilon_0r_{ij}}.
```

For distinct orthogonal orbitals in a first-order helium model, and for alkali binding energies measured from ionization,

```math
E_{\mathrm{singlet/triplet}}=E^{(0)}+J_C\pm K,
\qquad
E_{nl}\simeq-\frac{hcR_M}{(n-\delta_l)^2}.
```

```math
\begin{aligned}
\text{LS:}\quad&
\mathbf L=\sum_i\mathbf l_i,\quad
\mathbf S=\sum_i\mathbf s_i,\quad
\mathbf J=\mathbf L+\mathbf S,\\
\text{jj:}\quad&
\mathbf j_i=\mathbf l_i+\mathbf s_i,\quad
\mathbf J=\sum_i\mathbf j_i,\\
&E_J-E_{J-1}=A_{\mathrm{LS}}J
\quad\text{within an isolated LS term.}
\end{aligned}
```

**Syllabus coverage.** Spectra of helium and alkali atoms; LS and JJ coupling. Explain the approximate LS rule $`\Delta S=0`$ through helium, and how state mixing weakens it. Unit 5 supplies the fuller transition framework. Introduce the additional, correlated mass shift in many-electron atoms.

**Connection to Unit 4.** Electron interactions and angular-momentum coupling explain multiplet patterns and suggest assignments of the states. A zero-field spectrum does not fully establish their magnetic moments or electric response. How can applied fields test those assignments and let us manipulate the states?

## Unit 4 · Atoms in external fields

**Central question.** How do electric and magnetic fields shift, split and connect atomic states?

**Motivating observation.** Unit 3 assigns angular momenta to atomic states; those assignments predict magnetic responses beyond the zero-field energies. Propose a calibrated field-off and field-on optical comparison, then test the predicted shifts and polarization patterns. Increase the field to test the assumed coupling, change to an electric perturbation to probe state mixing, and motivate magnetic resonance as a direct measurement between field-dependent states.

**Essential concepts.** Normal and anomalous Zeeman effects; Landé factors and polarized components; Paschen–Back decoupling when magnetic energies exceed spin–orbit intervals; degenerate and non-degenerate Stark perturbations; magnetic-dipole transitions; ESR and NMR; nuclear shielding and chemical shift. Use $`F`$ rather than $`J`$ where resolved hyperfine coupling controls the weak-field states.

The provisional draft uses sections 4.1–4.8: field predictions and the normal Zeeman effect; Landé factors, sodium patterns, polarization and hyperfine qualifications; Paschen–Back coupling changes; quadratic and degenerate Stark effects; direct magnetic resonance; ESR; NMR and chemical shifts; and the question of signal strengths and widths. Five visible TODO boxes identify the missing weak-field optical record, high-field crossover, Stark field series, ESR record and NMR environment comparison. Its calculated Zeeman figure is a model illustration, not an experimental trace.

**Prediction and test.** Use the assigned states to predict field-dependent energies, transition frequencies and polarization components. Vary a calibrated magnetic or electric field and record the spectrum. Compare weak- and strong-field behaviour to test the assumed coupling hierarchy. Then motivate magnetic-resonance measurements as direct tests of transitions between the field-dependent states, including nuclear shielding in NMR.

**Indispensable equations.**

```math
H_Z=\frac{\mu_BB}{\hbar}(L_z+g_sS_z),
\qquad
\Delta E_Z=g_J\mu_BBm_J
\quad\text{in the electronic weak-field limit}.
```

For LS coupling, with $`g_s\simeq2`$ and $`J>0`$,

```math
g_J=1+\frac{J(J+1)+S(S+1)-L(L+1)}{2J(J+1)}.
```

In the Paschen–Back limit, use $`m_L,m_S`$ and $`\Delta E_Z\simeq\mu_BB(m_L+g_sm_S)`$.

```math
H_E=-\mathbf d\cdot\boldsymbol{\mathcal E},
\qquad
\Delta E_{\mathrm{quadratic}}=-\frac12\alpha_{\mathrm{stat}}\mathcal E^2.
```

```math
h\nu_{\mathrm{ESR}}=g\mu_BB,
\qquad
\nu_{\mathrm{NMR}}=\frac{|\gamma_N|}{2\pi}B_0(1-\sigma),
\qquad
\delta_{\mathrm{ppm}}=10^6
\frac{\nu_{\mathrm{sample}}-\nu_{\mathrm{reference}}}
{\nu_{\mathrm{reference}}}.
```

**Syllabus coverage.** Zeeman, Paschen–Back and Stark effects; electron spin resonance; nuclear magnetic resonance and chemical shift. Magnetic-resonance line widths introduce coherence decay; Unit 5 develops its relation to line shape.

**Connection to Unit 5.** Field-dependent shifts and splittings test our description of the states. Their energies still leave much of the measured signal unexplained: lines at allowed energy differences can be weak, absent or broadened. What determines transition probabilities, populations and the time scales behind a spectrum?

## Unit 5 · Light–matter interaction

**Central question.** What determines spectral strengths and widths, and how can emission become sustained laser oscillation?

**Motivating observation.** Unit 4 predicts field-dependent resonance positions but leaves their strengths, widths and time dependence unexplained. Propose calibrated line-area and decay measurements, then vary temperature, pressure and preparation to test the signal model. Changing populations motivates optical pumping and weak-probe gain; adding feedback tests whether amplification becomes laser oscillation.

**Essential concepts.** Dipole coupling and transition matrix elements; the golden rule; polarization, parity and angular-momentum selection rules; spontaneous and stimulated emission; Einstein coefficients; populations and branching ratios. Develop natural, Doppler and collision broadening, homogeneous and inhomogeneous widths, and Voigt profiles.

Then follow absorption into optical pumping, dark states, population inversion and elementary three- and four-level laser cycles. Distinguish pumping from inversion and gain from laser oscillation. Explain gain, loss and threshold with rate equations, followed by longitudinal and transverse resonator modes and temporal coherence. Detailed laser dynamics can be refined later.

The provisional draft uses sections 5.1–5.10: line areas and matrix elements; Einstein rates; population lifetime and coherence decay; controlled broadening; optical pumping and dark states; gain, inversion and three-/four-level systems; laser rate equations and threshold; longitudinal and transverse modes; coherence and doublet beating; and molecular motion as the next question. Seven visible TODO boxes mark calibrated branching strengths, decay and isolated linewidth, controlled broadening, pumping and remixing, weak-probe gain, threshold and cavity spectra, and interferometric coherence. The line-shape and laser-level figures illustrate models, not measured records.

**Prediction and test.** Use transition probabilities and prepared populations to predict strengths, decay times and spectral widths. Vary temperature and density to distinguish broadening mechanisms, and compare time-domain decay with spectral width. For a pumped medium, predict the gain–loss threshold before measuring output against pump strength. Check which additional observations distinguish laser oscillation from increased fluorescence.

**Indispensable equations.**

```math
H'(t)=-\mathbf d\cdot\mathbf E(t),
\qquad
A_{ul}=\frac{\omega_{ul}^3}{3\pi\varepsilon_0\hbar c^3}
|\langle l|\mathbf d|u\rangle|^2,
\qquad
\tau_{\mathrm{rad},u}^{-1}=\sum_l A_{ul}.
```

The electric-dipole operator requires a parity change and $`\Delta J=0,\pm1`$, excluding $`J=0\leftrightarrow0`$; LS coupling adds approximate $`\Delta S=0`$. Optically thin emitted power also depends on population: $`P_{ul}\propto N_uA_{ul}h\nu`$.

With Einstein B coefficients defined using spectral energy density per unit frequency,

```math
g_lB_{lu}=g_uB_{ul},
\qquad
\frac{A_{ul}}{B_{ul}}=\frac{8\pi h\nu^3}{c^3}.
```

For Lorentzian homogeneous and Gaussian Doppler profiles, the frequency FWHM values are

```math
\Delta\nu_{\mathrm{hom}}=\frac{1}{\pi T_2},
\qquad
\frac{1}{T_2}=\frac{\Gamma_u+\Gamma_l}{2}+\gamma_{\mathrm{deph}},
\qquad
\Delta\nu_D=\frac{\nu_0}{c}
\sqrt{\frac{8k_BT\ln2}{M}}.
```

Thus a radiative upper state above a stable lower state has natural width $`1/(2\pi\tau_u)`$. Population decay and pure dephasing are different processes.

For an ideal four-level laser with a rapidly emptied lower laser level,

```math
\dot N=R_p-\frac{N}{\tau}-v_g\sigma_eNn_\gamma,
\qquad
\dot n_\gamma=(v_g\sigma_eN-\kappa)n_\gamma+\beta\frac{N}{\tau}.
```

Here $`N`$ and $`n_\gamma`$ are upper-state and photon densities, $`R_p`$ is the pump rate density, $`\kappa`$ is the photon-number loss rate and $`\beta`$ is the fraction of unstimulated upper-state decays producing a photon in the selected mode, including radiative branching. Threshold occurs at $`v_g\sigma_eN=\kappa`$. More generally, inversion requires $`N_u/g_u>N_l/g_l`$.

For an empty cavity of length $`L`$,

```math
\nu_q=\frac{qc}{2L},
\qquad
\Delta\nu_{\mathrm{FSR}}=\frac{c}{2L},
\qquad
L_c=c\tau_c.
```

For a single Lorentzian spectral line, defining $`\tau_c`$ by the field correlation’s $`1/e`$ decay gives $`\tau_c=1/(\pi\Delta\nu)`$. Coherence length therefore requires a stated spectral shape and convention.

**Syllabus coverage.** Width of spectral lines; selection rules; lasers; spontaneous and stimulated emission; Einstein A and B coefficients; optical pumping; population inversion; rate equations; resonator modes and coherence length. This is the fuller treatment of transition ideas introduced in Units 0–4.

**Connection to Unit 6.** Transition theory connects atomic energy differences to strengths, lifetimes and widths, while pumping can turn absorption into gain. In a molecule, however, the nuclei can also move relative to one another. How does this motion create levels beyond the electronic structure of an atom?

## Unit 6 · Molecules and nuclear motion

**Central question.** How can electronic binding and nuclear motion be separated sufficiently to calculate molecular levels?

**Motivating observation.** Follow carbon monoxide from its closely spaced microwave lines to much larger infrared intervals. Ask what nuclear motions could produce those scales, then use rotational assignments to predict an unused line and isotope substitution to test the common-potential model. Published measured JPL line centres provide a first rotational comparison; they and reference molecular constants remain distinct from detector-intensity records.

**Essential concepts.** Molecular bonding and potential-energy curves; the Born–Oppenheimer approximation; nuclear reduced mass; equilibrium separation and dissociation; rigid rotation and harmonic vibration; anharmonicity, centrifugal distortion and vibration–rotation coupling. Explain the hierarchy of electronic, vibrational and rotational scales and where separation can fail.

The provisional draft uses sections 6.1–6.8: new molecular spacings in CO; binding and a potential minimum; electronic–nuclear separation; a rotational prediction; harmonic vibration; a matched isotope test; higher-excitation corrections and dissociation; and probe-dependent access as the next question. Five TODO boxes mark a rotational record, a rovibrational interval record, a matched isotope comparison, a held-out higher-excitation ladder and a dissociation or potential test. The rotational comparison uses published measured JPL line centres. The Morse and harmonic potential figure is a calculated illustration, not CO data.

**Prediction and test.** Infer a candidate molecular potential from a selected band pattern, then predict additional rotational and vibrational intervals. Within the same electronic potential, isotope substitution tests the predicted inverse-mass rotational scaling and inverse-square-root-mass vibrational scaling. Higher excitations test centrifugal distortion, anharmonicity and the range of the separation between electronic and nuclear motion.

**Indispensable equations.**

```math
\Psi(\mathbf r,R)\simeq\phi_a(\mathbf r;R)\chi_{avJ}(R),
\qquad
[T_N+U_a(R)]\chi_{avJ}=E\chi_{avJ},
\qquad
\mu_{\mathrm{red}}=\frac{M_1M_2}{M_1+M_2}.
```

The potential $`U_a(R)`$ includes electronic energy and nuclear repulsion once. Neglecting couplings generated by nuclear derivatives is the central approximation; small nuclear kinetic energy does not guarantee accuracy near small electronic gaps. Here $`\mu_{\mathrm{red}}`$ denotes nuclear reduced mass, distinct from the nuclear magneton $`\mu_N`$ used earlier.

```math
E_{\mathrm{rot}}=\frac{\hbar^2J(J+1)}{2\mu_{\mathrm{red}}R_e^2}
=hcB_eJ(J+1),
\qquad
\omega_v=\sqrt{\frac{k}{\mu_{\mathrm{red}}}},
```

```math
E_v\simeq\hbar\omega_v\left(v+\frac12\right)
-\hbar\omega_vx_e\left(v+\frac12\right)^2.
```

Here $`B_e`$ is in wavenumber units, $`\omega_v`$ is an angular frequency, and $`k`$ is the potential curvature at equilibrium. Distinguish equilibrium $`B_e`$ from vibrationally averaged $`B_v`$, harmonic constants from observed fundamentals, and the well depth $`D_e`$ from the ground-level dissociation energy $`D_0`$.

**Syllabus coverage.** Born–Oppenheimer approximation; the level structure underlying electronic, rotational and vibrational spectra of diatomic molecules. Spectral spacings appear at a basic level here; probe-dependent selection rules and observed bands belong to Unit 7.

**Connection to Unit 7.** Separating electronic and nuclear motion gives rotational and vibrational levels and explains their isotope dependence. These levels alone do not specify the observed bands. Which transitions can infrared light, Raman scattering and electronic absorption reveal, and why do their intensities differ?

## Unit 7 · Molecular spectroscopy

**Central question.** How do different probes reveal molecular rotation, vibration and electronic structure?

**Motivating observation.** Begin with the same CO molecule used in Unit 6, comparing its known rotational levels with a measured infrared overview. Ask which dipole couplings produce the observed branches and predict unused lines. Missing ordinary dipole absorption in a nonpolar molecule then motivates testing polarizability through Raman scattering. Higher-energy electronic bands pose a further question: why does one electronic transition distribute strength across a nuclear progression?

**Essential concepts.** Pure rotational and rovibrational spectra; permanent dipole versus its bond-length derivative; infrared activity, overtones and P/R branch predictions; Raman scattering through polarizability; Stokes and anti-Stokes shifts, polarization and thermal populations; electronic band origins and molecular symmetry; Franck–Condon factors and vibrational progressions.

The provisional draft uses sections 7.1–7.8: CO infrared evidence and probe access; dipole selection; P/R predictions and combination differences; a motivated nonpolar Raman experiment; Raman shift and intensity tests; electronic band origins; Franck–Condon overlaps and progressions; and ambiguous mixed spectra as the next question. Six TODO boxes mark a fundamental/overtone comparison, high-resolution held-out P/R reconstruction, nonpolar Raman record, thermal/polarization Raman test, electronic-band assignment and corrected Franck–Condon progression. The NIST CO infrared overview is measured but processed, smoothed and limited to 4 cm⁻¹ resolution; the Franck–Condon illustration is a calculated model.

Pure rotational electric-dipole transitions require a permanent molecular dipole and have $`\Delta J=\pm1`$. Harmonic vibrational absorption requires $`(d\mu/dR)_e\ne0`$ and has $`\Delta v=\pm1`$; anharmonicity permits weak overtones. For simple $`\Sigma\leftrightarrow\Sigma`$ rovibrational bands, $`\Delta J=\pm1`$ gives P and R branches without a Q branch.

Raman activity depends on polarizability: rotational Raman shifts have $`\Delta J=\pm2`$, while vibrational Raman bands may include $`\Delta J=0,\pm2`$. For unchanged vibrational state, a $`\Delta J=0`$ contribution is unshifted Rayleigh scattering; $`\Delta J=0`$ can instead give a shifted Q branch when vibration changes.

**Prediction and test.** Combine Unit 6's levels with the interaction for each probe to predict accessible transitions and band strengths. If electric-dipole absorption misses a candidate excitation, ask whether its coupling through induced polarization makes a Raman measurement useful. Compare spectra of the same molecule under specified preparation. Test rotational branch spacings and vibrational progressions before refining the potential or transition-moment approximation.

**Indispensable equations.**

```math
\tilde{\nu}_{J\to J+1}\simeq2B_e(J+1),
\qquad
\nu_{\mathrm{Stokes/anti\text{-}Stokes}}
=\nu_L\mp\frac{\Delta E}{h}.
```

```math
\boldsymbol{\mu}_{\mathrm{ind}}
=\boldsymbol{\alpha}(R)\mathbf E,
\qquad
\boldsymbol{\alpha}(R)\simeq
\boldsymbol{\alpha}_e+
\left(\frac{\partial\boldsymbol{\alpha}}{\partial R}\right)_e(R-R_e).
```

In the Condon approximation, the electronic transition dipole varies slowly over the nuclear wavefunctions, giving the Franck–Condon factor

```math
q_{v'v}=
\left|\int u_{a'v'}^*(R)u_{av}(R)\,dR\right|^2.
```

Here $`u_{av}`$ are reduced radial nuclear functions normalized with $`dR`$, consistent with Unit 6. Corrected band strengths also require the electronic transition moment, populations, rotational factors and the appropriate frequency weighting.

**Syllabus coverage.** Electronic, rotational, vibrational and Raman spectra of diatomic molecules; molecular selection rules; Franck–Condon principle. Apply Unit 5’s transition framework to the levels established in Unit 6.

**Connection to Unit 8.** Molecular selection rules and wavefunction overlaps explain why different probes reveal different parts of the same level structure. We can now interpret individual transition mechanisms. How much of that information can we recover from a measured spectrum containing several species, unresolved blends and instrumental distortions?

## Unit 8 · Putting the ideas together

**Central question.** What microscopic conclusions can a complicated spectrum support, and what remains ambiguous?

**Motivating observation.** A processed Hg–Cd–Ar calibration archive contains features that invite candidate assignments and level reconstruction. Propose separate Hg, Cd and Ar control records first; they remain missing. Explain the empirical archive's continuum subtraction, segment normalization and stitching before interpreting its signal. Values of 10000 are normalization maxima, not established saturation.

**Essential concepts.** Candidate detection and guarded profile fits; reference assignments versus evidence; wavelength conventions, blends, resolution and uncertainty; conditional Ritz networks; independent closure tests and calibration; corrected branch areas; coupling and field-dependent tests. A four-edge tree connecting five levels reconstructs energies without independently testing a redundant relation.

The provisional draft uses sections 8.1–8.8: single-source controls; archive provenance; feature measurement; candidate identifications; conditional level reconstruction; an independent cycle test; strengths and field responses; and the evidence-to-next-measurement conclusion. Six TODO boxes mark single-element records, calibration and profile uncertainties, unused companions, a Ritz closure, calibrated branch areas and a field test. A numerical companion and machine-readable diagnostics reproduce the limited calculation without treating failed fits or imported labels as discoveries.

**Prediction and test.** Predict unused companion lines, a new transition closing a level cycle or field-dependent components. Compare those measurements with the existing assignments using independent calibration where required. Changing source, excitation, resolution or probe can distinguish alternatives. Preserve unassigned features and missing information explicitly.

**Indispensable equations.**

```math
\mathcal R=\frac{\lambda}{\delta\lambda},
\qquad
\tilde{\nu}_{ul}=\frac{E_u-E_l}{hc},
\qquad
\tilde{\nu}_{ua}-\tilde{\nu}_{ub}=\frac{E_b-E_a}{hc}.
```

A useful measurement model is

```math
S_{\mathrm{det}}(\lambda)=
[\eta(\lambda)S_{\mathrm{source}}(\lambda)]*G_{\mathrm{inst}}(\lambda)
+b(\lambda),
```

where $`\eta`$ represents spectral sensitivity, $`G_{\mathrm{inst}}`$ the instrumental profile and $`b`$ the background. Reference assignments and calibration standards are evidence entering the inference, not conclusions obtained from peak positions alone.

**Syllabus coverage.** Synthesis of quantum states, coupling, selection rules, intensities and widths, with external-field and molecular examples available for comparison. This unit adds no large theoretical topic.

**Closing connection.** We began with detector signals and asked what microscopic picture could account for them. We can now infer level spacings, test state assignments and recognize limits set by coupling, populations and the instrument. Which conclusions are established by the evidence, and what further measurement would distinguish the interpretations that remain?

## Draft status and further work

This records the present files and the remaining work after comparison with the course plan and supplied syllabus. The [Day 1 audit](day-1-audit.md) distinguishes the initial structural work from later unit development. The lamp calculation has been rerun with guarded core fits and an audited processing history. Its reference-calibrated axis still does not supply an independent wavelength test.

### Current notes and supporting material

| Current material | Destination and action |
|---|---|
| [Course README](README.md) and [top-level README](../README.md) | Navigation follows Units 0–8. State the actual drafting status and use a physical argument appropriate to each topic; the inherited seven-step format is not a requirement. |
| [Unit 0](unit-0-learning-from-measurements.md) | Six-section introduction to measurement and inference, with the measured hydrogen trace. Keep the final question as the reason to begin hydrogen. |
| [Former Lecture 0](reading-spectroscopy-as-response.md) | The course entrance is now the written [Unit 0](unit-0-learning-from-measurements.md). **Done:** retitled as optional response-theory reading attached to Unit 5 (Lorentz oscillator, polarizability, oscillator strengths, Kubo formula, sum rule and Kramers–Kronig relations), with sections renumbered R.1–R.8 and unit references updated to this map. Keep it as an optional companion after the core Unit 5 argument; the main unit does not require its response formulas. |
| [Unit 1](unit-1-hydrogen.md), sections 1.1–1.7 | Accepted as a provisional first draft, with writing to revisit: observed pattern, empirical rule, energy levels, Coulomb Hamiltonian, quantized bound states and tests using spectral series and deuterium. Franck–Hertz supplies independent excitation evidence. Basic selection rules preview Unit 5; measured Hδ excitation scans reveal structure beyond the Coulomb model and motivate Unit 2. |
| [Unit 2](unit-2-spin-fine-hyperfine.md), sections 2.1–2.8 | Provisional first connected draft: begin with the measured hydrogen excitation record, motivate a magnetic probe, then develop spin, angular-momentum addition, fine structure, the Lamb-shift test, hyperfine coupling and isotope shifts. Missing records and comparisons have visible TODO boxes. Its final question motivates helium and electron–electron interaction in Unit 3; further reader review and measurement enrichment remain. |
| [Unit 3](unit-3-many-electron-atoms.md), sections 3.1–3.8 | Provisional first connected draft: a controlled He⁺–He binding comparison leads through repulsion, screening, Pauli symmetry and exchange to helium's spectral families. Alkali series test a central-field quantum-defect model; multiplet intervals test LS coupling before jj and intermediate coupling. Missing records and comparisons have visible TODO boxes. The final question proposes external fields as a test of state assignments. |
| [Unit 4](unit-4-atoms-in-external-fields.md), sections 4.1–4.8 | Provisional first connected draft: predict field responses from the assigned states, test optical shifts and polarization, then develop coupling changes, electric-field mixing, ESR, NMR and chemical shielding. Five measurement comparisons remain visible TODOs. The calculated Zeeman figure displays predictions; the closing question motivates strengths, widths and dynamics in Unit 5. |
| [Unit 5](unit-5-light-matter-interaction.md), sections 5.1–5.10 | Provisional first connected draft: calibrated strengths lead to matrix elements and rates, decay and linewidth comparisons lead to coherence and broadening, and controlled populations lead to pumping, gain and laser oscillation. Cavity and interference tests develop modes and coherence before the molecular question. Seven measurement comparisons remain visible TODOs; line-shape and laser-level figures show models. |
| [Unit 6](unit-6-molecules-and-nuclear-motion.md), sections 6.1–6.8 | Provisional first connected draft: CO spacings motivate binding, Born–Oppenheimer separation, rotational and vibrational levels, then matched isotope and higher-excitation tests. Five records and comparisons remain TODOs. Published measured CO line centres test the rotational prediction; the calculated potential diagram illustrates the models. Neither the catalog centres nor reference constants supply a detector-intensity trace. The closing question motivates probe-dependent molecular spectra. |
| [Unit 7](unit-7-molecular-spectroscopy.md), sections 7.1–7.8 | Provisional first connected draft: measured CO infrared evidence motivates dipole selection and branch tests, a nonpolar comparison motivates Raman, and electronic progressions motivate Franck–Condon overlaps. Six measurement comparisons remain TODOs. Keep the processed measured infrared overview distinct from high-resolution records and the calculated overlap illustration. The closing question motivates competing assignments in Unit 8. |
| [Unit 8](unit-8-putting-the-ideas-together.md), sections 8.1–8.8 | Provisional synthesis from proposed single-source controls through an audited processed archive, guarded feature estimates and candidate assignments to conditional Ritz reconstruction and independent tests. Six measurement TODOs remain. The [numerical companion](worked-example-raw-spectrum.md) and current diagnostics replace unsupported precision, clipping and intensity claims in the older example. |

Unit and section numbers now organize the connected drafts. Optional response theory follows Unit 5; each unit closes with the next physical question.

Retain the present asset directories:

- **Units 1–4:** keep the hydrogen, sodium, helium and coupling figures with their corresponding discussions. Label diagrams, tabulated-level plots and the calculated field-response figure accurately.
- **Unit 5:** associate `lorentz-response.svg`, `oscillator-strengths.svg` and `line-shapes.svg` with transitions, response and broadening.
- **Unit 6:** keep calculated molecular potentials distinct from reference level data and detector records.
- **Unit 7:** retain the processed measured CO infrared overview and its provenance separately from the calculated Franck–Condon illustration. Its stated resolution and smoothing limit the branch-level inferences it supports.
- **Unit 8:** use the updated unlabelled archive overview, candidate-feature plot and conditional Ritz schematic. Preserve the original CSV, upstream FITS and processing-source copies, licence and legacy line table. The current analysis exports diagnostic CSV/JSON; the notes remain understandable without Python.

### Measurements and later refinement

The first connected writing pass now spans every syllabus topic in Units 0–8. The physical arguments and their proposed tests are present; the TODO records, independent uncertainty checks and reader reviews remain unfinished. This is a provisional course draft, not a statement that every experimental comparison has been completed.

Separate measured Hg, Cd and Ar control spectra are still absent. Add them before claiming that mixture-based candidate assignments have passed the proposed source test. Do not manufacture these records from selected mixture peaks. Other units retain their own specific measurement gaps.

### Scientific limits retained in the draft

- **Model precision.** Unit 2's leading fixed-nucleus comparison omits small corrections and is distinct from a precision centroid prediction.
- **Signal strengths.** Units 5, 7 and 8 distinguish line areas, photon counts, power, populations and detector response. The lamp archive does not supply a calibrated branching-strength measurement.
- **Archive interpretation.** Unit 8 verifies normalization maxima and processing, rejects unreliable core estimates and treats reference labels as hypotheses. Raw variances, independent calibration and a profile-response measurement remain missing.
- **Independent tests.** A reference-calibrated wavelength match or a four-edge reconstruction is not a new independent confirmation. The proposed unused transitions, field tests and cycle closures provide the next measurements.
- **Coherence.** Unit 5 distinguishes doublet beating from a single-line coherence envelope and states its linewidth conventions.
