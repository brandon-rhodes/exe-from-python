# Build everything

for program in hello harmonic_sum needs_crypto needs_m2crypto
do
    (cd cython && make TARGET=$program)
    (cd nuitka && make TARGET=$program)
done
