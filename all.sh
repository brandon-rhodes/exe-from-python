# Build everything

for program in hello harmonic_sum needs_crypto
do
    (cd cython && make TARGET=$program)
    (cd nuitka && make TARGET=$program)
done
