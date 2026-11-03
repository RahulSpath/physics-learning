# Unit 0 · How do we learn about the microscopic world?

> We cannot directly see the internal quantum states of an atom or molecule. How do we learn about them through measurements?

A hydrogen discharge produces light at distinct wavelengths. A sample exposed to microwaves gives a signal at particular magnetic field strengths. Neither instrument displays a quantum state. We need a physical argument connecting the recorded signal to the microscopic system.

This is the starting question of the [course map](course-map.md). It prepares the language needed for atomic and molecular structure and optical processes in CSIR–UGC NET Physical Sciences, Part B, Section VII.

**Conventions.** Visible wavelengths are quoted in air unless marked vacuum. Photon energies and spectroscopic wavenumbers use vacuum wavelengths. Constants follow CODATA 2018.

## 0.1 What does an experiment actually give us?

Consider two observations.

**An optical emission spectrum.** Light from a hydrogen discharge enters a spectrometer. A grating separates wavelengths, and a detector records a signal at each position. After wavelength calibration, the result can be displayed as detector counts against wavelength. Distinct bright lines appear above the background.

The detector has recorded light. Identifying a line with a transition between two atomic states is a further step, requiring energy conservation and a model of the atom.

**A resonance signal.** A sample is placed in a magnetic field and exposed to microwaves. At a fixed microwave frequency, varying the field reveals a change in the detected microwave signal near a particular field value. The immediate record is a detector voltage against field. Explaining why the signal changes there requires a model of the sample.

In both cases, distinguish three things: what the instrument recorded, how the apparatus transformed the physical signal, and what microscopic interpretation explains it. Wavelength calibration, background subtraction, detector sensitivity and finite resolution belong to this connection.

A peak is evidence to interpret. Its position, shape and strength become physical information only after we establish what the axes mean and how the measurement was made.

## 0.2 An atomic emission spectrum

Begin with hydrogen, rather than a mixture of elements. Its optical lines give a manageable observation: the light is concentrated near separated wavelengths, and the lines become more closely spaced towards shorter wavelengths.

Figure 0.1 is a real record of this light: the signal of a small spectrometer, recording a hydrogen plasma, against wavelength.

![Measured visible spectrum of a hydrogen plasma](figures/hydrogen-spectrum-usb2000.gif)

*Figure 0.1. Visible spectrum of a hydrogen plasma, measured with an Ocean Optics USB2000 spectrometer. Measured data: Profeta, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:H_plasma_spectrum.gif), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).*

The peaks in Figure 0.1 lie at the tabulated wavelengths of Hα, Hβ and Hγ. The tabulated air wavelengths of the visible lines, carried over from the [hydrogen notes](unit-1-hydrogen.md) (sources: Haken & Wolf; NIST Atomic Spectra Database), are:

| Line | Wavelength in air (nm) |
|---|---:|
| Hα | 656.28 |
| Hβ | 486.13 |
| Hγ | 434.05 |
| Hδ | 410.17 |
| Hε | 397.01 |

The tabulated Hδ and Hε lines do not appear in this trace because the spectrometer is not sensitive enough to distinguish them from the noise. A missing peak can mean a less sensitive instrument, not a missing line.

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

**How wide is it?** The full width at half maximum describes the interval over which a line remains above half its maximum, after accounting for background. Finite lifetimes, collisions and a distribution of atomic velocities can all contribute to broadening. The spectrometer adds its own width. A measured width therefore cannot immediately be read as an excited-state lifetime. Unit 5 separates these causes.

**How does it change under external conditions?** An applied magnetic or electric field may shift or split a line. Temperature changes can redistribute populations and change the spread of atomic velocities that broadens lines; pressure changes can reveal collision effects. Such controlled changes help distinguish competing interpretations. A line’s response to a field can reveal information about the states that its zero-field position alone cannot establish.

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

The argument now runs in both directions. From a proposed Hamiltonian, state preparation and coupling, predict observable transitions. From measured spectra, constrain that model and ask which further measurement could distinguish alternative explanations. Unit 5 will make transition probabilities quantitative.

## 0.5 The same reasoning across physics

As the course meets each new kind of measurement, we will use the same reasoning: ask what the instrument records, how the probe couples to the system, and which model connects the recorded signal to microscopic properties.

## 0.6 Questions that will guide the course

Many interesting questions will arise as we go. The course will answer them as they arise.

Our first observation remains unexplained: hydrogen emits at separated wavelengths that form a regular pattern. Converting those wavelengths into photon energies tells us the energy differences a model must reproduce. We now need a model that predicts those differences and explains why only certain bound energies occur. [Unit 1](unit-1-hydrogen.md) begins with this pattern and asks what the electron–nucleus interaction can explain.

---

## Sources of the data

- Figure 0.1: [H plasma spectrum](https://commons.wikimedia.org/wiki/File:H_plasma_spectrum.gif), measured with an Ocean Optics USB2000 spectrometer; by Profeta, Wikimedia Commons, [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
- Hydrogen wavelengths: Haken & Wolf, *The Physics of Atoms and Quanta*; NIST Atomic Spectra Database.
- Constants: CODATA 2018.
