# Build everything

for program in hello harmonic_sum
do
    (cd cython; make $program)
    (cd nuitka; nuitka ../$program.py)
done
