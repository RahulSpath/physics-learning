# Unit 0 · How do we learn about the microscopic world?

> We cannot directly see the internal quantum states of an atom or molecule. How do we learn about them through measurements?

A hydrogen discharge produces light at distinct wavelengths. A magnetic-resonance experiment produces a signal at particular frequencies or magnetic fields. Neither instrument displays a quantum state. We need a physical argument connecting the recorded signal to the microscopic system.

This is the starting question of the [course map](course-map.md). It prepares the language needed for the atomic structure, molecular spectroscopy and optical processes in CSIR–UGC NET Physical Sciences, Part B, Section VII.

**Conventions.** Visible wavelengths are quoted in air unless marked vacuum. Photon energies and spectroscopic wavenumbers use vacuum wavelengths. Constants follow CODATA 2018.

## 0.1 What does an experiment actually give us?

Consider two observations.

**An optical emission spectrum.** Light from a hydrogen discharge enters a spectrometer. A grating separates wavelengths, and a detector records a signal at each position. After wavelength calibration, the result can be displayed as detector counts against wavelength. Distinct bright lines appear above the background.

The detector has recorded light. Identifying a line with a transition between two atomic states is a further step, requiring energy conservation and a model of the atom.

**A magnetic-resonance signal.** In electron spin resonance, a sample is placed in a magnetic field and exposed to microwaves. At a fixed microwave frequency, scanning the field reveals a resonant change in the detected microwave signal. The immediate record is a detector voltage against field. Interpreting it as a transition between magnetic states requires a model of their energies and their interaction with the microwave field. Many instruments display a derivative of the absorption signal, so even locating the resonance requires knowing how the signal was detected.

In both cases, distinguish three things: what the instrument recorded, how the apparatus transformed the physical signal, and what microscopic interpretation explains it. Wavelength calibration, background subtraction, detector sensitivity and finite resolution belong to this connection.

A peak is evidence to interpret. Its position, shape and strength become physical information only after we establish what the axes mean and how the measurement was made.

## 0.2 An atomic emission spectrum

Begin with hydrogen, rather than a mixture of elements. Its optical lines give a manageable observation: the light is concentrated near separated wavelengths, and the lines become more closely spaced towards shorter wavelengths.

The following representative air wavelengths are carried over from the [hydrogen notes](unit-1-hydrogen.md), whose sources include Haken & Wolf and the NIST Atomic Spectra Database.

| Line | Wavelength in air (nm) |
|---|---:|
| Hα | 656.28 |
| Hβ | 486.13 |
| Hγ | 434.05 |
| Hδ | 410.17 |
| Hε | 397.01 |

![Selected hydrogen Balmer line positions on an air-wavelength axis](figures/balmer-spectrum.svg)

*Figure 0.1. An illustration of selected tabulated hydrogen Balmer line positions. This is not a measured intensity trace: the drawn heights, widths and colours do not provide measured line strengths or profiles. The dashed marker indicates the series limit, not another emission line.*

The table and illustration preserve the observed positional pattern without supplying an experimental line shape.

> **Measured spectrum still needed.** Add a documented hydrogen-discharge spectrogram or intensity trace covering approximately 390–670 nm. Retain its wavelength convention, intensity units, stated resolution and source credit. A source to inspect is the hydrogen-spectrum discussion in Haken & Wolf, *The Physics of Atoms and Quanta*, or an archived Balmer-discharge laboratory measurement. Record the exact edition and figure or dataset when selected. The NIST Atomic Spectra Database’s H I line query supplies comparison wavelengths; a line list or synthesized stick spectrum does not supply a measured intensity trace. No such hydrogen trace is currently present in `data/`.

What does the horizontal axis tell us? **Wavelength** is the spatial period of the light; **frequency** is the number of oscillations per second. Their vacuum relation is

```math
\nu=\frac{c}{\lambda_{\mathrm{vac}}}.
```

Frequency does not change when light enters air, but its wavelength does:

```math
\lambda_{\mathrm{vac}}
=n_{\mathrm{air}}\lambda_{\mathrm{air}}.
```

At visible wavelengths, $`n_{\mathrm{air}}\simeq1.00028`$ is adequate for rough conversions. Precision work requires its dependence on wavelength and air conditions. Consequently, using $`c/\lambda_{\mathrm{air}}`$ directly introduces a systematic error.

Spectroscopists also use **wavenumber**, conventionally the reciprocal of the vacuum wavelength:

```math
\tilde{\nu}=\frac{1}{\lambda_{\mathrm{vac}}}
=\frac{\nu}{c}.
```

It is often reported in $`\mathrm{cm}^{-1}`$, taking the wavelength in centimetres. The photon relation connects these coordinates to energy:

```math
E_\gamma=h\nu
=\frac{hc}{\lambda_{\mathrm{vac}}}
=hc\tilde{\nu},
\qquad
hc\simeq1239.84\ \mathrm{eV\,nm}.
```

Thus shorter wavelengths correspond to higher photon energies. These equations translate line positions into the energies carried by individual photons. They do not yet explain why hydrogen emits preferentially at those energies.

## 0.3 What information does a spectral line contain?

A line raises four different questions.

**Where is the line?** Its centre gives a characteristic photon energy. In a transition model, this constrains an energy difference between states. Motion, external fields and collisions can shift the observed centre, so the conditions and wavelength calibration matter. An apparently single line can also contain unresolved components.

**How strong is it?** Emission depends on how many atoms occupy the emitting state and how readily that state radiates into the transition. The photon energy, collection geometry and detector response also affect the recorded signal. A bright line need not represent the most highly populated state. Comparing background-subtracted integrated line signals is generally more useful than comparing peak heights, but even integrated signals require an intensity-response calibration. Reabsorption within the source can further alter the escaping light.

**How wide is it?** The full width at half maximum describes the interval over which a line remains above half its maximum, after accounting for background. Finite lifetimes, collisions and a distribution of atomic velocities can all contribute to broadening. The spectrometer adds its own width. A measured width therefore cannot immediately be read as an excited-state lifetime. Distinguishing population decay, loss of phase coherence and instrumental broadening will become important in Unit 5.

**How does it change under external conditions?** An applied magnetic or electric field may shift or split a line. Temperature changes can redistribute populations and alter Doppler broadening; pressure changes can reveal collision effects. Such controlled changes help distinguish competing interpretations. A line’s response to a field can reveal information about the states that its zero-field position alone cannot establish.

These questions separate energy structure, transition strengths, populations and dynamics. Explaining a line position is only the first part of explaining a spectrum.

## 0.4 From observations to a mathematical model

A quantum model begins with a **Hamiltonian** $`H`$, the operator representing the system’s energy. Its stationary states satisfy

```math
H|n\rangle=E_n|n\rangle.
```

The state label $`n`$ here is general; it need not be hydrogen’s principal quantum number. The model specifies which degrees of freedom and interactions are included. Solving it gives allowed energies and states from which measurable predictions can be constructed.

For an isolated atom at rest, neglecting photon recoil, emission from an upper state $`|u\rangle`$ to a lower state $`|l\rangle`$ obeys

```math
E_u-E_l=h\nu.
```

Absorption reverses the energy transfer: a photon can supply the difference between a lower and an upper state.

A spectral line therefore constrains a **difference of energies**, rather than displaying one energy eigenvalue. Adding the same constant to every energy leaves all transition frequencies unchanged. Nor does one wavelength, by itself, identify the two states involved. Assignments become convincing when several transitions, their strengths and their responses to controlled changes fit one consistent model.

The Hamiltonian alone is insufficient to determine visibility. We must also specify **how the system couples to the probe**. For absorption from an applied optical field, the electric-dipole interaction is

```math
V(t)=-\mathbf d\cdot\mathbf E(t),
```

where $`\mathbf d`$ is the atomic electric-dipole operator and $`\mathbf E(t)`$ is the light’s electric field. The coupling between two states involves the dipole matrix element

```math
\mathbf d_{lu}=\langle l|\mathbf d|u\rangle.
```

The light’s polarization selects a component of this matrix element. Symmetry can make that component vanish even when the energy difference matches the photon energy. The same atomic dipole matrix elements enter electric-dipole emission. Other interactions can connect different pairs of states.

This gives an essential distinction:

**What we measure is not everything that exists in the system.**

An absent emission line may mean that the upper state was scarcely populated, that the relevant coupling is weak or forbidden in the approximation being used, or that the instrument cannot resolve or detect it. A forbidden electric-dipole transition does not imply absent energy levels or rule out every other transition mechanism.

The argument now runs in both directions. From a proposed Hamiltonian, state preparation and coupling, predict observable transitions. From measured spectra, constrain that model and ask which further measurement could distinguish alternative explanations. Unit 5 will make transition probabilities quantitative; no response-function derivation is needed to establish this logic.

## 0.5 The same reasoning across physics

Atomic emission records photons produced by an excited sample. Absorption compares transmitted light with incident light and asks where energy has been removed from the beam. Both can constrain atomic energy differences, but their signals depend differently on populations and measurement conditions.

The same habit of connecting signal, coupling and model extends beyond optical atomic lines.

| Measurement | What connects the signal to microscopic physics? |
|---|---|
| **Molecular spectroscopy** | Infrared absorption and Raman frequency shifts can reveal rotational and vibrational energy differences. Infrared activity depends on electric-dipole coupling; Raman activity depends on polarizability. A molecular motion can therefore be visible to one probe and weak or absent in another. |
| **Magnetic resonance** | Microwave or radio-frequency excitation couples to magnetic moments. ESR and NMR constrain electron-spin and nuclear-spin energy differences, respectively. Resonance shifts and widths also depend on the local environment and spin dynamics. |
| **Photoemission** | The measured kinetic energies and directions of escaping electrons, together with the incident photon energy, constrain electron-removal energies. The final system has one fewer electron, and interpretation also requires the transition matrix elements and the outgoing electron’s interaction with its surroundings. |
| **Inelastic scattering** | Counts of scattered particles or photons are recorded against energy and angle. Energy transfer can reveal excitations, while momentum transfer and the probe’s coupling determine which spatial or spin correlations contribute to the signal. |

These experiments need not reveal the same excitations with the same weights. Matrix elements select what the probe can access; populations determine the starting states; correlations describe relationships among microscopic degrees of freedom; dynamics influence the frequency dependence and widths.

Elastic X-ray diffraction supplies another example of measurement and inference, but its principal information concerns spatial structure and correlations. It should not be identified with an atomic emission spectrum. Inelastic scattering, where the probe exchanges energy with the sample, can directly constrain excitation energies.

The transferable idea is to ask what physical quantity the apparatus is sensitive to before interpreting its peaks.

## 0.6 Questions that will guide the course

The measurement argument leaves the main physics to be explained. The [course map](course-map.md) follows these questions through the remaining units.

| Unresolved question | Where we take it up |
|---|---|
| Why are bound-state energies discrete, and why do hydrogen lines form regular series? | [Unit 1 · The hydrogen atom](course-map.md#unit-1--the-hydrogen-atom): spectral patterns, the Coulomb problem and quantum states. |
| Why do lines split, and why can changing the isotope shift them? | [Unit 2 · Spin and atomic fine structure](course-map.md#unit-2--spin-and-atomic-fine-structure): spin, relativistic corrections, hyperfine interactions and isotope shifts. |
| How do additional electrons change the spectrum? | [Unit 3 · Many-electron atoms](course-map.md#unit-3--many-electron-atoms): helium, alkalis, exchange and angular-momentum coupling. |
| What do field-dependent shifts, splittings and magnetic resonances reveal? | [Unit 4 · Atoms in external fields](course-map.md#unit-4--atoms-in-external-fields): Zeeman, Paschen–Back and Stark effects; ESR, NMR and chemical shifts. |
| Why are some transitions absent, and what determines spectral strengths and widths? | [Unit 5 · Light–matter interaction](course-map.md#unit-5--lightmatter-interaction): matrix elements, selection rules, populations, lifetimes and broadening. |
| How can pumping produce optical gain and laser oscillation? | [Unit 5](course-map.md#unit-5--lightmatter-interaction): spontaneous and stimulated emission, inversion, rate equations, resonator modes and coherence. |
| Why do molecules have spectral structures beyond atomic electronic lines? | [Unit 6 · Molecules and nuclear motion](course-map.md#unit-6--molecules-and-nuclear-motion): bonding, the Born–Oppenheimer approximation, rotation and vibration. |
| Why do infrared, Raman and electronic probes reveal different molecular patterns? | [Unit 7 · Molecular spectroscopy](course-map.md#unit-7--molecular-spectroscopy): molecular selection rules and Franck–Condon physics. |
| What can we infer when several species, unresolved lines and instrumental effects overlap? | [Unit 8 · Putting the ideas together](course-map.md#unit-8--putting-the-ideas-together): individual-element spectra, mixtures, calibration and limits of inference. |

Our first observation remains unexplained: hydrogen emits at separated wavelengths that form a regular pattern. Converting those wavelengths into photon energies tells us the energy differences a model must reproduce. We now need a model that predicts those differences and explains why only certain bound energies occur. [Unit 1](unit-1-hydrogen.md) begins with this pattern and asks what the electron–nucleus interaction can explain.
